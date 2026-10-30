# OPERATIONAL REFERENCE: MLOPS & PIPELINE ORCHESTRATION ENGINE
> Panduan teknis operasional Pram untuk orkestrasi siklus hidup machine learning, alokasi komputasi, dan evaluasi berbasis bukti.

---

## 1. MLOps Lifecycle DAG Architecture

Pram mengatur pipeline pembelajaran mesin melalui siklus hidup Directed Acyclic Graph (DAG) bertahap:

```text
Data Ingestion 
      │
      ▼
[Gate 1: Schema & Anomaly Validation] ──(FAIL)──► Quarantine / DLQ
      │ (PASS)
      ▼
Preprocessing & Feature Engineering
      │
      ▼
[Gate 2: Anti-Leakage Split & Scaling] 
      │ (PASS)
      ▼
Model Training (Seed & Resource Pinned)
      │
      ▼
[Gate 3: Evaluation & Metric Threshold] ──(FAIL)──► Reject / Retune
      │ (PASS)
      ▼
Model Registry (Artefak & Lineage Locked)
      │
      ▼
Deployment (Shadow / Canary Rollout)
      │
      ▼
Observability & Drift Monitoring ──(DRIFT DETECTED)──► Trigger Review / Retrain
```

---

## 2. Definisi Tahapan & Quality Gates Pipeline

### Tahap 1: Data Ingestion & Schema Validation (Gate 1)
- **Input**: Sumber data mentah (PostgreSQL, ClickHouse, Parquet Lakehouse, S3/GCS, CSV/JSON scraper).
- **Tata Kelola Direktori Dataset Bersih (Clean Dataset Discipline)**:
  - Direktori `raw/` wajib fokus 100% pada data mentah sebelum pembersihan (hanya 1 berkas sumber terpusat, read-only/immutable). Dilarang menempatkan berkas hasil pembersihan (seperti `*-clean.csv`) di dalam `raw/`.
  - Berkas historis, subset coba-coba, atau varian eksperimen wajib diisolasi ke `archive/` disertai `README.md` penjelas agar tidak mengotori alur pipeline utama.
  - Setiap perubahan lokasi dataset wajib diverifikasi terhadap pengujian regresi (`pytest tests/`) untuk menjamin tidak ada alur yang terputus.
- **Quality Gate 1 (Pandera / Great Expectations)**:
  - Validasi tipe kolom, rentang nilai (min/max), dan ambang batas nilai kosong (*missing values* <= 5%).
  - Anomali format langsung dikarantina ke *Dead Letter Queue (DLQ)*. Dilarang meneruskan data kotor ke training.
- **Output Terverifikasi**: Dataset terverifikasi dalam format biner kolom efisien (**Apache Arrow / Parquet**) atau CSV terstandardisasi pada `processed/`.

