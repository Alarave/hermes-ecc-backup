# Sintesis State-of-the-Art (SOTA) 42 Referensi Jurnal Riset

Dokumen ini memuat pemetaan komprehensif 42 literatur ilmiah (35 jurnal internasional peer-reviewed/ArXiv Q1 + 7 skripsi dan jurnal nasional terakreditasi) yang menjadi landasan teoritis dan metodologis skripsi:
*Komparasi Kinerja Model Multimodal Konvensional Hibrida (Florence-2 dan PaddleOCR) terhadap Agentic MLLM (Qwen2-VL) untuk Verifikasi Kesesuaian Iklan Katalog Kosmetik Sociolla*.

---

## 1. Pemetaan 5 Pilar Penelitian ke Literatur

| Pilar | Domain Fokus | Paper Kunci | Kontribusi Ilmiah terhadap Skripsi |
|---|---|---|---|
| **Pilar 1** | **Visual Grounding & Phrase Localization** | Xiao et al. (2024), Wu et al. (2023 - CPG), Giahi et al. (2025 - VL-CLIP), Rantisi (2025) | Dasar penggunaan `<CAPTION_TO_PHRASE_GROUNDING>` pada Florence-2-base untuk melokalisasi koordinat bounding box atribut merek dan netto pada kanvas 640x640. Normalisasi koordinat spasial ke rentang [0.0, 1.0]. |
| **Pilar 2** | **Scene Text Detection & Recognition (OCR)** | Du et al. (2023 - PP-OCRv4), Liao et al. (2022 - DBNet++), Du et al. (2022 - SVTR), Liu et al. (2026 - TransAnyText), Putri (2026) | Dasar pemilihan PaddleOCR PP-OCRv4 (DBNet++ 4.5M + SVTR-LCNet 12.8M) untuk membaca teks non-planar, melengkung, dan reflektif pada botol/kemasan kosmetik dengan latensi < 60 ms. |
| **Pilar 3** | **Agentic Multimodal LLM & Active Reasoning** | Wang et al. (2024 - Qwen2-VL), Yao et al. (2023 - ReAct), Kumar et al. (2026 - TRACE), Wu et al. (2026 - Visual Search CoT) | Dasar rancangan siklus penalaran ReAct otonom (<= 5 langkah) dengan micro-tools `crop_roi`, `enhance_patch`, dan `finalize_verdict` untuk verifikasi aktif kemasan kosmetik Sociolla. |
| **Pilar 4** | **Data Leakage & Preprocessing Standard** | Kaufman et al. (2012), Yang et al. (2022 - MAVE), Zuiderveld (1994 - CLAHE), Chen et al. (2026 - Element-Aware) | Justifikasi pemisahan bebas bocor stratified group split by brand (70:15:15) pada 3.168 sampel bersih, letterbox padding 640x640 latar putih, dan CLAHE kanal L ruang warna LAB. |
| **Pilar 5** | **Evaluasi Metrik & Signifikansi Statistik** | Dietterich (1998 - McNemar Test), Ningrum, Mutiara, & Ikasari (2026 - WVisionBERT-VL Gunadarma), Levenshtein (1966) | Formulasi uji McNemar dengan koreksi kontinuitas Edwards (alpha = 0.05) pada data uji berpasangan 476 produk, evaluasi CER/WER, dan string matching Levenshtein >= 0.85. |

---

## 2. Bedah 35 Jurnal Internasional Inti

1. **Gong et al. (2025) - Visual Zero-Shot E-Commerce Product Attribute Value Extraction (ArXiv 2502.15979)**:
   - *Inti Masalah*: Deskripsi seller sering noisy/kosong.
   - *Metode*: Visual prompting patch salient tanpa bergantung pada teks deskripsi.
   - *Relevansi*: Membuktikan citra fisik kemasan adalah sumber kebenaran utama (ground truth).

2. **Giahi et al. (2025) - VL-CLIP: Visual Grounding and LLM-Augmented Embeddings (ArXiv 2507.17080)**:
   - *Inti Masalah*: CLIP global kehilangan teks kecil dan detail label lokal.
   - *Metode*: Two-stage visual grounding untuk deteksi Region of Interest (RoI).
   - *Relevansi*: Justifikasi pemisahan area badan kemasan vs area label teks detail.

