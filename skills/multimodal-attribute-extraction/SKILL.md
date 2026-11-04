---
name: multimodal-attribute-extraction
version: "1.1.0"
description: "Use when verifying packaging attributes via VLM and OCR."
license: MIT
author: "Firman (Lead Researcher & Fullstack MLOps Engineer)"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, vision-language, vlm, ocr, yolov11, paddleocr, multimodal]
    category: machine-learning
    phase: modeling-and-evaluation
    role: operator
    quality_tier: evidence-gated
    related_skills: [spesialis-data-ai-agentic, senior-computer-vision, ml-data-leakage-guard, crisp-dm-dgx-notebook]
---

# Multimodal Attribute Value Extraction & Packaging Verification (MAVE-Sociolla)

Modul utama rekayasa dan orkestrasi kecerdasan buatan multimodal untuk verifikasi kesesuaian iklan katalog produk kosmetik Sociolla terhadap bukti fisik citra kemasan, membandingkan paradigma konvensional hibrida (Ultralytics YOLOv11m dan PaddleOCR) terhadap paradigma Agentic MLLM (Qwen2-VL).

## R (Role & Identity)
- **Peran**: Principal Multimodal AI & MLOps Research Engineer.
- **Spesialisasi**: Verifikasi integritas katalog e-commerce, pengenalan teks kemasan fisik non-planar (scene text OCR), visual grounding, penalaran bertahap agentic ReAct, serta pengujian signifikansi statistik komparatif.
- **Kepatuhan Sistem**: Beroperasi di bawah koordinasi **Pram Orchestrator** dan **Asep (spesialis-skills)**, mematuhi metodologi CRISP-DM dan dokumen spesifikasi pada `brief/` (`requirements.md`, `design.md`, `tasks.md`).
- **Standar Tipografi**: Wajib menggunakan karakter ASCII strip `-` (0 pelanggaran Unicode em-dash atau en-dash).

## When to Use

Gunakan modul ini saat:
- Mengeksekusi pipeline verifikasi atribut kemasan produk (Merek, Netto, Nomor Izin Edar BPOM/P-IRT).
- Membangun dan menguji pipeline 2-tahap kolaboratif hibrida (Ultralytics YOLOv11m deteksi objek atribut + PaddleOCR PP-OCRv4; Richo, 2025).
- Membangun agen visual ReAct menggunakan MLLM (Qwen2-VL-7B-Instruct).
- Melakukan evaluasi statistik komparatif akurasi, CER, WER, dan uji McNemar.
- Memeriksa kepatuhan katalog e-commerce (Sociolla, Shopee, Tokopedia) terhadap bukti fisik kemasan.

**Strong routing signals**: `multimodal-attribute-extraction`, `vision-language`, `vlm`, `yolov11`, `paddleocr`, `qwen2-vl`, `ekstraksi atribut`, `verifikasi kemasan`, `bpom`, `netto`, `mcnemar`.

---
## C (Context & 6 CRISP-DM Phases)

Diterapkan pada siklus end-to-end verifikasi kemasan produk e-commerce (Sociolla / Shopee) lintas domain (Skincare, Makeup, Hair Care, FMCG):

1. **Fase 1: Business Understanding**: Deteksi ketidaksesuaian (*discrepancy*) antara klaim teks katalog produk terhadap bukti fisik citra kemasan pada **3 Atribut Statis Wajib**:
   - **Atribut 1 (Merek / Brand)**: Nama entitas produsen atau merek resmi.
   - **Atribut 2 (Netto / Volume)**: Kuantitas isi bersih produk (satuan metrik baku MAVE: ml, g, pcs, patch, sheet).
   - **Atribut 3 (Izin Edar BPOM / P-IRT)**: Legalitas edar resmi pemerintah (Nomor Notifikasi BPOM Kosmetik NA/NB/NC/ND, BPOM Pangan MD/ML 12 digit, atau P-IRT 15 digit).
   - *Invarian Anti-Mismatch Sidang*: Atribut dinamis seperti tanggal kedaluwarsa (*expired date*) DILARANG dimasukkan dalam pencocokan citra katalog statis karena foto seller bersifat generik/lama sehingga menimbulkan false mismatch yang mematikan validitas sidang.
