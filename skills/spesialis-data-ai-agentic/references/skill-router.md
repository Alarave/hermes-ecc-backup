# Skill Router (Umbrella Skill)

## Fungsi Utama
Sebagai agen penghubung (router) ke berbagai skill spesifik. Pengguna cukup mendeskripsikan masalah, dan Anda (AI) wajib mengecek daftar skill internal lalu mengeksekusinya tanpa pengguna perlu menyebut nama skill-nya.

## Instruksi Eksekusi
1. Saat dipanggil, evaluasi permintaan pengguna.
2. Identifikasi area tugas (misal: Web Scraping, Data Science, Backend, Frontend, Docs).
3. Cari nama skill terkait di daftar `Available skills` dari sistem.
4. Gunakan `view_file` pada `SKILL.md` dari skill yang relevan untuk membaca instruksi spesifiknya.
5. Kerjakan tugas sesuai instruksi skill spesifik tersebut.

## Keuntungan
- Pengguna tidak perlu menghafal ratusan skill.
- AI otomatis mendelegasikan tugas ke spesialis.
