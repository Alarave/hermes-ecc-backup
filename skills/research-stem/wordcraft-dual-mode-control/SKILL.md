---
name: wordcraft-dual-mode-control
description: "Use when controlling WordCraft via headless or live GUI."
license: MIT
metadata:
  hermes:
    tags: [wordcraft, mcp, gui-control, docx, live-editing, academic-typesetting]
---

# WordCraft Dual-Mode Control & In-Place Typesetting (wordcraft-dual-mode-control)

## R (Role & Identity)
- **Peran**: WordCraft Document Controller & Live In-Place Typesetting Operator.
- **Standar**: Menghasilkan naskah akademik berformat Word native (.docx) dengan presisi estetika, formula, dan tipografi setara LaTeX.

---
## C (Context & Operating Modes)

### 1. Dual-Mode Architecture
WordCraft menyediakan dua mode kendali terprogram bagi Hermes Agent:

#### Mode 1: Headless Background Engine (`wordcraft-cli mcp`)
- Berjalan murni di latar belakang tanpa memunculkan jendela GUI di monitor.
- Digunakan untuk otomasi cepat, pembacaan struktur teks, manipulasi blok, dan konversi multi-format (.docx ke .pdf).
- Dikonfigurasi di `config.yaml` dengan `command: C:\Program Files\WordCraft\wordcraft-cli.exe` dan `args: [mcp]`.

#### Mode 2: Live GUI Control Channel (`--control <port>`)
- WordCraft desktop dibuka dengan argumen: `wordcraft.exe --control 7981 [FILE.docx]`.
- WordCraft membuka saluran kendali lokal TCP port 7981 (JSON control protocol).
- Hermes terhubung via bridge: `wordcraft-cli mcp --connect 127.0.0.1:7981` (diatur di `config.yaml` `mcp_servers.wordcraft.args`).
- Token sesi tersimpan otomatis di `AppData/Roaming/WordCraft/control-key.local-7981`.
- Pengguna melihat langsung kursor bergerak, teks tertulis, dan dokumen terformat di layar monitor secara real-time.
- **Pola Kerja Berdampingan (Side-by-Side)**: WordCraft desktop tidak memiliki jendela chat internal. Alur kerja resmi menempatkan jendela chat Hermes Desktop di sisi kiri dan jendela aplikasi WordCraft di sisi kanan monitor.

#### Mode 3: Headless In-Place Fallback (Direct OpenXML via Python stdlib)
- Digunakan saat WordCraft live GUI port 7981 tidak aktif (`connection timed out`) dan lingkungan komputasi tidak memiliki dependensi pihak ketiga (`python-docx`).
- Menggunakan modul bawaan Python `zipfile` dan `xml.etree.ElementTree` untuk memodifikasi `word/document.xml` secara bedah langsung di tempat:
  ```python
  import zipfile, xml.etree.ElementTree as ET
  with zipfile.ZipFile(docx_path, 'r') as z_in:
      namelist = z_in.namelist()
      xml_content = z_in.read('word/document.xml')
      other_files = {name: z_in.read(name) for name in namelist if name != 'word/document.xml'}
  root = ET.fromstring(xml_content)
  # Modifikasi node w:pPr dan w:r pada body...
  new_xml = ET.tostring(root, encoding='utf-8', xml_declaration=True)
  with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as z_out:
      z_out.writestr('word/document.xml', new_xml)
      for name, data in other_files.items():
          z_out.writestr(name, data)
  ```
- Menjamin kelestarian 100% berkas relasi, media internal, dan style tanpa memicu pembengkakan ukuran arsip.

---
## C (Constraints & Procedural Steps)

### 1. Prosedur Penyuntingan Sub-Bab In-Place Bedah (Surgical Sub-Chapter Replacement)
1. **Cadangan Pengaman Fisik Pra-Modifikasi**:
   - Selalu buat cadangan dokumen fisik sebelum modifikasi: `cp "[NASKAH].docx" "[NASKAH].docx.bak_safety"`.
2. **Buka Dokumen di WordCraft**:
   - Panggil `mcp__wordcraft__open_document(path="...")`. Verifikasi status enkripsi false dan total paragraf terlaporkan.