3. **Xu et al. (2024) - MIND: Multimodal Shopping Intention Distillation (ArXiv 2406.10701)**:
   - *Inti Masalah*: Large VLM komputasi lambat dan mahal untuk ribuan katalog.
   - *Metode*: Distilasi pengetahuan LVLM ke model compact.
   - *Relevansi*: Justifikasi komparasi efisiensi parameter dan VRAM antara model ringkas (Florence-2 + PaddleOCR ~250M) vs model besar (Qwen2-VL-7B).

4. **Nulli et al. (2026) - Adapting Vision-Language Models for E-commerce at Scale (ArXiv 2602.11733)**:
   - *Inti Masalah*: VLM domain umum tidak peka teks katalog teknis.
   - *Metode*: E-commerce instruction tuning dan dynamic attribute schema.
   - *Relevansi*: Landasan perancangan system prompt dan JSON formatting pada pipeline agentic.

5. **Shukla & Sonalkar (2025) - Fine-Grained Attribute Prediction Zero-Shot Analysis (ArXiv 2507.09950)**:
   - *Inti Masalah*: Evaluasi frontier VLM (GPT-4o mini, Gemini 2.0 Flash) pada atribut mikro.
   - *Temuan*: Akurasi makro >86%, namun teks kemasan anjlok <62% karena halusinasi angka.
   - *Relevansi*: **Argumen kunci Bab 1 & Bab 2**: VLM tunggal rentan halusinasi angka/karakter fisik, membuktikan perlunya cabang OCR terdedikasi (PaddleOCR).

6. **Wu et al. (2026) - Visual Search Augmented Chain-of-Thought Reasoning (ArXiv 2609.06410)**:
   - *Inti Masalah*: Halusinasi penalaran langsung pada kemasan produk kompleks.
   - *Metode*: CoT bertahap: lokalisasi bukti -> verifikasi keterbacaan -> ekstraksi terkonfirmasi.
   - *Relevansi*: Diadopsi langsung pada alur ReAct `Thought -> Action (crop_roi) -> Observation`.

7. **Khandelwal et al. (2023) - Large Scale Generative Multimodal Attribute Extraction (ArXiv 2306.00379)**:
   - *Metode*: Formulasi ekstraksi sebagai sequence-to-sequence generatif terbuka.
   - *Relevansi*: Menangani variasi format netto kemasan bebas.

8. **Wu et al. (2023) - Catalog Phrase Grounding (CPG) (ArXiv 2308.16354)**:
   - *Metode*: Phrase grounding memetakan kata kunci teks ke koordinat visual kemasan.
   - *Relevansi*: Rujukan task `<CAPTION_TO_PHRASE_GROUNDING>` Florence-2.

9. **Zhang et al. (2025) - Bridging Modality Gaps via Vision-Language Alignment (ArXiv 2508.10116)**:
   - *Metode*: Penyelarasan ruang fitur visual kemasan dan klaim teks.
   - *Relevansi*: Menghilangkan bias visual background katalog.

10. **Liu et al. (2021) - CMA-CLIP: Cross-Modality Attention CLIP (ArXiv 2112.03562)**:
    - *Temuan*: Interaksi intermediate layer jauh lebih unggul dibanding late-fusion dot product.

11. **Ye et al. (2026) - Pailitao-MMSearch: Native E-Commerce Multimodal Search (ArXiv 2607.17499)**:
    - *Metode*: Integrasi token teks OCR sebagai first-class citizen dalam pemrosesan visual.
    - *Relevansi*: Standar industri Alibaba untuk verifikasi produk e-commerce.

12. **Hongwimol et al. (2026) - AutoPKG: Dynamic E-commerce Product-Attribute Knowledge Graph (ArXiv 2604.16950)**:
    - *Metode*: Kanonisasi atribut otomatis dan reduksi inkonsistensi satuan sebesar 84%.
    - *Relevansi*: Menjadi acuan modul `Attribute_Canonicalizer` (standarisasi ml, g, pcs, patch, sheet).

13. **Zhang et al. (2026) - Correcting to Predict: Pseudo-Value Correction (ArXiv 2609.34383)**:
    - *Metode*: PVC-Net mendeteksi inkonsistensi teks seller vs bukti visual kemasan.
    - *Relevansi*: Logika deteksi diskrepansi (discrepancy score) pada modul verifikasi.

