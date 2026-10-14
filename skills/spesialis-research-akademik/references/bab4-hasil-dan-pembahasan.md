# STANDAR OPERASIONAL & TEMPLATE: BAB IV HASIL DAN PEMBAHASAN
> Dokumen referensi resmi penulisan Bab 4 Hasil dan Pembahasan (Standar Evaluasi Fungsional Black-Box, Metrik Kuantitatif, Uji Signifikansi Statistik, dan Diskusi Korelatif Empiris).

---

## 🏛️ PEDOMAN ARSITEKTUR BAB IV (RULES & CONSTRAINTS)

### 1. Struktur Pengujian Ganda (Dual Testing Standard)
Bab 4 wajib menyajikan dua dimensi pengujian:
1. **Pengujian Fungsional (Black-Box Testing)**:
   - Wajib menyajikan tabel pengujian fungsi sistem/antarmuka secara lengkap (Skenario Uji, Input, Output Harapan, Hasil Aktual, dan Status Kelulusan).
   - Menjamin bahwa sistem atau pipeline inferensi berjalan stabil tanpa error runtime.
2. **Pengujian Kinerja Kuantitatif**:
   - Wajib melaporkan metrik performa multivariat sesuai domain riset:
     - *Regresi / Prediksi Time-Series*: RMSE, MAE, MAPE, $R^2$, dan Directional Accuracy (MDA).
     - *Klasifikasi*: Precision, Recall, Macro-F1, Confusion Matrix, dan Area Under Curve (ROC-AUC).
     - *Generative AI / RAG*: Context Relevance, Groundedness, Answer Relevance (RAGAS).

---

### 2. Standar Uji Signifikansi Statistik (Diebold-Mariano / Wilcoxon)
- **Kewajiban Uji Signifikansi**:
  - Khusus riset komparasi model AI / Time-Series: Klaim "Model A lebih baik dari Model B" TIDAK SAH jika hanya berdasarkan selisih persentase penurunan error biasa.
  - Wajib menyertakan hasil **Uji Diebold-Mariano (DM-Test)** atau **Wilcoxon Signed-Rank Test**.
  - Catat nilai statistik uji ($DM$) dan nilai *p-value*. Jika $p < 0.05$, hipotesis nol ditolak, membuktikan keunggulan model signifikan secara saintifik (bukan faktor kebetulan).

---

### 3. Pembahasan Korelatif Empiris (Discussion of Findings)
- Dilarang hanya membacakan kembali isi tabel atau grafik dalam bentuk kalimat (*anti-redundancy*).
- Pembahasan WAJIB menjawab 3 pertanyaan kritis:
  1. *Akar Masalah Kegagalan/Keberhasilan*: Mengapa model bekerja sangat baik pada kondisi A namun mengalami kenaikan error pada kondisi B?
  2. *Ablation Study*: Sejauh mana modul optimasi/preprocessing (misal: dekomposisi atau attention) berkontribusi terhadap penurunan error total?
  3. *Korelasi Masalah Lapangan*: Bagaimana temuan angka ini mengonfirmasi atau membantah fenomena empiris yang diangkat pada Bab 1?

---

## 📝 TEMPLATE STRUKTUR BAB IV HASIL DAN PEMBAHASAN

