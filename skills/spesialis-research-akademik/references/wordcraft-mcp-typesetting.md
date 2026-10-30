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
Konversi satuan: `1 cm = 28.3465 pt` (`4 cm = 113.39 pt`, `3 cm = 85.04 pt`, `1 cm = 28.35 pt`).

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
    {"command": "para.indents", "params": {"firstLine": 28.35}}
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
1. **Identifikasi Batas Blok Presisi**:
   - Cari batas awal bab target (`1. PENDAHULUAN`) via `mcp__wordcraft__select_text`.
   - Cari blok teks terakhir dari bab yang diganti (misal paragraf terakhir Bab 3) via teks uniknya, catat indeks path dan panjang karakternya.
   - **Pitfall Batas Seleksi**: DILARANG mengarahkan `focus` ke `off: 0` pada blok *Section Break* (`w:sectPr`) atau bab selanjutnya (`4. HASIL DAN PEMBAHASAN`). Menghapus dengan seleksi hingga `off: 0` blok selanjutnya dapat memotong teks heading atau merusak atribut section break bab berikutnya. Selalu arahkan `focus` ke karakter terakhir teks bab target (`off: len(last_paragraph_text)`).
2. **Eksekusi Penghapusan Terarah**:
   - Eksekusi `select.range` dengan `anchor: {"path": [start_block], "off": 0, "story": "body"}` dan `focus: {"path": [end_block], "off": last_len, "story": "body"}`.
   - Panggil `text.delete` untuk mengosongkan blok bab lama.
3. **Kompilasi & Injeksi Bab Baru**:
   - Susun teks bab baru (Markdown) dan kompilasi ke `.docx` menggunakan Pandoc dengan `--reference-doc` menunjuk ke naskah asli agar format gaya tabel, font, dan persamaan matematika OMML identik.
   - Tempatkan kursor ke `[start_block], off: 0` via `select.range`.
   - Panggil `insert.textFromFile` dengan path berkas `.docx` yang telah dikompilasi.
4. **Penataan Ulang Pemisah Halaman Antar-Bab**:
   - Cari heading bab utama (`2. LANDASAN TEORI`, `3. METODOLOGI PENELITIAN`) menggunakan `select_text`.
   - Posisikan kursor pada `off: 0` sebelum heading dan panggil `insert.pageBreak` agar setiap bab dimulai pada halaman baru.
5. **Penyimpanan In-Place & Audit Visual**:
   - Panggil `mcp__wordcraft__save_document` tanpa argumen `path` untuk menyimpan berkas secara langsung di tempat.
   - Verifikasi halaman awal bab menggunakan `mcp__wordcraft__render_page` yang dianalisis melalui `vision_analyze`.
