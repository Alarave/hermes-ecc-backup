# WordCraft MCP & CLI Academic Typesetting Reference

Panduan integrasi native **WordCraft MCP (`mcp__wordcraft__*`)** dan **`wordcraft-cli`** untuk penyusunan, pemformatan geometri 4-4-3-3, sitasi Zotero, ekspor multi-format (`.docx` dan `.pdf`), serta audit visual halaman (`render_page`) pada klaster `/research`.

## 1. Konfigurasi Server MCP
- **Nama Server**: `wordcraft`
- **Biner**: `C:\Program Files\WordCraft\wordcraft-cli.exe`
- **Argumen**: `["mcp"]` (mode headless otomatis) atau `["mcp", "--connect", "127.0.0.1:7981"]` (mode bridge ke aplikasi desktop `wordcraft.exe --control 7981`).

## 2. Daftar 16 Tool Utama `mcp__wordcraft__*`
| Tool | Fungsi Utama dalam Riset & Skripsi |
|---|---|
| `mcp__wordcraft__new_document` | Membuat dokumen baru (`blank`, `report`, `letter`, `resume`, `sample`). |
| `mcp__wordcraft__open_document` | Membuka berkas `.docx`, `.doc`, `.odt`, `.rtf`, `.md`, `.tex`, `.html`, `.txt`, atau `.json`. |
| `mcp__wordcraft__save_document` | Menyimpan/mengekspor dokumen ke `.docx`, `.pdf`, `.odt`, `.rtf`, `.html`, `.md`, `.tex`, `.txt`, atau `.xml` berdasarkan ekstensi path. |
| `mcp__wordcraft__batch` | Mengeksekusi serangkaian perintah pemformatan secara atomik dalam satu langkah. |
| `mcp__wordcraft__execute` | Mengeksekusi satu perintah spesifik berdasarkan `id` dan `params`. |
| `mcp__wordcraft__type_text` | Mengetik teks pada posisi kursor aktif. |
| `mcp__wordcraft__select_text` | Memilih kemunculan ke-N dari string teks untuk pemformatan terarah. |
| `mcp__wordcraft__get_text` | Membaca teks isi dokumen (mengabaikan tracked deletions). |
| `mcp__wordcraft__inspect_document` | Memeriksa struktur blok, gaya (styles), formatting runs, daftar, tabel, dan section. |
| `mcp__wordcraft__render_page` | Merender halaman dokumen menjadi citra `.png` untuk verifikasi visual tata letak dan margin. |
| `mcp__wordcraft__list_commands` | Mencari ID perintah dan skema parameter di katalog perintah WordCraft. |
| `mcp__wordcraft__parity` | Memeriksa cakupan fitur word-processor. |
| `mcp__wordcraft__ui_inspect` | Memeriksa state UI aplikasi desktop WordCraft (membutuhkan `--connect`). |
| `mcp__wordcraft__screenshot` | Mengambil tangkapan layar jendela WordCraft desktop. |
| `mcp__wordcraft__click` | Klik koordinat pada jendela aplikasi desktop. |
| `mcp__wordcraft__key` | Menekan kombinasi tombol pada aplikasi desktop. |

## 3. Preset Batch Standar Skripsi Gunadarma (A4, Margin 4-4-3-3 cm, Times New Roman 12pt, Spasi 1.5)
Konversi satuan: `1 cm = 28.3465 pt` (`4 cm = 113.39 pt`, `3 cm = 85.04 pt`, `1,27 cm = 36.0 pt / 0,5 in`).

Gunakan `mcp__wordcraft__batch` segera setelah `mcp__wordcraft__new_document`:
```json
{
  "commands": [
    {"command": "layout.size", "params": {"name": "A4"}},
    {"command": "layout.margins", "params": {"top": 113.39, "left": 113.39, "bottom": 85.04, "right": 85.04}},
    {"command": "format.font", "params": {"name": "Times New Roman"}},
    {"command": "format.size", "params": {"size": 12}},
    {"command": "para.oneAndHalf", "params": {}},
    {"command": "para.justify", "params": {}},
    {"command": "para.indents", "params": {"firstLine": 36.0}}
  ]
}
```