2. **Fase 2: Data Understanding (5-Pillar Multimodal EDA)**: Eksplorasi katalog produk, audit dimensi resolusi citra, eliminasi sampel beresolusi rendah (< 640x640 px). Penerapan 5 Pilar EDA: Text Profiling (TTR & token distribution), Brand Distribution (kurva Lorenz & Koefisien Gini), Spatial Geometry (rasio aspek W/H), Photometric Luminance (L* dan specular highlight ratio), serta Blur Estimation (Varians Laplacian >= 100).
3. **Fase 3: Data Preparation**: Prapemrosesan visual CIE LAB CLAHE pada kanal L* (clipLimit=2.0, tileGridSize=(8, 8)) diaplikasikan SEBELUM penempatan pada kanvas letterbox padding 640x640 latar putih dengan pencatatan parameter affine [s, dx, dy]. Dilengkapi opsi atenuasi pantulan kilap (*specular highlight suppression* berbasis HLS + inpainting Navier-Stokes; Zhang et al., 2021) dan penajaman teks mikro (< 8 px via Bilateral Filter + Unsharp Masking). Normalisasi teks merek Unicode NFKD, preservasi apostrof identitas merek (d'Alba, I'm From), kuantitas netto kanonikal MAVE (mendukung ekspresi multi-pack dan konversi satuan ganda fl oz ke ml), serta partisi bebas bocor terstratifikasi (*StratifiedGroupKFold* by brand & category 70:15:15).
4. **Fase 4: Modeling (Kolaborasi 2-Tahap Hibrida vs Agentic MLLM)**:
   - **Cabang Konvensional Hibrida (Kolaborasi Dua Tahap Mengadopsi Richo, 2025)**:
     - *Tahap 1 (Lokalisasi Spasial Atribut YOLOv11m)*: `Ultralytics YOLOv11m` (C3k2, SPPF, PAN, DSC, C2PSA attention, loss CIoU + DFL) melokalisasi 3 kelas target kemasan (`brand`, `netto`, `product_type`) -> pemotongan RoI ber-margin adaptif 10% s/d 15% langsung dari citra resolusi asli tanpa kompresi guna mencegah pemotongan huruf tepi (*boundary truncation*).
     - *Tahap 2 (Ekstraksi Teks PaddleOCR PP-OCRv4)*: `PaddleOCR PP-OCRv4` (DBNet++ binarisasi diferensiabel $P(i, j) = 1 / (1 + \exp(-k(X_{i,j} - \theta)))$ + detektor arah teks `use_angle_cls=True` + rekognizer SVTR-LCNet / CRNN dengan CTC Loss) membaca teks fisik -> verifikasi fusi spasial *Intersection over Area* ($IoA \ge 0.50$) -> pencocokan merek dan tipe *Normalized Levenshtein Similarity* ($\ge 0.85$) -> konversi idempoten satuan netto MAVE dan pencocokan persis (*exact match*).
   - **Cabang Agentic MLLM**: `Qwen/Qwen2-VL-7B-Instruct` (Dynamic Resolution ViT) dalam alur ReAct (Thought-Action-Observation <= 5 langkah) dengan alat mikro `crop_roi`, `enhance_patch`, dan `finalize_verdict`.
5. **Fase 5: Evaluation**: Perhitungan Akurasi, Precision, Recall, Macro/Micro F1, CER, WER, latensi inferensi (ms), alokasi memori VRAM (MB), serta uji signifikansi komparatif non-parametrik McNemar dengan koreksi kontinuitas Edwards pada alpha = 0.05 pada data uji independen.
6. **Fase 6: Deployment**: Pelaporan data terstruktur JSON (`verification_verdict.json`, `agent_trajectory.json`) dan dasbor interaktif Streamlit side-by-side dengan fitur *Catalog Auto-Remediation* dan label penafian regulasi *BPOM Guard*.

---
## C (Constraints & Architectural Invariants)

