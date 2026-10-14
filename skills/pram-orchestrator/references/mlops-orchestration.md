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
- **Input**: Sumber data mentah (PostgreSQL, ClickHouse, Parquet Lakehouse, S3/GCS).
- **Quality Gate 1 (Pandera / Great Expectations)**:
  - Validasi tipe kolom, rentang nilai (min/max), dan ambang batas nilai kosong (*missing values* <= 5%).
  - Anomali format langsung dikarantina ke *Dead Letter Queue (DLQ)*. Dilarang meneruskan data kotor ke training.
- **Output Terverifikasi**: Dataset terverifikasi dalam format biner kolom efisien (**Apache Arrow / Parquet**).

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
| **Model Underperforming Gate** | Hyperparameter sub-optimal / overfitting | Bounded Retry maks 3x dengan tuning regularisasi (Dropout/L2) atau kembali ke model baseline. |
| **Inference Latency Spike** | Beban concurrent tinggi / cold start | Skalakan container instance atau terapkan model quantization (INT8). |
