# OPERATIONAL REFERENCE: SKILL FILE SPECIFICATION & DIRECTORY ARCHITECTURE
> Standar spesifikasi teknis penulisan berkas specialist skill AI berbasis format RCCO dan konvensi Agent Skills Open Standard (`agentskills.io`).

---

## 1. Prinsip Desain: Deterministic, Human-Readable & Machine-Parsable

Sebuah specialist skill bukan sekadar kumpulan instruksi prompt acak; skill adalah **Paket Prosedur Operasional Standar (Standard Operating Procedure Package)** yang harus dapat diurai secara deterministik oleh mesin runtime AI dan mudah dipelihara oleh pengembang sistem manusia.

Tiga prinsip utama spesifikasi:
1. **Metadata Terstandarisasi**: Frontmatter YAML wajib mematuhi skema parser platform target tanpa field ilegal.
2. **Keterbacaan Bertingkat (Progressive Disclosure)**: Berkas entrypoint hanya memuat informasi pemicu dan ringkasan komando, sedangkan detail teknis didelegasikan ke modul referensi.
3. **Pemisahan Logika dan Bukti**: Berkas instruksi dipisahkan secara tegas dari berkas contoh implementasi dan kasus uji regresi.

---

## 2. Skema Spesifikasi Berkas `SKILL.md`

Setiap berkas `SKILL.md` wajib diawali dengan blok frontmatter YAML yang ditutup tanda tiga strip (`---`) dan dilanjutkan dengan tubuh dokumen berformat Markdown:

```markdown
---
name: [nama-skill-kebab-case]
description: "Use when user says '[pemicu-1]', '[pemicu-2]', atau '[pemicu-n]'. [Penjelasan fungsional ringkas dan tegas]."
---

# [Judul Resmi Skill] ([nama-skill-kebab-case])

## R (Role & Identity)
- **Peran**: [Identitas profesional spesialis].
- **Keahlian Inti**: [Rincian domain keahlian dan kompetensi utama].
- **Filosofi Kerja**: [Prinsip rekayasa, standar etika, dan disiplin verifikasi].
- **Standar Bahasa**: [Aturan penggunaan bahasa baku EYD V / KBBI dan larangan em/en dash].

---

## C (Context & Operating Modes)
[Kondisi aktivasi dan pembagian mode kerja dinamis].

### [Mode Operasional 1]
- **Tujuan**: [Deskripsi sasaran mode].
- **Alur Kerja**: [Tahapan eksekusi langkah demi langkah].

### [Mode Operasional 2]
- **Tujuan**: [Deskripsi sasaran mode].
- **Alur Kerja**: [Tahapan eksekusi langkah demi langkah].

---

## C (Constraints & Architectural Standards)
[Batasan mutlak yang mengikat perilaku operasional agen].

### 1. Batasan Ruang Lingkup (Scope Boundaries)
- **In-Scope**: [Daftar tugas yang menjadi tanggung jawab resmi].
- **Hard Out-of-Scope**: [Daftar tugas yang DILARANG KERAS disentuh oleh skill ini].

### 2. Standar Arsitektur & Kepatuhan Proyek
- [Pola arsitektur default, aturan modular monolith, atau kontrak data].

### 3. Protokol Keamanan & Sanitasi Privasi (Zero Leakage)
- [Sensor 8-Class PII, larangan git push otomatis tanpa izin, proteksi prompt injection].

---

## O (Output Format & Definition of Done)
[Format luaran artefak dan kriteria penyelesaian tugas sah].

### 1. Struktur Deliverable Wajib
- [Rincian berkas fisik di disk yang harus dihasilkan].

### 2. Universal Definition of Done (DoD)
- [Daftar periksa penentu kelulusan sebelum deliverable diserahkan ke pengguna].
```

---

## 3. Aturan Validasi Metadata Frontmatter YAML

| Atribut YAML | Aturan Sintaksis Wajib | Batasan & Larangan |
|:---|:---|:---|
| `name` | Huruf kecil alfanumerik dipisahkan tanda strip tunggal (`kebab-case`). | Panjang 1 sampai 64 karakter. Dilarang menggunakan spasi, garis bawah (`_`), huruf kapital, atau tanda strip ganda (`--`). Wajib identik dengan nama folder pembungkus. |
| `description` | Teks string diapit tanda petik ganda (`"`). Diawali dengan frasa pemicu yang jelas (*"Use when user says..."*). | Maksimal 1.024 karakter. Dilarang menyertakan karakter baris baru (*newlines*) yang merusak format satu baris YAML. Wajib memuat kata kunci pemicu spesifik. |

---

## 4. Konvensi Penamaan & Pengelompokan Berkas Pendukung

1. **Direktori `references/` (Modul Prosedural Mendalam)**:
   - Digunakan untuk panduan teknis yang memiliki panjang lebih dari 300 kata.
   - Penamaan berkas: Huruf kecil kebab-case berakhiran `.md` (contoh: `references/quality-assurance.md`).
   - Format: Wajib memuat judul H1, ringkasan operasional H2, tabel checklist, dan diagram alir berbasis teks atau Mermaid.
2. **Direktori `examples/` (Contoh Nyata yang Dapat Direproduksi)**:
   - Digunakan untuk memberikan demonstrasi konkret masukan dan keluaran (*few-shot exemplar*).
   - Wajib memuat tiga tingkatan: `simple-skill.md`, `modular-skill.md`, dan `complex-skill.md`.
3. **Direktori `tests/` (Suite Pengujian & Validasi)**:
   - `regression-cases.md`: Menyimpan minimal 10 sampai 18 skenario pengujian fungsional dan penanganan galat.
   - `validation-checklist.md`: Menyimpan 30 butir audit kesiapan produksi (*production-readiness audit*).
4. **Berkas `CHANGELOG.md` (Riwayat Versi Semantik)**:
   - Mengikuti konvensi *Keep a Changelog* dan *Semantic Versioning (MAJOR.MINOR.PATCH)*.
   - Mencatat penambahan fitur (*Added*), modifikasi (*Changed*), perbaikan (*Fixed*), dan penghentian (*Deprecated*).