"""
sync_bidirectional_history.py
Jembatan Sinkronisasi 2-Arah: Hermes Agent <-> Antigravity
1. Arah 1: Antigravity -> claude-mem (SQLite)
2. Arah 2: Hermes -> Antigravity (Obsidian Vault Chats/ & 00_INDEX.md)
"""

import subprocess
import sqlite3
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime, timezone

def sync_antigravity_to_claude_mem():
    claude_mem_path = Path.home() / ".claude-mem" / "claude-mem.db"
    if not claude_mem_path.exists():
        print(f"Error: claude-mem.db tidak ditemukan di {claude_mem_path}")
        return

    conn_dst = sqlite3.connect(claude_mem_path)
    c_dst = conn_dst.cursor()
    total_inserted = 0

    # Ingest Markdown Chats
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
                pass

    # Ingest conversation_summaries.db
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
                pass
        conn_src.close()

    conn_dst.commit()
    conn_dst.close()
    print(f"[Arah 1] Antigravity -> claude-mem: {total_inserted} sesi baru ditambahkan.")


def sync_hermes_to_antigravity():
    temp_dir = Path("C:/Users/HP/AppData/Local/hermes/cache/scratch/hermes_export")
    temp_dir.mkdir(parents=True, exist_ok=True)
    antigravity_chats = Path("E:/history antigravity/history antigravity/Chats")
    index_file = Path("E:/history antigravity/history antigravity/00_INDEX.md")

    # 1. Export from Hermes
    cmd = [
        "hermes", "sessions", "export",
        "--format", "md",
        "--source", "desktop",
        "--newer-than", "30d",
        "--redact",
        "--force",
        str(temp_dir)
    ]
    subprocess.run(cmd, capture_output=True, text=True)

    # 2. Sync to Chats/
    existing_ids = set()
    for f in antigravity_chats.glob("*.md"):
        m = re.search(r'- ([0-9a-fA-F_]+)\.md$', f.name)
        if m:
            existing_ids.add(m.group(1).lower())

    new_rows = []
    synced_count = 0

    for ef in temp_dir.glob("*.md"):
        text = ef.read_text(encoding="utf-8", errors="ignore")
        m_fm = re.match(r"^---\n([\s\S]*?)\n---\n([\s\S]*)$", text)
        if not m_fm:
            continue
        
        fm_raw = m_fm.group(1)
        body = m_fm.group(2)
        
        fm = {}
        for line in fm_raw.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"\'')
                
        sess_id = fm.get("session_id", ef.stem.split("-")[0])
        short_id = sess_id.split("_")[-1] if "_" in sess_id else sess_id[:8]
        
        if short_id.lower() in existing_ids or sess_id.lower() in existing_ids:
            continue
            
        created_at = fm.get("created_at", "2026-10-01")
        date_str = created_at[:10]
        title = fm.get("title", ef.stem)
        clean_title = re.sub(r'[\\/*?:"<>|]', '', title)[:45].strip()
        
        target_name = f"{date_str} - {clean_title} - {short_id}.md"
        target_file = antigravity_chats / target_name
        
        new_header = (
            f"---\n"
            f'conversation_id: "{sess_id}"\n'
            f'date: "{date_str}"\n'
            f"tags: [hermes, chat-history]\n"
            f'source: "hermes-desktop"\n'
            f"---\n\n"
        )
        target_file.write_text(new_header + body, encoding="utf-8")
        existing_ids.add(short_id.lower())
        synced_count += 1
        
        topic_display = clean_title
        link_display = f"[[Chats/{target_name}|{topic_display}]]"
        new_rows.append(f"| {date_str} | {topic_display} | {link_display} | `{short_id}` |")

    # 3. Update 00_INDEX.md
    if new_rows and index_file.exists():
        index_content = index_file.read_text(encoding="utf-8")
        new_rows.sort(reverse=True)
        table_marker = "| :--- | :--- | :--- | :--- |"
        if table_marker in index_content:
            parts = index_content.split(table_marker, 1)
            updated_index = parts[0] + table_marker + "\n" + "\n".join(new_rows) + parts[1]
            
            m_count = re.search(r'> Total Sesi:\s*(\d+)', updated_index)
            if m_count:
                old_c = int(m_count.group(1))
                new_c = old_c + synced_count
                updated_index = updated_index.replace(f"> Total Sesi: {old_c}", f"> Total Sesi: {new_c}", 1)
                
            index_file.write_text(updated_index, encoding="utf-8")

    print(f"[Arah 2] Hermes -> Antigravity: {synced_count} sesi baru disinkronkan ke Obsidian Chats & 00_INDEX.md.")


def main():
    print("=== Memulai Sinkronisasi 2-Arah Hermes <-> Antigravity ===")
    sync_antigravity_to_claude_mem()
    sync_hermes_to_antigravity()
    print("=== Sinkronisasi 2-Arah Selesai! ===")

if __name__ == "__main__":
    main()