14. **Shin et al. (2022) - e-CLIP: Large-Scale Representation in E-commerce (ArXiv 2207.00208)**:
    - *Relevansi*: Model representasi khusus ritel komersial.

15. **De la Comble et al. (2022) - Multi-Modal Attribute Extraction for E-Commerce (ArXiv 2203.03441)**:
    - *Metode*: Gated multimodal fusion adaptif mengatur dominansi citra vs teks per atribut.

16. **Zhou et al. (2026) - SAM-D2Q: Multimodal Doc2Query (ArXiv 2609.04961)**:
    - *Relevansi*: Pemetaan variasi sinonim seller vs teks kemasan resmi.

17. **Cheng et al. (2025) - VideoAVE: Multi-Attribute Video/Multi-view Benchmark (ArXiv 2508.11801)**:
    - *Relevansi*: Pentingnya seleksi sudut pandang tajam untuk OCR.

18. **Chen et al. (2023) - Unified Vision-Language Representation for Same-Style Retrieval (ArXiv 2302.05093)**:
    - *Relevansi*: Membedakan produk identik vs beda varian/ukuran.

19. **Kumar et al. (2026) - TRACE: Agentic Catalog Enrichment with Multi-source Evidence Grounding (ArXiv 2608.20844)**:
    - *Metode*: Framework agentic berbasis tool OCR + tool inspeksi visual + rule-based verifier.
    - *Capaian*: Akurasi audit 94.2% dengan 100% auditability trace.
    - *Relevansi*: **Rujukan utama alur Agentic Qwen2-VL** dan pencatatan jejak keputusan JSON.

20. **Zhang et al. (2026) - KwaiMind Technical Report (ArXiv 2609.26375)**:
    - *Relevansi*: Kebutuhan resolusi tinggi pada area teks kemasan komersial.

21. **Chen et al. (2025) - Factorized Transport Alignment (ArXiv 2512.18117)**:
    - *Relevansi*: Pemisahan representasi sudut kemasan dari semantik teks atribut.

22. **Zhang et al. (2025) - MOON: Generative MLLM-based Multimodal Representation (ArXiv 2508.11999)**:
    - *Relevansi*: Kombinasi penalaran generatif dan scoring numerik.

23. **Lin et al. (2021) - PAM: Product Attention Module Cross Category (ArXiv 2106.04630)**:
    - *Relevansi*: Kondisioning atensi berdasarkan kategori skincare Sociolla.

24. **Chen et al. (2026) - Element-Aware Group Learning (ArXiv 2608.00584)**:
    - *Metode*: Dekomposisi layer visual untuk membuang stiker promosi/watermark seller.
    - *Relevansi*: Eliminasi noise grafis non-kemasan sebelum OCR.

25. **Liu et al. (2026) - TransAnyText: Translating Arbitrary Text in E-commerce (ArXiv 2608.16284)**:
    - *Temuan*: OCR scene text DBNet/SVTR capai F-measure 88.7% pada teks melengkung botol, sedangkan Tesseract hanya 41.2%.
    - *Relevansi*: Justifikasi mutlak pemilihan PaddleOCR dibanding OCR dokumen biasa.

26. **Jenq & Shen (2025) - Turning Adversaries into Allies: Reversing Typographic Attacks (ArXiv 2511.05325)**:
    - *Relevansi*: Isolasi teks via OCR fisik mencegah manipulasi teks editan seller.

27. **Yang et al. (2024) - Hierarchical Knowledge Graph Construction (ArXiv 2410.21237)**:
    - *Relevansi*: Taksonomi hierarki merek dan atribut kemasan kosmetik.

28. **Tur et al. (2024) - Fine-grained Retail Product Discrimination (ArXiv 2409.14963)**:
    - *Relevansi*: Pembedaan varian kemasan yang mirip melalui prompt ensembling.

29. **Qin et al. (2026) - TexTailor: Texture-Preserving Video Conditioning (ArXiv 2609.39335)**:
    - *Relevansi*: Menghindari kompresi downscaling ekstrem pada area label teks kemasan.

30. **Kulunk et al. (2025) - Optimizing Product Deduplication in E-Commerce (ArXiv 2509.15858)**:
    - *Relevansi*: Cosine similarity dan vector thresholding untuk konsistensi katalog.

31. **Cui et al. (2023) - PV2TEA: Patching Visual Modality to Textual IE (ArXiv 2306.01016)**:
    - *Relevansi*: Desain modular adaptif ekstraksi teks dan bukti visual.