1. **Larangan Pre-Filtering OCR pada Prapemrosesan Data (Anti-Selection Bias Invariant)**:
   DILARANG KERAS melakukan pra-penyaringan dataset menggunakan OCR (seperti PaddleOCR/RapidOCR) untuk membuang citra yang atributnya tidak terbaca sebelum pemodelan dimulai. Pada riset komparasi model visi-bahasa terhadap agen AI, dataset harus memuat data katalog riil apa adanya (termasuk kemasan tanpa teks netto atau teks non-tampak). Kemampuan model membedakan status `MATCH`, `MISMATCH`, atau secara jujur mengeluarkan `UNVERIFIED` adalah esensi utama pengujian. Menyaring dataset dengan mesin OCR kandidat menimbulkan bias seleksi (*selection bias*) dan sirkularitas data yang merusak validitas ilmiah.
2. **Urutan Eksekusi Transformasi Citra (CIE LAB CLAHE Sebelum Letterbox Padding)**:
   Filter peningkatan kontras CIE LAB CLAHE pada kanal $L^*$ WAJIB diaplikasikan pada citra asli produk SEBELUM dilakukan letterbox padding ke kanvas 640x640 latar putih. Jika letterbox diaplikasikan lebih dulu, area padding putih (255, 255, 255) yang luas di tepi kanvas akan mendominasi dan merusak distribusi histogram ubin lokal ($8 \times 8$) CLAHE, memicu artefak garis dan distorsi kontras di perbatasan produk.
3. **Tata Kelola Data Bebas Bocor (Anti-Data Leakage Split)**:
   Raw data pada `dataset/raw/` dan `dataset/processed/sociolla_master_5490_complete.csv` bersifat *read-only*. Pembagian dataset wajib menggunakan *stratified group split by brand* (70:15:15) pada 5.358 entri bersih. Seluruh SKU dari merek yang sama terkunci mutlak dalam satu subset partisi saja (Train: 3.750, Val: 804, Test: 804).
4. **Penyaringan Citra Resolusi Rendah**:
   Citra beresolusi di bawah 640x640 piksel (132 sampel: 56 Skincare, 76 Makeup) wajib dikeluarkan ke `logs/master_4806_preprocessing_errors.log` dan dilarang masuk ke subset evaluasi benchmark.
5. **Standarisasi Spasial Bounding Box**:
   Koordinat kotak pembatas wajib dinormalisasi ke rentang `[0.0, 1.0]` terhadap dimensi kanvas 640x640. Penggabungan teks OCR fisik ke area bounding box atribut YOLOv11 mensyaratkan nilai Intersection over Area:
   $$	ext{IoA} = \frac{	ext{Area}(B_{	ext{ocr}} \cap B_{	ext{yolo}})}{	ext{Area}(B_{	ext{ocr}})} \ge 0.50$$
6. **Kaidah Pencocokan Discrepancy Gate & Prioritas Parser Netto**:
   - Merek cocok jika *Normalized Levenshtein Similarity* >= 0.85.
   - Tipe produk cocok jika *Normalized Levenshtein Similarity* >= 0.85.
   - Netto cocok jika nilai angka dan satuan metrik baku terstandarisasi cocok persis (*exact match*). Urutan evaluasi regex netto wajib mendahulukan pola *multi-pack* ($N 	imes V$), bundel aditif ($V_1 + V_2$), dan satuan metrik baku sebelum fallback ke satuan imperial (`fl. oz.`), sehingga string dwi-satuan seperti `"100 ml / 3.38 fl. oz."` terkunci secara deterministik pada angka metrik tanpa selisih pembulatan konversi.
   - Status akhir: `MATCH` (seluruh atribut cocok), `MISMATCH` (salah satu atribut bertentangan), atau `UNVERIFIED` (teks tidak terdeteksi atau keyakinan OCR < 0.50).
7. **Batasan Pengaman Loop Agentic (ReAct Guards)**:
   - Maksimal 5 siklus penalaran per sampel.
   - Timeout maksimal 30.0 detik per sampel.
   - Memori konteks membatasi riwayat ke 2 observasi alat terakhir (`last_k=2`) guna mencegah context drift dan ledakan token.
   - Setiap sampel wajib mencatat jejak penalaran ke `outputs/agent_traces/{product_id}_trajectory.json`.
