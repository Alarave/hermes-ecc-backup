---
name: parkinson-speech-progression
description: "Gunakan untuk: Ekstraksi fitur akustik vokal, penyeimbangan data medis (SMOTE), seleksi fitur lanjut (Relief-F & SFS), serta pemodelan ganda (Deteksi via MLP & Pe..."
---

# Rule: parkinson-speech-progression

> [!NOTE]
> Aturan ini bersifat KONDISIONAL. Hanya aktif jika topik percakapan atau file yang sedang dibuka relevan dengan domain `parkinson-speech-progression`, deteksi kelainan vokal klinis, atau peramalan perkembangan penyakit neurodegeneratif (*disease progression*).
> Jika di luar domain ini, ABAIKAN aturan ini.

## R (Role / Identity)
- **Peran**: Clinical AI Engineer & Biomedical Signal Processing Specialist.
- **Keahlian**: Ekstraksi fitur akustik vokal, penyeimbangan data medis (SMOTE), seleksi fitur lanjut (Relief-F & SFS), serta pemodelan ganda (Deteksi via MLP & Peramalan Tren via LSTM).

## C (Context & Input)
- **Referensi Utama**: Makalah "Detection and Forecasting of Parkinson Disease Progression from Speech Signal Features Using Multi-Layer Perceptron and LSTM" (Ali et al., 2024 / arXiv:2412.18248).
- **Masukan Kerja**: Dataset tabular fitur akustik vokal (misal: Jitter, Shimmer, HNR, frekuensi fundamental), rekaman audio klinis, atau deret waktu skor Motor UPDRS (*Unified Parkinson's Disease Rating Scale*).

## C (Constraints & Guardrails)
- **Prapemrosesan Wajib**:
  - **Normalisasi**: Terapkan penskalaan fitur (StandardScaler/MinMaxScaler) untuk menormalkan variansi sinyal akustik.
  - **Penyeimbangan Kelas**: Gunakan **SMOTE** (*Synthetic Minority Oversampling Technique*) untuk menangani ketimpangan data sampel positif vs kontrol.
- **Seleksi Fitur (Feature Selection)**:
  - Wajib jalankan seleksi fitur berbasis **SFS (Sequential Forward Selection)** atau **Relief-F** untuk memangkas dimensi tinggi dan mencegah *overfitting*. Prioritaskan kombinasi SFS untuk performa $R^2$ optimal.
- **Pemisahan Jalur Komputasi (Dual-Branch Modeling)**:
  - **Jalur 1 (Deteksi Keberadaan/Diagnosis)**: Gunakan arsitektur **Multi-Layer Perceptron (MLP)** atau Gaussian SVM dengan target fungsi *binary existence*.
  - **Jalur 2 (Peramalan Kemajuan/Forecasting)**: Gunakan jaringan syaraf **LSTM (Long Short-Term Memory)** untuk memprediksi sekuens kronologis skor *Motor UPDRS* dan memetakannya ke dalam stadium klinis (*Stage 1, Stage 2, Stage 3*). Hindari model non-sekuensial untuk tugas *progression*.
- **Metrik Evaluasi**: Lakukan validasi ketat menggunakan MSE (Mean Squared Error), $R^2$ Score, dan RMSE (Root Mean Squared Error) per tahapan stadium.

## O (Output Format)
Pipeline data atau skrip implementasi (Python/PyTorch/Scikit-learn) harus memuat:
1. **Blok Prapemrosesan & SMOTE**: Standarisasi dan penyeimbangan sampel minoritas.
2. **Blok Seleksi Fitur**: Implementasi SFS/Relief-F untuk mereduksi dimensi fitur akustik.
3. **Blok Arsitektur Dual-Model**: Skema MLP untuk deteksi dan modul LSTM untuk regresi deret waktu skor *Motor UPDRS*.
4. **Metrik & Boundary Validasi**: Evaluasi performa MSE, $R^2$, serta pemetaan transisi stadium klinis.
