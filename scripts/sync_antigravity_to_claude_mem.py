"""
sync_antigravity_to_claude_mem.py
Sinkronisasi dua arah riwayat chat Antigravity ke database SQLite claude-mem.
Membaca:
1. File Markdown di E:\history antigravity\history antigravity\Chats\
2. SQLite conversation_summaries.db di ~/.gemini/antigravity/
Menyimpan ke:
~/.claude-mem/claude-mem.db
"""

import sqlite3
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime, timezone

def sync_antigravity_chats():
    claude_mem_path = Path.home() / ".claude-mem" / "claude-mem.db"
    if not claude_mem_path.exists():
        print(f"Error: claude-mem.db tidak ditemukan di {claude_mem_path}")
        return

    conn_dst = sqlite3.connect(claude_mem_path)
    c_dst = conn_dst.cursor()

    total_inserted = 0

    # 1. Ingest Markdown Chats
    chats_dir = Path("E:/history antigravity/history antigravity/Chats")
    if chats_dir.exists():
        for f in chats_dir.glob("*.md"):
            try:
                content = f.read_text(encoding="utf-8", errors="ignore")
                m_id = re.search(r'conversation_id:\s*["\']?([^"\'\n]+)', content)
                conv_id = m_id.group(1).strip() if m_id else f.stem
                
                m_title = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                title = m_title.group(1).strip() if m_title else f.stem
                
                m_date = re.search(r'date:\s*["\']?([^"\'\n]+)', content)
                date_str = m_date.group(1).strip() if m_date else "2026-08-01"
                try:
                    dt = datetime.fromisoformat(date_str).replace(tzinfo=timezone.utc)
                except Exception:
                    dt = datetime(2026, 8, 1, tzinfo=timezone.utc)
                    
                epoch_ms = int(dt.timestamp() * 1000)
                iso_str = dt.isoformat()
                
                user_matches = re.findall(r'### User\s+`[^`]+`\s*\n\n(.*?)(?=\n---\n|\n### Assistant|\Z)', content, re.DOTALL)
                user_snippet = " \n".join(u.strip() for u in user_matches[:2])
                if len(user_snippet) > 1000:
                    user_snippet = user_snippet[:1000] + "..."
                    
                narrative = f"Title: {title}\nDate: {date_str}\nUser Context:\n{user_snippet}"
                mem_sess_id = f"manual-antigravity-{conv_id}"
                content_sess_id = f"manual-content-antigravity-{conv_id}"
                
                c_dst.execute("""
                    INSERT OR IGNORE INTO sdk_sessions (
                        content_session_id, memory_session_id, project, platform_source,
                        user_prompt, started_at, started_at_epoch, status
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (content_sess_id, mem_sess_id, "antigravity", "antigravity", user_snippet[:200], iso_str, epoch_ms, "completed"))
                
                content_hash = hashlib.sha256(narrative.encode('utf-8')).hexdigest()[:16]
                c_dst.execute("SELECT id FROM observations WHERE memory_session_id = ?", (mem_sess_id,))
                if not c_dst.fetchone():
                    c_dst.execute("""
                        INSERT INTO observations (
                            memory_session_id, project, text, type, title, subtitle,
                            facts, narrative, concepts, files_read, files_modified,
                            created_at, created_at_epoch, content_hash, metadata
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        mem_sess_id, "antigravity", None, "discovery", f"Antigravity Session: {title}",
                        f"Antigravity Chat {date_str}", "[]", narrative, "[]", "[]", "[]",
                        iso_str, epoch_ms, content_hash, json.dumps({"platformSource": "antigravity", "conversation_id": conv_id})
                    ))
                    total_inserted += 1
            except Exception as e:
                print(f"Error reading {f.name}: {e}")

    # 2. Ingest conversation_summaries.db
    db_source = Path.home() / ".gemini" / "antigravity" / "conversation_summaries.db"
    if db_source.exists():
        conn_src = sqlite3.connect(db_source)
        c_src = conn_src.cursor()
        rows = c_src.execute("SELECT conversation_id, title, preview, last_modified_time, workspace_uris FROM conversation_summaries;").fetchall()
        for conv_id, title, preview, last_mod, uris in rows:
            try:
                title = (title or "Untitled Conversation").strip()
                preview = (preview or "").strip()
                date_str = str(last_mod)[:19]
                try:
                    dt = datetime.fromisoformat(date_str.replace(" ", "T")).replace(tzinfo=timezone.utc)
                except Exception:
                    dt = datetime(2026, 10, 21, tzinfo=timezone.utc)
                    
                epoch_ms = int(dt.timestamp() * 1000)
                iso_str = dt.isoformat()
                
                narrative = f"Title: {title}\nDate: {date_str}\nWorkspace: {uris}\nSummary Preview:\n{preview}"
                mem_sess_id = f"manual-antigravity-{conv_id}"
                content_sess_id = f"manual-content-antigravity-{conv_id}"
                
                c_dst.execute("""
                    INSERT OR IGNORE INTO sdk_sessions (
                        content_session_id, memory_session_id, project, platform_source,
                        user_prompt, started_at, started_at_epoch, status
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (content_sess_id, mem_sess_id, "antigravity", "antigravity", title[:200], iso_str, epoch_ms, "completed"))
                
                content_hash = hashlib.sha256(narrative.encode('utf-8')).hexdigest()[:16]
                c_dst.execute("SELECT id FROM observations WHERE memory_session_id = ?", (mem_sess_id,))
                if not c_dst.fetchone():
                    c_dst.execute("""
                        INSERT INTO observations (
                            memory_session_id, project, text, type, title, subtitle,
                            facts, narrative, concepts, files_read, files_modified,
                            created_at, created_at_epoch, content_hash, metadata
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        mem_sess_id, "antigravity", None, "discovery", f"Antigravity Session: {title}",
                        f"Antigravity Chat {date_str}", "[]", narrative, "[]", "[]", "[]",
                        iso_str, epoch_ms, content_hash, json.dumps({"platformSource": "antigravity", "conversation_id": conv_id, "workspace": uris})
                    ))
                    total_inserted += 1
            except Exception as e:
                print(f"Error reading db row {conv_id}: {e}")
        conn_src.close()

    conn_dst.commit()
    conn_dst.close()
    print(f"Sinkronisasi selesai! Berhasil menambahkan {total_inserted} sesi baru ke claude-mem.")

if __name__ == "__main__":
    sync_antigravity_chats()
