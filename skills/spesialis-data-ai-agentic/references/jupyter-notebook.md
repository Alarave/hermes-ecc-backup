# Jupyter Notebook Best Practices for Data Science & AI

Panduan standar pembuatan, scaffolding, dan pemeliharaan file `.ipynb` yang reproduktif dan bersih untuk eksperimen data dan machine learning.

## 1. Scaffolding Cepat via Helper CLI
Gunakan CLI bawaan dari skill `jupyter-notebook`:
```bash
python ~/.gemini/antigravity/skills/jupyter-notebook/scripts/new_notebook.py \
  --kind experiment \
  --title "Judul Eksperimen" \
  --out "output/notebook.ipynb"
```

Opsi mode:
- `--kind experiment`: Eksplorasi data, komparasi model, pengujian hipotesis, dan validasi metrik.
- `--kind tutorial`: Langkah bertahap berorientasi pengajaran atau panduan implementasi.

## 2. Struktur Standar Urutan Cell
1. **Title & Objective (Markdown)**:
   - Judul, rumusan masalah, metrik target, batasan data.
2. **Environment & Seed Setup (Code)**:
   - Import library esensial (`numpy`, `pandas`/`polars`, `torch`/`sklearn`, `matplotlib`/`seaborn`).
   - Penetapan random seed deterministik (`torch.manual_seed(42)`, `np.random.seed(42)`).
3. **Data Ingestion & Sanitasi (Code)**:
   - Muat dataset (utamakan Parquet/Arrow).
   - Sanitasi data & auto-masking PII sebelum profiling.
4. **Exploratory Data Analysis / EDA (Code & Markdown)**:
   - Visualisasi distribusi, deteksi outlier, korelasi fitur.
5. **Preprocessing & Feature Engineering (Code)**:
   - Data cleaning, scaling, encoding, pipeline transformasi.
6. **Model Baseline & Candidate Training (Code)**:
   - Train/Val/Test split (e.g. 70/15/15 stratified).
   - Baseline model -> Model kandidat utama -> Hyperparameter tuning.
7. **Evaluasi & Error Analysis (Code & Markdown)**:
   - Metrik komprehensif (F1-score, AUC-ROC, PR-AUC, Confusion Matrix, SHAP).
   - Analisis False Positive & False Negative.
8. **Summary & Export (Markdown & Code)**:
   - Simpan model final (`.joblib` / `.pt` / `.onnx`).
   - Ekstrak artefak ke laporan (sinkronkan ke format laporan 20 bab `create-readme`).

## 3. Aturan Higiene & Keamanan
- **Dilarang Menyimpan Secret**: API key, token database, atau private key dilarang ada di sel kode maupun output metadata notebook.
- **Bersihkan Output Berat**: Hapus gambar beresolusi raksasa atau dump ratusan ribu baris log sebelum commit Git.
- **State Determinism**: Pastikan notebook dapat dieksekusi dari awal sampai akhir via *Restart Kernel and Run All Cells* tanpa error NameError atau Out-of-Order Execution.
