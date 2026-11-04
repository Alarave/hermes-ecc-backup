# STANDAR OPERASIONAL & TEMPLATE: BAB V PENUTUP
> Dokumen referensi resmi penulisan Bab 5 Penutup (Standar Pemetaan 1:1 Kesimpulan terhadap Tujuan, dan Rekomendasi Teknis Actionable).

---

## 🏛️ PEDOMAN ARSITEKTUR BAB V (RULES & CONSTRAINTS)

### 1. Pemetaan 1:1 Kesimpulan terhadap Tujuan Penelitian
- **Cermin Sempurna (One-to-One Alignment)**:
  - Setiap butir kesimpulan WAJIB menjawab langsung nomor butir Tujuan Penelitian (Sub-bab 1.3).
  - Jika Tujuan Penelitian memiliki 3 butir, maka Kesimpulan wajib memiliki 3 butir yang bersesuaian urutannya.
- **Wajib Didukung Angka Nyata (Evidence-Grounded)**:
  - Dilarang membuat kesimpulan kualitatif abstrak atau klaim tanpa bukti (misal: "Sistem telah berhasil dibuat dengan sangat baik").
  - Wajib menyertakan metrik angka konkret hasil eksperimen Bab 4 (contoh: persentase akurasi, nilai RMSE, atau hasil uji signifikansi $p$-value).

---

### 2. Standar Saran Penelitian Lanjutan (Actionable Recommendations)
- **Saran Teknis Spesifik**:
  - Dilarang keras menulis saran klise (seperti *"Perlu ditingkatkan lagi sistemnya"* atau *"Diharapkan bermanfaat bagi masyarakat"*).
  - Saran wajib ditujukan kepada **peneliti lanjutan** dan memuat rekomendasi teknis konkret mengenai apa yang belum sempat diteliti karena batasan Ruang Lingkup (Sub-bab 1.2).
- **Cakupan Saran**:
  1. *Eksplorasi Metode/Arsitektur Baru*: Rekomendasi penambahan mekanisme layer, transformer, atau algoritma alternatif.
  2. *Ekspansi Data*: Rekomendasi penambahan rentang waktu data atau pengujian pada domain yang lebih menantang.
  3. *Infrastruktur & Deployment*: Rekomendasi optimasi latensi, kompresi bobot (ONNX/TensorRT), atau integrasi perangkat IoT/Edge.

---

## 📝 TEMPLATE STRUKTUR BAB V PENUTUP

```markdown
# 5. PENUTUP

## 5.1 Kesimpulan
Berdasarkan serangkaian perancangan, implementasi, dan evaluasi eksperimental yang telah dipaparkan pada bab-bab sebelumnya, dapat ditarik beberapa kesimpulan utama yang menjawab tujuan penelitian:
1. **Perancangan dan Implementasi Arsitektur**: Arsitektur [Model Usulan] berhasil dibangun dengan protokol *anti-data leakage* yang memisahkan partisi data latih dan uji sebelum tahapan penskalaan nilai, menghasilkan kurva pelatihan yang stabil tanpa indikasi *overfitting*.
2. **Evaluasi Kinerja Komparatif**: Model yang diusulkan terbukti mengungguli model baseline secara komparatif pada data uji independen, dengan capaian nilai RMSE sebesar [Nilai RMSE] (penurunan kesalahan sebesar [X]%) dan peningkatan akurasi arah tren (*Mean Directional Accuracy*) mencapai [Nilai MDA]%.
3. **Signifikansi Statistik**: Hasil uji hipotesis Diebold-Mariano menghasilkan nilai statistik $DM = [Nilai DM]$ dengan $p$-value sebesar $[Nilai p] < 0.05$, yang secara saintifik membuktikan penolakan hipotesis nol ($H_0$) dan menegaskan bahwa keunggulan performa model usulan signifikan secara statistik pada tingkat kepercayaan 95%.

## 5.2 Saran
Untuk menyempurnakan dan memperluas cakupan penelitian di masa mendatang, beberapa rekomendasi teknis yang disarankan antara lain:
1. **Eksplorasi Mekanisme Perhatian Dinamis**: Peneliti selanjutnya disarankan untuk mengintegrasikan mekanisme *Temporal Self-Attention* guna menguji apakah bobot dependensi jangka panjang dapat ditangkap lebih adaptif pada kondisi volatilitas ekstrem.
2. **Ekspansi Dataset Multivariat**: Mengingat penelitian ini dibatasi pada data univariat [Nama Objek], penelitian lanjutan disarankan untuk memasukkan variabel eksternal seperti sentimen berita atau indeks makroekonomi untuk memperkaya representasi fitur.
3. **Optimalisasi Inferensi untuk Produksi**: Disarankan untuk melakukan kuantisasi model (*INT8 Quantization*) dan ekspor ke *ONNX Runtime* agar latensi inferensi dapat ditekan di bawah 20 milidetik untuk kebutuhan serving *real-time*.
```