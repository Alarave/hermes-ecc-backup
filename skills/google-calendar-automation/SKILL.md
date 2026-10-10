---
name: google-calendar-automation
description: "Use when user says 'jadwal', 'atur jadwal', 'jadwalin', 'agenda', 'google calendar', 'tambah acara', 'buat janji', 'catat di kalender'. Manage Google Calendar events, scheduling, and availability via Rube MCP."
requires:
  mcp: [rube]
---

# Google Calendar Automation (via Rube MCP)

Mengotomatiskan alur kerja Google Calendar termasuk pembuatan acara, penjadwalan, cek ketersediaan waktu luang, manajemen peserta, dan pencarian acara menggunakan Composio's Google Calendar toolkit di dalam Rube MCP.

## Setup & Koneksi Awal
Jika user pertama kali menggunakan fitur ini:
1. Pastikan Anda (Pram) mengeksekusi `RUBE_SEARCH_TOOLS` untuk memeriksa apakah server siap.
2. Panggil `RUBE_MANAGE_CONNECTIONS` dengan parameter `toolkit: "googlecalendar"`.
3. Jika statusnya belum ACTIVE, berikan *link autentikasi* ke user untuk login ke akun Google mereka. Tunggu user mengonfirmasi login sebelum melanjutkan langkah lain.

## Core Workflows (Alur Kerja)

### 1. Membuat Acara (Schedule Event)
**Alur:** `GOOGLECALENDAR_LIST_CALENDARS` -> `GOOGLECALENDAR_GET_CURRENT_DATE_TIME` -> `GOOGLECALENDAR_FIND_FREE_SLOTS` (opsional) -> `GOOGLECALENDAR_CREATE_EVENT`

**Aturan Ketat (Constraints):**
- Waktu mulai (`start_datetime`) WAJIB format **ISO 8601** (contoh: `2026-10-15T14:00:00`). Jangan pakai format bahasa manusia ("besok", "lusa").
- Zona Waktu (`timezone`) WAJIB format **IANA** (contoh: `Asia/Jakarta`, bukan WIB, EST, atau PST).
- Parameter `event_duration_minutes` MAKSIMAL 59. Jika 60 menit, gunakan `event_duration_hour=1` dan `event_duration_minutes=0`.
- Peserta (`attendees`) hanya menerima alamat email, BUKAN nama.

### 2. Cek Ketersediaan / Jadwal Kosong (Find Free Slots)
**Alur:** `GOOGLECALENDAR_GET_CURRENT_DATE_TIME` -> `GOOGLECALENDAR_FIND_FREE_SLOTS`

### 3. Hapus / Ubah Acara
**Alur:** `GOOGLECALENDAR_FIND_EVENT` (untuk mendapatkan `event_id` spesifik) -> `GOOGLECALENDAR_PATCH_EVENT` atau `GOOGLECALENDAR_DELETE_EVENT`.
**Penting:** Selalu cari event_id terlebih dahulu. Jangan pernah menebak `event_id`.

## Eksekusi Anti-Halusinasi (The RCCO Way)
- **Jangan Mengarang Tanggal/Waktu**: Selalu pastikan tanggal referensi hari ini dengan `GOOGLECALENDAR_GET_CURRENT_DATE_TIME` sebelum menjadwalkan "Jumat depan".
- **Verifikasi**: Setelah acara dibuat, berikan konfirmasi ke user (Judul, Waktu, Link Google Meet jika ada).
