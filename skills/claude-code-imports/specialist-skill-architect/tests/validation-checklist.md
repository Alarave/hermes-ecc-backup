# DAFTAR PERIKSA VALIDASI KELAYAKAN RILIS SPECIALIST SKILL
> Daftar periksa audit komprehensif 30 butir yang wajib divalidasi oleh Specialist Skill Architect sebelum sebuah specialist skill dinyatakan lulus dan siap dioperasikan di produksi.

---

## Bagian A: Metadata & Sintaks Frontmatter YAML (Butir 1 s.d. 6)
- [ ] **1. Kebab-Case Valid**: Atribut `name` ditulis murni dalam huruf kecil alfanumerik dipisahkan strip tunggal (`kebab-case`).
- [ ] **2. Keselarasan Nama Folder**: Nilai atribut `name` identik 100% dengan nama direktori pembungkusnya.
- [ ] **3. Format Description Valid**: Atribut `description` diapit tanda petik ganda (`"`), tidak melebihi 1.024 karakter, dan berada dalam satu baris.
- [ ] **4. Frasa Pemicu Eksplisit**: Deskripsi diawali dengan pola baku: *"Use when user says '[kata-kunci-1]', '[kata-kunci-2]'..."*.
- [ ] **5. Nol Karakter Karriage Ilegal**: Berkas bersih dari karakter kontrol yang merusak pembacaan parser YAML.
- [ ] **6. Penutup Tiga Strip**: Blok frontmatter ditutup dengan tepat menggunakan baris `---`.

---

## Bagian B: Struktur Arsitektur & Kepatuhan RCCO (Butir 7 s.d. 12)
- [ ] **7. Keberadaan Blok R (Role)**: Memuat definisi kepribadian profesional, lingkup keahlian, dan standar etika kerja.
- [ ] **8. Keberadaan Blok C (Context)**: Menjelaskan kondisi aktivasi dan pembagian mode operasional kerja dinamis.
- [ ] **9. Keberadaan Blok C (Constraints)**: Menetapkan batasan tegas ruang lingkup (In-Scope vs Hard Out-of-Scope).
- [ ] **10. Keberadaan Blok O (Output Format)**: Mendefinisikan struktur luaran fisik dan kriteria penyelesaian tugas (DoD).
- [ ] **11. Efisiensi Ukuran Berkas**: Berkas `SKILL.md` utama berukuran ringkas (< 5.000 token) dan mendelegasikan rincian ke `references/`.
- [ ] **12. Kepatuhan Bahasa Baku**: Naskah ditulis dalam bahasa Indonesia baku mematuhi EYD V dan KBBI tanpa kata klise AI-slop.

---

## Bagian C: Integritas Modul Referensi & Progressive Disclosure (Butir 13 s.d. 18)
- [ ] **13. Ketersediaan Berkas Fisik**: Seluruh berkas yang terdaftar di blok `Linked References` ada secara fisik di disk.
- [ ] **14. Struktur Berkas Referensi Baku**: Setiap modul referensi diawali dengan judul H1 dan tujuan operasional yang jelas.
- [ ] **15. Pemisahan Topik Mandiri**: Berkas referensi tidak saling tumpang tindih dan menerapkan prinsip tanggung jawab tunggal.
- [ ] **16. Bebas Siklus Ketergantungan**: Referensi tidak saling menautkan satu sama lain dalam siklus melingkar yang membingungkan.
- [ ] **17. Keterbacaan Bertahap**: Modul referensi hanya dimuat saat fase kerja terkait aktif, bukan sekaligus di awal.
- [ ] **18. Pemeliharaan Berkas Contoh**: Menyertakan contoh konkret masukan dan keluaran pada direktori `examples/`.

---

## Bagian D: Keamanan Data, Privasi & Kepatuhan Git (Butir 19 s.d. 24)
- [ ] **19. Nol Kebocoran Path Komputer Lokal**: Bebas dari penulisan path absolut lokal (`C:\...` atau `E:\...`).
- [ ] **20. Nol Kebocoran Kredensial & PII**: Seluruh 8 kategori PII telah disamarkan menjadi `[REDACTED]`.
- [ ] **21. Pengasingan File Konfigurasi**: Rahasia disimpan di `.env` lokal yang terdaftar di `.gitignore`; hanya `.env.example` yang di-track.
- [ ] **22. Proteksi Prompt Injection**: Seluruh data masukan eksternal diperlakukan sebagai Data Payload pasif yang terisolasi.
- [ ] **23. Kepatuhan Konvensi Commit**: Seluruh komit lokal menggunakan prefix baku bahasa Indonesia (`fitur:`, `perbaikan:`, dll).
- [ ] **24. Larangan Git Push Otomatis**: Dilarang menjalankan perintah `git push` tanpa izin atau instruksi eksplisit dari Project Owner.

---

## Bagian E: Verifikasi Linter & Pengujian Regresi (Butir 25 s.d. 30)
- [ ] **25. Lolos Audit Linter 100/100**: Meraih skor sempurna 100/100 pada pengujian linter resmi `scripts/audit_incoming_skills.py`.
- [ ] **26. Bebas Tanda Pisah Em/En Dash**: Naskah 100% bersih dari tanda pisah panjang em-dash atau en-dash.
- [ ] **27. Ketersediaan Kasus Uji**: Direktori `tests/regression-cases.md` memuat minimal 18 skenario pengujian representatif.
- [ ] **28. Pembedaan Status Pembuktian**: Hasil uji membedakan secara tegas antara status `VERIFIED`, `SIMULATED`, dan `BLOCKED`.
- [ ] **29. Verifikasi Kesiapan Fallback**: Modul `tool-routing.md` mendokumentasikan jalur cadangan jika tools utama gagal.
- [ ] **30. Pembaruan Berkas CHANGELOG**: Riwayat perubahan versi dicatat secara rapi dan akurat pada `CHANGELOG.md`.