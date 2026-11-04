# OPERATIONAL REFERENCE: TDD INSTRUCTION ENGINEERING (writing-skills)
> Panduan rekayasa instruksi berbasis Test-Driven Development (TDD) untuk specialist skill AI: Siklus Red-Green-Refactor, pressure-testing sub-agen, dan penutupan celah kepatuhan (anti-loophole).

---

## 1. Prinsip Utama TDD untuk Skill AI

Menulis instruksi skill pada dasarnya adalah Test-Driven Development yang diterapkan pada dokumentasi operasional:
- **Prinsip Inti**: Jika Anda belum melihat agen AI gagal tanpa instruksi tersebut, Anda belum tahu apakah instruksi yang ditulis mengajarkan hal yang benar.
- **Tujuan**: Menghindari instruksi berbasis asumsi (*wishful thinking*) dan memastikan setiap batasan terbukti mampu mengendalikan model probabilistik di bawah tekanan.

| Konsep TDD Perangkat Lunak | Padanan Rekayasa Skill AI |
|:---|:---|
| **Test Case** | Skenario uji tekanan (*pressure test*) dengan sub-agen |
| **Production Code** | Berkas instruksi `SKILL.md` dan referensi |
| **Test Fails (RED)** | Agen melanggar aturan atau berhalusinasi saat skill absen |
| **Test Passes (GREEN)** | Agen patuh 100% dan menghasilkan deliverable valid saat skill aktif |
| **Refactor** | Memadatkan kata, menghemat token, dan menutup celah rasionalisasi |

---

## 2. Alur Eksekusi 5 Langkah (Red-Green-Refactor Cycle)

### Langkah 1: Rancang Skenario Gagal (Write Failing Test - RED)
- Berikan tugas realistis ke agen tanpa memuat skill baru.
- Catat dengan tepat bagaimana agen menyimpang:
  * Apakah agen membuat asumsi liar?
  * Apakah agen menggunakan sintaksis yang salah?
  * Apa alasan atau pembenaran (*rationalization*) yang diberikan agen saat ditekan?

### Langkah 2: Identifikasi Pola Rasionalisasi Agen
Model AI sering mencari jalan pintas dengan pola khas:
- *"Ini hanya skrip sederhana, tidak perlu validasi."*
- *"Saya langsung asumsikan skema datanya seperti ini."*
- *"Karena dependensi opsional, saya lewati saja langkah ujinya."*
Catat seluruh frasa pembenaran ini untuk dijadikan target batasan keras.

### Langkah 3: Tulis Batasan Keras Terfokus (Make It Pass - GREEN)
- Tambahkan klausul larangan eksplisit pada bagian Constraints (C) di `SKILL.md`.
- Gunakan aturan deterministik, bukan saran moral.
  * Buruk: *"Harap berhati-hati saat mengeksekusi shell."*
  * Baik: *"DILARANG menjalankan sintaks bash `&&` pada host Windows PowerShell. Wajib gunakan pemisah `;`."*
- Jalankan ulang skenario. Pastikan agen patuh secara deterministik.

### Langkah 4: Uji Celah Logika (Loophole Hunting)
- Coba dorong agen melanggar aturan dengan prompt pancingan bertingkat.
- Jika agen menemukan celah baru (misal: memindahkan logika terlarang ke sub-eksekusi lain), perketat batas definisi di `SKILL.md`.

### Langkah 5: Refactor & Optimasi Token Budget
- Ringkas teks instruksi tanpa mengurangi daya kekang (*constraint strength*).
- Pindahkan penjelasan latar belakang panjang ke folder `references/`.
- Pastikan berkas entrypoint tetap di bawah 5.000 token.
