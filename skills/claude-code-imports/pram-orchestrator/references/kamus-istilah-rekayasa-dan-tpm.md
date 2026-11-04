# GLOSARIUM RESMI: SENARAI PADANAN ISTILAH REKAYASA SISTEM, TATA KELOLA AGEN & MANAJEMEN PROYEK TEKNIS
> Pedoman kosakata baku bahasa Indonesia, kebijakan tata istilah, dan standarisasi taklimat operasional untuk Technical Project Manager (TPM), Systems Architect, dan Chief AI Orchestrator (Pram).

---

## 1. Kebijakan & Kaidah Penggunaan Istilah Asing vs Padanan Bahasa Indonesia

Tujuan komunikasi teknis adalah ketepatan makna, ketegasan perintah, dan keterpahaman mutlak tanpa ambiguitas. Mengadopsi pedoman ejaan resmi (EYD V) dan Badan Pengembangan dan Pembinaan Bahasa, seluruh istilah teknis dalam komunikasi orkestrasi dan dokumentasi sistem diklasifikasikan ke dalam 3 kelas pemakaian:

### Kelas A: Padanan Sudah Baku dan Lazim Digunakan
- **Kaidah**: WAJIB menggunakan padanan bahasa Indonesia secara langsung tanpa menyertakan istilah asingnya.
- **Contoh**:
  - *unduh* (bukan download)
  - *unggah* (bukan upload)
  - *daring / luring* (bukan online / offline)
  - *tautan* (bukan link)
  - *peramban* (bukan browser)
  - *pemangku kepentingan* (bukan stakeholder)
  - *pencilan* (bukan outlier)
  - *peubah / variabel* (bukan variable)
  - *basis data* (bukan database)
  - *berkas* (bukan file)
  - *tangkapan layar* (bukan screenshot)
  - *tembolok* (bukan cache)
  - *rekayasa* (bukan engineering)
  - *perangkat lunak / perangkat keras* (bukan software / hardware)
  - *sumber terbuka* (bukan open source)
  - *repositori* (bukan repository)
  - *fungsi* (bukan function)
  - *masukan / luaran* (bukan input / output)
  - *alur kerja* (bukan workflow)
  - *tenggat* (bukan deadline)
  - *gawai* (bukan gadget)
  - *pemutakhiran* (bukan update)
  - *peningkatan* (bukan upgrade)
  - *pencadangan* (bukan backup)
  - *bawaan / baku* (bukan default)
  - *galat* (bukan error)
  - *templat* (bukan template)
  - *umpan balik* (bukan feedback)
  - *tindak lanjut* (bukan follow up)
  - *tinjauan / telaah* (bukan review)
  - *kerangka kerja* (bukan framework)
  - *peta jalan* (bukan roadmap)
  - *tonggak capaian* (bukan milestone)
  - *penilaian / asesmen* (bukan assessment)

### Kelas B: Padanan Dikenal Namun Istilah Asing Masih Sering Digunakan
- **Kaidah**: Gunakan padanan bahasa Indonesia terlebih dahulu, lalu sertakan istilah asing dalam tanda kurung dan dicetak miring pada penyebutan PERTAMA. Untuk penyebutan selanjutnya, gunakan padanan bahasa Indonesia secara konsisten.
- **Contoh Format Penyebutan Pertama**:
  - *pembelajaran mesin (machine learning)*
  - *mahadata (big data)*
  - *penambangan data (data mining)*
  - *kecerdasan buatan (artificial intelligence)*
  - *jaringan saraf tiruan (neural network)*
  - *rekayasa prompt (prompt engineering)*
  - *pembelajaran mendalam (deep learning)*
  - *rekayasa perangkat lunak (software engineering)*
  - *manajemen proyek teknis (technical project management)*
  - *validasi silang (cross-validation)*
  - *rekayasa fitur (feature engineering)*
  - *dasbor (dashboard)*
  - *kontrol versi (version control)*
  - *pohon kerja (worktree)*
  - *titik pemeriksaan (checkpoint)*
  - *penarikan sampel (sampling)*
  - *selang kepercayaan (confidence interval)*
  - *tolok ukur (benchmark)*
  - *garis dasar / acuan (baseline)*
  - *komputasi awan (cloud computing)*
  - *perusahaan rintisan (startup)*
  - *penelaahan sejawat (peer review)*

