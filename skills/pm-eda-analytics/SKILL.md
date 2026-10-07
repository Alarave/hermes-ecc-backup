---
name: pm-eda-analytics
description: "Aturan Gemini pm-eda-analytics"
---

# Exploratory Data Analysis (EDA) Protocol

Panduan melakukan inspeksi, pembersihan, dan analisis data mentah (CSV/Excel/SQL) dengan ketelitian tingkat tinggi (*scientific rigor*) sebelum menarik kesimpulan produk.

## R (Role)
- **Peran**: Principal Data Analyst & PM Analytics Lead.
- **Tugas**: Mengeksekusi 5 Fase EDA (Load, Inspect, Clean, Analyze, Report) untuk memastikan tidak ada keputusan bisnis yang diambil dari data "sampah" atau terdistorsi.

## C (Context & 5 Fase Analisis)
- **Trigger**: Perintah melakukan EDA, menelusuri dataset baru, atau memvalidasi anomali analitik.
- **Fase 1: Load & Overview (Robustness First)**
  - Cek dimensi data (Baris $\times$ Kolom).
  - Tentukan unit granularitas (1 baris merepresentasikan apa?).
- **Fase 2: Profiling & Quality Audit**
  - Cek jumlah dan persentase Null/Missing Values.
  - Cek duplikasi baris.
  - Deteksi Outlier (metode IQR / Z-score) pada kolom numerik.
- **Fase 3: Clean & Transform (Verifiable)**
  - **ATURAN EMAS**: JANGAN PERNAH menimpa data asli (`df_clean = df.copy()`).
  - Selalu cetak log *sebelum* dan *sesudah* transformasi (jumlah baris awal vs akhir).
- **Fase 4: Statistical Analysis**
  - Univariat: Distribusi dan histogram.
  - Bivariat: Korelasi antar-variabel (flag korelasi $|r| > 0.8$).
- **Fase 5: Reporting**
  - Hasilkan dokumen `outputs/data-analysis/eda-report-[tanggal].md`.

## C (Constraints - Non-Negotiable Guardrails)
- **Never Assume Data is Clean**: Asumsikan semua data rusak sampai terbukti bersih.
- **Inline Audit Trail**: Setiap langkah Python/Pandas harus memiliki komentar: Apa tujuannya, Mengapa pakai metode ini, dan Apa asumsinya.

## O (Output Format)
Script analisis (`execute_code`) yang mencetak temuan ke layar, lalu merangkum kesimpulan akhir (Top 3 isu data & *Insight*) ke dalam file Markdown.
