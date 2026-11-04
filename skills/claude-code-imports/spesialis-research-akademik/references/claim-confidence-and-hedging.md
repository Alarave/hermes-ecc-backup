# Sistem Audit Claim Confidence dan Academic Hedging Berbasis Bukti Empiris
> Panduan Standar Operasional Verifikasi Integritas Asersi Ilmiah, Mitigasi Over-Claiming, dan Transformasi Bahasa Akademik Berbobot Bukti (Evidence-Gated Assertion).

---

## 1. Landasan Filosofis: Dari Asersi Liar Menuju Klaim Teruji

Kelemahan paling fatal dalam penulisan karya ilmiah dan ujian sidang sarjana adalah *over-claiming*, yaitu menyajikan pernyataan atau klaim keberhasilan metode secara berlebihan tanpa landasan data yang sah.

Diadaptasi dari sistem *Claim Confidence Engine* pada Jenni AI dan diselaraskan dengan etika riset "Bukan, Melainkan":
- **Bukan** membuat klaim bombastis agar terlihat hebat di depan penguji.
- **Melainkan** menyajikan pernyataan terukur yang didukung secara presisi oleh angka metrik, sitasi primer, dan uji signifikansi statistik formal.

Setiap kalimat deklaratif yang menyatakan keunggulan, pengaruh, hubungan sebab-akibat, atau kesimpulan dalam naskah wajib melewati gerbang *Claim Confidence Audit*.

---

## 2. Taksonomi 6 Kategori Cacat Klaim Ilmiah

Sistem audit mengklasifikasikan setiap klaim ke dalam 6 status deterministik:

| Kategori Cacat | Definisi dan Ciri Utama | Dampak saat Ujian Sidang | Tindakan Perbaikan Wajib |
|---|---|---|---|
| **1. Unsupported** | Klaim faktual tanpa rujukan pustaka, tanpa sitasi, atau tanpa bukti angka eksperimen. | Dicecar penguji mengenai dasar asumsi. | Berikan sitasi primer atau lampirkan data tabel uji. |
| **2. Weakly Supported** | Klaim didukung pustaka sekunder, artikel opini non-peer-reviewed, atau sampel terlalu sedikit. | Diragukan validitas generalisasinya. | Ganti dengan rujukan jurnal bereputasi atau uji pada partisi data yang representatif. |
| **3. Overstated** | Bahasa melebih-lebihkan temuan (misal: menemukan korelasi lemah namun mengklaim hubungan kausal mutlak). | Menjadi sasaran empuk bantahan dosen penguji. | Lakukan pelemahan klaim (*academic hedging*) sesuai p-value nyata. |
| **4. Misrepresented** | Kutipan memelintir atau menyimpulkan hal yang bertolak belakang dengan argumen penulis asli. | Pelanggaran etika atribusi ilmiah. | Baca dokumen asli dan tulis ulang intisari sesuai konteks asli. |
| **5. Contradicted** | Klaim di satu bab bertentangan dengan temuan di bab lain (misal: abstrak menyatakan akurat, pembahasan menyatakan gagal). | Nilai inkonsistensi naskah jatuh seketika. | Rekonsiliasi data dan sesuaikan kesimpulan dengan data terburuk. |
| **6. Unverifiable** | Klaim menggunakan data privat yang tidak dapat direproduksi atau diverifikasi pihak luar. | Gugurnya prinsip keterbukaan sains (*Open Science*). | Unggah skrip evaluasi dan sertakan tautan repositori dataset publik. |

---

## 3. Matriks Transformasi Academic Hedging (Kamus Konversi Bahasa)

*Academic Hedging* adalah teknik linguistik ilmiah untuk membatasi derajat kepastian suatu klaim agar sesuai dengan bobot bukti yang tersedia.

### A. Matriks Kata Kerja Klaim (Claim Verbs Matrix)

