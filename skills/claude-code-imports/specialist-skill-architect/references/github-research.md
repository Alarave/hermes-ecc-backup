# OPERATIONAL REFERENCE: GITHUB RESEARCH & EXTERNAL SOTA HARVESTING
> Panduan operasional komprehensif Specialist Skill Architect untuk meneliti repositori GitHub, mengevaluasi standar arsitektur kecerdasan buatan kelas dunia, mengaudit lisensi perangkat lunak, dan menyerap pola desain mutakhir tanpa membawa sampah kode (*zero-slop distillation*).

---

## 1. Filosofi Penyerapan Repositori Eksternal (Distillation Over Cloning)

Di era ledakan ekosistem kecerdasan buatan, ribuan repositori skill dan agen AI beredar secara publik di GitHub. Namun, banyak dari repositori tersebut mengandung utang teknis, dependensi lingkungan yang tidak kompatibel dengan Windows lokal, atau format instruksi yang tidak terstandarisasi.

Specialist Skill Architect menerapkan prinsip **Distilasi Arsitektural Mengalahkan Kloning Mentah (*Architectural Distillation Over Raw Cloning*)**:
1. **Dilarang Kloning Membabi Buta**: Mengkloning repositori mentah yang berisi ratusan berkas sering kali mengotori direktori kerja dengan script shell Linux, dependensi Python usang, dan tabrakan nama skill lokal.
2. **Ekstraksi Pola Desain (Pattern Extraction)**: Ambil arsitektur logis, alur penalaran, algoritma evaluasi, skema validasi, dan standar kualitas dari repositori rujukan, lalu tulis ulang secara bersih ke dalam format baku RCCO.
3. **Pemberian Atribusi Jujur (Attribution & Lineage)**: Catat URL sumber, nama pengembang, lisensi resmi, dan nomor commit/rilis repositori rujukan pada berkas dokumentasi atau `CHANGELOG.md`.

---

## 2. Taksonomi Sumber Rujukan Eksternal Bereputasi Tinggi

Arsitek memprioritaskan pencarian pada 4 tingkatan repositori GitHub bereputasi:

### Tingkat 1: Repositori Standar Resmi Industri (Official Standard Repositories)
- `anthropics/anthropic-quickstarts` & `anthropics/courses`: Standar resmi arsitektur Agent Skills dan Tool Use.
- `openai/openai-cookbook` & `openai/symphony`: Implementasi Proof-of-Work, deterministik structured outputs, dan mitigasi halusinasi.
- `getsentry/sentry-agent-skills`: Praktik terbaik pembuatan berkas referensi modular dan arsitektur SDK skill bundles.

### Tingkat 2: Repositori Riset Ilmiah & Benchmark Akademik (Peer-Reviewed Research)
- `ynulihao/AgentSkillOS` (arXiv:2603.02176): Arsitektur Hierarchical Capability Tree, multi-format deliverable artifacts, dan benchmark evaluasi skill berbasis Bradley-Terry.
- `foryourhealth111-pixel/Vibe-Skills`: Metodologi Two-Stage Progressive Skill Routing, pemisahan skala tugas Level L vs Level XL, dan optimasi context window.

### Tingkat 3: Repositori Utilitas Spesialis & Engine Vektor
- `Sleepy-Avacado/FigGenie-paper-diagram-skill`: Compiler diagram arsitektur vektor ilmiah (SVG, PDF tight-box, PPTX native shape).
- `rohitg00/agentbrain` & `juanquijandria/prisma-harness`: Pola pengujian bukti eksekusi independen (*independent proof gate*) dan state machine deterministik.

### Tingkat 4: Repositori Kurasi Komunitas Terverifikasi
- Repositori kurasi komunitas yang memiliki dokumentasi jelas, lisensi terbuka (MIT/Apache-2.0), dan riwayat commit aktif. Dilarang mengadopsi repositori tanpa lisensi atau repositori eksperimental yang ditinggalkan pemiliknya (*abandoned repos*).

