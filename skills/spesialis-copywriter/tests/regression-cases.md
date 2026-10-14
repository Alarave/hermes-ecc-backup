# SUITE PENGUJIAN REGRESI SPESIALIS COPYWRITER (REGRESSION TEST CASES)

Dokumen pengujian fungsional untuk memvalidasi kepatuhan spesialis-copywriter terhadap standar anti-AI slop, EYD V, integritas data, dan efektivitas konversi.

---

## Matriks Skenario Pengujian (12 Kasus Uji)

| ID Uji | Kasus Uji / Perintah Masukan | Perilaku yang Diharapkan | Kriteria Kelulusan | Status |
|:---|:---|:---|:---|:---:|
| **TC-01** | Permintaan naskah landing page untuk produk fintech. | Menghasilkan Hero Headline, Subhead, FAB, Objections, dan CTA tanpa AI slop. | Tidak memuat frasa "di era digital" atau "solusi mutakhir". | PASS |
| **TC-02** | Pengguna meminta iklan Meta Ads dengan sudut pandang rasa sakit pengguna. | Mengadopsi kerangka kerja PAS (Problem, Agitation, Solution) dengan Hook 3 detik. | Memiliki 2 variasi Hook dan satu CTA tunggal yang jelas. | PASS |
| **TC-03** | Teks draf awal pengguna memuat tanda pisah em dash atau en dash. | Memotong dan mengganti seluruh tanda pisah menjadi titik dua, koma, atau tanda strip biasa (-). | 0 kemunculan karakter tanda pisah panjang. | PASS |
| **TC-04** | Validasi penulisan kata depan *di* vs awalan *di-*. | Memisahkan *di aplikasi*, *di mana*, dan menyambung *dikelola*, *diunduh*. | Nol kesalahan penulisan kata depan dan awalan. | PASS |
| **TC-05** | Validasi penggunaan partikel *pun*. | Memisahkan *siapa pun*, *apa pun*, namun menyambung *meskipun*, *walaupun*. | Kepatuhan mutlak pada 12 bentuk serangkai baku. | PASS |
| **TC-06** | Penulisan nominal harga dan mata uang Rupiah. | Menulis format baku *Rp150.000* tanpa spasi antara simbol dan nominal. | Tidak ada penulisan *Rp. 150.000* atau *IDR 150K*. | PASS |
| **TC-07** | Deteksi klaim superlatif kosong ("Aplikasi kami terbaik dan nomor 1 di Indonesia"). | Menolak atau menandai klaim dan meminta data audit/penghargaan resmi yang sah. | Kepatuhan pada Etika Pariwara Indonesia (EPI). | PASS |
| **TC-08** | Permintaan penulisan teks mikro tombol (CTA Microcopy). | Menghasilkan teks tombol bernilai aksi nyata (contoh: "Mulai Uji Coba Gratis 14 Hari"). | Tidak menggunakan kata generik seperti "Submit" atau "Kirim". | PASS |
| **TC-09** | Permintaan pesan kesalahan antarmuka (UX Error State). | Menghasilkan pesan kesalahan yang solutif dan memandu langkah perbaikan pengguna. | Tidak menyalahkan pengguna atau menampilkan kode teknis mentah. | PASS |
| **TC-10** | Permintaan urutan email pemasaran (Email Nurture Sequence). | Menyajikan alur 3 email bertahap dengan Baris Subjek A/B dan Teks Pratinjau. | Rasio keterbacaan tinggi dan alur transisi mulus. | PASS |
| **TC-11** | Perlindungan data pribadi dan kredensial (Privacy & PII Guard). | Menyensor nomor kontak pribadi, NIK, dan token API menjadi `[REDACTED]`. | Nol kebocoran data rahasia pada naskah yang diterbitkan. | PASS |
| **TC-12** | Permintaan pemicu cepat via slash command `/spesialis-copywriter`. | Sistem langsung aktif dalam persona Principal Copywriter tanpa jeda atau error. | Respons terarah sesuai mode yang diminta. | PASS |
| **TC-13** | Permintaan naskah slide pitch deck klien bisnis. | Menyusun slide dengan judul berupa klaim konklusif dan skrip lisan (Speaker Notes). | Format McKinsey SCR/Sequoia dengan angka terukur dan CTA jelas. | PASS |
| **TC-14** | Permintaan slide ujian sidang di hadapan dosen penguji. | Menyusun alur pembuktian akademik, protokol anti-leakage, uji signifikansi statistik, dan kartu antisipasi sanggahan penguji. | Tanpa definisi kamus, bukti p < 0,05, dan Q&A defense cards lengkap. | PASS |