---
name: cross-agent-sync
description: "Use when syncing memories between Hermes and Antigravity."
---

# Cross-Agent Memory & History Synchronization (`cross-agent-sync`)

## R (Role & Purpose)
- **Peran**: Multi-Agent Memory Architect & Cross-Platform Synchronization Engine.
- **Tanggung Jawab**: Mengelola sinkronisasi riwayat obrolan dan observasi dua arah antara Hermes Agent, Google Antigravity, dan Obsidian Vault.

## C (Context & Architecture)
- **Database Sentral SQLite**: `~/.claude-mem/claude-mem.db` (tabel `observations`, `sdk_sessions`, dan virtual index `observations_fts`).
- **Vault Catatan Antigravity**: `E:\history antigravity\history antigravity\Chats\` dan `00_INDEX.md`.
- **MCP Toolset**: `claude-mem` MCP server (`search`, `timeline`, `get_observations`, `build_corpus`).

## C (Constraints & Production Rules)

### 1. Hook Gap Mechanism (Akar Masalah Sinkronisasi)
- `claude-mem` hanya merekam percakapan otomatis jika runtime agen mengeksekusi lifecycle hooks (`SessionStart`, `PostToolUse`, `SessionEnd`).
- Hermes dan Claude Code mengeksekusi hook ini.
- Antigravity IDE dan Antigravity CLI (`agy`) TIDAK mengeksekusi hook tersebut, sehingga berstatus *Read-Only MCP Consumer*. Percakapan baru di Antigravity tidak masuk otomatis ke database tanpa prosedur backfill.

### 2. Jembatan Sinkronisasi 2-Arah Terpadu (Bidirectional Sync)
Jalankan skrip jembatan sinkronisasi terpadu:
```bash
python scripts/sync_bidirectional_history.py
```

Skrip ini mengeksekusi dua alur sekaligus:
- **Arah 1 (Antigravity -> claude-mem)**: Mengekstrak berkas Markdown di `E:/history antigravity/.../Chats/*.md` dan `~/.gemini/antigravity/conversation_summaries.db`, lalu menyuntikkannya ke `claude-mem.db` dengan tag `project="antigravity"`.
- **Arah 2 (Hermes -> Antigravity Vault)**: Mengekspor sesi desktop Hermes (`hermes sessions export --format md --source desktop --newer-than 30d --redact`) ke folder `E:/history antigravity/history antigravity/Chats/` dan memperbarui daftar tautan di `00_INDEX.md`.

Kedua alur menggunakan verifikasi hash SHA-256 dan deteksi ID sesi yang sudah ada, sehingga aman dijalankan berulang tanpa duplikasi data.

### 3. Aturan Pencarian Lintas Agen (Cross-Project Scoping)
- **Pitfall**: Pencarian dengan parameter `project` spesifik akan memblokir riwayat dari agen lain.
  - Hermes menandai sesi dengan `project: "hermes-agent"`.
  - Antigravity ditandai dengan `project: "antigravity"`.
- **Solusi**: Saat mencari konteks lampau lintas platform, JANGAN isi parameter `project` pada tool `search` agar seluruh memori dari kedua platform dapat ditemukan sekaligus.

### 4. Dual-Store Defense
Selain database SQLite `claude-mem`, selalu simpan keputusan arsitektur penting dan ringkasan tugas ke dalam vault Obsidian (`E:/BELAJAR BANGET/SKILL BELAJAR`) sebagai *human-readable single source of truth*.

## O (Verification & Deliverables)
1. Jalankan pencarian verifikasi via tool `mcp__claude_mem__search(query="<kata-kunci>")`.
2. Pastikan hasil pencarian menampilkan riwayat dari kedua platform (Hermes Session dan Antigravity Session).
3. Verifikasi pembaruan berkas `E:\history antigravity\history antigravity\00_INDEX.md` dengan jumlah total sesi yang sinkron.
