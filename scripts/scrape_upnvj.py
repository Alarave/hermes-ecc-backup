#!/usr/bin/env python3
"""
scripts/scrape_upnvj.py
Scraper EPrints UPNVJ untuk mengunduh metadata skripsi, abstrak,
dan berkas publik (AWAL.pdf, ABSTRAK.pdf, DAFTAR PUSTAKA.pdf).
"""

import os
import sys
import re
import ssl
import time
import json
import base64
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "cache" / "upnvj_skripsi_2026"

ctx = ssl.create_default_context()
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# Cek apakah ada autentikasi dari environment variable UPNVJ_AUTH (format: username:password)
if os.environ.get("UPNVJ_AUTH"):
    auth_b64 = base64.b64encode(os.environ["UPNVJ_AUTH"].strip().encode()).decode()
    HEADERS["Authorization"] = f"Basic {auth_b64}"
    print("[AUTH] Menggunakan kredensial Basic Auth dari environment variable UPNVJ_AUTH.")

def fetch_url(url, retries=2, timeout=8):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as he:
            # Jangan retry jika 401, 403, 404
            if he.code in [401, 403, 404]:
                return None
            if i == retries - 1:
                return None
            time.sleep(0.5)
        except Exception:
            if i == retries - 1:
                return None
            time.sleep(0.5)
    return None

def clean_filename(s):
    return re.sub(r'[\\/*?:"<>|]', "", s).strip()[:50]

