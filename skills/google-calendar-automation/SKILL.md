---
name: google-calendar-automation
description: "Use when user wants to manage Google Calendar events."
requires:
  mcp: [rube]
---

# Google Calendar Automation (via Rube MCP)

Mengotomatiskan alur kerja Google Calendar termasuk pembuatan acara, penjadwalan, cek ketersediaan waktu luang, manajemen peserta, dan pencarian acara menggunakan Composio's Google Calendar toolkit di dalam Rube MCP.

## Setup & Koneksi Awal
Jika user pertama kali menggunakan fitur ini atau sesi baru:
1. Pastikan Rube (Composio) MCP sudah terhubung via `manage_connections(action="authorize", connectors=[{"name": "rube", "mcp": true}])`.
   - **Pitfall URL:** Jika koneksi MCP Rube gagal (DNS error/host unresolvable ke rube.app), konfigurasi lama Rube mungkin mati. Gunakan terminal untuk update URL: `hermes config set mcp_servers.rube.url https://connect.composio.dev/mcp` dan `hermes config set mcp_servers.rube.auth oauth`.
2. Gunakan tool `mcp__rube__COMPOSIO_MANAGE_CONNECTIONS` dengan parameter `{"toolkits": [{"name": "googlecalendar", "action": "list"}]}`. (Jangan tambahkan field `reason` di arguments).
3. Jika statusnya `active_connections: 0`, panggil ulang dengan `action: "add"` untuk mendapatkan `redirect_url`.
4. Berikan *link autentikasi* (markdown clickable link) ke user untuk login ke akun Google mereka. Tunggu konfirmasi user sebelum melanjutkan.

## Eksekusi Tool (Composio Runner)
- Tool-tool `GOOGLECALENDAR_*` tidak dipanggil sebagai root tool terpisah, melainkan dieksekusi melalui `mcp__rube__COMPOSIO_MULTI_EXECUTE_TOOL`:
  ```json
  {
    "sync_response_to_workbench": false,
    "tools": [
      {
        "tool_slug": "GOOGLECALENDAR_ACTION_NAME",
        "arguments": { ... }
      }
    ]
  }
  ```
- **Bulk/Parallel Execution:** Saat perlu menambahkan beberapa jadwal yang tidak saling bergantung (misal dari file jadwal semesteran atau banyak tanggal event), batched ke dalam array `tools` dalam satu kali pemanggilan `COMPOSIO_MULTI_EXECUTE_TOOL`. Jangan lakukan pemanggilan tool satu per satu.

## Core Workflows (Alur Kerja)

### 1. Membuat Acara (Schedule Event)
**Alur:** `GOOGLECALENDAR_LIST_CALENDARS` -> `GOOGLECALENDAR_GET_CURRENT_DATE_TIME` -> `GOOGLECALENDAR_CREATE_EVENT`

**Aturan Ketat (Constraints):**
- Waktu mulai (`start_datetime`) WAJIB format **ISO 8601** (contoh: `2026-10-15T14:00:00+07:00`) jika timed.
- **Acara Seharian (All-day Event):** Gunakan `start_date` dan `end_date` (format YYYY-MM-DD), **tanpa** parameter `start_datetime` dan `end_datetime`. Catatan: `end_date` harus eksklusif (H+1 dari tanggal berakhir).
- Zona Waktu (`timezone`) WAJIB format **IANA** (contoh: `Asia/Jakarta`, bukan WIB, EST, atau PST).
- Parameter `event_duration_minutes` MAKSIMAL 59. Jika 60 menit, gunakan `event_duration_hour=1` dan `event_duration_minutes=0`.
- Peserta (`attendees`) hanya menerima alamat email, BUKAN nama.

### Pitfall Import Excel Schedule:
- **Tanggal Excel:** Jika user melampirkan Excel berisi jadwal mingguan dan kolom tanggalnya berupa serial angka (contoh: 46293), ketahuilah itu adalah hari dihitung dari 30 Desember 1899. Gunakan Python `datetime(1899, 12, 30) + timedelta(days=serial)` untuk mendapatkan tanggal pastinya.
- **Jadwal Rutin Mingguan:** Jangan buat satu event per baris Excel jika jadwal tersebut berulang setiap minggu untuk mata kuliah yang sama. Tambahkan opsi `recurrence: ["RRULE:FREQ=WEEKLY;COUNT=15"]` (atau jumlah minggu yang sesuai) pada `GOOGLECALENDAR_CREATE_EVENT`.

### 2. Cek Ketersediaan / Jadwal Kosong (Find Free Slots)
**Alur:** `GOOGLECALENDAR_GET_CURRENT_DATE_TIME` -> `GOOGLECALENDAR_FIND_FREE_SLOTS`

### 3. Hapus / Ubah Acara
**Alur:** `GOOGLECALENDAR_FIND_EVENT` (untuk mendapatkan `event_id` spesifik) -> `GOOGLECALENDAR_PATCH_EVENT` atau `GOOGLECALENDAR_DELETE_EVENT`.
**Penting:** Selalu cari event_id terlebih dahulu. Jangan pernah menebak `event_id`.

### 4. Menghapus / Mengosongkan Kalender
- **Pitfall Primary Calendar:** Kalender utama (`primary`) bawaan akun Google **TIDAK BISA** dihapus atau di-unsubscribe menggunakan `GOOGLECALENDAR_CALENDARS_DELETE` atau `GOOGLECALENDAR_CALENDAR_LIST_DELETE` (Google API akan menolak dengan error 400 / 403 `cannotUnsubscribeFromOwnedCalendar`).
- Jika user meminta untuk menghapus kalender utama atau membersihkan semua agenda di dalamnya, konfirmasikan ke user lalu panggil `GOOGLECALENDAR_CLEAR_CALENDAR` dengan parameter `calendar_id: "primary"`.
- Untuk kalender sekunder buatan user, penghapusan permanen dapat menggunakan `GOOGLECALENDAR_CALENDARS_DELETE` dengan `calendar_id` spesifik (bukan primary).

## Eksekusi Anti-Halusinasi (The RCCO Way)
- **Jangan Mengarang Tanggal/Waktu**: Selalu pastikan tanggal referensi hari ini dengan `GOOGLECALENDAR_GET_CURRENT_DATE_TIME` sebelum menjadwalkan "Jumat depan".
- **Verifikasi**: Setelah acara dibuat atau dihapus, berikan konfirmasi ke user (Judul, Waktu, Link Google Meet jika ada).