# Preset Diagram Skripsi & Naskah Ilmiah Indonesia
*(Standar Format Vektor FigGenie untuk Tugas Akhir, Skripsi, dan Jurnal Nasional)*

Modul ini adalah acuan baku rendering visual arsitektur sistem, kerangka pikir penelitian, dan alur metodologi agar sesuai dengan tradisi akademik Indonesia (Gunadarma, UPNVJ, UI, ITB) dan siap disisipkan ke Word (`.docx`) maupun PDF via Typst/LaTeX.

---

## 1. Parameter Geometri & Tipografi Wajib

| Parameter | Spesifikasi Baku | Keterangan |
|---|---|---|
| **Keluarga Huruf (Font Family)** | `Times New Roman`, `serif` | Wajib identik dengan font teks tubuh naskah skripsi |
| **Ukuran Huruf Judul Blok** | 10 pt sampai 11 pt (Bold) | `font-weight: 600`, kapitalisasi judul (Title Case) |
| **Ukuran Huruf Keterangan / Item** | 8.5 pt sampai 9.5 pt (Regular) | `font-weight: 400`, tidak boleh lebih kecil dari 8 pt |
| **Ukuran Huruf Anotasi / Dimensi** | 7.5 pt sampai 8 pt (Italic) | Untuk keterangan ukuran layer, parameter shape, atau hiperparameter |
| **Tebal Garis Batas (Stroke)** | 0.75 pt sampai 1 pt | Garis tepi kotak proses dan kontainer utama |
| **Tebal Garis Panah Alur** | 1 pt sampai 1.25 pt | Garis aliran data/proses utama dengan kepala panah tegas |
| **Latar Belakang (Background)** | `#FFFFFF` (Putih Solid) | **DILARANG transparan** agar tidak berbayang saat dicetak atau di-convert ke DOCX |

---

## 2. Palet Warna Akademik Formal (Anti-Warna Neon AI)

Dilarang menggunakan palet warna neon khas slide presentasi AI (ungu cerah, gradasi pelangi). Gunakan palet resmi monokrom atau aksen biru akademik (*academic slate*):

- **Kontainer Latar / Grup**: `#F8F9FA` atau `#F1F3F5` (Abu-abu sangat lembut, border `#CED4DA`).
- **Kotak Input / Data Mentah**: `#E9ECEF` (Border `#ADB5BD`, teks `#212529`).
- **Kotak Proses / Algoritma**: `#E7F5FF` (Biru lembut formal, border `#339AF0` atau `#1C7ED6`, teks `#1864AB`).
- **Kotak Output / Keputusan**: `#E6FCF5` (Hijau lembut formal, border `#20C997`, teks `#087F5B`).
- **Kotak Evaluasi / Pengujian**: `#FFF4E6` (Oranye lembut formal, border `#FF922B`, teks `#D9480F`).

---

## 3. Aturan Tata Letak & Anti-Tumpang Tindih (Anti-Overlap)

1. **Jarak Antar-Blok (Spacing)**:
   - Jarak horizontal antar tahapan proses minimal 24 pt.
   - Jarak vertikal antar sub-komponen minimal 14 pt.
   - Bantalan dalam kotak (padding) minimal 8 pt di semua sisi teks.
2. **Arah Aliran Standar**:
   - Kerangka Pikir (Bab 3.1): Aliran Vertikal Atas-ke-Bawah (*Top-to-Bottom*) atau Kiri-ke-Kanan (*Left-to-Right*).
   - Arsitektur Model / Pipeline (Bab 3.2): Aliran Linear Kiri-ke-Kanan dengan percabangan paralel yang simetris.
3. **Penamaan Komponen Bahasa Indonesia Baku**:
   Gunakan istilah baku:
   - "Pengumpulan Data" (bukan sekadar Data Gathering)
   - "Pra-pemrosesan Data" (bukan Preprocessing mentah)
   - "Ekstraksi Fitur"
   - "Pelatihan Model"
   - "Evaluasi & Pengujian Metrik"

---

## 4. Format Keluaran Fisik Ganda (Dual Output Requirement)

Setiap pembuatan diagram wajib mengekspor dua format di direktori `figures/` naskah:
1. `figures/<nama-gambar>.svg`: Berkas vektor murni beresolusi tak terhingga untuk kompilasi Typst/LaTeX.
2. `figures/<nama-gambar>.png`: Render raster beresolusi tinggi (300 DPI) dengan latar putih solid untuk disisipkan ke naskah Word (`.docx`) tanpa distorsi font.

---

## 5. Tata Cara Penyisipan ke Naskah (The Caption Protocol)

Sesuai aturan naskah skripsi Indonesia:
- **Kalimat Pengantar Wajib**: Wajib ada kalimat di paragraf sebelum gambar:
  *"Kerangka pikir penelitian disajikan pada Gambar 3.1 sebagai berikut:"*
- **Posisi Label Gambar**: Selalu diletakkan di **BAWAH** gambar, rata tengah:
  ```text
  Gambar 3.1 Kerangka Pikir Penelitian Klasifikasi Sentimen
  ```
  *(Times New Roman 11 pt, spasi 1.0)*