def scrape_division_2026(limit=10, download_files=False):
    list_url = "https://repository.upnvj.ac.id/view/divisions/511/2026.html"
    print(f">>> Mengambil daftar skripsi dari: {list_url}")
    
    html_bytes = fetch_url(list_url)
    if not html_bytes:
        print("[ERROR] Gagal memuat halaman divisi UPNVJ.")
        return []
    
    html = html_bytes.decode("utf-8", errors="ignore")
    
    pattern = re.compile(
        r"<span[^>]*class=\"person_name\"[^>]*>(.*?)</span>\s*\((\d{4})\)\s*<a\s+href=\"https?://repository\.upnvj\.ac\.id/(\d+)/?\"><em>(.*?)</em></a>",
        re.DOTALL
    )
    
    matches = pattern.findall(html)
    total_found = len(matches)
    print(f"[OK] Ditemukan {total_found} entri skripsi Informatika 2026.\n")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    all_data = []
    index_md_path = OUTPUT_DIR / "00_MASTER_INDEX_SKRIPSI_2026.md"
    
    count = 0
    target_count = min(limit, total_found)
    for author, year, item_id, title in matches[:target_count]:
        count += 1
        clean_author = re.sub(r"<[^>]+>", "", author).strip().rstrip(", .")
        clean_title = re.sub(r"<[^>]+>", "", title).strip()
        
        folder_name = f"{item_id}_{clean_filename(clean_author)}"
        item_folder = OUTPUT_DIR / folder_name
        item_folder.mkdir(parents=True, exist_ok=True)
        md_file_path = item_folder / "CATATAN_SKRIPSI.md"
        
        # Jika sudah selesai, cukup baca metadata yang sudah ada
        if md_file_path.exists():
            print(f"[{count}/{target_count}] [SKIP/EXIST] ID: {item_id} | {clean_author}")
            all_data.append({
                "id": item_id,
                "author": clean_author,
                "year": year,
                "title": clean_title,
                "folder": str(item_folder.relative_to(BASE_DIR)).replace("\\", "/")
            })
            continue

        print(f"[{count}/{target_count}] Scraping ID: {item_id} | {clean_author}...")
        
        item_url = f"https://repository.upnvj.ac.id/{item_id}/"
        item_html_bytes = fetch_url(item_url)
        abstract_text = "Abstrak tidak ditemukan di repositori."
        documents = []
        
        if item_html_bytes:
            item_html = item_html_bytes.decode("utf-8", errors="ignore")
            
            # Ambil abstract
            abs_match = re.search(r"<h2>Abstract</h2>\s*<p[^>]*>(.*?)</p>", item_html, re.DOTALL | re.IGNORECASE)
            if abs_match:
                raw_abs = abs_match.group(1)
                abstract_text = re.sub(r"<[^>]+>", "", raw_abs).strip()
                abstract_text = abstract_text.replace("&#13;", "\n").replace("&quot;", '"').replace("&amp;", "&")
            
            # Ambil link berkas dokumen
            doc_links = re.findall(r"<a\s+class=\"ep_document_link\"\s+href=\"([^\"]+)\"", item_html)
            for d in doc_links:
                fname = urllib.parse.unquote(d.split("/")[-1])
                is_public = any(k in fname.upper() for k in ["AWAL", "ABSTRAK", "PUSTAKA", "DAFTAR"])
                downloaded_file = None
                
                # Jika ada Authorization aktif, unduh SEMUA berkas (termasuk Bab 1-3)
                should_download = download_files and (is_public or "Authorization" in HEADERS)
                
                if should_download:
                    target_pdf = item_folder / fname
                    if not target_pdf.exists():
                        pdf_bytes = fetch_url(d)
                        if pdf_bytes and len(pdf_bytes) > 1000:
                            with open(target_pdf, "wb") as f:
                                f.write(pdf_bytes)
                            downloaded_file = fname
                            print(f"    -> [PDF Unduh] {fname} ({len(pdf_bytes)//1024} KB)")
                    else:
                        downloaded_file = fname
                
                documents.append({
                    "name": fname,
                    "url": d,
                    "is_public": is_public,
                    "downloaded": downloaded_file is not None
                })
        
        # Simpan versi Teks Lengkap (Markdown per Skripsi)
        md_content = f"""# {clean_title}

- **ID Repositori**: [{item_id}]({item_url})
- **Penulis**: {clean_author}
- **Tahun**: {year}
- **Program Studi**: S1 Informatika, Fakultas Ilmu Komputer, UPNVJ

---

## 📄 Abstrak (Teks Lengkap)

{abstract_text}

---

## 📂 Berkas Dokumen Terkait

| Nama Berkas | Status Akses | Link File |
|---|:---:|---|
"""
        for doc in documents:
            status_badge = "🟢 Publik (Tersimpan Lokal)" if doc.get("downloaded") else ("🟡 Publik" if doc["is_public"] else "🔒 Restricted (401)")
            local_link = f"[{doc['name']}](./{doc['name']})" if doc.get("downloaded") else f"[{doc['name']}]({doc['url']})"
            md_content += f"| {local_link} | {status_badge} | [Link Web]({doc['url']}) |\n"

        with open(item_folder / "CATATAN_SKRIPSI.md", "w", encoding="utf-8") as f:
            f.write(md_content)
        
        all_data.append({
            "id": item_id,
            "author": clean_author,
            "year": year,
            "title": clean_title,
            "abstract": abstract_text,
            "folder": str(item_folder.relative_to(BASE_DIR)).replace("\\", "/")
        })
            
    # Tulis Master Index Markdown
    with open(index_md_path, "w", encoding="utf-8") as f:
        f.write(f"""# 📚 KATALOG SKRIPSI INFORMATIKA UPNVJ (ANGKATAN 2026)
> Total Skripsi Terkatalog: {len(all_data)} Judul  
> Direktori Penyimpanan: `cache/upnvj_skripsi_2026/`

| No | ID | Penulis | Judul Skripsi | Folder & Teks Lengkap |
|---|:---:|---|---|---|
""")
        for i, item in enumerate(all_data, start=1):
            f.write(f"| {i} | {item['id']} | {item['author']} | {item['title']} | [Buka Teks & PDF](./{item['id']}_{clean_filename(item['author'])}/CATATAN_SKRIPSI.md) |\n")

    # Simpan rekap JSON
    json_path = OUTPUT_DIR / "skripsi_2026_rekap_lengkap.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
        
    print(f"\n[SELESAI] Rekap metadata berhasil disimpan di: {json_path}")
    print(f"Master Index: {index_md_path}")
    return all_data

if __name__ == "__main__":
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    dl = "--download" in sys.argv
    import urllib.parse
    scrape_division_2026(limit=lim, download_files=dl)
