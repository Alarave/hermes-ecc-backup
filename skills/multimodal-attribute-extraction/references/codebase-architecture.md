# Arsitektur Komparatif 21 Repositori Kode Referensi

Dokumen ini memetakan 21 repositori kode sumber terbuka lokal (`REFERENSI CODE/`) dan menyelaraskannya dengan kebutuhan skripsi:
*Komparasi Kinerja Model Multimodal Konvensional Hibrida (Florence-2 dan PaddleOCR) terhadap Agentic MLLM (Qwen2-VL) untuk Verifikasi Kesesuaian Iklan Katalog Kosmetik Sociolla*.

---

## 1. Pemetaan 21 Repositori ke 6 Fase CRISP-DM / Tasks

```text
+---------------------------------------------------------------------------------+
|                                 CRISP-DM PIPELINE                               |
|                                                                                 |
| 1. Ingestion & EDA          2. Preprocessing & Split     3. Conventional Hybrid |
| (Task 1)                    (Task 2)                     (Task 3)               |
| Repos: 01-04, 05            Repos: 05, 19                Repos: 07, 13, 14, 15  |
|                             (MAVE, LayoutLM Box)         (PaddleOCR, Florence-2)|
|                                                                                 |
| 4. Agentic MLLM             5. Benchmark & McNemar       6. Interactive Demo    |
| (Task 4)                    (Task 5)                     (Task 6)               |
| Repos: 12, 17, 22           Repos: 08, 20, 21            Repos: 01-04           |
| (Qwen-VL, LLaVA, ReAct)     (Scipy/Statsmodels, Eval)    (Streamlit Dashboard)  |
+---------------------------------------------------------------------------------+
```

---

## 2. Taksonomi Repositori Lokal

### Kategori A: Pipeline Pencocokan Produk E-Commerce (Folder 01 s.d. 04)
- **01_shopee_product_matching_jingxuan**: Ekstraksi fitur visual (EfficientNet) dan teks judul katalog (TF-IDF/BERT) dengan cosine distance. Diadopsi untuk arsitektur feature extraction baseline.
- **02_shopee_product_matching_cr21**: Penerapan ArcFace margin loss untuk memisahkan representasi visual produk beda varian. Memberi wawasan pemisahan varian botol kosmetik serupa.
- **03_shopee_product_matching_mingrui**: Arsitektur ensemble multimodal (Timm + HuggingFace Transformers) untuk mencocokkan kemiripan cross-modal gambar dan judul.
- **04_shopee_product_matching_jackson**: Pipeline prapemrosesan gambar e-commerce dan pipeline ekstraksi NLP berbasis Scikit-learn dan OpenCV.

### Kategori B: Standar Taksonomi Atribut Multimodal (Folder 05)
- **05_google_mave_dataset_tools**: Repositori resmi Google Research untuk *Multi-source Attribute Value Extraction*.
  - *Fungsi*: Menjadi acuan penataan kamus atribut (Brand Name, Net Volume/Weight, Unit Normalization), struktur data JSON, dan pembersihan token noise pada klaim penjual.

### Kategori C: Model Vision-Language Foundation & Grounding (Folder 07 s.d. 12, 22)
- **07_ofa_multimodal_foundation**: Framework Sequence-to-Sequence multimodal untuk visual grounding `<grounding>` dan phrase localization.
- **08_openai_clip**: Repositori resmi OpenAI CLIP. Digunakan sebagai pembanding zero-shot similarity visual-tekstual global.
- **09_salesforce_blip**: Bootstrapping Language-Image Pretraining dengan modul multimodal cross-attention.
- **10_vilt_vision_language_transformer**: Vision-Language Transformer cepat tanpa region convolution.
- **11_pytorch_torchmultimodal**: Pustaka modular Meta AI untuk arsitektur fusi multimodal.
- **12_haotian_llava**: Visual instruction tuning dan alur inferensi percakapan visual resolusi tinggi.
- **22_qwen_vl_multimodal**: Repositori resmi Qwen-VL (basis arsitektur Qwen2-VL-7B-Instruct). Mendukung resolusi dinamis (*Native Dynamic Resolution*) dan membaca koordinat spasial format `[ymin, xmin, ymax, xmax]` secara zero-shot. Menjadi inti implementasi **Task 4 (Agentic MLLM Pipeline)**.

### Kategori D: Optical Character Recognition & Text Spotting (Folder 13 s.d. 17)
- **13_paddlepaddle_paddleocr**: Repositori PP-OCRv4 (DBNet++ detektor + SVTR rekognizer).
  - *Fungsi*: Mesin OCR utama pada **Task 3 (Conventional Pipeline)** untuk mengekstrak teks fisik kemasan melengkung dan label netto dengan keyakinan >= 0.50.
- **14_jaidedai_easyocr**: Model CRAFT detektor + BiLSTM recognizer. Digunakan sebagai baseline komparasi pemilihan mesin OCR.
- **15_openmmlab_mmocr**: Toolbox Key Information Extraction (KIE) berbasis deteksi poligon teks.
- **16_mindee_doctr**: Document & Scene Text Recognition untuk parsing hierarki teks pada citra kemasan.
- **17_ucas_got_ocr2**: End-to-End Vision-Language Model OCR untuk ekstraksi teks kompleks resolusi tinggi.

### Kategori E: Visual Document Understanding & Spatial Grounding (Folder 18, 19)
- **18_clovaai_donut**: OCR-free VDU Transformer untuk memetakan citra langsung ke JSON terstruktur.
- **19_microsoft_unilm_layoutlm**: Multimodal spatial-text transformer.
  - *Fungsi*: Menjadi rujukan normalisasi koordinat bounding box spasial 2D ke rentang seragam `[0.0, 1.0]` dan formula kalkulasi *Intersection over Area* (IoA).

### Kategori F: Algoritma Pencocokan, NLP, & Vektor (Folder 20, 21)
- **20_cross_modality_attention**: Parsing entitas NLP spesifik dan pemisahan kuantitas numerik dengan satuannya.
- **21_faiss_vector_similarity**: Library pencarian kemiripan vektor embeddings efisien skala besar.

---

## 3. Integrasi Implementasi Teknis ke Alur Pengerjaan

1. **Prapemrosesan Citra (Task 2)**: Mengadopsi filter CLAHE OpenCV dan letterbox padding dari repositori `04_shopee_product_matching_jackson`.
2. **Kanonisasi Atribut (Task 2)**: Mengadopsi parser regex kuantitas numerik dan pemetaan satuan dari repositori `05_google_mave_dataset_tools`.
3. **Pipeline Konvensional (Task 3)**: Menggabungkan task visual grounding Florence-2-base dengan detektor DBNet++ dan rekognizer SVTR dari repositori `13_paddlepaddle_paddleocr`.
4. **Pipeline Agentic (Task 4)**: Menerapkan model Qwen2-VL dari repositori `22_qwen_vl_multimodal` dalam siklus ReAct 5 langkah dengan alat inspeksi visual `crop_roi` dan `enhance_patch`.
5. **Evaluasi Benchmark (Task 5)**: Menggunakan metrik evaluasi klasifikasi scikit-learn, Levenshtein distance, CER/WER, dan uji McNemar statsmodels.
6. **Dasbor Peraga (Task 6)**: Membangun dasbor interaktif Streamlit yang menyajikan perbandingan visual side-by-side kedua paradigma.