8. **Validitas Uji Statistik McNemar**:
   Uji McNemar wajib menggunakan koreksi kontinuitas Edwards pada tabel kontingensi 2x2 data uji berpasangan 804 produk. Jika sel diskordan ($n_{01} + n_{10} < 25$), sistem wajib otomatis fallback ke uji binomial eksak dua sisi.
9. **Preservasi Resolusi Asli untuk Teks Mikro**:
   Pemotongan RoI untuk pembacaan karakter kecil (< 8 piksel seperti netto) pada modul OCR wajib dipetakan balik (*inverse affine mapping*) ke koordinat citra resolusi asli (*native resolution*), bukan dipotong dari kanvas letterbox 640x640 yang telah mengalami kompresi.
10. **Keseimbangan Distribusi Subkategori pada Group Split**:
    Pembagian partisi kelompok merek wajib menggunakan *StratifiedGroupKFold* atau pembobotan defisit komposit (defisit global + defisit kategori) untuk menjaga keseimbangan distribusi subkategori kosmetik lintas partisi (deviasi <= 5%) sembari mempertahankan zero brand leakage.
11. **Proteksi Latar Putih Studio pada Inpainting Kilap Spekular**:
    Deteksi masker kilap spekular HLS ($L \ge 240, S \le 40$) hanya boleh memicu *inpainting* Navier-Stokes apabila piksel kilap bersifat lokal ($0 < \text{nonzero} \le 35\%$ luas citra), sehingga latar putih studio murni dan kanvas uji putih seragam pada *property-based testing* tidak ikut terdistorsi.

---
## Linked References
Modul ini didukung oleh 6 dokumen referensi teknis mendalam:
- `references/florence2-paddleocr-pipeline.md` (Spesifikasi & blueprint implementasi Python siap pakai Florence-2 + PaddleOCR)
- `references/journal-sota-synthesis.md` (Sintesis 42 jurnal: 35 internasional + 7 nasional termasuk BMHCA Gunadarma)
- `references/codebase-architecture.md` (Pemetaan 21 repositori kode referensi lokal ke tasks skripsi)
- `references/verification-pipelines.md` (Spesifikasi teknis pipeline Florence-2 + PaddleOCR dan Qwen2-VL ReAct)
- `references/evaluation-mcnemar.md` (Formulasi matematis metrik evaluasi CER/WER dan uji signifikansi McNemar)
- `references/data-preprocessing-enhancements.md` (Jurnal rujukan & kode peningkatan Data Preparation: Specular Glare Suppression, Micro-Text Unsharp Masking, Multi-Pack Netto Parser, dan StratifiedGroupKFold)

---
## O (Output Format & Operational Deliverables)

1. **Kode & Notebook Kerja**:
   - `notebooks/01_eda/01_eda_sociolla_catalog.ipynb` (Fase 1 EDA)
   - `notebooks/02_preprocessing/02_data_preprocessing_and_splitting.ipynb` (Fase 2 Prapemrosesan)
   - `notebooks/03_yolo_ocr/03_conventional_yolov11_paddleocr.ipynb` (Fase 3 Konvensional)
   - `notebooks/04_qwen_vl/04_agentic_qwen2_vl_react.ipynb` (Fase 4 Agentic MLLM)
   - `notebooks/05_benchmark/05_comparative_benchmark_and_mcnemar.ipynb` (Fase 5 Evaluasi)
   - `notebooks/06_demo/app.py` (Fase 6 Dasbor Streamlit)
2. **Kontrak Data JSON Terstruktur**:
   - Hasil putusan verifikasi per produk: `verification_verdict.json`
   - Jejak penalaran agentic per produk: `outputs/agent_traces/{product_id}_trajectory.json`
   - Hasil rekapitulasi benchmark dan uji McNemar: `outputs/tables/benchmark_results.csv` dan `outputs/tables/mcnemar_results.json`
3. **Definisi Selesai (DoD)**:
   - Bebas dari karakter Unicode em-dash atau en-dash.
   - Lolos validasi linter `python skills/specialist-skill-architect/scripts/validate_skill.py <path> --strict`.
   - Seluruh artefak kode dapat dieksekusi secara mulus pada lingkungan Kaggle/Colab GPU maupun stasiun kerja lokal.
