---
name: claude-mem-sync
description: "Use when syncing claude-mem history across agents."
---

# Claude-Mem Cross-Agent Synchronization (`claude-mem-sync`)

## R (Role & Purpose)
- **Peran**: Multi-Agent Memory Architect & Cross-Platform Synchronization Engine.
- **Tanggung Jawab**: Menjembatani riwayat percakapan, observasi, dan memori jangka panjang antara Hermes Agent, Google Antigravity, Claude Code, dan Codex yang berbagi basis data `~/.claude-mem/claude-mem.db`.

## C (Context & Architecture)
- **Penyimpanan Sentral**: SQLite database di `~/.claude-mem/claude-mem.db` dengan tabel `observations`, `sdk_sessions`, dan virtual index FTS (`observations_fts`).
- **Antarmuka MCP**: Server `scripts/mcp-server.cjs` mengekspos tool baca (`search`, `timeline`, `get_observations`, `build_corpus`).

## C (Constraints & Production Rules)

### 1. Hook Gap Mechanism (Akar Masalah Sinkronisasi)
- `claude-mem` hanya merekam percakapan otomatis jika runtime agen mengeksekusi lifecycle hooks (`SessionStart`, `PostToolUse`, `SessionEnd`).
- Hermes dan Claude Code mengeksekusi hook ini.
- Antigravity IDE dan Antigravity CLI (`agy`) TIDAK mengeksekusi hook tersebut, sehingga berstatus *Read-Only MCP Consumer*. Percakapan baru di Antigravity tidak masuk otomatis ke database tanpa prosedur backfill.

### 2. Prosedur Ingest & Backfill Berkala
Untuk menyedot riwayat chat Antigravity (berkas markdown di `E:/history antigravity/.../Chats/*.md` atau `~/.gemini/antigravity/conversation_summaries.db`):
- Jalankan skrip sinkronisasi deterministik:
  ```bash
  python scripts/sync_antigravity_to_claude_mem.py
  ```
- Skrip menggunakan `INSERT OR IGNORE` dan verifikasi hash SHA-256 (`content_hash`) sehingga aman dijalankan berulang tanpa duplikasi data.

### 3. Aturan Pencarian Lintas Agen (Cross-Project Scoping)
- **Pitfall**: Pencarian dengan parameter `project` spesifik akan memblokir riwayat dari agen lain.
- Hermes menandai sesi dengan `project: "hermes-agent"`.
- Antigravity ditandai dengan `project: "antigravity"`.
- **Solusi**: Saat mencari konteks lampau lintas platform, JANGAN isi parameter `project` pada tool `search` agar seluruh memori dari kedua platform dapat ditemukan.

### 4. Dual-Store Defense
Selain database SQLite `claude-mem`, selalu simpan keputusan arsitektur penting dan ringkasan tugas ke dalam vault Obsidian (`E:/BELAJAR BANGET/SKILL BELAJAR`) sebagai *human-readable single source of truth*.

## O (Verification & Deliverables)
1. Jalankan pencarian verifikasi via tool `mcp__claude_mem__search(query="<kata-kunci>")`.
2. Pastikan hasil pencarian menampilkan riwayat dari kedua platform (Hermes Session dan Antigravity Session).
