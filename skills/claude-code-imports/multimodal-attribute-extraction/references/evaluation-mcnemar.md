# Evaluasi Kinerja Komparatif & Uji Signifikansi Statistik McNemar

Dokumen ini memuat formulasi matematis metrik evaluasi kinerja dan uji signifikansi komparatif non-parametrik McNemar pada data uji berpasangan (476 sampel) sesuai `brief/design.md`.

---

## 1. Metrik Evaluasi Klasifikasi Verifikasi

Evaluasi dilakukan secara independen untuk kedua paradigma model pada subset data uji (15% atau 476 produk bersih dengan isolasi merek) dengan presisi 4 desimal (`0.0000` s.d. `1.0000`).

1. **Akurasi (Accuracy)**:
   $$\text{Akurasi} = \frac{TP + TN}{TP + TN + FP + FN}$$

2. **Presisi (Precision)**:
   $$\text{Presisi} = \frac{TP}{TP + FP}$$

3. **Recall (Sensitivitas)**:
   $$\text{Recall} = \frac{TP}{TP + FN}$$

4. **Macro F1-Score & Micro F1-Score**:
   $$\text{F1} = 2 \times \frac{\text{Presisi} \times \text{Recall}}{\text{Presisi} + \text{Recall}}$$
   - *Macro F1*: Rata-rata aritmatika tak berbobot dari F1-score tiap kelas verifikasi (`MATCH`, `MISMATCH`, `UNVERIFIED`).
   - *Micro F1*: Dihitung secara global dari agregasi total $TP, FP, FN$ lintas seluruh kelas.

---

## 2. Metrik Kualitas Ekstraksi Teks Fisik Kemasan

Mengukur ketepatan karakter alfanumerik yang dibaca dari label kemasan fisik terhadap teks ground truth:

1. **Character Error Rate (CER)**:
   $$\text{CER} = \frac{S_c + D_c + I_c}{N_c}$$
   Di mana $S_c$ adalah jumlah substitusi karakter, $D_c$ adalah delesi karakter, $I_c$ adalah insersi karakter, dan $N_c$ adalah total karakter pada string ground truth.

2. **Word Error Rate (WER)**:
   $$\text{WER} = \frac{S_w + D_w + I_w}{N_w}$$
   Di mana $S_w, D_w, I_w$ adalah operasi tingkat kata dan $N_w$ adalah total kata ground truth.

---

## 3. Metrik Efisiensi Komputasi & Profil Sumber Daya

1. **Latensi Inferensi Rata-Rata**: Diukur dalam milidetik (ms) per produk dari saat citra masukan diterima hingga keputusan akhir diterbitkan.
2. **Puncak Alokasi Memori GPU (Peak VRAM)**: Diukur dalam megabyte (MB) via `torch.cuda.max_memory_allocated()`.
   - *Target Konvensional Hibrida*: ~1.5 GB s.d. 2.0 GB VRAM.
   - *Target Agentic MLLM*: ~5.8 GB (AWQ 4-bit) s.d. ~15 GB (FP16).

---

## 4. Uji Signifikansi Statistik Non-Parametrik McNemar

### Landasan & Tabel Kontingensi 2x2
Uji McNemar (Dietterich, 1998) digunakan untuk mengevaluasi apakah perbedaan akurasi antara dua model yang diuji pada dataset berpasangan yang sama (*paired test set* 476 sampel) berbeda secara signifikan atau hanya kebetulan acak.

Bentuk tabel kontingensi $2 \times 2$:

| | Agentic MLLM Benar | Agentic MLLM Salah | Total |
|---|:---:|:---:|:---:|
| **Konvensional Benar** | $n_{11}$ (Keduanya Benar) | $n_{10}$ (Hanya Konvensional Benar) | $n_{1\cdot}$ |
| **Konvensional Salah** | $n_{01}$ (Hanya Agentic Benar) | $n_{00}$ (Keduanya Salah) | $n_{0\cdot}$ |
| **Total** | $n_{\cdot 1}$ | $n_{\cdot 0}$ | $N = 476$ |

### Formulasi Uji Statistik
1. **Statistik Uji Chi-Kuadrat McNemar dengan Koreksi Kontinuitas Edwards**:
   $$\chi^2 = \frac{(|n_{01} - n_{10}| - 1)^2}{n_{01} + n_{10}}$$
   Derajat kebebasan ($df$) = 1.

2. **Tingkat Signifikansi**: $\alpha = 0.05$. Nilai kritis $\chi^2_{0.05, 1} = 3.841$.

3. **Kaidah Keputusan**:
   - Jika $\chi^2 > 3.841$ atau $p\text{-value} < 0.05$: Tolak $H_0$. Perbedaan performa antara Pipeline Multimodal Konvensional Hibrida dan Agentic MLLM signifikan secara statistik.
   - Jika $\chi^2 \le 3.841$ atau $p\text{-value} \ge 0.05$: Gagal tolak $H_0$. Tidak terdapat perbedaan signifikan secara statistik.

4. **Uji Binomial Eksak (Small Sample Fallback)**:
   Jika $n_{01} + n_{10} < 25$, koreksi chi-kuadrat tidak valid dan sistem otomatis menjalankan uji binomial dua sisi eksak:
   $$p = 2 \times \sum_{k=0}^{\min(n_{01}, n_{10})} \binom{n_{01} + n_{10}}{k} (0.5)^{n_{01} + n_{10}}$$

---

## 5. Struktur Berkas Luaran Hasil Evaluasi

- `outputs/tables/benchmark_results.csv`: Tabel ringkasan perbandingan metrik Akurasi, Precision, Recall, Macro F1, Micro F1, CER, WER, Latensi (ms), dan VRAM (MB).
- `outputs/tables/mcnemar_results.json`: Nilai $n_{00}, n_{01}, n_{10}, n_{11}$, nilai statistik $\chi^2$, $p\text{-value}$, dan interpretasi hipotesis.
- `outputs/figures/confusion_matrices.png`: Matriks kontingensi dan confusion matrix multi-kelas kedua model.
- `outputs/figures/latency_vs_accuracy.png`: Diagram sebaran komparasi trade-off latensi vs akurasi.
