# EDA (Exploratory Data Analysis) Data & AI Agentic Workflow

Diadaptasi dari ekstraksi dan analisis 1.000 repositori EDA teratas di GitHub, dioptimalkan untuk pedoman `spesialis-data-ai-agentic`.

---

## 1. Posisi EDA dalam Agentic & ML Pipeline
Berdasarkan data 1.000 repo GitHub, EDA bukanlah laporan statis belaka, melainkan **gerbang wajib** sebelum data masuk ke algoritma klasifikasi (seperti *Sentiment Analysis* EV) atau sebelum diumpankan sebagai *knowledge base* ke agen LLM (RAG).

## 2. Arsitektur Stack (The Industry Standard)
- **Environment:** Jupyter Notebook (`.ipynb`). (Menguasai 65% pangsa pasar).
- **Core Library:** Python, Pandas, Numpy, Matplotlib, Seaborn.
- **Reporting/Dashboard:** Streamlit (Mulai menggeser laporan HTML statis).
- **Deprecations:** Hindari R dan MATLAB kecuali untuk riset akademis murni non-produksi.

## 3. Protokol Sel Atomik (Gunadarma / Kompetisi Standar)
Setiap skrip atau sel di dalam Notebook harus mengikuti aturan ketat **Satu Sel = Satu Tugas**:
1. **Sel 1: Setup & Import** $\rightarrow$ Semua import `pandas`, `seaborn`, dll ada di sini.
2. **Sel 2: Load & Robustness Check** $\rightarrow$ `df = pd.read_csv(...)` diikuti `df.shape`, `df.dtypes`.
3. **Sel 3: Missing Value & Duplicate Check** $\rightarrow$ Menampilkan null count dan persentasenya.
4. **Sel 4: Univariate Analysis** $\rightarrow$ Menampilkan statistik deskriptif (`df.describe()`).
5. **Sel 5: Plotting/Visualisasi** $\rightarrow$ HANYA berisi *code* untuk *plot chart* bivariat/korelasi, terpisah dari logika pembersihan data.

## 4. Analisis Kesehatan Data (Data Robustness)
- Selalu salin dataset (`df_copy = df.copy()`) sebelum membuang kolom/baris.
- Jika missing value $<5\%$, lakukan *imputation* (mean/median/modus) atau *drop*. Jika $>50\%$, pertimbangkan untuk menjatuhkan kolom tersebut karena akan menyesatkan agen AI/ML.
- Gunakan aturan kuartil (IQR) atau Z-Score untuk mendeteksi data pencilan (outlier).

## 5. Output Akhir: Feature Selection
Setelah grafik dan korelasi selesai dibuat, EDA harus menghasilkan *Feature Recommendation* untuk tahap *Modeling*:
- **Drop Candidates:** Variabel dengan kolinearitas tinggi ($|r| > 0.85$) yang redundant.
- **Key Predictors:** Variabel yang memiliki korelasi kuat dengan target kelas (misal: label sentimen positif/negatif).
- **Agentic Context:** Kolom mana yang harus diubah menjadi teks metadata untuk vektor pencarian jika menggunakan AI.
