# OPERATIONAL REFERENCE: STRATEGY SELECTION ENGINE & DECISION MATRIX
> Panduan operasional komprehensif Specialist Skill Architect untuk memilih strategi rekayasa terbaik di antara 7 strategi standar (REUSE, EXTEND, COMBINE, CREATE, ADAPT, REFACTOR, DEPRECATE).

---

## 1. Prinsip Minimal Disrupsi & Ketepatan Solusi

Setiap perubahan pada ekosistem skill memiliki biaya kognitif, biaya pemeliharaan, dan risiko regresi. Specialist Skill Architect tidak boleh memilih strategi berdasarkan preferensi pribadi atau kebiasaan semata. Pemilihan strategi wajib ditentukan secara objektif melalui **Evaluasi Kuantitatif Kesenjangan Kapabilitas (*Capability Gap Scoring*)**.

Prinsip pemandu:
- Jangan membuat skill baru jika memperluas skill yang ada menghasilkan arsitektur yang lebih kohesif.
- Jangan menggabungkan skill jika penggabungan tersebut menciptakan monolit instruksi yang membingungkan.
- Jangan mempertahankan skill usang yang memicu tabrakan pemicu dan memboroskan konteks.

---

## 2. Taksonomi 7 Strategi Rekayasa Specialist Skill

```text
                                [Kebutuhan Kapabilitas Baru]
                                              │
                     ┌────────────────────────┴────────────────────────┐
                     ▼                                                 ▼
          [Kapabilitas Sudah Ada?]                           [Kapabilitas Belum Ada?]
          ├── Ya (Kesesuaian >= 90%) ──► REUSE               ├── Diperlukan dari Nol ──────► CREATE
          ├── Butuh Tambahan Fitur  ──► EXTEND              └── Ada Rujukan Luar/GitHub ──► ADAPT
          ├── Ada Fragmentasi Domain ──► COMBINE
          ├── Terlalu Kusut/Membengkak ─► REFACTOR
          └── Tidak Lagi Relevan ─────► DEPRECATE
```

### 1. REUSE (Gunakan Kembali Tanpa Modifikasi)
- **Definisi**: Mengarahkan eksekusi ke skill yang sudah terpasang karena telah mencakup 90% atau lebih kebutuhan tugas.
- **Kondisi Pemilihan**: Ada kecocokan pemicu yang tepat, batasan kerja selaras, dan output yang dihasilkan memenuhi ekspektasi pengguna.
- **Tindakan**: Dokumentasikan nama skill ke dalam Task Ledger dan orkestrasikan eksekusi tanpa mengubah berkas apapun.

### 2. EXTEND (Perluas Kemampuan Eksisting)
- **Definisi**: Menambahkan bab referensi baru, skrip pembantu, atau mode operasional baru ke dalam skill yang sudah ada.
- **Kondisi Pemilihan**: Domain keahlian selaras secara kohesif, namun membutuhkan prosedur tambahan (contoh: menambahkan dukungan format ekspor baru atau panduan regulasi kampus baru).
- **Tindakan**: Tambahkan berkas panduan di direktori `references/` skill terkait, perbarui deskripsi pemicu jika perlu, dan jalankan uji regresi.

### 3. COMBINE (Gabungkan Dua Skill atau Lebih)
- **Definisi**: Mengonsolidasikan dua skill atau lebih yang memiliki irisan fungsional besar atau fragmentasi domain menjadi satu skill komprehensif.
- **Kondisi Pemilihan**: Terdapat dua skill yang sering dipanggil bersamaan, terjadi tabrakan kata pemicu, atau salah satu skill hanya berfungsi sebagai pembungkus kosong (*wrapper stub*).
- **Contoh Nyata**: Penggabungan `spesialis-laporan-akademik` ke dalam `spesialis-research-akademik`.
- **Tindakan**: Satukan referensi, perluas deskripsi pemicu pada skill penerima, hapus atau arsipkan direktori skill lama, dan catat riwayat migrasi.

