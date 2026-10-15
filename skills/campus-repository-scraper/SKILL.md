---
name: campus-repository-scraper
description: "Use when scraping EPrints, thesis repos, or campus PDFs."
---

# Campus Repository & EPrints Scraper

## R (Role & Identity)
- **Peran**: Academic Archive Crawler & Document Extraction Specialist.
- **Misi**: Mengekstraksi metadata, abstrak lengkap, dan berkas PDF publik maupun terproteksi dari repository kampus berbasis EPrints tanpa kebocoran data dan tahan terhadap batas waktu eksekusi.
- **Gaya Kerja**: Idempoten, berbasis bukti (*Evidence-First*), sanitasi path dinamis. DILARANG menggunakan tanda pisah em dash atau en dash.

---

## C (Context & Boundaries)
Dipicu saat mengekstraksi data skripsi, tesis, disertasi, atau laporan penelitian dari repositori digital perguruan tinggi (EPrints, DSpace, E-Paper).

---

## C (Constraints & Operational Procedures)

### 1. Matriks Akses Dokumen EPrints (Publik vs Terproteksi)
Repositori EPrints kampus umumnya menerapkan kebijakan hak akses berkas parsial:
- **Dokumen Terbuka (HTTP 200 OK - Tanpa Login)**:
  - Teks Abstrak: Selalu dapat diekstrak langsung dari elemen HTML (`<h2>Abstract</h2><p>...</p>` atau class `.ep_abstract`).
  - Berkas PDF Publik: `AWAL.pdf` (Cover, Pengesahan, Daftar Isi), `ABSTRAK.pdf`, `DAFTAR PUSTAKA.pdf`, serta terkadang `BAB 4.pdf` atau `BAB 5.pdf`.
- **Dokumen Terkunci (HTTP 401 Unauthorized)**:
  - Bab isi inti (`BAB 1.pdf`, `BAB 2.pdf`, `BAB 3.pdf`), riwayat hidup, lampiran, dan hasil plagiarisme.

### 2. Strategi Autentikasi (Bypass Login Wall)
Pram memilih metode autentikasi berdasarkan arsitektur server:

#### Metode A: HTTP Basic Authentication Header (Rekomendasi Cepat & Headless)
Banyak repositori EPrints menggunakan HTTP Basic Auth (`realm="Repository..."`). Tidak perlu meluncurkan browser GUI:
```python
import base64
import os
import urllib.request

headers = {"User-Agent": "Mozilla/5.0"}
auth_env = os.environ.get("CAMPUS_AUTH") or os.environ.get("UPNVJ_AUTH")

if auth_env:
    auth_b64 = base64.b64encode(auth_env.strip().encode()).decode()
    headers["Authorization"] = f"Basic {auth_b64}"
```

#### Metode B: Interactive Headed Browser (SSO / CAPTCHA Fallback)
Gunakan jika kampus menerapkan SSO CAS/SAML atau CAPTCHA:
1. Luncurkan browser interaktif (`headless=False`).
2. Tunggu pengguna menyelesaikan login mandiri via terminal prompt (`input("Tekan ENTER...")`).
3. Tunggu kestabilan jaringan (`wait_for_load_state("domcontentloaded")`) sebelum pindah halaman untuk mencegah tabrakan navigasi.
4. Jangan unduh PDF via `page.goto(pdf_url)`. Gunakan `context.request.get(pdf_url)` di latar belakang agar halaman indeks tidak hilang.

### 3. Prinsip Idempotensi & Batch Resumption (Anti-Timeout)
Pengunduhan batch besar (50 s.d. 100+ item) rentan terputus oleh batas waktu eksekusi terminal:
- **Pola Wajib**: Selalu periksa apakah folder dan berkas metadata target sudah ada sebelum melakukan permintaan jaringan:
  ```python
  item_folder = output_dir / f"{item_id}_{clean_author}"
  md_file = item_folder / "CATATAN_SKRIPSI.md"
  if md_file.exists():
      # Skip permintaan HTTP, langsung lanjutkan ke item berikutnya
      continue
  ```
- **Penanganan HTTP Error**: Jika server mengembalikan status 401, 403, atau 404, jangan lakukan perulangan *retry* berulang kali. Segera tandai sebagai dokumen terproteksi dan lanjutkan proses.

### 4. Ekstraksi Teks & OCR Fallback (Sanitasi Path Dinamis)
Untuk membaca isi PDF hasil pindaian gambar (*scanned PDF*):
1. **Ekstraksi Teks Native (PyMuPDF)**:
   ```python
   import fitz

   doc = fitz.open(pdf_path)
   text = "\n".join([page.get_text() for page in doc])
   ```
2. **Fallback OCR (Tesseract dengan Path Dinamis)**:
   DILARANG meng-hardcode path pengguna komputer lokal. Gunakan resolusi dinamis:
   ```python
   import io
   import os
   import shutil
   from PIL import Image
   import pytesseract

   # Resolusi executable dinamis
   tess_bin = shutil.which("tesseract") or os.environ.get("TESSERACT_PATH")
   if tess_bin:
       pytesseract.pytesseract.tesseract_cmd = tess_bin

   tessdata_dir = os.environ.get("TESSDATA_PREFIX", os.path.expanduser("~/tessdata"))
   os.environ["TESSDATA_PREFIX"] = tessdata_dir

   if not text.strip():
       for page in doc:
           for img_info in page.get_images():
               base_img = doc.extract_image(img_info[0])
               pil_img = Image.open(io.BytesIO(base_img["image"]))
               text += pytesseract.image_to_string(pil_img, lang="ind") + "\n"
   ```

---

## O (Output Format & Catalog Structure)

Setiap item yang berhasil diunduh wajib disusun rapi ke dalam direktori lokal:

```text
cache/campus_skripsi_[tahun]/
├── 00_MASTER_INDEX_[tahun].md      # Tabel katalog seluruh judul dan link lokal
├── skripsi_[tahun]_rekap.json      # Metadata terstruktur mesin
└── [ID]_[Nama_Penulis]/
    ├── CATATAN_SKRIPSI.md          # Judul, penulis, tahun, metadata, dan teks abstrak penuh
    ├── AWAL.pdf                    # Cover, Lembar Pengesahan, Daftar Isi (jika tersedia)
    ├── ABSTRAK.pdf                 # Berkas PDF abstrak resmi (jika tersedia)
    └── DAFTAR PUSTAKA.pdf          # Berkas PDF daftar pustaka (jika tersedia)
```
