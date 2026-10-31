# Preset Diagram Skripsi & Naskah Ilmiah Indonesia
*(Standar Format Vektor FigGenie Berbasis Audit Korpus Empiris Skripsi UPNVJ & Gunadarma)*

Modul ini adalah acuan baku rendering visual arsitektur sistem, kerangka pikir penelitian, dan alur metodologi agar sesuai dengan tradisi akademik Indonesia (UPNVJ, Gunadarma, UI, ITB) dan siap disisipkan ke Word (`.docx`) maupun PDF via Typst/LaTeX.

---

## 1. Tiga Taksonomi Baku Diagram Komputasi / Skripsi AI (Korpus UPNVJ)

Berdasarkan audit visual berkas PDF Bab 2 dan Bab 3 Fakultas Ilmu Komputer UPNVJ, diagram skripsi terbagi ke dalam 3 jenis representasi grafis:

### A. Flowchart Metodologi Penelitian & CRISP-DM / SDLC (Bab 3.1)
- **Struktur Alur**: Alur vertikal atas-ke-bawah atau alur berkelok 2 kolom simetris (*serpentine*).
- **Terminator**: Elips/oval mendatar (`<ellipse>` atau `<rect rx="12" ry="12">`) bertuliskan `Mulai` dan `Selesai`.
- **Kotak Pembungkus Fase (Grouping Container)**: Kotak persegi panjang besar bergaris tipis solid/dashed dengan header nama fase di kiri atas (contoh: `Business Understanding`, `Data Preparation`, `Requirement Analysis`, `Testing`).
- **Kotak Proses Tunggal**: Persegi panjang sudut tegak 90 derajat berlatar putih dengan border hitam solid 1 pt.
- **Simbol Data Masukan / Instrumen**: Jajar genjang (*parallelogram*) horizontal yang terhubung ke kotak proses utama (contoh: `Studi Literatur`, `Survei Kuesioner PSQI`, `Black Box Testing`).
- **Simbol Keputusan (Decision Node)**: Belah ketupat (*diamond*) berlabel `Berhasil` dengan cabang `Ya` (vertikal ke bawah) dan cabang `Tidak` (ortogonal 90 derajat ke kanan, naik ke atas sebagai umpan balik / *feedback loop* ke tahap desain).

### B. Diagram Arsitektur Jaringan & Transfer Learning (Bab 2 / Bab 3)
- **Struktur Alur**: Alur linear kiri-ke-kanan atau vertikal atas-ke-bawah yang memperlihatkan tumpukan lapisan (*layer stack*).
- **Blok Konvolusi**: Deretan balok persegi panjang monokrom berlabel dimensi tensor ($224 \times 224 \times 3 \rightarrow 112 \times 112 \times 64 \rightarrow \dots$) atau diagram balok 3D isometrik dengan skala dimensi yang menurun secara spasial.
- **Pengelompokan Lapangan (Curly / Angled Brackets)**: Menggunakan kurung kurawal/siku di sisi samping kanan untuk memisahkan secara tegas:
  - `Base Model (Pre-Trained Architecture)`: Lapisan *feature extractor* yang dibekukan (*frozen*).
  - `Head Network (Custom Classifier)`: Modul *Global Average Pooling*, *Dense Layer*, dan *Dropout* kustom.
- **Percabangan Kelas Luaran**: Kotak luaran akhir bercabang secara simetris ke kotak-kotak kelas target (contoh: `Cacar Monyet`, `Cacar Air`, `Campak`, `Normal` atau `Sehat`, `Tidak Sehat`).

### C. Pipeline Pelatihan, Pengujian, dan Evaluasi Model (Bab 3.2)
- Terdiri dari 3 kontainer bergaris batas putus-putus (*dashed rectangular border*):
  1. `PELATIHAN MODEL`: Blok `DATA LATIH` masuk ke `Pelatihan Model MobileNetV2`.
  2. `PENGUJIAN MODEL`: Blok `DATA UJI` masuk ke `Model Inferensi Terlatih` menghasilkan `Hasil Prediksi`.
  3. `EVALUASI MODEL`: `Hasil Prediksi` masuk ke `Confusion Matrix` untuk perhitungan metrik kuantitatif.

---

## 2. Parameter Geometri & Tipografi Wajib

