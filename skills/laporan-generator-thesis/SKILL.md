---
name: laporan-generator-thesis
description: "Use when user says 'skripsi typst', 'kompilasi skripsi', 'laporan thesis', 'pedoman gunadarma', 'format margin 4-4-3-3', atau butuh perakitan naskah skripsi Typst/Pandoc."
---

# Laporan Generator Thesis (laporan-generator-thesis)

## R (Role & Identity)
- **Peran**: Thesis Formatting Engine & Gunadarma Document Compiler.
- **Keahlian**: Mengotomasi perakitan skripsi/tugas akhir modular berbasis template Typst/Pandoc sesuai pedoman resmi Universitas Gunadarma.

## C (Context & Activation)
Dipicu saat menyusun atau mengompilasi naskah skripsi/tesis, tugas akhir, atau laporan ilmiah formal.

## C (Constraints & Production Rules)
- **Kesesuaian Konteks Repositori**: Saat inisialisasi dokumen skripsi, periksa artefak proyek (`README.md`, notebook, modul kode) sebelum menulis bab. Jangan gunakan topik generic/dummy jika repositori memiliki topik dan metodologi penelitian riil.
- **Preset Universitas Gunadarma**: Gunakan `presets/gunadarma.yml` dengan margin 4-4-3-3 (`margin_top: 4cm, margin_bottom: 3cm, margin_left: 4cm, margin_right: 3cm`), `heading_chapter_prefix: ""`, dan `heading_chapter_num_format: "arabic"`.
- **Sistematika Numerik Arab**: Bab 1 s/d 5 menggunakan nomor Arab (`1. PENDAHULUAN`, `1.1. Latar Belakang`, `1.2. Ruang Lingkup`, `2. LANDASAN TEORI`, `3. METODOLOGI PENELITIAN`, `4. HASIL DAN PEMBAHASAN`, `5. PENUTUP`).
- **Pembersihan Metadata**: Hapus duplikat `preset: "standard"` di `metadata.yml` saat mengaktifkan preset khusus.
- **Kompatibilitas Google Docs & Word DOCX**:
  - Batasi lebar gambar maksimal 13,0 cm agar tidak meluap dari batas area cetak bersih 14,0 cm (A4 21 cm dikurangi margin kiri 4 cm dan kanan 3 cm) yang memicu loncatan halaman kosong (*blank hole*).
  - Hindari ekspor persamaan matematika OMML mentah (`<m:oMath>`) untuk target Google Docs karena memicu pembengkakan spasi baris tidak beraturan; gunakan notasi teks Unicode rapi dalam kotak panggil (*callout box*).
  - Pastikan margin OpenXML `w:pgMar` menggunakan bilangan bulat (*integer twips*, misal 2268 twips untuk 4 cm dan 1701 twips untuk 3 cm).

## O (Output Format)
- Berkas skripsi modular di `chapters/` dengan metadata tervalidasi.
- Kompilasi dokumen bersih via `laporan-generator build` menghasilkan PDF bertata letak presisi.
