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
| `mcp__wordcraft__save_document` | Menyimpan/mengekspor dokumen ke `.docx`, `.pdf`, `.odt`, `.rtf`, `.html`, `.md`, `.tex`, `.txt`, atau `.xml` berdasarkan ekstensi path. Simpan in-place tanpa argumen path. |
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
  - Persamaan disajikan dalam tabel 1 baris 2 kolom tanpa garis batas selebar 14,0 cm (kolom kiri 12,0 cm untuk rumus rata tengah, kolom kanan 2,0 cm untuk nomor persamaan rata kanan). Dilarang kotak panggil (callout box).
  - Equation: `{"command": "insert.equation", "params": {}}` diikuti `{"command": "equation.type", "params": {"text": "..."}}`
  - Gambar FigGenie: `{"command": "insert.picture", "params": {"path": "laporan/figures/arsitektur.png"}}` (lebar maks 13,0 cm rata tengah).

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

## 6. Prosedur Penyuntingan Sub-Bab In-Place Bedah (Surgical Sub-Chapter Replacement)
Saat memperbarui judul dan narasi sub-bab tertentu (seperti 2.1) secara langsung di dalam naskah WordCraft:
1. **Cadangan Pengaman Fisik**: Selalu jalankan `cp "[NASKAH].docx" "[NASKAH].docx.bak_safety"`.
2. **Buka Dokumen**: `mcp__wordcraft__open_document(path="...")`.
3. **Penyuntingan Heading Sub-Bab**:
   - Pilih judul sub-bab di badan teks dengan `mcp__wordcraft__select_text(occurrence=2, text="[Judul Lama]")` (kemunculan ke-2 melewati entri Daftar Isi).
   - Ganti teks dengan judul baru 1-2 kata murni via `mcp__wordcraft__type_text(text="2.X Judul Baru")`.
   - Terapkan hanging indent 36 pt: `para.indents: {left: 36.0, firstLine: -36.0}` via `mcp__wordcraft__batch`.
4. **Penyuntingan Paragraf Narasi**:
   - Dapatkan panjang karakter paragraf target via `document.paragraph` (`path: [P_idx]`).
   - Pilih seluruh teks paragraf via `select.range` (`anchor: {path: [P_idx], off: 0, story: "body"}`, `focus: {path: [P_idx], off: P_len, story: "body"}`).
   - Ketik narasi baru (formula deduktif 4-kalimat) via `mcp__wordcraft__type_text`.
   - Terapkan gaya paragraf resmi via `mcp__wordcraft__batch`: Times New Roman 12 pt, 1.5 spasi, justified, firstLine indent 36.0 pt.
   - Format istilah asing (*e-commerce*, *visual ground truth*, dll.) dengan `format.italic: {value: true}`.
5. **Sinkronisasi Daftar Isi (TOC)**:
   - Pilih kemunculan judul lama pada Daftar Isi via `mcp__wordcraft__select_text(occurrence=1, text="[Judul Lama]")`.
   - Ganti teks entri dengan judul baru via `mcp__wordcraft__type_text`.
6. **Penyimpanan In-Place**:
   - Panggil `mcp__wordcraft__save_document()` tanpa argumen path.

## 7. Protokol Penggantian Bab Skripsi Berskala Besar
Saat mengganti sekumpulan bab (contoh: Bab 1 s.d. 3) pada naskah skripsi komprehensif tanpa merusak lembar pengesahan/abstrak di depan (*front matter*) dan Bab 4-5 di belakang:
1. **Cadangan Pengaman Fisik Pra-Modifikasi**:
   - Selalu buat cadangan dokumen fisik via terminal: `cp "[NASKAH].docx" "[NASKAH].docx.bak_safety"`.
2. **Identifikasi Batas Blok Presisi**:
   - Cari batas awal bab target (`1. PENDAHULUAN`) via `mcp__wordcraft__select_text`.
   - Cari blok teks terakhir dari bab yang diganti via teks uniknya, catat indeks path dan panjang karakternya.
   - **Pitfall Batas Seleksi**: DILARANG mengarahkan `focus` ke `off: 0` pada blok *Section Break* (`w:sectPr`) atau bab selanjutnya. Selalu arahkan `focus` ke karakter terakhir teks bab target (`off: len(last_paragraph_text)`).
3. **Eksekusi Penghapusan Terarah**:
   - Eksekusi `select.range` dan panggil `text.delete`.
4. **Kompilasi Multi-Berkas & Injeksi Bab Baru**:
   - Oper berkas-berkas bab terpisah secara berurutan ke baris perintah Pandoc:
     ```bash
     pandoc -s BAB_1.md BAB_2.md BAB_3.md -o "BAB_1_3_STYLED.docx" --reference-doc="[NASKAH].docx" --resource-path=.
     ```
   - Tempatkan kursor ke `[start_block], off: 0` via `select.range`.
   - Panggil `insert.textFromFile` dengan path berkas `BAB_1_3_STYLED.docx`.
5. **Penataan Ulang Pemisah Halaman Antar-Bab (Page Break Before)**:
   - Cari heading bab utama (`1. PENDAHULUAN`, `2. LANDASAN TEORI`, `3. METODOLOGI PENELITIAN`) menggunakan `select.text`.
   - Terapkan `para.pageBreakBefore: {"value": true}` pada heading paragraf tersebut.
6. **Penyelarasan Metadata Front Matter & Tabel Sampul**:
   - Pindai kemunculan nama lama dan NPM via `select.text`, ganti dengan `text.insert`.
7. **Sinkronisasi Daftar Isi (TOC) & Update Fields**:
   - Mutakhirkan Daftar Isi dengan `references.updateToc: {}` dan `references.updateFields: {"all": true}`.
8. **Penyimpanan In-Place, Ekspor PDF & Audit XML Zero-Dependency**:
   - Panggil `mcp__wordcraft__save_document` tanpa argumen `path`.
   - Ekspor naskah ke PDF via `mcp__wordcraft__save_document` dengan path berakhiran `.pdf`.
