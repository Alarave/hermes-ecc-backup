import sqlite3
import time
import os
import json
import urllib.request

DB_PATH = r"C:\Users\HP\AppData\Local\hermes\state.db"
SYNC_STATE_PATH = r"C:\Users\HP\AppData\Local\hermes\.claude_mem_last_id"
API_URL = "http://127.0.0.1:37777/api/memory/save"

def get_last_id():
    if os.path.exists(SYNC_STATE_PATH):
        with open(SYNC_STATE_PATH, "r") as f:
            return int(f.read().strip())
    return 0

def set_last_id(last_id):
    with open(SYNC_STATE_PATH, "w") as f:
        f.write(str(last_id))

def send_to_claude_mem(text, session_id):
    payload = {
        "text": text,
        "title": f"Hermes Session: {session_id}",
        "project": "hermes-agent",
        "metadata": {"platformSource": "hermes", "session_id": session_id}
    }
    req = urllib.request.Request(API_URL, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req, timeout=5)
    except Exception as e:
        print(f"Error sending to claude-mem: {e}")

def run_sync():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    last_id = get_last_id()
    
    # Get new messages
    c.execute("""
        SELECT id, session_id, role, content 
        FROM messages 
        WHERE id > ? AND role IN ('user', 'assistant') AND active=1 AND content IS NOT NULL
        ORDER BY id ASC
    """, (last_id,))
    
    rows = c.fetchall()
    if not rows:
        return
        
    sessions = {}
    max_id = last_id
    for row in rows:
        msg_id, session_id, role, content = row
        if session_id not in sessions:
            sessions[session_id] = []
        sessions[session_id].append(f"{role.upper()}: {content}")
        if msg_id > max_id:
            max_id = msg_id
            
    for session_id, msgs in sessions.items():
        text = "\n\n".join(msgs)
        send_to_claude_mem(text, session_id)
        
    set_last_id(max_id)
    print(f"Synced up to msg {max_id}")

if __name__ == "__main__":
    while True:
        try:
            run_sync()
        except Exception as e:
            pass
        time.sleep(30)
