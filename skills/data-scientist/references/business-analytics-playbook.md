# Buku Panduan Analisis Bisnis & MLOps Produksi (business-analytics-playbook)

Panduan penerjemahan metrik machine learning ke dampak bisnis riil, analisis siklus hidup pelanggan, dan operasionalisasi model produksi.

## 1. Analisis Siklus Hidup Pelanggan (Customer Analytics)
- **Prediksi Customer Churn**:
  - Definisikan horizon observasi (observation window) dan horizon prediksi (prediction window) secara tegas.
  - Analisis kurva biaya kesalahan (Cost Matrix): Biaya False Negative (kehilangan pelanggan) vs Biaya False Positive (biaya insentif retensi terbuang).
  - Tentukan ambang batas probabilitas klasifikasi (decision threshold) berbasis maksimalisasi Expected Financial Value, bukan default 0.50.
- **Customer Lifetime Value (CLV)**:
  - Terapkan model probabilistik Buy 'Til You Die (BTYD: BG/NBD untuk frekuensi transaksi, Gamma-Gamma untuk nilai moneter).
- **Segmentasi Pelanggan**:
  - Klasterisasi RFM (Recency, Frequency, Monetary) dipadukan dengan algoritma K-Means terstandarisasi Silhouette Score > 0.50.

## 2. Analisis Pemasaran & Operasional
- **Marketing Mix Modeling (MMM)**:
  - Memodelkan efek carryover (adstock decay) dan diminishing returns (Hill function) pada kanal periklanan digital dan tradisional.
- **Optimasi Stok & Peramalan Permintaan**:
  - Hitung Safety Stock = Z_alpha * sqrt(Lead_Time * Var_Demand + Demand_Avg^2 * Var_Lead_Time).
  - Penyetelan titik pemesanan ulang (Reorder Point) berbasis target Service Level (95% atau 99%).

## 3. MLOps & Penerapan Produksi
- **Pelacakan Eksperimen & Registri Model**:
  - Gunakan MLflow untuk mencatat parameter, metrik, artefak grafik, dan versi bobot model.
- **Penyajian API & Inferensi**:
  - Kemas model ke dalam microservice FastAPI dengan validasi skema input Pydantic dan kontainer Docker.
- **Pemantauan Drift (Model Monitoring)**:
  - Pantau Data Drift (perubahan distribusi fitur via uji Kolmogorov-Smirnov atau Population Stability Index / PSI > 0.25).
  - Pantau Concept Drift (penurunan metrik kinerja model terhadap ground truth berkala) dan picu retraining otomatis.