### Kelas C: Istilah Asing Sangat Spesifik / Padanan Belum Populer
- **Kaidah**: Gunakan istilah asing (dicetak miring) sebagai istilah utama, lalu sertakan padanan bahasa Indonesia dalam tanda kurung pada penyebutan pertama sebagai penjelas. Selanjutnya gunakan istilah asing tersebut secara konsisten. Singkatan teknis industri (API, SQL, GPU, CPU, REST, CI/CD, JSON, DTO, DAG, WBS, PII) ditulis dengan huruf kapital tegak tanpa cetak miring.
- **Contoh Format Penyebutan Pertama**:
  - *pipeline* (alur pipa data)
  - *server* (peladen)
  - *overfitting* (kondisi kelewat pas model)
  - *underfitting* (kondisi kurang pas model)
  - *linter* (pemeriksa sintaks kode otomatis)
  - *refactoring* (penataan ulang struktur kode)
  - *deadlock* (kondisi saling kunci antarsumber daya)
  - *throughput* (daya lolos data persatuan waktu)
  - *latency* (waktu tunggu inferensi)
  - *payload* (muatan data transaksi)
  - *idempotent* (sifat operasi berkali-kali berluaran identik)
  - *bottleneck* (hambatan leher botol komputasi)
  - *sandbox* (lingkungan isolasi kotak pasir)
  - *grounding* (penambatan fakta pada bukti riil)
  - *hallucination* (halusinasi fakta model)
  - *embedding* (penyematan vektor semantik)
  - *inference* (inferensi model)
  - *deployment* (penggelaran / penerapan sistem)
  - *rollback* (pemulihan mundur ke titik stabil)
  - *circuit breaker* (pemutus sirkuit kegagalan)
  - *backpressure* (tekanan balik beban antrean)
  - *jitter* (variasi jeda acak)

---

## 2. Glosarium Domain 1: Manajemen Proyek Teknis (Technical Project Management / TPM)

| Istilah Asing | Padanan Baku Indonesia | Definisi Operasional & Konteks Penggunaan Pram |
|:---|:---|:---|
| **Work Breakdown Structure (WBS)** | Struktur Rincian Kerja (SRK) | Dekomposisi hierarkis inisiatif proyek menjadi paket kerja atomik yang dapat diestimasi durasi, dependensi, dan penanggung jawabnya. |
| **Critical Path Method (CPM)** | Metode Jalur Kritis (MJK) | Rangkaian tugas terpanjang dalam graf dependensi yang menentukan durasi total proyek; keterlambatan pada jalur ini menunda rilis final. |
| **Milestone** | Tonggak Capaian | Titik pemeriksaan utama penanda selesainya sebuah fase arsitektural tanpa durasi waktu sendiri. |
| **Scope Creep** | Pemekaran Lingkup | Penambahan fitur atau requirement di luar dokumen spesifikasi awal tanpa penyesuaian waktu dan anggaran. |
| **Acceptance Criteria** | Kriteria Keberterimaan | Batasan syarat spesifik yang wajib dipenuhi agar sebuah fitur disahkan oleh Project Owner. |
| **Definition of Done (DoD)** | Batasan Tuntas | Daftar periksa universal yang wajib lolos (tes, build, linter, keamanan) sebelum tugas berstatus VERIFIED. |
| **Spike** | Eksplorasi Prototipe Terbatas | Investigasi teknis singkat berbatas waktu untuk memitigasi ketidakpastian sebelum estimasi WBS dilakukan. |
| **Technical Debt** | Utang Teknis | Biaya pemeliharaan masa depan akibat pengambilan jalan pintas arsitektur demi mengejar kecepatan rilis jangka pendek. |
| **Baseline** | Acuan Garis Dasar | Titik referensi performa, biaya, atau jadwal yang telah disetujui sebagai pembanding capaian aktual. |
| **Roadmap** | Peta Jalan | Panduan strategis tingkat tinggi yang memetakan evolusi visi produk terhadap waktu. |
| **Retrospective** | Retrospeksi | Sesi evaluasi akhir sprint untuk membedah apa yang berhasil, apa yang gagal, dan perbaikan alur kerja. |
| **Gatekeeper** | Penjaga Gerbang Kendali | Mekanisme verifikasi mutlak yang memblokir eksekusi sebelum syarat kualitas terpenuhi. |
| **Single Entry Point** | Pintu Masuk Tunggal | Pola komando di mana seluruh instruksi pengguna disaring melalui Pram sebelum didistribusikan ke sub-agen. |
| **Traceability** | Keterlacakan | Kemampuan menelusuri kebutuhan bisnis dari PRD hingga baris kode dan hasil pengujian terkait. |
| **Zero Cognitive Load** | Beban Kognitif Nol | Prinsip perancangan di mana pengguna tidak dibebani nama alat internal atau rincian mekanis yang dapat diselesaikan otomatis. |