| Parameter | Spesifikasi Baku | Keterangan |
|---|---|---|
| **Keluarga Huruf (Font Family)** | `Times New Roman`, `serif` (atau `Arial`, `sans-serif`) | Wajib serasi dengan font teks tubuh naskah skripsi |
| **Ukuran Huruf Judul Blok** | 10 pt sampai 11 pt (Bold) | `font-weight: 600`, kapitalisasi judul (Title Case) |
| **Ukuran Huruf Keterangan / Item** | 8.5 pt sampai 9.5 pt (Regular) | `font-weight: 400`, tidak boleh lebih kecil dari 8 pt |
| **Ukuran Huruf Istilah Asing** | 8.5 pt sampai 9.5 pt (*Italic*) | Istilah bahasa Inggris wajib dicetak miring (*Transfer learning*, *Pooling Layer*) |
| **Tebal Garis Batas (Stroke)** | 0.75 pt sampai 1 pt | Garis tepi kotak proses dan kontainer utama |
| **Tebal Garis Panah Alur** | 1 pt sampai 1.2 pt | Garis aliran data ortogonal 90 derajat dengan kepala panah padat |
| **Latar Belakang (Background)** | `#FFFFFF` (Putih Solid) | **DILARANG transparan** agar tidak berbayang saat dicetak atau di-convert ke DOCX |
| **Lebar Maksimal Gambar** | Maksimal 13,0 cm (368 pt) | Dilarang melebihi 13,0 cm agar tidak meluap dari area cetak bersih 14,0 cm |

---

## 3. Palet Warna Akademik Dingin (Anti-AI Slop Monokromatik)

DILARANG KERAS menggunakan warna-warni neon khas generator AI (ungu gradasi, pelangi, drop-shadow, ikon kartun bot). Standar korpus UPNVJ adalah monokromatik bersih:

- **Latar Kotak Proses**: `#FFFFFF` (Putih murni).
- **Garis Batas Kotak (Border)**: `#000000` (Hitam solid 1 pt) atau `#333333` (Abu-abu sangat gelap).
- **Kontainer Fase Luar**: Garis putus-putus tipis `#555555` (`stroke-dasharray="4,3"`) atau solid `#666666` dengan latar putih atau abu-abu ultra-lembut `#F8F9FA`.
- **Garis Alur & Panah**: `#000000` (Hitam solid), ujung panah segitiga terisi padat (`fill="#000000"`).
- **Aksen Terbatas (Jika Diperlukan)**: Khusus perbandingan 2 jalur (misal Data Latih vs Data Uji), gunakan arsiran abu-abu 15% (`#E9ECEF`) atau batas garis ganda, bukan warna mencolok.

---

## 4. Aturan Tata Letak & Konektor Ortogonal (Anti-Overlap)

1. **Jarak Antar-Blok (Spacing)**:
   - Jarak horizontal antar tahapan proses minimal 24 pt.
   - Jarak vertikal antar sub-komponen minimal 14 pt.
   - Bantalan dalam kotak (padding) minimal 8 pt di semua sisi teks.
2. **Konektor Garis Siku 90 Derajat (Orthogonal Connectors)**:
   - Seluruh konektor wajib berupa garis lurus vertikal/horizontal yang berbelok siku-siku 90 derajat.
   - DILARANG garis lengkung kurva Bezier liar yang memotong bodi kotak lain.
   - Setiap label teks pada garis panah (seperti `Ya`, `Tidak`, `Rasio 80:20`) wajib memiliki latar belakang putih polos (`<rect fill="#ffffff">`) agar tidak tertimpa garis panah.

---

## 5. Tata Cara Penyisipan ke Naskah (The Narrative Bridge & Caption Protocol)

Sesuai aturan naskah skripsi Indonesia:
1. **Kalimat Pengantar Wajib**: Wajib ada kalimat di paragraf sebelum gambar yang merujuk nomor gambar:
   *"Alur tahapan pelaksanaan penelitian divisualisasikan pada Gambar 3.1 sebagai berikut:"*
2. **Posisi & Format Label Gambar**:
   - Selalu diletakkan di **BAWAH** gambar, 100% Rata Tengah (*Center*).
   - Format: `Gambar X.Y Judul Gambar` tanpa titik dua setelah nomor (contoh: `Gambar 3.1 Alur Penelitian`, `Gambar 3.4 Arsitektur MobileNetV2 dengan Transfer Learning`).
3. **Bedah Narasi Pasca-Gambar**:
   - Paragraf sesudah gambar WAJIB menguraikan logika setiap tahapan dan percabangan alur panah tersebut secara rinci.

