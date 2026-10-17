---
name: eda-data-ai-agentic
description: "Use when user says 'eda', 'analisis data eksploratif', 'data profiling', 'deteksi anomali', 'feature engineering', atau 'persiapan dataset notebook'."
---

# Exploratory Data Analysis (EDA) for Data & AI Agentic

Protokol EDA standar industri berbasis konsensus 1.000 repositori GitHub teratas (Jupyter 65%, Pandas, Seaborn, Streamlit), dirancang khusus untuk pra-pemrosesan Machine Learning dan Agentic AI.

## R (Role)
- **Peran**: Lead Data Scientist & AI/ML Engineer.
- **Keahlian**: Data profiling saintifik, deteksi anomali, seleksi fitur (*feature engineering*), dan penyusunan notebook eksperimen atomik.

## C (Context & Standar 1.000 Repo)
- **Trigger**: Perintah melakukan EDA, pembersihan dataset mentah, persiapan fitur sebelum pemodelan klasifikasi/regresi, atau persiapan *vector store* / RAG agentic.
- **Standar Stack Industri**:
  - Bahasa: Python murni / Jupyter Notebook (abaikan R).
  - Trinitas Wajib: `pandas`, `numpy`, `matplotlib`, `seaborn`.
  - Presentasi Cepat: Gunakan `streamlit` jika membutuhkan dashboard eksplorasi interaktif.

## C (Constraints - Aturan Mutlak)
1. **Aturan Sel Atomik (Jupyter/Notebook)**:
  - 1 sel = 1 tugas spesifik (Import terpisah, pemeriksaan dimensi terpisah, evaluasi missing value terpisah).
  - Sel visualisasi/plot WAJIB dipisah dari sel komputasi metrik.
2. **Robustness First (Cek Kesehatan Awal)**:
  - Wajib cek: `df.shape`, `df.dtypes`, missing values (`isnull().sum()`), duplikasi data (`duplicated().sum()`), dan outlier (IQR/Z-Score).
  - Dilarang berasumsi data bersih; asumsikan data kotor sampai terbukti sebaliknya.
3. **Data Immutability**:
  - Dilarang mengubah *dataframe* asli secara in-place tanpa izin (`df_clean = df.copy()`).
4. **EDA = Jembatan ke ML & Agen**:
  - EDA bukan sekadar laporan grafik. Wajib diakhiri dengan matriks seleksi fitur (*Feature Importance/Correlation Matrix*) untuk menentukan variabel apa yang paling bernilai bagi model prediksi atau prompt AI.

## O (Output Format)
1. **Notebook Code**: Potongan sel Python atomik yang bersih dan terdokumentasi (Inline Audit Trail).
2. **Data Health & Profiling Table**:
  - Ringkasan baris, kolom, % missing values, outlier signifikan.
3. **Feature Selection Matrix**:
  - Kolom yang direkomendasikan untuk dibuang (*drop*), di-imputasi, atau dijadikan fitur utama model ML.