## 4. Pengaturan Dual Pagination, Daftar Isi, Caption, & Persamaan Matematika
- **Section Break (Pemisah Bagian Awal Romawi vs Bab Inti Arab)**:
  - `{"command": "layout.break", "params": {"kind": "nextPage"}}`
  - `{"command": "layout.linkToPrevious", "params": {}}` (putuskan tautan header/footer antar section)
- **Format Nomor Halaman**:
  - Bagian Awal: `{"command": "layout.pageNumberFormat", "params": {"format": "lowerRoman", "start": 1}}` + `{"command": "insert.pageNumber", "params": {"position": "bottom", "align": "center"}}`
  - Bagian Inti (Bab 1-5): `{"command": "layout.differentFirstPage", "params": {}}` + `{"command": "layout.pageNumberFormat", "params": {"format": "decimal", "start": 1}}` + `{"command": "insert.pageNumber", "params": {"position": "top", "align": "right"}}`
- **Daftar Isi Otomatis (TOC)**:
  - `{"command": "references.toc", "params": {"levels": 3, "title": "DAFTAR ISI", "pageNumbers": true, "rightAlign": true, "tabLeader": "dot", "hyperlinks": true}}`
  - Pembaruan field: `{"command": "references.updateToc", "params": {}}` atau `{"command": "references.updateFields", "params": {}}`
- **Caption Tabel (Di Atas) & Gambar (Di Bawah)**:
  - Tabel: `{"command": "references.caption", "params": {"label": "Tabel", "text": " Hasil Evaluasi Model", "position": "above", "chapter": 1, "separator": "."}}`
  - Gambar: `{"command": "references.caption", "params": {"label": "Gambar", "text": " Diagram Alir Penelitian", "position": "below", "chapter": 1, "separator": "."}}`
- **Persamaan Matematika & Ilustrasi Vektor**:
  - Equation: `{"command": "insert.equation", "params": {}}` diikuti `{"command": "equation.type", "params": {"text": "..."}}`
  - Gambar FigGenie: `{"command": "insert.picture", "params": {"path": "laporan/figures/arsitektur.png"}}`

## 5. Integrasi Sitasi Zotero & Konversi CLI (`wordcraft-cli`)
Untuk operasi batch dari terminal atau injeksi sitasi langsung dari Zotero desktop yang sedang berjalan:
- **Konversi Multi-Format (Markdown / LaTeX / DOCX ke DOCX & PDF)**:
  ```bash
  "/c/Program Files/WordCraft/wordcraft-cli.exe" convert input.md output.docx --update-fields
  "/c/Program Files/WordCraft/wordcraft-cli.exe" convert output.docx output.pdf --update-fields
  ```
- **Injeksi Sitasi & Bibliografi Zotero**:
  ```bash
  "/c/Program Files/WordCraft/wordcraft-cli.exe" zotero setDocPrefs naskah.docx --save naskah.docx
  "/c/Program Files/WordCraft/wordcraft-cli.exe" zotero refresh naskah.docx --save naskah.docx
  "/c/Program Files/WordCraft/wordcraft-cli.exe" zotero addEditBibliography naskah.docx --cmd caret.docEnd --save naskah.docx
  ```
- **Audit Visual Halaman (Machine Seal)**:
  Gunakan `mcp__wordcraft__render_page` atau CLI `wordcraft-cli render naskah.docx page1.png --page 1` untuk memastikan tidak ada tabel atau gambar yang melewati batas margin 4-4-3-3.

## 6. Protokol Penggantian Bab Skripsi Berskala Besar (Surgical Chapter Replacement)
Saat mengganti sekumpulan bab (contoh: Bab 1 s.d. 3) pada naskah skripsi komprehensif tanpa merusak lembar pengesahan/abstrak di depan (*front matter*) dan Bab 4-5 di belakang:
1. **Cadangan Pengaman Fisik Pra-Modifikasi**:
   - Selalu buat cadangan dokumen fisik via terminal: `cp "[NASKAH].docx" "[NASKAH].docx.bak_safety"`.
2. **Identifikasi Batas Blok Presisi**:
   - Cari batas awal bab target (`1. PENDAHULUAN`) via `mcp__wordcraft__select_text`.
   - Cari blok teks terakhir dari bab yang diganti (misal paragraf terakhir Bab 3) via teks uniknya, catat indeks path dan panjang karakternya.
   - **Pitfall Batas Seleksi**: DILARANG mengarahkan `focus` ke `off: 0` pada blok *Section Break* (`w:sectPr`) atau bab selanjutnya (`4. HASIL DAN PEMBAHASAN`). Menghapus dengan seleksi hingga `off: 0` blok selanjutnya dapat memotong teks heading atau merusak atribut section break bab berikutnya. Selalu arahkan `focus` ke karakter terakhir teks bab target (`off: len(last_paragraph_text)`).
