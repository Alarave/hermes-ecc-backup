# Pemodelan Pembelajaran Mesin & Rekayasa Fitur (ml-predictive-modeling)

Panduan teknis algoritma supervised/unsupervised machine learning, rekayasa fitur, optimasi hyperparameter, dan interpretasi model.

## 1. Rekayasa Fitur (Feature Engineering)
- **Transformasi & Imputasi**:
  - Lakukan pemisahan train-test split sebelum imputasi nilai hilang atau scaling (StandardScaler/RobustScaler) untuk mencegah kebocoran data (data leakage).
  - Gunakan Target Encoding dengan K-Fold out-of-fold regularization untuk variabel kategorikal berkardinalitas tinggi guna mencegah overfitting.
- **Seleksi Fitur Terarah**:
  - Hapus fitur berkorelasi tinggi (Spearman/Pearson correlation > 0.85) menggunakan Variance Inflation Factor (VIF).
  - Terapkan seleksi berbasis pentingnya fitur (Recursive Feature Elimination / Mutual Information Gain).

## 2. Supervised Learning & Ensemble Methods
- **Algoritma Gradient Boosting**:
  - XGBoost, LightGBM, CatBoost: Pilih LightGBM untuk dataset tabular besar (histogram-based binning), CatBoost untuk data dengan banyak fitur kategorikal teks.
  - Parameter kunci: learning_rate (0.01 - 0.1), max_depth / num_leaves, subsample, colsample_bytree, reg_alpha (L1), reg_lambda (L2).
- **Penanganan Kelas Tidak Seimbang (Class Imbalance)**:
  - Evaluasi metrik PR-AUC (Precision-Recall AUC) dan F1-Score Makro, bukan Akurasi standar.
  - Gunakan pembobotan kelas (scale_pos_weight / class_weight='balanced') atau teknik resampling (SMOTE / Tomek links) eksklusif pada data latih.

## 3. Optimasi Hyperparameter (Optuna)
- Gunakan Tree-structured Parzen Estimator (TPE) pada Optuna dengan strategi early stopping (MedianPruner).
- Validasi silang bertingkat (Stratified K-Fold / GroupKFold) 5-fold untuk memastikan stabilitas parameter terhadap partisi acak.

## 4. Evaluasi & Diagnostik Model
- **Metrik Klasifikasi**: Confusion matrix, ROC-AUC, Brier score (kalibrasi probabilitas), Expected Calibration Error (ECE).
- **Metrik Regresi**: MAE (robust outlier), RMSE, MAPE, R-squared terdistribusi.
- **Interpretasi Model (Explainable AI)**:
  - Hitung SHAP (SHapley Additive exPlanations) TreeExplainer untuk atribusi kontribusi fitur global dan lokal.
  - Tampilkan partial dependence plots (PDP) untuk menganalisis hubungan non-linear antara fitur kunci dan target prediksi.
