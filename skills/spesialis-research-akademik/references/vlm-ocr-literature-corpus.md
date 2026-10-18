# Korpus Sintesis Literatur & Riset Empiris Vision-Language dan OCR (vlm-ocr-literature-corpus)

Dokumen rujukan komprehensif 35 jurnal internasional (2021-2026), 6 skripsi dan jurnal nasional Indonesia, taksonomi klaster model, komparasi platform deployment, serta kerangka storytelling sidang sarjana untuk topik *Penerapan Model Hibrida Vision-Language dan OCR untuk Verifikasi Atribut Kemasan Produk Katalog E-Commerce Shopee*.

---

## 1. Taksonomi 3 Klaster Pilar Model Berdasarkan 35 Literatur

Sintesis terhadap 35 referensi jurnal internasional memetakan arsitektur riset ke dalam 3 klaster pilar fungsional:

### Klaster 1: Vision-Language Encoder (Backbone Visual-Semantik)
- **Model Utama**: CLIP (ViT-B/16, ViT-L/14), SigLIP (Google), e-CLIP, CMA-CLIP, PaliGemma-3B, Qwen2-VL.
- **Peran Riset**: Mengekstrak representasi visual kemasan produk dan menyelaraskannya dengan representasi teks judul atau deskripsi katalog ke dalam ruang vektor bersama (*joint embedding space*).
- **Rujukan Kunci**:
  * *Gong et al. (2025)*: Visual Zero-Shot AVE mengekstrak atribut kemasan langsung dari citra tanpa teks seller (Macro-F1 +14.2%).
  * *Shukla & Sonalkar (2025)*: Evaluasi frontier VLM membuktikan VLM murni akurat pada atribut makro (>86%), namun anjlok drastis pada teks kemasan kecil (<62%), membuktikan perlunya engine OCR terdedikasi.
  * *Yada et al. (Mercari, 2025)*: Fine-tuning SigLIP dengan sigmoid cross-entropy loss mengungguli softmax contrastive pada e-commerce (CTR +50%, CVR +14%).

### Klaster 2: Scene Text Spotting & Deep OCR (Ekstraksi Teks Fisik Kemasan)
- **Model Utama**: DBNet++ (detektor teks bentuk kurva/arbitrary), SVTR / CRNN (pengenal deretan teks alfanumerik), PaddleOCR-v4, LayoutLMv3.
- **Peran Riset**: Membaca teks fisik yang tercetak pada kemasan produk (label netto, nomor registrasi BPOM RI, tanggal kedaluwarsa, daftar komposisi) tanpa terdistorsi bentuk fisik kemasan botol, kaleng, atau pouch melengkung.
- **Rujukan Kunci**:
  * *Liu et al. (2026)*: TransAnyText membuktikan deteksi teks kemasan melengkung berbasis DBNet++ mencapai F-measure 88.7%, melampaui OCR dokumen datar (Tesseract: 41.2%).
  * *Wu et al. (2023)*: Catalog Phrase Grounding (CPG) menghubungkan frasa atribut teks dengan koordinat bounding box pada citra kemasan via modulated transformer.

### Klaster 3: Cross-Modal Verification & Discrepancy Gate (Logika Audit & Fusi)
- **Model Utama**: PVC-Net, CPG, TRACE Agent, Gated Cross-Attention Unit, Dual-Stream Discrepancy Detector.
- **Peran Riset**: Menghitung skor konsistensi (*cross-modal consistency score*) antara klaim seller pada katalog dengan bukti fisik yang terkonfirmasi pada kemasan produk.
- **Rujukan Kunci**:
  * *Zhang et al. (2026)*: PVC-Net (Correcting to Predict) mendeteksi ketidaksesuaian label seller dan bukti fisik kemasan (F1-score +11.4% pada label noise 30%).
  * *Kumar et al. (2026)*: TRACE Agent menghadirkan audit katalog e-commerce berbasis multi-source evidence grounding dengan akurasi audit 94.2% dan jejak audit (auditability trace) 100%.
  * *Jenq & Shen (eBay, 2025)*: Mengisolasi teks gambar via OCR memangkas kerentanan manipulasi teks kemasan palsu hingga 76%.

---

## 2. Sintesis 6 Skripsi & Jurnal Nasional Indonesia (Empirical Baselines)

