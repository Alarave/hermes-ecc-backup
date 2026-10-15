import os
import sys
import time
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]

lock = threading.Lock()
completed_count = 0
uploaded_bytes = 0
total_count = 0
total_bytes = 0
start_time = None

def get_credentials(client_id, client_secret, token_path):
    creds = None
    if os.path.exists(token_path):
        try:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception:
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                creds = None
        if not creds:
            client_config = {
                "installed": {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                    "redirect_uris": ["http://localhost"]
                }
            }
            flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, "w") as tf:
            tf.write(creds.to_json())

    return creds

def get_existing_remote_files(service, folder_id):
    existing = set()
    page_token = None
    query = f"'{folder_id}' in parents and trashed = false"

    while True:
        results = service.files().list(
            q=query,
            pageSize=1000,
            fields="nextPageToken, files(id, name)",
            pageToken=page_token
        ).execute()

        for f in results.get("files", []):
            existing.add(f["name"])

        page_token = results.get("nextPageToken")
        if not page_token:
            break

    return existing

def upload_single_file(creds, folder_id, filename, filepath, filesize):
    global completed_count, uploaded_bytes, total_count, total_bytes, start_time

    service = build("drive", "v3", credentials=creds, cache_discovery=False)
    file_metadata = {"name": filename, "parents": [folder_id]}

    media = MediaFileUpload(
        filepath,
        resumable=filesize > 5 * 1024 * 1024
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            req = service.files().create(body=file_metadata, media_body=media, fields="id")
            res = req.execute()
            with lock:
                completed_count += 1
                uploaded_bytes += filesize
                elapsed = time.time() - start_time
                pct = (completed_count / total_count) * 100 if total_count > 0 else 100
                speed = (uploaded_bytes / (1024 * 1024)) / elapsed if elapsed > 0 else 0
                print(f"[{completed_count}/{total_count}] ({pct:.1f}%) {filename} ({filesize/(1024*1024):.1f}MB) | {speed:.1f}MB/s")
            return res.get("id")
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                with lock:
                    print(f"[FAILED] {filename}: {e}", file=sys.stderr)
                return None

def main():
    parser = argparse.ArgumentParser(description="Upload local directory files to Google Drive folder")
    parser.add_argument("--local-dir", required=True, help="Local directory containing files")
    parser.add_argument("--folder-id", required=True, help="Target Google Drive folder ID")
    parser.add_argument("--client-id", required=True, help="Google OAuth Client ID")
    parser.add_argument("--client-secret", required=True, help="Google OAuth Client Secret")
    parser.add_argument("--token-path", default="gdrive_token.json", help="Path to token cache file")
    parser.add_argument("--workers", type=int, default=4, help="Concurrent upload workers")
    args = parser.parse_args()

    global completed_count, total_count, uploaded_bytes, total_bytes, start_time

    creds = get_credentials(args.client_id, args.client_secret, args.token_path)
    service = build("drive", "v3", credentials=creds, cache_discovery=False)

    existing = get_existing_remote_files(service, args.folder_id)
    local_files = [f for f in os.listdir(args.local_dir) if os.path.isfile(os.path.join(args.local_dir, f))]
    pending = [(f, os.path.join(args.local_dir, f), os.path.getsize(os.path.join(args.local_dir, f)))
               for f in local_files if f not in existing]

    total_count = len(pending)
    total_bytes = sum(sz for _, _, sz in pending)
    completed_count = 0
    uploaded_bytes = 0

    print(f"Total: {len(local_files)} | Existing: {len(existing)} | To Upload: {total_count} ({total_bytes/(1024*1024):.1f} MB)")
    if total_count == 0:
        print("All files already synchronized.")
        return

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(upload_single_file, creds, args.folder_id, fn, fp, sz): fn for fn, fp, sz in pending}
        for f in as_completed(futures):
            f.result()

    print(f"Finished in {(time.time() - start_time)/60:.1f} minutes.")

if __name__ == "__main__":
    main()
