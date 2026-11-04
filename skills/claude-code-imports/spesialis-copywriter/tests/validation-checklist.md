# DAFTAR PERIKSA KESIAPAN PRODUKSI (PRODUCTION VALIDATION CHECKLIST)

Daftar periksa 30 butir audit kesiapan produksi spesialis-copywriter sebelum skill diintegrasikan ke lingkungan kerja utama dan dialokasikan ke Chief AI Orchestrator (Pram).

---

## 1. Audit Integritas Berkas & Direktori (Butir 1-6)
- [x] **01**: Berkas entrypoint `SKILL.md` tersimpan fisik di `skills/spesialis-copywriter/SKILL.md`.
- [x] **02**: Nama skill pada frontmatter YAML identik dengan nama direktori (`spesialis-copywriter`).
- [x] **03**: Format frontmatter memuat atribut `name` dan `description` satu baris yang valid.
- [x] **04**: Deskripsi frontmatter memuat kata kunci pemicu eksplisit (*"Use when user says..."*).
- [x] **05**: Seluruh berkas referensi pendukung tersedia di direktori `references/`.
- [x] **06**: Seluruh berkas contoh implementasi tersedia di direktori `examples/`.

---

## 2. Kepatuhan Arsitektur RCCO & Kaidah Bahasa (Butir 7-12)
- [x] **07**: Memuat seksi R (Role & Identity) yang mendefinisikan persona profesional secara tegas.
- [x] **08**: Memuat seksi C (Context & Operating Modes) dengan 4 mode operasional mandiri.
- [x] **09**: Memuat seksi C (Constraints & Standards) yang mengikat batasan dan aturan main.
- [x] **10**: Memuat seksi O (Output Format & DoD) dengan format luaran dan kriteria selesai terukur.
- [x] **11**: Seluruh teks instruksi menggunakan bahasa Indonesia baku mematuhi EYD V dan KBBI.
- [x] **12**: Nol karakter tanda pisah panjang em dash atau en dash di seluruh berkas.

---

## 3. Ketahanan Sistem Anti-AI Slop (Butir 13-18)
- [x] **13**: Memiliki daftar hitam frasa pembuka bertele-tele (throat-clearing).
- [x] **14**: Memiliki daftar hitam kata sifat superlatif kosong tanpa pembuktian data.
- [x] **15**: Menegakkan aturan dominasi kalimat aktif (>85% porsi naskah).
- [x] **16**: Mewajibkan variasi ritme kalimat (paduan kalimat pendek dan sedang).
- [x] **17**: Mewajibkan penyertaan mekanisme konkret dan angka satuan nyata.
- [x] **18**: Menerapkan Uji Penggantian Produk (The Replacement Test) pada setiap klaim.

---

## 4. Kepatuhan Ejaan Pemasaran & Regulasi (Butir 19-24)
- [x] **19**: Penegakan pemisahan kata depan *di* dan perangkaian awalan *di-*.
- [x] **20**: Penegakan aturan penulisan partikel *pun* (pisah vs padu 12 kata).
- [x] **21**: Penegakan aturan bentuk terikat asing/Sanskerta (serangkai tanpa spasi).
- [x] **22**: Format mata uang Rupiah ditulis baku (*Rp150.000* tanpa spasi).
- [x] **23**: Kepatuhan penuh pada Etika Pariwara Indonesia terkait klaim nomor satu/terbaik.
- [x] **24**: Glosarium padanan istilah pemasaran dan produk digital terstandarisasi.

---

## 5. Privasi, Keamanan, & Integrasi Orkestrasi (Butir 25-30)
- [x] **25**: Protokol Zero Leakage aktif (penyensoran 8-Class PII menjadi `[REDACTED]`).
- [x] **26**: Nol kebocoran path direktori Windows lokal milik pengguna.
- [x] **27**: Terdaftar secara resmi pada matriks audit sub-agent Chief AI Orchestrator (Pram).
- [x] **28**: Memiliki alias perintah cepat di `skills/commands/spesialis-copywriter.md`.
- [x] **29**: Memiliki berkas pengujian otomatis `tests/test_spesialis_copywriter.py`.
- [x] **30**: Lolos uji linter resmi `scripts/audit_incoming_skills.py` dengan skor 100/100.