Rujukan nasional resmi untuk memperkuat landasan konteks lokal pada Bab 2 dan Bab 3:

| No | Peneliti & Institusi | Judul & Publikasi | Metode | Temuan Kunci & Metrik | Relevansi untuk Skripsi |
|---|---|---|---|---|---|
| 1 | Farhan Abel Rantisi (Univ. Sriwijaya, 2025) | Penerapan Named Entity Recognition (NER) Menggunakan Arsitektur LayoutLM untuk Ekstraksi Informasi Nutrisi Label Makanan Kemasan | LayoutLM (Multimodal Transformer + 2D Bounding Box Spatial) | F1-Score: 92.69% pada label kemasan produk fisik komersial | Landasan Bab 2 & 3: Ekstraksi atribut kemasan wajib memanfaatkan koordinat spasial 2D normalized `[0, 1000]`. |
| 2 | Nadya Putri (UIN Ar-Raniry, 2026) | Implementasi Optical Character Recognition Untuk Otomatisasi Penginputan Agenda Surat | PaddleOCR (DBNet + SVTR) terintegrasi Web Backend | Presisi pengenalan karakter tinggi pada teks bahasa Indonesia | Template metodologi pengujian kinerja PaddleOCR pada teks berbahasa Indonesia. |
| 3 | Tim Peneliti Univ. Pasundan (2024) | Deteksi Tanggal Kedaluwarsa pada Produk Kemasan: Analisis Komparatif YOLOv8 dan YOLOv11 Berbasis PaddleOCR (Jurnal Infomatek) | Deteksi RoI Kemasan + PaddleOCR | Akurasi karakter: 94.76% pada teks kemasan komersial | Rujukan langsung ekstraksi atribut Tanggal Kedaluwarsa (*Expired Date*). |
| 4 | Alexander W. T. Huma dkk. (Univ. Nusa Cendana, 2026) | Deteksi dan Ekstraksi Kandungan Gula pada Kemasan Menggunakan YOLOv8 dan PaddleOCR (Sainstek Undana) | Decoupled Head RoI + PaddleOCR Teks Alfanumerik | Presisi ekstraksi entitas nama dan kuantitas unit | Rujukan pemisahan entitas atribut dan nilai besaran (contoh: 'Netto' dan '100 ml'). |
| 5 | Peneliti Univ. Muhammadiyah Gresik (2024) | Implementasi OCR dan Algoritma Aho-Corasick untuk Deteksi Bahan Berbahaya Produk Skincare (Jurnal Indexia) | OCR Kemasan Skincare + String Matching Aho-Corasick | Deteksi bahan berbahaya otomatis berbasis kamus aturan | Rujukan alur verifikasi pencocokan teks kemasan terhadap database regulasi BPOM. |
| 6 | Peneliti Univ. Islam Lamongan (2024) | Analisis Akurasi Pembacaan Karakter Menggunakan YOLOv8 dan EasyOCR (Jurnal Teknika) | Preprocessing Citra Fisik + EasyOCR Character Parsing | Evaluasi CER dan WER pada citra sudut bervariasi | Dasar komparasi pemilihan engine OCR (PaddleOCR vs EasyOCR) pada Bab 3. |

---

## 3. Matriks 5 Atribut Target Kemasan Shopee & Aturan Verifikasi

| No | Atribut Target | Modalitas Sumber | Model Ekstraktor | Logika Verifikasi & Pencocokan | Toleransi Error |
|---|---|---|---|---|---|
| 1 | **Merek / Brand** | Citra Visual (Logo) + Teks OCR | SigLIP + PaddleOCR | Bounding Box Grounding + Fuzzy Jaro-Winkler Matching | Similarity >= 0.85 |
| 2 | **Isi Bersih / Netto** | Teks OCR Kemasan | PaddleOCR + Regex Parser | Normalisasi Satuan (g/kg/ml/l) vs Atribut Judul Katalog | Selisih nilai = 0 (Eksak setelah konversi unit) |
| 3 | **Nomor Izin BPOM / P-IRT** | Teks OCR Kemasan | Regex Formal BPOM (NA/MD/ML 11-12 digit) | Pencocokan Pola Karakter Eksak (Deterministic Regex) | Zero Tolerance (Harus 100% karakter valid) |
| 4 | **Varian / Rasa / Aroma** | Visual + Teks OCR | Vision-Language (Qwen2-VL / CLIP) | Cross-Attention Classification vs Klaim Varian Seller | Cosine Similarity >= 0.80 |
| 5 | **Tanggal Kedaluwarsa** | Teks OCR Kemasan | PaddleOCR + Date Parser | Parsing format DD/MM/YYYY atau MM/YYYY | Validasi tanggal >= hari audit verifikasi |