| Kategori Derajat Kepastian | Kata Kerja / Frasa yang Dilarang (Kecuali Terbukti Mutlak) | Kata Kerja Ilmiah Baku (Hedged & Responsible) |
|---|---|---|
| **Kausalitas & Pengaruh** | Membuktikan secara mutlak, pasti menyebabkan, menjamin 100% | Mengindikasikan, mengarah pada, memberikan indikasi kuat bahwa |
| **Keunggulan Model** | Model terbaik di dunia, sempurna mengatasi masalah, tanpa cela | Menunjukkan performa lebih kompetitif, mencatat penurunan galat |
| **Signifikansi Perbedaan** | Jelas sangat berbeda, unggul telak, jauh melampaui | Berbeda secara signifikan pada taraf uji p < 0.05 |
| **Generalisasi Luas** | Berlaku untuk semua kondisi, tidak terpengaruh apapun | Berlaku dalam batasan ruang lingkup pengujian, teramati pada kondisi |

### B. Pola Transformasi Kalimat Kalibrasi

#### Contoh Kasus 1: Evaluasi Model Prediksi Deret Waktu
- **Klaim Asli (Overstated / Ditolak)**:
  "Arsitektur LSTM yang diusulkan terbukti sempurna dalam memprediksi seluruh pergerakan harga saham BBCA tanpa kesalahan."
- **Audit Cacat**: Overstated dan Unverifiable (tidak ada model prediksi yang sempurna tanpa galat).
- **Hasil Transformasi (Hedged / Diterima)**:
  "Berdasarkan evaluasi pengujian, arsitektur CEEMDAN-LSTM mencatat nilai MAPE sebesar 1.42% pada data uji, yang mengindikasikan tingkat akurasi prediksi yang kompetitif dalam batasan deret waktu yang diteliti."

#### Contoh Kasus 2: Perbandingan Baseline
- **Klaim Asli (Weakly Supported / Ditolak)**:
  "Model kami jelas jauh lebih hebat dibandingkan model baseline XGBoost."
- **Audit Cacat**: Weakly Supported dan Non-Academic Slop (menggunakan kata emosional "hebat" tanpa ukuran terukur).
- **Hasil Transformasi (Hedged / Diterima)**:
  "Model yang diusulkan menghasilkan penurunan RMSE sebesar 14.8% dibandingkan model baseline XGBoost. Hasil uji Diebold-Mariano menunjukkan nilai p = 0.012 (p < 0.05), yang membuktikan bahwa keunggulan akurasi tersebut signifikan secara statistik dan bukan akibat fluktuasi acak."

---

## 4. Protokol Verifikasi Statistik Sebelum Membuat Asersi Keunggulan

Sebelum penulis diizinkan menulis frasa *"lebih unggul secara signifikan"* atau *"significantly outperforms"*, protokol berikut wajib terpenuhi:

1. **Uji Hipotesis Formal Terpenuhi**:
   - Untuk prediksi deret waktu: Wajib Uji Diebold-Mariano (DM-test).
   - Untuk data klasifikasi berpasangan: Wajib Uji McNemar atau Wilcoxon Signed-Rank Test.
   - Untuk perbandingan multikelompok: Wajib ANOVA / Kruskal-Wallis diikuti uji lanjut Tukey / Dunn.
2. **Ambang Batas Signifikansi**:
   Nilai $p < 0.05$ (atau taraf signifikansi $\alpha = 5\%$) tercatat secara eksplisit di Bab 4.
3. **Format Pelaporan Baku**:
   Wajib mencantumkan nilai statistik hitung ($t$, $z$, atau $W$), derajat kebebasan, dan nilai p-value tepat di samping kalimat kesimpulan.

---

## 5. Checklist Verifikasi Mandiri Sebelum Sidang Skripsi (Anti-Grill Gate)

Gunakan checklist ini sebelum mencetak naskah atau menyerahkan draf ke dosen pembimbing:

- [ ] Apakah setiap klaim pada Bab 1.1 memiliki rujukan pustaka ber-DOI aktif?
- [ ] Apakah tidak ada klaim kausalitas mutlak tanpa uji korelasi atau regresi formal?
- [ ] Apakah kata "signifikan" HANYA digunakan saat merujuk hasil uji statistik formal ber-p-value?
- [ ] Apakah seluruh kelemahan atau anomali data diakui secara transparan pada Bab 4.4 Pembahasan?
- [ ] Apakah kesimpulan pada Bab 5.1 hanya memuat fakta yang telah terbukti pada Bab 4?
- [ ] Apakah naskah 100% bebas dari kata sifat hiperbolis dan bebas tanda pisah em-dash atau en-dash?