```markdown
# 4. HASIL DAN PEMBAHASAN

## 4.1 Lingkungan Eksperimen dan Implementasi Model
Eksperimen pemodelan dieksekusi pada lingkungan komputasi terkontrol untuk menjamin reproduktibilitas:
- **Perangkat Keras**: CPU [Spesifikasi], RAM [Kapasitas] GB, GPU [Tipe / VRAM] GB.
- **Perangkat Lunak**: Sistem Operasi Windows 11 / Linux, Python 3.10+, PyTorch, Polars, Scikit-learn.
- **Kunci Reproduktibilitas**: *Random seed* dikunci pada nilai 42 di level Python, NumPy, dan PyTorch.

Dokumentasi kurva konvergensi pelatihan (*training and validation loss*) disajikan pada Gambar 4.1:

![Kurva Pelatihan Model](figures/training_loss_curve.png)  
*Gambar 4.1: Kurva Fungsi Kerugian Pelatihan dan Validasi Model*

## 4.2 Pengujian Fungsional Sistem (Black-Box Testing)
Pengujian fungsional modul inferensi dan validasi input dilakukan menggunakan metode *Black-Box Testing* dengan ringkasan pada Tabel 4.1:

**Tabel 4.1 Hasil Pengujian Fungsional Black-Box Sistem**
| ID Kasus | Deskripsi Skenario Uji | Masukan (Input) | Ekspektasi Luaran | Hasil Aktual | Kesimpulan |
|:---:|:---|:---|:---|:---|:---:|
| TC-01 | Pemuatan dataset historis | File CSV/Parquet valid | Data termuat 100% tanpa nilai hilang | Data termuat sempurna | Valid |
| TC-02 | Partisi data anti-leakage | Rasio 80:20 temporal | Data uji terisolasi dari scaler latih | Normalisasi terisolasi | Valid |
| TC-03 | Eksekusi inferensi model | Vektor lag masukan | Nilai estimasi numerik dan arah tren | Output terprediksi < 50ms | Valid |
| TC-04 | Penanganan input anomali | Data teks kosong/rusak | Error warning tertangkap secara anggun | Exception handling aktif | Valid |

## 4.3 Evaluasi Kinerja Kuantitatif Model
Kinerja model yang diusulkan dibandingkan secara *head-to-head* terhadap model pembanding (baseline) menggunakan data uji yang tidak pernah dilihat sebelumnya (*unseen test data*), seperti terangkum pada Tabel 4.2:

**Tabel 4.2 Perbandingan Metrik Kinerja Model pada Data Uji**
| Model / Arsitektur | RMSE | MAE | MAPE (%) | MDA (%) |
|:---|:---:|:---:|:---:|:---:|
| Baseline Model (Standar) | 142.50 | 110.20 | 2.45 | 54.20 |
| Model Usulan (Varian Dasar) | 98.30 | 74.15 | 1.62 | 65.80 |
| **Model Usulan Lengkap (Optimasi Hibrida)** | **62.40** | **45.10** | **1.05** | **78.50** |

Berdasarkan Tabel 4.2, integrasi modul optimasi berhasil memangkas nilai RMSE sebesar 56.2% dan meningkatkan akurasi arah tren (MDA) sebesar 24.3% dibanding model baseline.

## 4.4 Hasil Uji Signifikansi Statistik (Diebold-Mariano Test)
Untuk memastikan keunggulan model bukan merupakan akibat variasi acak (*random chance*), dilakukan pengujian statistik Diebold-Mariano dengan hasil pada Tabel 4.3:

**Tabel 4.3 Hasil Uji Signifikansi Statistik Diebold-Mariano**
| Perbandingan Model | Statistik DM | Nilai p-value | Signifikansi ($\alpha=0.05$) | Kesimpulan |
|:---|:---:|:---:|:---:|:---|
| Model Usulan vs Baseline | -4.821 | 0.000014 | Ya ($p < 0.05$) | Menolak $H_0$, Model Usulan Lebih Unggul Signifikan |
| Model Usulan vs Varian Dasar | -2.415 | 0.016200 | Ya ($p < 0.05$) | Menolak $H_0$, Modul Optimasi Berdampak Nyata |

Nilai $p < 0.05$ pada seluruh skenario membuktikan secara saintifik bahwa arsitektur yang diusulkan mengungguli baseline secara signifikan pada tingkat kepercayaan 95%.

## 4.5 Pembahasan Temuan Ilmiah (Discussion)
Berdasarkan hasil eksperimen pada Sub-bab 4.3 dan 4.4, keberhasilan model usulan didorong oleh beberapa faktor kunci:
1. **Dekomposisi Derau**: Penguraian frekuensi tinggi berhasil mengisolasi komponen derau acak, sehingga model utama hanya mempelajari tren deterministik.
2. **Ketahanan pada Volatilitas Tinggi**: Pada periode data dengan fluktuasi ekstrem, model usulan mempertahankan kesalahan prediksi di bawah 2%, sementara model baseline mengalami *lagging* parah.
3. **Konfirmasi Masalah Lapangan**: Peningkatan metrik MDA menjadi 78.5% secara langsung menjawab inefisiensi yang diangkat pada Latar Belakang Masalah Bab 1, membuktikan kelayakan implementasi praktis sistem.
```