---

## 3. Glosarium Domain 2: Rekayasa Perangkat Lunak & Arsitektur Sistem

| Istilah Asing | Padanan Baku Indonesia | Definisi Operasional & Konteks Penggunaan Pram |
|:---|:---|:---|
| **Modular Monolith** | Monolit Modular | Arsitektur satu repositori dan basis data di mana batas domain bisnis diisolasi secara internal via antarmuka DTO. |
| **Bounded Context** | Konteks Terikat | Batas ruang lingkup bisnis spesifik dalam Domain-Driven Design tempat model data tertentu berlaku murni. |
| **Decoupling** | Pemisahan Keterikatan | Pengurangan ketergantungan langsung antar-modul agar perubahan pada modul A tidak merusak modul B. |
| **Interface Contract** | Kontrak Antarmuka | Spesifikasi format masukan dan luaran data yang mengikat secara matematis antarmodul (dikunci via hash SHA-256). |
| **Inversion of Control (IoC)** | Pembalikan Kendali | Prinsip rekayasa di mana alur kontrol program diserahkan ke kerangka kerja, bukan kode aplikasi langsung. |
| **Dependency Injection (DI)** | Injeksi Ketergantungan | Pola penyediaan dependensi objek dari luar untuk meningkatkan kemudahan pengujian unit (*testability*). |
| **Refactoring** | Penataan Ulang Kode | Modifikasi struktur internal kode program tanpa mengubah perilaku eksternalnya sedikit pun. |
| **Scalability** | Keterukuran / Skalabilitas | Kemampuan sistem menangani lonjakan beban komputasi dengan penambahan sumber daya terprediksi. |
| **High Availability (HA)** | Ketersediaan Tinggi | Karakteristik sistem yang menjamin operasional berkelanjutan dengan meminimalkan waktu henti (*downtime*). |
| **Fault Tolerance** | Toleransi Kesalahan | Kemampuan sistem tetap berfungsi normal meskipun terjadi kegagalan pada salah satu komponen internalnya. |
| **Disaster Recovery (DR)** | Pemulihan Bencana | Rencana kebijakan dan prosedur teknis untuk memulihkan infrastruktur kritis pasca-insiden katastropik. |
| **Single Point of Failure (SPOF)**| Titik Kegagalan Tunggal | Satu komponen rapuh yang jika mengalami kerusakan akan menyebabkan kegagalan total seluruh sistem. |
| **Concurrency** | Keserempakan / Konkurensi | Kemampuan menjalankan beberapa alur komputasi secara tumpang tindih dalam rentang waktu yang sama. |
| **Throughput** | Daya Lolos Data | Volume data atau jumlah transaksi yang berhasil diproses tuntas oleh sistem per satuan waktu. |
| **Latency** | Waktu Tunggu / Latensi | Durasi penundaan antara pengiriman permintaan (*request*) hingga diterimanya respons pertama. |
| **Idempotence** | Keidempotenan | Karakteristik aksi yang jika dieksekusi sekali maupun berulang kali menghasilkan keadaan akhir yang sama persis. |
| **Bottleneck** | Hambatan Leher Botol | Titik penyempitan kapasitas yang memperlambat laju aliran pemrosesan seluruh sistem. |
| **Circuit Breaker** | Pemutus Sirkuit | Pola perlindungan yang menghentikan panggilan ke layanan eksternal yang gagal untuk mencegah kehabisan sumber daya. |
| **Backpressure** | Tekanan Balik | Mekanisme di mana penerima data memberi sinyal ke pengirim untuk memperlambat laju transfer data saat beban penuh. |

---

## 4. Glosarium Domain 3: Sistem Kontrol Versi, Git & Isolasi Alur Kerja

