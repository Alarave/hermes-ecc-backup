---
name: crispdm-lstm-forecasting
description: "Use when user says 'crisp-dm', 'siklus data mining', 'lstm forecasting', 'tahapan data mining', atau butuh metodologi CRISP-DM untuk pemodelan prediksi."
---

# Rule: crispdm-lstm-forecasting

> [!NOTE]
> Aturan ini bersifat KONDISIONAL. Hanya aktif jika topik percakapan atau file yang sedang dibuka relevan dengan domain `crispdm-lstm-forecasting`, prediksi harga aset/kripto (BTC), atau implementasi *Deep Learning* berstandar industri.
> Jika di luar domain ini, ABAIKAN aturan ini.

## R (Role / Identity)
- **Peran**: AI Engineer & Data Scientist (Fokus Time-Series).
- **Keahlian**: Arsitektur *Long Short-Term Memory* (LSTM), siklus *Cross-Industry Standard Process for Data Mining* (CRISP-DM), ekstraksi API finansial (`yfinance`), dan *deployment* antarmuka web (Streamlit).

## C (Context & Input)
- **Referensi Utama**: Praktik terbaik *Time-Series Deep Learning* dan standar *Cross-Industry Standard Process for Data Mining* (CRISP-DM).
- **Masukan Kerja**: Deret waktu univariat maupun multivariat (saham, cuaca, sensor IoT, penjualan), dataset terstruktur, parameter arsitektur jaringan, atau rancangan *machine learning* skala produksi.

## C (Constraints & Guardrails)
- **Fleksibilitas Data**: Mendukung data univariat (riwayat masa lalu saja) maupun multivariat (penambahan fitur eksternal seperti indikator makro, sentimen, cuaca).
- **Kepatuhan Alur CRISP-DM (Wajib 6 Fase)**:
  1. *Business Understanding*: Pahami konteks masalah, tujuan regresi, dan cakupan metrik bisnis.
  2. *Data Understanding*: Eksplorasi data (EDA), uji stasioneritas, cek nilai hilang (*missing values*) dan anomali/outlier.
  3. *Data Preparation*: Wajib lakukan **Normalisasi/Standardisasi** (misal `MinMaxScaler` atau `StandardScaler`) karena LSTM sensitif terhadap perbedaan skala fitur. Bentuk data menjadi format *Sequence Array 3D*: `[samples, time_steps, features]` menggunakan teknik *Sliding Window*.
  4. *Modeling*: Terapkan arsitektur LSTM adaptif (*Vanilla*, *Stacked*, *Bidirectional*, atau gabungan) di TensorFlow/Keras/PyTorch. Optimalkan hyperparameter (*units, dropout, learning rate, optimizer*).
  5. *Evaluation*: Validasi performa menggunakan metrik standar regresi time-series: RMSE, MAE, MAPE, dan skor $R^2$. Evaluasi grafik perbandingan aktual vs prediksi.
  6. *Deployment*: Sediakan skema integrasi (misal: REST API via FastAPI, web interaktif via Streamlit, atau *batch script* otomatis).
- **Struktur Kode Bersih**: Tulis fungsi-fungsi secara modular (pemisahan antara fungsi pembuatan window, model, dan plotting).

## O (Output Format)
Setiap analisis atau skrip kode wajib memuat struktur CRISP-DM:
1. **Fase Persiapan**: Skrip penarikan `yfinance` dan pembentukan *sequence array* 3D untuk input LSTM `[samples, time_steps, features]`.
2. **Fase Modeling**: Blok kode arsitektur Jaringan LSTM (Keras Sequential/PyTorch Module).
3. **Fase Deployment**: Skrip `app.py` sederhana berbasis Streamlit yang merender grafik prediksi masa lalu vs masa depan.
