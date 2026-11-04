---
name: doc
description: "Gunakan untuk: Panduan Pembuatan & Penyuntingan Dokumen (DOCX / Naskah)"
---

# Panduan Pembuatan & Penyuntingan Dokumen (DOCX / Naskah)

## 1. Prinsip Utama Penyuntingan Dokumen Pengguna
- **Penyuntingan Langsung di Tempat (*In-Place Editing*)**: Selalu sunting langsung berkas dokumen target. DILARANG membuat berkas perantara atau berkas duplikat baru (`_revised.docx`, `_edit.docx`) kecuali diminta secara eksplisit.
- **Larangan Skrip Perantara**: Dilarang membuat skrip Python sementara (`edit.py` atau `python -c`) hanya untuk menyunting berkas teks/dokumen. Gunakan WordCraft MCP (`mcp__wordcraft__*`), `wordcraft-cli`, Pandoc, atau patch langsung.
- **Integritas Naskah Akademik & Laporan**: Untuk dokumen skripsi, tesis, proposal, dan laporan formal, WAJIB mematuhi seluruh aturan naskah baku di bawah ini.

## 2. Aturan Baku Format Naskah & Paragraph Styles
1. **Geometri Kertas A4 (Margin 4-4-3-3 cm)**:
   - Atas (*Top*): **4,02 cm** (`114.0 pt`)
   - Kiri (*Left*): **4,00 cm** (`113.4 pt`)
   - Bawah (*Bottom*): **3,00 cm** (`85.0 pt`)
   - Kanan (*Right*): **2,90 s/d 3,00 cm** (`82.2 pt` s/d `85.0 pt`)
   - Lebar bidang cetak efektif: **14,1 cm** (rentang x = 113.4 pt s/d x = 513.2 pt).
2. **Normal / Body Text (Paragraf Narasi Standar)**:
   - Font: **Times New Roman 12 pt Regular**, spasi baris 1.5 (`para.oneAndHalf`).
   - Perataan: Rata Kiri-Kanan penuh (*Justified*).
   - **First-Line Indent Tepat 36.0 pt (1,27 cm / 0,5 inci)**: Baris pertama menjorok di `x = 149.4 pt`, baris kedua dst rata kiri di `x = 113.4 pt`.
   - Spasi Paragraf: Space before 0 pt, space after 0 pt (jika menggunakan baris kosong pemisah) atau space after 8 pt (jika tanpa enter ganda).
3. **Heading 1 (Judul Bab Utama)**:
   - Font: Times New Roman 14 pt Bold rata tengah (*Center*), kapitalisasi penuh (*ALL CAPS*), properti `pageBreakBefore: true`.
   - Jarak ke teks/sub-bab berikutnya: 47.0 s/d 56.2 pt (~2,5 sampai 3 spasi).
4. **Heading 2 (Sub-Bab Tingkat 2)**:
   - Font: Times New Roman 12 pt Bold (*Bold Italic* untuk istilah asing).
   - Aturan Judul: Wajib **1 sampai 2 kata benda entitas murni** (maksimal 3 kata istilah resmi). Dilarang kata hubung 'dan'.
   - **Hanging Indent 36.0 pt (1,27 cm)**: Nomor sub-bab di `x = 113.4 pt`, teks judul dimulai di `x = 149.4 pt` sejajar baris pertama paragraf. Spasi 1.5, tanpa tanda titik penutup.
5. **Heading 3 (Sub-Sub-Bab Tingkat 3)**:
   - Font: Times New Roman 12 pt Bold (*Bold Italic* untuk istilah asing), batas 1-2 kata.
   - **Nested Hanging Indent +36.0 pt**: Nomor di `x = 149.4 pt`, teks judul di `x = 185.4 pt` (tab stop 72.0 pt).
6. **Daftar Butir (*Numbered Lists*)**:
   - Baris pertama nomor dimulai di `x = 131.4 pt` (indent 18.0 pt / 0,25 inci).
   - Baris teks kelanjutan dimulai di `x = 149.4 pt` (indent 36.0 pt / 0,5 inci).
7. **Tabel & Gambar**:
   - Judul Tabel: Di ATAS tabel, 100% rata tengah, Times New Roman 11-12 pt Regular, format `Tabel X.Y Judul Tabel` tanpa tanda titik dua.
   - Judul Gambar: Di BAWAH gambar, 100% rata tengah, format `Gambar X.Y Judul Gambar` tanpa tanda titik dua.
   - Lebar Gambar: Maksimal **13,0 cm** (rata tengah) agar tidak memicu overflow atau halaman bolong kosong di Google Docs.