### 4. CREATE (Bangun Skill Baru dari Nol)
- **Definisi**: Merancang dan membangun specialist skill baru lengkap dengan direktori dan berkas pendukungnya.
- **Kondisi Pemilihan**: Kebutuhan domain benar-benar baru, belum ada skill lokal yang relevan, dan perannya berdiri sendiri sebagai keahlian khusus (*distinct specialized domain*).
- **Tindakan**: Jalankan alur Mode CREATE 12 langkah, pastikan kepatuhan RCCO, bangun suite pengujian regresi, dan pastikan lolos audit linter 100/100.

### 5. ADAPT (Adaptasi Pola Eksternal GitHub)
- **Definisi**: Mengambil metodologi, alur penalaran, atau skema dari repositori luar dan menulisnya kembali sesuai standar lokal.
- **Kondisi Pemilihan**: Repositori GitHub terbukti unggul secara empiris, berlisensi terbuka, namun tidak kompatibel jika diinstal secara mentah di lingkungan Windows host.
- **Tindakan**: Lakukan distilasi pola desain, buang dependensi Linux yang tidak perlu, tulis ulang dalam format RCCO bahasa Indonesia baku, dan sertakan atribusi sumber.

### 6. REFACTOR (Tata Ulang Struktur Internal)
- **Definisi**: Merestrukturisasi isi berkas skill tanpa menambah atau mengubah perilaku luarnya.
- **Kondisi Pemilihan**: Berkas `SKILL.md` membengkak melampaui batas efisiensi, instruksi bercampur aduk antara panduan teknis dan filosofi, atau ditemukan pelanggaran tipografi (tanda pisah em/en dash).
- **Tindakan**: Pindahkan teks mendalam ke berkas modular di `references/`, terapkan progressive disclosure, dan bersihkan tata bahasa.

### 7. DEPRECATE (Hentikan Penggunaan Skill Usang)
- **Definisi**: Menghentikan operasional skill yang sudah tidak relevan, usang teknologinya, atau fungsinya telah sepenuhnya diserap oleh skill lain.
- **Kondisi Pemilihan**: Skill menggunakan API yang sudah dimatikan (*sunset*), digantikan oleh standar yang lebih mutakhir, atau menyebabkan tabrakan routing.
- **Tindakan**: Berikan label `[DEPRECATED]` pada frontmatter, arahkan pemicu ke skill penerus, hapus berkas fisik dari direktori aktif jika disetujui, dan simpan log arsip.

---

## 3. Matriks Pembobotan Pemilihan Strategi (Quantitative Scoring Matrix)

Ketika timbul keraguan dalam memilih antara EXTEND, COMBINE, atau CREATE, arsitek menghitung skor pembobotan evaluasi:

| Kriteria Evaluasi | Bobot | Pertanyaan Penentu |
|:---|:---:|:---|
| **Kohesi Domain (Domain Cohesion)** | 30% | Apakah kemampuan baru memiliki tujuan bisnis dan konteks kerja yang sama dengan skill yang sudah ada? (Skor tinggi = EXTEND/COMBINE, Skor rendah = CREATE). |
| **Beban Konteks Token (Context Load)** | 25% | Jika kemampuan digabungkan ke skill lama, apakah berkas `SKILL.md` akan membengkak dan menurunkan fokus agen? (Skor tinggi = CREATE terpisah, Skor rendah = EXTEND via referensi). |
| **Kemandirian Peran (Role Independence)**| 20% | Apakah pekerjaan ini dijalankan oleh profil profesional yang berbeda dalam tim engineering? (Misal: DevOps vs Data Scientist = CREATE terpisah). |
| **Kompleksitas Ketergantungan** | 15% | Apakah penambahan kemampuan membawa dependensi pustaka atau tools yang bertentangan dengan skill lama? |
| **Risiko Regresi Fungsional** | 10% | Seberapa besar risiko perubahan merusak alur kerja lama yang sudah stabil? |

### Formula Skor Keputusan:
$$	ext{Index Kohesi} = \sum (	ext{Skor Kriteria} 	imes 	ext{Bobot})$$
- Jika Index Kohesi >= 75%: Pilih **EXTEND** pada skill yang sudah ada.
- Jika Index Kohesi berada di antara 45% s.d. 74%: Evaluasi apakah kedua skill perlu di-**COMBINE**.
- Jika Index Kohesi < 45%: Pilih **CREATE** sebagai skill spesialis baru.