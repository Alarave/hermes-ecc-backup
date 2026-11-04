# OPERATIONAL REFERENCE: TOOL AND CAPABILITY ROUTING ENGINE
> Panduan operasional komprehensif Specialist Skill Architect untuk memetakan kapabilitas skill ke tools fisik runtime, mengelola izin operasi, menegakkan rantai fallback, dan mencegah fabrikasi eksekusi alat (*zero fabricated execution*).

---

## 1. Prinsip Realisme Alat: Fakta Mengalahkan Halusinasi

Salah satu kegagalan fatal pada agen kecerdasan buatan adalah **Halusinasi Eksekusi Alat (*Fabricated Tool Execution*)**. Agen sering kali mengklaim di jendela obrolan bahwa mereka telah *"menjalankan unit test dan hasilnya lulus"* atau *"membuat file di server"*, padahal pada kenyataannya fungsi tool tersebut tidak pernah dipanggil, mengalami galat timeout, atau bahkan tool tersebut tidak ada di sistem.

Specialist Skill Architect menegakkan doktrin **Realisme Alat Mutlak (*Absolute Tool Realism*)**:
- Agen HANYA boleh mengklaim sebuah tindakan berhasil jika didukung oleh log eksekusi terminal riil dengan kode keluar 0 (*exit code 0*), bukti perubahan berkas di disk, atau tangkapan respons API otentik.
- Jika sebuah tool tidak tersedia, mengalami galat izin, atau gagal koneksi, agen WAJIB menyatakan status tersebut secara jujur sebagai `BLOCKED` atau `FAILED` dan mengaktifkan prosedur penanganan cadangan (*fallback*).

---

## 2. Klasifikasi 4 Status Ketersediaan Kapabilitas

Arsitek membagi seluruh kapabilitas sistem ke dalam 4 kategori status operasional:

| Kategori Status | Definisi Operasional | Perilaku Agen yang Diwajibkan |
|:---|:---|:---|
| **AVAILABLE** | Tool terpasang, terverifikasi, dan dapat dipanggil langsung tanpa hambatan (misal: `terminal`, `read_file`, `write_file`, `patch`). | Eksekusi langsung secara efisien dan simpan bukti keluaran (*stdout/stderr*). |
| **PERMISSION_GATED**| Tool tersedia tetapi membutuhkan konfirmasi izin pengguna (misal: perintah destruktif `rm`, modifikasi konfigurasi sistem, atau `git push`). | Hentikan eksekusi, sajikan rincian dampak, dan minta persetujuan eksplisit. |
| **CONCEPTUAL_ONLY** | Prosedur logis yang dijelaskan dalam dokumentasi tetapi tidak memiliki antarmuka tool mandiri (misal: review kode visual manual). | Jalankan sebagai penalaran internal tanpa berpura-pura memanggil tool eksternal fiktif. |
| **UNAVAILABLE** | Tool tidak terpasang, server down, atau dependensi sistem operasi tidak mendukung (misal: daemon Linux pada host Windows). | Berikan peringatan kegagalan secara transparan dan aktifkan rantai fallback. |

---

## 3. Matriks Pemetaan Tools & Rantai Fallback

Setiap kali specialist skill dirancang, arsitek memetakan kebutuhan fungsinya ke tool fisik beserta jalur cadangannya:

| Kebutuhan Fungsional | Tool Utama (Primary Tool) | Kondisi Kegagalan | Tool Cadangan (Fallback Strategy) |
|:---|:---|:---|:---|
| **Inspeksi Berkas Teks** | `read_file` (dengan line offset) | File tidak ditemukan / format biner | Gunakan `search_files` untuk mencari lokasi berkas, atau utilitas CLI via `terminal`. |
| **Pencarian Kode Cepat** | `search_files` (Ripgrep engine) | Pola regex terlalu luas | Batasi pencarian menggunakan ekstensi berkas spesifik (`file_glob: "*.md"`). |
| **Pengeditan Berkas Presisi** | `patch` (Fuzzy matching) | Pola teks unik tidak cocok (*patch rejection*) | Baca ulang isi berkas secara utuh via `read_file`, lalu tulis ulang via `write_file`. |
| **Penulisan Berkas Utuh** | `write_file` (Atomic write) | Gagal izin / folder belum ada | Buat folder induk secara manual via perintah `mkdir -p` di terminal sebelum menulis ulang. |
| **Eksekusi Pengujian & Skrip** | `terminal` (MSYS bash) | Perintah timeout / dependensi hilang | Catat status `BLOCKED`, simpan log galat terminal, dan laporkan dependensi yang kurang. |
| **Penelitian Literatur Luar** | `web_search` & `web_extract` | Akses internet terputus / HTTP 403 | Gunakan berkas korpus teks lokal di direktori `cache/` atau tandai sitasi `[UNVERIFIED_OFFLINE]`. |
| **Pembuatan Diagram Vektor** | Engine lokal `figgenie-paper-diagram` | Dependensi compiler grafis hilang | Ekspor draf diagram ke format teks Mermaid murni sebagai visualisasi alternatif. |