3. **Eksekusi Penghapusan Terarah**:
   - Eksekusi `select.range` dengan `anchor: {"path": [start_block], "off": 0, "story": "body"}` dan `focus: {"path": [end_block], "off": last_len, "story": "body"}`.
   - Panggil `text.delete` untuk mengosongkan blok bab lama.
4. **Kompilasi Multi-Berkas & Injeksi Bab Baru**:
   - **Multi-File Serial Pandoc**: Hindari menyatukan naskah ke dalam satu berkas Markdown raksasa (>100k karakter) via `write_file` karena rentan penolakan overwrite akibat batas paginasi; langsung oper berkas-berkas bab terpisah secara berurutan ke baris perintah Pandoc:
     ```bash
     pandoc -s BAB_1.md BAB_2.md BAB_3.md -o "BAB_1_3_STYLED.docx" --reference-doc="[NASKAH].docx" --resource-path=.
     ```
   - Argumen `--reference-doc` memastikan format gaya tabel, font, margin, dan formula matematika OMML native tetap identik dengan naskah utama.
   - Tempatkan kursor ke `[start_block], off: 0` via `select.range`.
   - Panggil `insert.textFromFile` dengan path berkas `BAB_1_3_STYLED.docx`.
5. **Penataan Ulang Pemisah Halaman Antar-Bab (Page Break Before)**:
   - Cari heading bab utama (`1. PENDAHULUAN`, `2. LANDASAN TEORI`, `3. METODOLOGI PENELITIAN`) menggunakan `select.text`.
   - Terapkan `para.pageBreakBefore: {"value": true}` pada heading paragraf tersebut. Menyetel properti paragraf ini jauh lebih stabil dibandingkan `insert.pageBreak` karena tidak menciptakan baris kosong semu (*phantom blank lines*) atau merusak margin atas.
6. **Penyelarasan Metadata Front Matter & Tabel Sampul**:
   - Pada draf naskah berbasis templat kampus (Gunadarma/UPNVJ), identitas mahasiswa, judul skripsi, dan pembimbing di Halaman Judul, Lembar Pernyataan, Lembar Pengesahan, dan Kata Pengantar sering tersimpan di dalam sel tabel tanpa bingkai (`borderless table` pada `path: [table_block, row, col, 0]`).
   - Pindai kemunculan nama lama dan NPM via `select.text`, ganti dengan `text.insert`.
   - Jika judul lama terpecah ke beberapa baris di luar tabel (misal overflow `Machine Learning\ndan\nIndoBERT`), pilih baris berlebih dan hapus dengan `text.delete`.
7. **Sinkronisasi Daftar Isi (TOC) & Update Fields**:
   - Entri Daftar Isi sering berupa paragraf teks statis dengan titik-titik pemandu (*dot leaders*). Pilih rentang entri bab lama yang diganti via `select.range`, timpa dengan daftar sub-bab baru berformat titik pemandu yang selaras ke nomor halaman bab berikutnya, lalu jalankan `references.updateToc: {}` dan `references.updateFields: {"all": true}`.
8. **Penyimpanan In-Place, Ekspor PDF & Audit XML Zero-Dependency**:
   - Panggil `mcp__wordcraft__save_document` tanpa argumen `path` untuk menyimpan berkas secara langsung di tempat.
   - Ekspor naskah ke PDF via `mcp__wordcraft__save_document` dengan path berakhiran `.pdf` (misal `[NASKAH]_FORMATTED.pdf`).
   - Jika pustaka `python-docx` tidak tersedia pada lingkungan Python lokal, audit integritas dokumen XML secara deterministik menggunakan pustaka standar Python `zipfile` dan `xml.etree.ElementTree` (`word/document.xml`) untuk memvalidasi jumlah paragraf, keberadaan seluruh heading, ketiadaan istilah terlarang (`et al.`, `niaga elektronik`), dan ketiadaan tanda pisah em-dash/en-dash.
