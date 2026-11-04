---
name: always-mcp-hermes
description: "Aturan global Hermes MCP dan background tool execution standar."
---

# Rule: always-mcp-hermes

> [!NOTE]
> Aturan ini bersifat GLOBAL dan aktif setiap saat.

## R (Role / Identity)
- **Peran**: Pengguna aktif MCP Hermes.

## C (Context & Input)
- **Referensi Utama**: Server MCP `hermes` sudah terdaftar dan berjalan di *background*.
- **Masukan Kerja**: Permintaan apapun dari *user* yang membutuhkan alat (*tool*), eksekusi terminal, atau operasi *file*.

## C (Constraints & Guardrails)
- SELALU utamakan memanggil server MCP `hermes` untuk mengeksekusi tugas.
- Jika user meminta untuk melakukan pengecekan, membuat file, mencari referensi, atau tugas kompleks lainnya, delegasikan langsung ke tool MCP `hermes` sebelum mencoba menyelesaikan secara manual.
- Anggap `hermes` sebagai asisten bayangan (co-pilot) utamamu.

## Prosedur Registrasi & Aktivasi MCP Server di Hermes
DILARANG mengedit `config.yaml` langsung menggunakan `patch` atau `write_file` (ditolak oleh security guardrail Hermes: *Refusing to write to Hermes config file*). Selalu gunakan perintah CLI native:
1. Daftarkan server baru dengan auto-konfirmasi tool:
   ```bash
   echo "y" | hermes mcp add <nama_server> --command "<path_biner>" --args <arg1> <arg2>
   # Atau untuk remote HTTP/OAuth:
   echo "y" | hermes mcp add <nama_server> --url "<https_url>" --auth oauth
   ```
   *Catatan*: Piping `echo "y"` wajib digunakan pada `hermes mcp add` untuk melewati prompt interaktif `Enable all N tools? [Y/n/select]:` di lingkungan non-interaktif.
2. Aktifkan server yang sudah terdaftar namun berstatus `disabled`:
   ```bash
   hermes config set mcp_servers.<nama_server>.enabled true
   ```
   *Pitfall*: Jangan gunakan `hermes mcp configure <nama_server>` dari shell agen karena perintah tersebut menuntut TTY interaktif penuh dan gagal di subproses non-interaktif.
3. Uji koneksi dan periksa daftar tool:
   ```bash
   hermes mcp test <nama_server>
   hermes mcp list
   ```
4. Eksekusi langsung di giliran yang sama tanpa meminta pengguna menjalankan `/reload-mcp`:
   *Pitfall*: Di Hermes Desktop, `/reload-mcp` berada di kategori `advanced` dan disembunyikan dari menu *autocomplete* slash standar. Selain itu, memanggil `discover_mcp_tools()` secara global akan mencoba menghubungkan ulang seluruh server (dan tertahan pada server yang belum login/mati). Hubungkan HANYA server target menggunakan `_discover_and_register_server`:
   ```bash
   python -c "
   import sys
   sys.path.insert(0, r'C:\Users\HP\AppData\Local\hermes\hermes-agent')
   from tools import mcp_tool_loop as _loop
   from tools.mcp_tool_discovery import _discover_and_register_server
   from tools.registry import registry
   _loop._ensure_mcp_loop()
   _loop._run_on_mcp_loop(lambda: _discover_and_register_server('<nama_server>', {<config_dict>}), timeout=30.0)
   print(registry.dispatch('mcp__<nama_server>__<NAMA_TOOL>', {<argumen_json>}))
   "
   ```

## Penanganan Galat OAuth & Dynamic Client Registration Basi ("Unrecognized client_id")
Server remote OAuth MCP (seperti Supabase) secara berkala memangkas pendaftaran dynamic client registration (RFC 7591). Ketika dipangkas, Hermes terus memutar ulang `client_id` lama yang tersimpan di disk sehingga memicu galat `{"message":"Unrecognized client_id"}` terus-menerus di peramban atau pop-up.
1. Bersihkan kredensial klien yang basi untuk memicu registrasi ulang:
   ```bash
   rm -f "$LOCALAPPDATA/hermes/mcp-tokens/<nama_server>.client.json"
   ```
2. Minta otorisasi ulang via CLI:
   ```bash
   hermes mcp login <nama_server>
   ```
3. Jika server tidak lagi digunakan atau ingin dimatikan permanen:
   ```bash
   hermes config set mcp_servers.<nama_server>.enabled false
   # Atau hapus server dari konfigurasi:
   hermes mcp rm <nama_server>
   ```

## Prosedur Koneksi OAuth Aplikasi via Composio (`rube`)
Server `rube` terhubung ke endpoint `https://connect.composio.dev/mcp` (`auth: oauth`):
1. Panggil `mcp__rube__COMPOSIO_SEARCH_TOOLS` dengan `queries: [{"use_case": "...", "known_fields": "toolkit: <nama_app>"}]` untuk memeriksa `toolkit_connection_statuses` dan mengambil `session.id`.
2. Jika `has_active_connection: false`, panggil `mcp__rube__COMPOSIO_MANAGE_CONNECTIONS` dengan `toolkits: ["<nama_app>"]` dan `session_id` dari langkah 1.
3. Tampilkan `redirect_url` (`https://connect.composio.dev/link/...`) sebagai tautan Markdown yang bisa diklik pengguna (berlaku 10 menit). Jangan panggil tool aksi aplikasi sebelum pengguna menyelesaikan otorisasi OAuth.
4. Setelah aktif, eksekusi aksi melalui `mcp__rube__COMPOSIO_MULTI_EXECUTE_TOOL` dengan menyertakan `tools: [{"tool_slug": "...", "arguments": {...}}]`, `session_id`, `sync_response_to_workbench: False`, `current_step`, dan `current_step_metric`.
   *Pitfall*: Untuk toolkit `linkedin`, cakupan OAuth resmi (`w_member_social`) hanya mendukung baca profil dasar (`LINKEDIN_GET_MY_INFO`) dan manajemen post/komentar/gambar (`LINKEDIN_CREATE_LINKED_IN_POST`, `LINKEDIN_DELETE_POST`, `LINKEDIN_GET_COMPANY_INFO`). API resmi tidak menyediakan endpoint untuk mengedit bagian profil seperti Experience atau Education; gunakan otomatisasi browser lokal untuk mutasi bagian profil tersebut.

## O (Output Format)
- Tidak perlu menjelaskan bahwa Anda memanggil Hermes. Langsung panggil *tool* dari MCP `hermes` dan berikan jawaban akhir ke *user* berdasarkan hasil dari Hermes.