3. **Penyuntingan Heading Sub-Bab**:
   - Cari judul sub-bab di badan dokumen menggunakan `mcp__wordcraft__select_text(occurrence=2, text="[Judul Lama]")` (kemunculan ke-2 digunakan untuk melewati kemunculan judul pada Daftar Isi).
   - Ganti judul dengan 1 sampai 2 kata benda entitas murni menggunakan `mcp__wordcraft__type_text(text="2.X Judul Baru")`.
   - Terapkan hanging indent 36 pt: panggil `mcp__wordcraft__batch` dengan `para.indents: {left: 36.0, firstLine: -36.0}`.
4. **Penyuntingan Bodi Paragraf Narasi**:
   - Periksa panjang karakter paragraf target melalui `mcp__wordcraft__execute(command="document.paragraph", params={"path": [P_idx]})`.
   - Pilih seluruh rentang teks paragraf via `select.range` dengan `anchor: {path: [P_idx], off: 0, story: "body"}` dan `focus: {path: [P_idx], off: P_len, story: "body"}`.
   - Ketik draf teks baru yang mematuhi formula deduktif 4-kalimat per paragraf via `mcp__wordcraft__type_text`.
   - Terapkan gaya paragraf resmi melalui `mcp__wordcraft__batch`:
     - `format.font: {name: "Times New Roman"}`
     - `format.size: {size: 12}`
     - `para.oneAndHalf: {}`
     - `para.justify: {}`
     - `para.indents: {firstLine: 36.0}` (1,27 cm / 0,5 inci)
5. **Pemformatan Istilah Bahasa Inggris**:
   - Pilih istilah teknis asing (seperti *e-commerce*, *stock keeping unit*, *catalog ingestion*, *visual ground truth*, *non-planar*) menggunakan `mcp__wordcraft__select_text` atau `select.range`.
   - Terapkan format miring via `mcp__wordcraft__execute(command="format.italic", params={"value": true})`.
6. **Sinkronisasi Daftar Isi (TOC)**:
   - Pilih kemunculan judul lama pada Daftar Isi menggunakan `mcp__wordcraft__select_text(occurrence=1, text="[Judul Lama]")`.
   - Ganti teks entri dengan judul baru via `mcp__wordcraft__type_text`.
7. **Penyimpanan In-Place**:
   - Panggil `mcp__wordcraft__save_document()` tanpa argumen path.
   - Verifikasi respon `{"saved": true}` dan pastikan ukuran berkas di disk termutakhirkan.

### 2. Standar Paritas Tipografi LaTeX di Word (.docx)
1. **Margin & Kertas**: A4 margin 4-4-3-3 cm (Top 113.39 pt, Left 113.39 pt, Bottom 85.04 pt, Right 85.04 pt).
2. **Font & Spasi**: Times New Roman 12 pt, spasi 1.5, justified, indentasi awal paragraf 36.0 pt (1,27 cm).
3. **Heading 2 (Sub-Bab)**: 1-2 kata benda murni, hanging indent 36.0 pt (nomor di 113.4 pt, teks di 149.4 pt).
4. **Persamaan Matematika**: Tabel 1x2 tanpa garis batas (borderless) selebar 14,0 cm (kolom kiri 12,0 cm untuk rumus OMML di tengah, kolom kanan 2,0 cm untuk nomor persamaan rata kanan). DILARANG kotak panggil (callout box).
5. **Paginasi Ganda**: Romawi tengah bawah (front matter) vs Arab kanan atas (isi bab), kecuali awal bab baru di tengah bawah.

### 3. Pitfall & Aturan Mutlak
- **Mandat In-Place**: DILARANG membuat skrip perantara Python atau membuat file duplikat `.docx` baru. Sunting langsung berkas asli di tempat.
- **Batas Seleksi Teks**: Jangan mengarahkan `focus` seleksi ke `off: 0` pada blok paragraf berikutnya saat menghapus teks, karena dapat menghapus batas paragraf atau merusak atribut heading berikutnya.
- **Anti-AI-Slop Sub-Bab**: Judul sub-bab wajib 1-2 kata benda murni. Dilarang menggabungkan dua topik dengan kata hubung 'dan' atau menggunakan kalimat panjang.

---
## O (Output & Verification)
Dokumen tersimpan in-place via `mcp__wordcraft__save_document` tanpa file duplikat, terverifikasi bebas teks klise AI slop dan bebas tanda pisah em-dash atau en-dash.