| Istilah Asing | Padanan Baku Indonesia | Definisi Operasional & Konteks Penggunaan Pram |
|:---|:---|:---|
| **Repository** | Repositori / Lumbung Kode | Direktori penyimpanan berkas proyek lengkap beserta seluruh riwayat perubahan terindeks. |
| **Worktree** | Pohon Kerja Terisolasi | Saluran kerja tambahan yang memungkinkan beberapa cabang (*branch*) dibuka pada folder terpisah secara serempak. |
| **Commit** | Rekam Perubahan | Pencatatan snapshot perubahan kode ke dalam riwayat lokal berlabel pesan deskriptif baku. |
| **Branch** | Cabang Pengembangan | Jalur riwayat perubahan terisolasi yang bercabang dari garis utama untuk pengembangan fitur mandiri. |
| **Fast-Forward Merge** | Penggabungan Maju Cepat | Penggabungan cabang di mana pointer target langsung dipindahkan ke ujung cabang tanpa membuat commit merge baru. |
| **Rebase** | Penataan Ulang Basis | Pemindahan basis cabang fitur ke ujung commit terbaru cabang utama untuk menghasilkan riwayat lurus rapi. |
| **Stash** | Penyimpanan Sementara | Penyimpanan perubahan kerja yang belum selesai ke tumpukan memori sementara agar working tree kembali bersih. |
| **Cherry-Pick** | Petik Pilih Perubahan | Pengambilan satu commit spesifik dari cabang lain untuk diterapkan pada cabang kerja saat ini. |
| **Conflict Resolution** | Resolusi Tabrakan Kode | Tindakan mendamaikan perbedaan kode yang saling bertentangan pada baris berkas yang sama. |
| **Rollback** | Pembatalan Mundur | Tindakan mengembalikan basis kode atau lingkungan penerapan ke titik pemeriksaan stabil sebelumnya. |

---

## 5. Glosarium Domain 4: Kecerdasan Buatan, Pembelajaran Mesin & MLOps

| Istilah Asing | Padanan Baku Indonesia | Definisi Operasional & Konteks Penggunaan Pram |
|:---|:---|:---|
| **Data Ingestion** | Penyerapan Data | Proses penarikan data mentah dari berbagai sumber masukan ke dalam penyimpanan danau data (*data lake*). |
| **Data Leakage** | Kebocoran Data | Kesalahan metodologi di mana informasi dari data uji merembes ke data latih, menghasilkan evaluasi palsu. |
| **Train/Test Split** | Partisi Data Latih dan Uji | Pemisahan dataset menjadi subkumpulan latihan dan pengujian sebelum dilakukan transformasi nilai apa pun. |
| **Feature Engineering** | Rekayasa Fitur | Proses memilih, mengubah, dan mengombinasikan variabel mentah menjadi fitur prediktif yang informatif. |
| **Loss Function** | Fungsi Kerugian | Formula matematika yang menghitung selisih antara luaran prediksi model dengan nilai target aktual. |
| **Hyperparameter Tuning** | Penalaan Hiperparameter | Proses optimasi konfigurasi eksternal model yang nilainya ditentukan sebelum pelatihan dimulai. |
| **Overfitting** | Kelewat Pas | Kondisi di mana model menghafal data latih beserta deraunya sehingga gagal menggeneralisasi pada data baru. |
| **Underfitting** | Kurang Pas | Kondisi di mana model terlalu sederhana untuk menangkap pola relasi mendasar di dalam data. |
| **Model Registry** | Registri Model | Repositori terpusat untuk menyimpan, melacak versi, dan mengelola siklus rilis bobot model teruji. |
| **Data Drift** | Pergeseran Distribusi Data | Perubahan statistik pada sebaran data masukan di produksi dibandingkan sebaran data latih awal. |
| **Concept Drift** | Pergeseran Konsep | Perubahan relasi statistik antara fitur masukan dengan variabel target aktual seiring berjalannya waktu. |
| **Inference Latency** | Latensi Inferensi | Waktu komputasi yang dihabiskan model untuk menghasilkan prediksi sejak masukan diterima. |
| **Canary Deployment** | Penerapan Burung Kenari | Strategi rilis model baru ke sebagian kecil pengguna (5-10%) sebelum dialihkan penuh ke seluruh sistem. |
| **Shadow Deployment** | Penerapan Bayangan | Strategi rilis di mana model baru menerima traffic produksi paralel tanpa memengaruhi respons pengguna riil. |
| **Dead-Letter Queue (DLQ)** | Antrean Surat Mati | Antrean penampungan data rusak atau anomali yang gagal diproses agar tidak merusak alur komputasi utama. |
| **Hybrid Retrieval** | Temu Kembali Hibrida | Penggabungan pencarian vektor rapat (*dense*) dan kata kunci jarang (*sparse*) untuk hasil pencarian semantik akurat. |
| **Grounding** | Penambatan Fakta | Penambatan respons model generatif pada bukti dokumen terverifikasi untuk mengeliminasi halusinasi. |

---

## 6. Glosarium Domain 5: Keamanan Aplikasi, Pengujian & Jaminan Mutu (QA)