8. **Persamaan Matematika (Bukan Callout Box)**:
   - DILARANG menggunakan kotak panggil (*callout box*), tabel berarsir abu-abu, atau bingkai bergaris biru vertikal.
   - Formula diletakkan di tengah, nomor persamaan `(X.Y)` rata batas margin kanan 14,0 cm pada baris yang sama.
   - Disajikan via tabel 1 baris 2 kolom tanpa bingkai (*borderless table* 14,0 cm: kolom 12,0 cm rumus, kolom 2,0 cm nomor) atau berkas PNG 300 DPI via Typst.
9. **Daftar Pustaka (Bibliography Entry)**:
   - Heading 14 pt Bold Center.
   - Teks: Times New Roman 12 pt Regular, spasi 1.5, space after 8 pt antar-entri rujukan.
   - **Hanging Indent 36.0 pt (1,27 cm)**: Baris pertama di `x = 113.4 pt`, baris kedua dan seterusnya menjorok di `x = 149.4 pt`. Format Harvard Author-Date.
10. **Sitasi & Anti-AI Slop**:
    - Sitasi first-mention: 3-5 penulis wajib disebut lengkap ('Ramadhani, Dewanta, dan Gunawan (2026)'), baru berikutnya 'dkk.'. Dilarang 'et al.' atau '&'.
    - Dilarang pola kurung ganda terjemahan: `padanan (*istilah asing*)`. Gunakan istilah murni cetak miring (*deep learning*, *backbone*).

## 3. Alur Kerja Rekomendasi (WordCraft MCP / CLI)
1. **Buka Dokumen**: Gunakan `mcp__wordcraft__open_document` dengan path dokumen yang ada.
2. **Terapkan Batch Formatting / Edits**: Gunakan `mcp__wordcraft__batch` atau `mcp__wordcraft__type_text` / `mcp__wordcraft__select_text`.
3. **Simpan In-Place**: Panggil `mcp__wordcraft__save_document` tanpa argumen path untuk menyimpan pembaruan ke berkas asli.
4. **Verifikasi Visual**: Gunakan `mcp__wordcraft__render_page` untuk memeriksa tata letak dan memastikan tidak ada teks atau tabel yang terpotong.

## When to use
- Read or review DOCX content where layout matters (tables, diagrams, pagination).
- Create or edit DOCX files with professional formatting.
- Validate visual layout before delivery.

## Workflow
1. Prefer visual review (layout, tables, diagrams).
   - If `soffice` and `pdftoppm` are available, convert DOCX -> PDF -> PNGs.
   - Or use `scripts/render_docx.py` (requires `pdf2image` and Poppler).
   - If these tools are missing, install them or ask the user to review rendered pages locally.
2. Use `python-docx` for edits and structured creation (headings, styles, tables, lists).
3. After each meaningful change, re-render and inspect the pages.
4. If visual review is not possible, extract text with `python-docx` as a fallback and call out layout risk.
5. Keep intermediate outputs organized and clean up after final approval.

## Temp and output conventions
- Use `tmp/docs/` for intermediate files; delete when done.
- Write final artifacts under `output/doc/` when working in this repo.
- Keep filenames stable and descriptive.

## Dependencies (install if missing)
Prefer `uv` for dependency management.

Python packages:
```
uv pip install python-docx pdf2image
```
If `uv` is unavailable:
```
python3 -m pip install python-docx pdf2image
```
System tools (for rendering):
```
# macOS (Homebrew)
brew install libreoffice poppler

# Ubuntu/Debian
sudo apt-get install -y libreoffice poppler-utils
```

If installation isn't possible in this environment, tell the user which dependency is missing and how to install it locally.

## Environment
No required environment variables.

## Rendering commands
DOCX -> PDF:
```
soffice -env:UserInstallation=file:///tmp/lo_profile_$$ --headless --convert-to pdf --outdir $OUTDIR $INPUT_DOCX
```

PDF -> PNGs:
```
pdftoppm -png $OUTDIR/$BASENAME.pdf $OUTDIR/$BASENAME
```

Bundled helper:
```
python3 scripts/render_docx.py /path/to/file.docx --output_dir /tmp/docx_pages
```

## Quality expectations
- Deliver a client-ready document: consistent typography, spacing, margins, and clear hierarchy.
- Avoid formatting defects: clipped/overlapping text, broken tables, unreadable characters, or default-template styling.
- Charts, tables, and visuals must be legible in rendered pages with correct alignment.
- Use ASCII hyphens only. Avoid U+2011 (non-breaking hyphen) and other Unicode dashes.
- Citations and references must be human-readable; never leave tool tokens or placeholder strings.

## Final checks
- Re-render and inspect every page at 100% zoom before final delivery.
- Fix any spacing, alignment, or pagination issues and repeat the render loop.
- Confirm there are no leftovers (temp files, duplicate renders) unless the user asks to keep them.
