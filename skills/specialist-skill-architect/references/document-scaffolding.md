# OPERATIONAL REFERENCE: DOCUMENT EXTRACTION & SCAFFOLDING (claude-skills & skill-creator)
> Panduan ekstraksi materi domain mentah (dokumentasi teknis, API, repositori) menjadi arsitektur skill terstruktur, hemat token, dan siap pakai.

---

## 1. Aturan Emas Hemat Konteks (Token Economy)

Konteks window adalah sumber daya bersama. Setiap baris di `SKILL.md` bersaing dengan riwayat percakapan, instruksi sistem, dan permintaan pengguna.
- **Asumsi Dasar**: LLM sudah sangat cerdas dan memahami konsep umum. Jangan jelaskan teori dasar dari nol.
- **Prinsip Eliminasi**: Tanyakan pada setiap paragraf: *"Apakah model AI benar-benar butuh penjelasan ini untuk bekerja, atau cukup disajikan contoh pola langsung?"*
- **Tingkat Kebebasan (Degrees of Freedom)**:
  * **Tinggi (Teks Panduan)**: Untuk tugas heuristik dengan banyak solusi valid.
  * **Sedang (Pseudocode / Pola Regex)**: Untuk alur standar dengan sedikit variasi.
  * **Ketat (Skrip Deterministik / CLI)**: Untuk operasi rapuh, format data ketat, atau urutan tanpa toleransi error.

---

## 2. Alur Ekstraksi Materi Mentah Menjadi Skill

### Langkah 1: Isolasi Pola Frekuensi Tinggi (Quick Reference)
- Dari ratusan halaman dokumentasi atau ribuan baris kode, pilih maksimal 10 sampai 20 pola yang paling sering dieksekusi.
- Sajikan sebagai blok teks siap salin atau perintah satu baris.
- Batasi Quick Reference agar tidak lebih dari 20 pola.

### Langkah 2: Pisahkan Dokumen Panjang ke `references/`
- Jangan pernah menumpuk materi panduan panjang di `SKILL.md` (*anti-pattern: Doc Dump*).
- Pecah materi pendukung ke berkas modular di direktori `references/`:
  * `references/api-specs.md` untuk rincian endpoint dan skema payload.
  * `references/troubleshooting.md` untuk penanganan galat langka.
  * `references/anti-patterns.md` untuk hal-hal yang dilarang.
- Sertakan `references/index.md` sebagai daftar isi navigasi.

### Langkah 3: Sertakan Minimal 3 Contoh Nyata Reproduktif
Setiap skill wajib memiliki minimal 3 contoh konkret:
- **Input**: Bentuk masukan nyata pengguna atau format data mentah.
- **Steps**: Langkah eksekusi berurutan yang diambil agen.
- **Expected Output / Acceptance**: Kriteria keberhasilan yang dapat diverifikasi (*Definition of Done*).

### Langkah 4: Tentukan Batas Lingkup (Not For / Boundaries)
Skill wajib menyatakan apa yang TIDAK boleh dilakukan agar tidak terjadi salah panggil (*misfire*):
- Bukan untuk tugas domain X (arahkan ke skill Y).
- Kebutuhan input wajib: jika parameter belum lengkap, wajib minta 1 sampai 3 pertanyaan klarifikasi sebelum mulai.