### Tahap 1B: Multimodal Visual Curation & Metadata Parity Protocol
- **Model-Agnostic Preprocessing Invariant (Anti-Selection-Bias)**: Dalam riset komparasi visi-bahasa atau OCR (misalnya Florence-2 + PaddleOCR vs Agentic MLLM Qwen2-VL), tahap prapemrosesan (Task 02) DILARANG menggunakan OCR atau model yang berkerabat dengan model yang diuji untuk memfilter/menyeleksi sampel kemasan. Hal ini menimbulkan bias seleksi (selection bias) dan sirkularitas data yang merusak validitas ilmiah. Prapemrosesan wajib murni agnostik (filter resolusi >= 640px, kanonisasi teks katalog, letterbox, CLAHE, dan split anti-leakage). Tugas mengidentifikasi keberadaan atribut fisik kemasan adalah tugas murni dari model yang diuji (menguji apakah model mampu mendeteksi MATCH, MISMATCH, atau UNVERIFIED secara objektif tanpa berhalusinasi).
- **Zero Data Loss via Quarantine Move**: Saat memfilter dataset multimodal berdasarkan kriteria teknis citra, DILARANG melakukan penghapusan fisik permanen (`os.remove` / `rm`). Pindahkan berkas citra yang tereksklusi ke direktori karantina (`dataset/archive/excluded_images/`) dan terbitkan audit log lengkap (`logs/visual_filtering_audit.csv`) yang mencatat alasan kegagalan per sampel.
- **Strict 1:1 Image-to-Metadata Parity**: Setiap eliminasi citra wajib memperbarui data tabular master secara atomik untuk mencegah *dangling references* (citra tanpa metadata atau metadata tanpa citra fisik).
- **Post-Filter Split Recomputation**: Setiap perubahan kardinalitas dataset membatalkan partisi data latih dan uji sebelumnya. Wajib melakukan komputasi ulang partisi (*Stratified Group Split by Brand* 70:15:15) agar pembagian data tetap bebas bocor (*anti-data leakage*).
- **Two-Tier Multimodal Evaluation Architecture**:
  * *Tier-1 (Core Benchmark)*: Dievaluasi pada subset kemasan yang terverifikasi memuat atribut lengkap (merek, netto, tipe produk, nama produk) guna menguji kemampuan murni model dalam pelokalan spasial, pembacaan OCR (CER/WER), dan penalaran atribut tanpa bias ketiadaan data fisik.
  * *Tier-2 (Robustness & Anti-Hallucination Audit)*: Menguji sampel kemasan yang dikarantina (noise visual) secara terpisah untuk memvalidasi ketahanan model dalam menolak klaim (`UNVERIFIED`) tanpa berhalusinasi (*zero false positive hallucination*).

### Tahap 2: Preprocessing & Anti-Leakage Guard (Gate 2)
- **Aturan Mutlak Anti-Leakage**:
  - Untuk data time-series: Pemisahan data latih dan uji (*Train/Test Split*) WAJIB dilakukan sebelum operasi apapun.
  - Normalisasi (*MinMaxScaler / StandardScaler*) dan dekomposisi sinyal (seperti CEEMDAN/Wavelet) hanya boleh di-*fit* pada data *Train*, lalu di-*transform* ke data *Test*.
- **Output Terverifikasi**: Matriks fitur terisolasi dengan hash SHA-256 tercatat.

### Tahap 3: Resource-Aware Training Execution
- **Alokasi Hardware**:
  - *CPU Baseline*: Utamakan validasi skrip dan pengujian baseline cepat pada CPU lokal.
  - *GPU Acceleration*: Alokasikan GPU (CUDA/MPS) dengan ukuran batch (*batch size*) terkontrol untuk mencegah *Out-of-Memory (OOM)*.
- **Reproducibility Locking**:
  - Wajib mengunci *random seed* di level Python runtime, NumPy, dan framework DL (PyTorch/TensorFlow).
  - Catat alokasi VRAM, estimasi TFLOPS, dan durasi komputasi per epoch.

### Tahap 4: Evaluation Threshold Gate (Gate 3)
- **Evaluasi Multivariat**:
  - Dilarang hanya melaporkan akurasi atau loss tunggal.
  - Regresi / Time-Series: Wajib menyajikan RMSE, MAE, MAPE, $R^2$, dan uji signifikansi **Diebold-Mariano** vs model Naive.
  - Klasifikasi: Wajib menyajikan Precision, Recall, F1-Score macro/micro, ROC-AUC, dan Confusion Matrix.
  - Generative AI / RAG: Wajib mengukur RAG Triad (Context Relevance, Groundedness, Answer Relevance).
- **Threshold Policy**: Jika metrik model baru tidak melampaui baseline produksi sebesar delta minimum (+2% margin signifikansi), deployment **DIBLOKIR**.

### Tahap 5: Model Registry & Artifact Lineage
- **Penyimpanan Terstruktur (MLflow / W&B / Local Bundle)**:
  - File bobot model terkompilasi (.onnx / TorchScript / .keras).
  - File scaler / preprocessor (.joblib / .pkl).
  - File konfigurasi hyperparameter (JSON/YAML).
  - Metadata lineage: Commit hash Git kode pembuat dan checksum dataset sumber (DVC).
  - *Prinsip Pragmatis*: Untuk proyek akademik, tugas akhir, atau prototipe lokal, penyimpanan bundel lokal (`models/` + `metadata.json`) sudah cukup; DILARANG memaksakan instalasi server MLflow/DVC jika infrastruktur lokal tidak memadai.