---

## 4. Evaluasi 4 Platform Deployment untuk Sidang Sarjana

| Platform / Framework | Kompleksitas | Latensi Respon | Keunggulan untuk Sidang Skripsi | Posisi Rekomendasi |
|---|---|---|---|---|
| **Streamlit (Python Web App)** | Sangat Rendah | Cepat (In-memory) | Integrasi native PyTorch/OpenCV, visualisasi bounding box interaktif, tabel audit, drag-and-drop foto produk. | **PILIHAN UTAMA (#1) DEMO SIDANG** |
| **Gradio (Hugging Face)** | Rendah | Cepat | Cocok untuk prototipe satu fungsi inferensi, namun layout multi-tabel katalog e-commerce terbatas. | Alternatif Prototipe Cepat |
| **FastAPI + React / Vue** | Tinggi | Sangat Cepat (Asinkron) | Arsitektur standar industri microservices, namun membutuhkan waktu pengembangan frontend terpisah. | Tingkat Lanjut (Production Benchmark) |
| **ONNX Runtime / TensorRT** | Menengah | Ultra Cepat | Mengoptimasi bobot model Vision-Language agar inferensi ringan dan lancar di laptop saat sidang. | Optimasi Akselerasi Inferensi |

---

## 5. Kerangka Storytelling Sidang: Alur Operasional & Alur Riset

### A. Narasi Alur Operasional (Kacamata Pengguna / Auditor Shopee)
1. **Kasus Nyata (The Problem)**: Seller mendaftarkan produk dengan judul *"Serum Wajah 100ml BPOM NA18211900123"*, namun mengunggah foto kemasan sampel 50 ml. Pembeli dirugikan dan katalog e-commerce mengalami inkonsistensi data.
2. **Tahap 1 - Ingestion**: Sistem menerima foto kemasan produk beserta teks judul dan deskripsi dari etalase seller.
3. **Tahap 2 - Preprocessing**: Filter watermark stiker promo ("Gratis Ongkir", "COD") dan normalisasi orientasi kemasan.
4. **Tahap 3 - Dual-Path Extraction**:
   - Jalur Fisik (PaddleOCR): Membaca teks netto (50 ml) dan deretan digit BPOM (NA18211900123).
   - Jalur Semantik (SigLIP/Qwen2-VL): Memverifikasi bentuk botol, logo brand, dan varian rasa/warna.
5. **Tahap 4 - Normalisasi & Kanonisasi**: Penyelarasan satuan volume dan format teks.
6. **Tahap 5 - Discrepancy Gate**: Komparasi klaim seller (100 ml) vs bukti fisik (50 ml) menghasilkan status **MISMATCH**.
7. **Tahap 6 - Laporan Audit Interaktif**: Ditampilkan pada dashboard Streamlit dengan bukti visual crop kemasan, koordinat bounding box, dan rekomendasi aksi moderasi.

### B. Narasi Alur Riset (Kacamata Metodologis Peneliti / Bab 1-5 CRISP-DM)
1. **Business Understanding**: Identifikasi pelanggaran UU No. 8/1999 dan Peraturan BPOM No. 31/2018 akibat deskripsi katalog seller yang tidak sesuai kemasan fisik.
2. **Data Understanding**: Analisis karakteristik citra e-commerce (kemasan melengkung, pencahayaan reflektif, font artistik).
3. **Data Preparation**: Anotasi bounding box 2D koordinat `[0, 1000]`, augmentasi rotasi dan kontras CLAHE.
4. **Modeling**: Perancangan pipeline hibrida dua cabang (Scene Text Spotting + Vision-Language Representation).
5. **Evaluation**: Pengujian akurasi verifikasi, CER/WER OCR, Macro-F1, serta uji signifikansi statistik formal McNemar Test ($p < 0.05$) terhadap model baseline tunggal.