32. **Zhai et al. (2023) - Sigmoid Loss for Language Image Pre-Training (SigLIP) (ArXiv 2303.15343)**:
    - *Metode*: Sigmoid cross-entropy independen menggantikan softmax global CLIP.

33. **Liao et al. (2022) - Real-Time Scene Text Detection with Differentiable Binarization (DBNet++)**:
    - *Metode*: Binarisasi adaptif terintegrasi FPN untuk lokalisasi teks presisi.

34. **Du et al. (2022) - SVTR: Single Visual Model for Single Visual Text Recognition**:
    - *Metode*: Transformer visual murni untuk pengenalan karakter tanpa ketergantungan RNN.

35. **Du et al. (2023/2024) - PP-OCRv4: A Compact and Effective OCR System**:
    - *Metode*: Detektor DBNet++ 4.5M + SVTR-LCNet 12.8M dengan latency < 60 ms.

---

## 3. Bedah 7 Skripsi & Jurnal Nasional Indonesia

36. **Ningrum, Mutiara, & Ikasari (2026) - WVisionBERT-VL (IJ-AI Vol 15 No 4, DOI: 10.11591/ijai.v15.i4.pp3365-3375)**:
    - *Afiliasi*: Universitas Gunadarma (Prof. Dr. Achmad Benny Mutiara).
    - *Kontribusi*: Arsitektur Bidirectional Multi-Head Cross Attention (BMHCA) untuk fusi modalitas visual dan bahasa Indonesia dengan F1-Score 94.12%.
    - *Peran Skripsi*: Rujukan teoritis kunci Universitas Gunadarma untuk fusi cross-modal teks klaim dan bukti visual kemasan.

37. **Farhan Abel Rantisi (2025) - Penerapan LayoutLM untuk Ekstraksi Informasi Nutrisi Label Kemasan**:
    - *Afiliasi*: Universitas Sriwijaya.
    - *Kontribusi*: Pemanfaatan koordinat spasial 2D bounding box `[0, 1000]` mencapai Macro F1 92.69%.
    - *Peran Skripsi*: Justifikasi harmonisasi spasial koordinat bounding box antara Florence-2 dan PaddleOCR.

38. **Nadya Putri (2026) - Implementasi PaddleOCR untuk Ekstraksi Karakter Alfanumerik**:
    - *Afiliasi*: UIN Ar-Raniry Banda Aceh.
    - *Kontribusi*: Bukti empiris akurasi PaddleOCR >94% pada data karakter bahasa Indonesia dengan latensi < 1 detik.
    - *Peran Skripsi*: Validasi keandalan PaddleOCR pada lingkungan riset Indonesia.

39. **Tim Peneliti Unpas (2024) - Deteksi Tanggal Kedaluwarsa Kemasan YOLOv8 vs YOLOv11 + PaddleOCR**:
    - *Afiliasi*: Universitas Pasundan (Jurnal Infomatek).
    - *Kontribusi*: Akurasi karakter 94.76% pada teks fisik kemasan dengan memisahkan isolasi RoI dan OCR.

40. **Tagi Huma & Fanggidae (2026) - Deteksi dan Ekstraksi Kandungan Gula Kemasan (Jurnal Sainstek Undana)**:
    - *Kontribusi*: Presisi 91.2% dalam memisahkan entitas nama atribut dan kuantitas angka serta satuannya.
    - *Peran Skripsi*: Rujukan parser regex netto dan normalisasi satuan metrik.

41. **Peneliti UMG (2024) - OCR dan Algoritma Pencocokan String untuk Skincare (Jurnal Indexia)**:
    - *Kontribusi*: Akurasi pencocokan 89.5% menggunakan kombinasi OCR dan string matching terstruktur.
    - *Peran Skripsi*: Dasar pemilihan ambang batas Levenshtein Similarity >= 0.85 untuk nama merek kosmetik.

42. **Peneliti Unisla (2024) - Analisis Akurasi Karakter YOLOv8 dan EasyOCR (Jurnal Teknika)**:
    - *Kontribusi*: Prapemrosesan citra meningkatkan akurasi karakter sebesar 14.8%.
    - *Peran Skripsi*: Justifikasi penerapan filter CLAHE ruang warna LAB sebelum ekstraksi OCR.