### Tahap 6: Serving & Release Strategy
- **Format Serving**: Utamakan ekspor ke **ONNX Runtime** atau **TorchScript** via FastAPI / Triton Server untuk meminimalkan latensi inferensi (<50ms P95).
- **Rollout Strategy**:
  - *Shadow Deployment*: Salurkan duplikat 100% traffic live ke model baru di background tanpa mempengaruhi respons pengguna.
  - *Canary Deployment*: Alihkan 5% traffic produksi, amati error rate dan latensi selama 24 jam sebelum migrasi 100%.

---

## 3. Observability, Drift Monitoring, & Retraining Policy

### Pemantauan Berkelanjutan (Evidently AI / Whylogs / Local Baseline Drift Script)
- **Data Drift**: Pergeseran distribusi fitur input ($P(X)$) menggunakan uji Kolmogorov-Smirnov atau Wasserstein Distance.
- **Concept Drift**: Pergeseran relasi antara input dan target aktual ($P(Y|X)$).
- **Kebijakan Retraining**: Retraining otomatis TIDAK BOLEH dipicu secara buta berdasarkan jadwal jam atau kalender. Retraining hanya diizinkan jika terdeteksi data drift signifikan yang terbukti menurunkan metrik bisnis nyata, didukung pertimbangan biaya komputasi dan persetujuan Project Owner.

---

## 4. Pemilihan Alat & Skala Sistem (Pragmatic Tool Selection)

Pram memilih tumpukan alat MLOps berdasarkan kompleksitas sistem aktual:
1. **Tingkat 1 (Eksperimen Akademik / Prototipe Lokal)**:
   - Tooling: Python native, Scikit-learn, PyTorch, Polars/DuckDB, local `.parquet`, `joblib`, dan skrip validasi mandiri.
   - Tanpa overhead server eksternal, 100% dapat direproduksi di PC lokal.
2. **Tingkat 2 (Sistem Produksi Menengah)**:
   - Tooling: FastAPI, ONNX Runtime, SQLite/PostgreSQL, Docker container mandiri, GitHub Actions CI.
3. **Tingkat 3 (Platform Enterprise / Big Data)**:
   - Tooling: Apache Airflow / Dagster, DVC, MLflow Registry, Triton Inference Server, Kubernetes cluster, Evidently AI monitoring.

---

## 5. Failure Handling & Recovery Matrix

| Jenis Kegagalan | Penyebab Utama | Prosedur Pemulihan Pram |
|---|---|---|
| **GPU Out of Memory (OOM)** | Ukuran batch terlalu besar / memory leak | Kurangi batch size 50%, aktifkan gradient accumulation, atau beralih ke mixed-precision (FP16/BF16). |
| **Data Schema Mismatch** | Perubahan upstream API / data kotor | Karantina data anomali ke DLQ, kirim notifikasi alert, gunakan checkpoint data valid terakhir. |
| **Dangling Multimodal References** | Penghapusan parsial (citra dihapus tapi CSV tertinggal atau sebaliknya) | Terapkan atomic synchronization: update master CSV bersamaan dengan perpindahan citra ke karantina, lalu verifikasi paritas 1:1. |
| **Python Toolchain Package Mismatch** | Python default shell tidak memiliki dependensi ML/OCR | Auto-detect executable Python yang memuat modul kritis (misalnya RapidOCR/PyTorch) sebelum eksekusi pipeline atau runner test suite. |
| **Model Underperforming Gate** | Hyperparameter sub-optimal / overfitting | Bounded Retry maks 3x dengan tuning regularisasi (Dropout/L2) atau kembali ke model baseline. |
| **Inference Latency Spike** | Beban concurrent tinggi / cold start | Skalakan container instance atau terapkan model quantization (INT8). |