---

## 3. Matriks Evaluasi Kelayakan Repositori GitHub

Sebelum mengadopsi ide atau modul dari GitHub, arsitek menjalankan evaluasi 8 dimensi:

| Dimensi Evaluasi | Parameter Ambang Batas Minimum | Tindakan Jika Tidak Memenuhi |
|:---|:---|:---|
| **Kesesuaian Lisensi** | Wajib open-source permisif (MIT, Apache-2.0, BSD-3, CC-BY-4.0). | Tolak secara mutlak jika berlisensi GPL kaku, proprietary komersial tertutup, atau tanpa lisensi. |
| **Kompatibilitas Host** | Logika dapat dieksekusi di Windows 11 host (POSIX bash via MSYS atau native Python/Node). | Jika mewajibkan dependensi Linux native (seperti AppArmor, bubblewrap, iptables), adopsi polanya saja tanpa menginstal paket fisiknya. |
| **Kemandirian Dependensi** | Minim dependensi runtime berat; hindari kebutuhan server database eksternal berbayar jika SQLite/Ripgrep mencukupi. | Sederhanakan implementasi ke library standar bahasa pemrogramannya (YAGNI). |
| **Kebersihan Arsitektur** | Memisahkan instruksi logika dari data mentah; modularitas jelas. | Lakukan refactoring total saat memformat ulang ke RCCO. |
| **Keamanan Rantai Pasok** | Bebas dari script instalasi tersembunyi, curl ke bash berbahaya, atau file biner yang tidak diaudit. | Audit seluruh script baris demi baris sebelum dijalankan di terminal lokal. |
| **Ketahanan Prompt Injection** | Bebas dari teks instruksi tersembunyi yang mencoba mengambil alih kendali sistem agen. | Lakukan sanitasi teks dan validasi input. |
| **Pemisahan Konteks** | Format dokumentasi mendukung pemuatan bertahap (*progressive disclosure*). | Pecah berkas besar menjadi berkas referensi modular terpisah. |
| **Kualitas Pembuktian** | Menyertakan bukti pengujian nyata atau benchmark empiris. | Tandai klaim tanpa bukti sebagai status *Unverified* hingga diuji di lingkungan lokal. |

---

## 4. Prosedur Operasional Distilasi SOTA GitHub (SOP 5 Langkah)

1. **Langkah 1: Pemeriksaan Metadata & Struktur Berkas**:
   - Periksa README, struktur direktori, berkas lisensi, dan arsitektur repositori target.
   - Identifikasi berkas inti yang memuat logika rekayasa dan abaikan aset dokumentasi berat atau galeri demo besar.
2. **Langkah 2: Audit Lisensi & Keamanan**:
   - Verifikasi izin penggunaan dan redistribusi kode.
   - Pindai script dari potensi eksekusi perintah destruktif.
3. **Langkah 3: Pemisahan Pola Desain dari Implementasi Fisik**:
   - Catat diagram alir, algoritma verifikasi, atau teknik prompt yang membuat repositori tersebut unggul.
   - Tentukan apakah repositori perlu diserap kodenya secara fisik atau hanya diadopsi prinsip logisnya.
4. **Langkah 4: Rekayasa Ulang ke Format RCCO**:
   - Terjemahkan pola desain ke dalam format Role, Context, Constraints, dan Output.
   - Tulis ulang teks dalam bahasa Indonesia baku (EYD V dan KBBI) tanpa tanda pisah em dash atau en dash.
5. **Langkah 5: Verifikasi Kepatuhan & Pencatatan Silsilah**:
   - Jalankan linter audit lokal `scripts/audit_incoming_skills.py` terhadap berkas hasil distilasi.
   - Catat asal-usul repositori rujukan pada `CHANGELOG.md` dan dokumentasi arsitektur.