| Istilah Asing | Padanan Baku Indonesia | Definisi Operasional & Konteks Penggunaan Pram |
|:---|:---|:---|
| **Static Application Security Testing (SAST)** | Pengujian Keamanan Statis | Analisis kode sumber tanpa menjalankan program untuk mendeteksi celah kerentanan sejak dini. |
| **Penetration Testing** | Uji Penetrasi | Simulasi serangan siber terkontrol untuk mengevaluasi ketahanan keamanan sistem secara nyata. |
| **Vulnerability** | Kerentanan / Celah Keamanan | Kelemahan pada desain, implementasi, atau konfigurasi sistem yang dapat dieksploitasi pihak luar. |
| **Proof-of-Concept (PoC)** | Bukti Konsep Serangan | Kode uji atau skrip minimal yang membuktikan sebuah celah kerentanan benar-benar dapat dieksploitasi. |
| **Surgical Patch** | Tambalan Bedah Minimalis | Perbaikan kode terarah dan hemat diff yang menutup celah keamanan tanpa mengubah logika bisnis lain. |
| **Zero Regression** | Nol Regresi | Jaminan bahwa penerapan patch atau fitur baru tidak merusak rangkaian pengujian unit yang sudah lulus sebelumnya. |
| **Sanitization** | Sanitasi Masukan | Pembersihan karakter berbahaya dari input pengguna sebelum diproses oleh database atau dirender ke DOM. |
| **Least Privilege** | Hak Akses Terkecil | Prinsip keamanan di mana setiap agen atau proses hanya diberi izin minimum yang diperlukan untuk tugasnya. |
| **Zero Trust** | Nol Kepercayaan | Paradigma keamanan di mana tidak ada entitas, pengguna, atau agen yang dipercaya secara bawaan tanpa verifikasi. |
| **Secret Scrubbing** | Penyensoran Kredensial | Tindakan otomatis menyamarkan token, sandi, dan kunci privat menjadi label REDACTED. |
| **Unit Testing** | Pengujian Unit | Pengujian terisolasi pada unit kode terkecil (fungsi/kelas) untuk memastikan kebenaran logikanya. |
| **Integration Testing** | Pengujian Integrasi | Pengujian gabungan antarmodul untuk memastikan komunikasi data dan antarmuka berjalan selaras. |
| **End-to-End Testing** | Pengujian Ujung ke Ujung | Pengujian alur kerja sistem lengkap dari perspektif pengguna akhir dari awal hingga tuntas. |
| **Test Coverage** | Cakupan Pengujian | Metrik persentase baris kode sumber yang dieksekusi saat rangkaian tes otomatis dijalankan (wajib >= 80%). |

---

## 7. Pedoman Sintaksis Taklimat Penugasan & Komando Dingin (Zero AI-Slop)

Dalam menyusun delegasi tugas ke sub-agen maupun laporan sprint ke Project Owner, Pram mewajibkan konstruksi kalimat komando yang mematuhi standar berikut:

### Pola Kalimat Komando Taklimat (Task Briefing Syntax):
```text
[SUBYEK OPERASIONAL] + [KATA KERJA OPERASIONAL AKTIF] + [OBJEK KOMPONEN] + [BATASAN / KONSTRAT] + [BUKTI LUARAN]
```
- **Contoh Benar**:
  > "Spesialis-Backend, implementasikan modul enkripsi voucher menggunakan algoritma AES-256-GCM pada berkas `src/security/token.go`, kunci interface via hash SHA-256, dan lampirkan log kelulusan unit test coverage minimal 80%."
- **Contoh Salah (AI-Slop & Basa-Basi)**:
  > ~~"Halo kawan! Tentu saja dengan senang hati saya akan membantu Anda membuat modul enkripsi yang sangat keren dan penting ini. Mari kita mulai..."~~ (DILARANG KERAS).

### Aturan Tipografi & Gaya Teks Pram:
1. **Dilarang Tanda Pisah Em/En Dash**: Jangan pernah menggunakan tanda pisah panjang em-dash atau en-dash. Gunakan titik dua (`:`), tanda kurung `()`, koma, atau tanda strip biasa (`-`).
2. **Lugaskan Klaim**: Ganti kata sifat hiperbolis dengan fakta numerik (bukan "performa sangat cepat", melainkan "latensi inferensi < 50 milidetik").
3. **Pemisahan Tegas**: Bedakan antara fakta yang telah terverifikasi mesin (*verified facts*), asumsi yang belum diuji (*assumptions*), dan risiko yang memerlukan persetujuan (*decision required*).