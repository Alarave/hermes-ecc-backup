# Orkestrasi Karier & Pipa Lamaran Kerja (career-job-orchestration)

Panduan operasional Chief AI Orchestrator & Technical Project Manager (Pram) dalam mengelola siklus pencarian kerja, evaluasi lowongan, penyesuaian (*tailoring*) berkas lamaran, hingga persiapan wawancara teknis dan manajerial.

---

## 1. Alur Kerja WBS Orkestrasi Karier (End-to-End Pipeline)

Setiap inisiatif pelamaran kerja diperlakukan layaknya sprint rekayasa perangkat lunak berstruktur DAG:

```text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   TSK-JOB-01    │ ──► │   TSK-JOB-02    │ ──► │   TSK-JOB-03    │
│ Triage Lowongan │     │ Analisis Gap &  │     │ Tailoring CV &  │
│ & Eligibilitas  │     │ Ekstraksi Kata  │     │ Formula XYZ     │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                ┌────────────────────────┴────────┐
                                ▼                                 ▼
                        ┌─────────────────┐             ┌─────────────────┐
                        │   TSK-JOB-04    │             │   TSK-JOB-05    │
                        │ Drafting Cover  │             │ Simulasi Interview│
                        │ Letter Tertarget│             │ & Pertanyaan Sokratis│
                        └─────────────────┘             └─────────────────┘
```

---

## 2. Pilar 1: Analisis Job Fit & Deteksi Kesenjangan Skill (Gap Analysis)

Sebelum merancang dokumen lamaran, Pram mengeksekusi audit kelayakan dua tahap:

### A. Gerbang Eligibilitas (Hard Eligibility Gate)
Memeriksa prasyarat mutlak yang tidak dapat dikompromikan:
- Hak Kerja / Visa: Apakah posisi mewajibkan status warga negara atau izin kerja spesifik?
- Lokasi & Pengaturan Kerja: On-site, Hybrid, atau Remote (perhatikan batas zona waktu).
- Jenjang Pendidikan & Pengalaman Minimal: Apakah ada batas keras yang menghalangi penyaringan awal?

### B. Matriks Ekstraksi Kata Kunci & Skoring Kesesuaian (Job Fit Scoring)
Dekomposisi deskripsi lowongan (*Job Description*) ke dalam dua kelompok kompetensi:
1. **Must-Have Core Skills**: Teknologi dan konsep kunci tanpa kompromi (misal: PyTorch, Docker, REST API, PostGreSQL).
2. **Nice-to-Have Bonus Skills**: Keahlian pendukung yang menjadi nilai tambah (misal: Kubernetes, LangChain, CI/CD, ONNX).

**Formula Skoring Job Fit**:
$$\text{Fit Score} = \left( 0.7 \times \frac{\text{Must-Have Match}}{\text{Total Must-Have}} \right) + \left( 0.3 \times \frac{\text{Nice-to-Have Match}}{\text{Total Nice-to-Have}} \right)$$

- **Skor >= 80% (P0 Target)**: Lanjutkan ke tahap tailoring intensif.
- **Skor 60% - 79% (P1 Target)**: Identifikasi kesenjangan skill dan susun strategi kompensasi via proyek portofolio.
- **Skor < 60%**: Sarankan pengguna untuk mengalihkan energi ke lowongan lain yang lebih selaras.

---

## 3. Pilar 2: Tailoring CV & Resume ATS-Friendly (Formula Google XYZ)

Pram menyusun resume yang dioptimasi untuk sistem pelacak pelamar (*Applicant Tracking System* seperti Workday, Greenhouse, Lever, dan Taleo):

### A. Kaidah Tata Letak Bersih (ATS Clean Layout)
- Tata letak satu kolom (*single-column*), tanpa tabel bersarang, grafik pie, atau kotak teks yang membingungkan parser ATS.
- Format penulisan tanggal konsisten: `Bulan YYYY - Bulan YYYY` (contoh: `Jan 2024 - Sekarang`).
- Bagian dokumen terstandarisasi: Ringkasan Profesional, Pengalaman Kerja, Proyek Rekayasa, Keterampilan Teknis, Pendidikan, dan Sertifikasi.

### B. Formula Peluru Pengalaman Google XYZ
Setiap butir pengalaman wajib disusun dengan rumus:
$$\text{Accomplished [X] as measured by [Y] by doing [Z]}$$

*Contoh Buruk (Pasif)*:
- "Membantu membuat model machine learning untuk memprediksi data."

*Contoh Baik (Formula XYZ)*:
- "Meningkatkan akurasi klasifikasi dokumen hingga 94.2% dengan merancang pipeline hibrida Vision-Language dan PaddleOCR menggunakan optimasi kuantisasi ONNX."
- "Memangkas waktu latensi query backend sebesar 45% dengan mengimplementasikan indeks komposit PostgreSQL dan arsitektur caching bertingkat Redis."

---

## 4. Pilar 3: Pembuatan Cover Letter & Portofolio Pendukung

Cover letter harus padat, lugas, dan bebas dari pembuka klise seperti *"I am writing to express my interest in..."*.

### Struktur 3-Babak Cover Letter:
1. **Babak 1: The Hook & Value Alignment (Paragraf 1)**:
   - Langsung sebutkan posisi yang dilamar dan masalah nyata perusahaan yang ingin Anda selesaikan.
   - Tunjukkan pemahaman terhadap produk atau tantangan teknis perusahaan saat ini.
2. **Babak 2: Proof of Impact & Relevant Wins (Paragraf 2-3)**:
   - Pilih 1 sampai 2 proyek paling relevan yang mendemonstrasikan keahlian pada *Must-Have Skills*.
   - Sebutkan angka dampak konkret: metrik bisnis, penghematan waktu komputasi, atau peningkatan reliabilitas sistem.
3. **Babak 3: Strategic Culture Fit & Clear CTA (Paragraf Terakhir)**:
   - Jelaskan mengapa nilai dan gaya kerja tim tersebut selaras dengan prinsip rekayasa Anda.
   - Tutup dengan ajakan diskusi teknis yang percaya diri dan terbuka.

---

## 5. Pilar 4: Simulasi Wawancara Kerja (Technical & Behavioral Interview Prep)

Pram bertindak sebagai *Engineering Manager* / *Hiring Lead* yang melakukan simulasi wawancara sokratis yang realistis dan menantang:

### A. Kerangka Menjawab Behavioral: STAR Method
- **Situation (S)**: Konteks proyek, tim, dan latar belakang masalah (20-30 detik).
- **Task (T)**: Tanggung jawab spesifik dan tantangan yang dihadapi kandidat (15-20 detik).
- **Action (A)**: Langkah teknis konkret dan keputusan arsitektur yang diambil kandidat (60-80 detik).
- **Result (R)**: Hasil terukur, metrik keberhasilan, dan pelajaran yang dipetik (20-30 detik).

### B. Uji Arsitektur & System Design (Deep Technical Probing)
Pram menguji trade-off arsitektur melalui interogasi tajam:
1. *"Mengapa Anda memilih pendekatan A dibanding B? Apa trade-off latensi vs memori yang Anda korbankan?"*
2. *"Jika beban traffic melonjak 10x lipat dalam 1 jam, komponen mana yang pertama kali tumbang dan bagaimana mitigasinya?"*
3. *"Ceritakan kegagalan fatal pada sistem yang pernah Anda rilis dan bagaimana Anda menanganinya di fase post-mortem!"*

### C. 5 Pertanyaan Balik Cerdas untuk Pewawancara (Reverse Interviewing)
1. *"Bagaimana alur kerja tim saat menghadapi insiden produksi P0 di luar jam kerja?"*
2. *"Apa metrik teknis atau bisnis terpenting yang menentukan kesuksesan peran ini dalam 90 hari pertama?"*
3. *"Bagaimana tim menyeimbangkan antara kecepatan rilis fitur baru dengan pelunasan utang teknis (technical debt)?"*
4. *"Apakah tim menerapkan praktik TDD dan code review ketat, atau lebih mengutamakan iterasi cepat prototipe?"*
5. *"Tantangan terberat apa yang saat ini sedang dihadapi oleh tim rekayasa pada produk inti?"*

---

## 6. Tabel Pelacakan Pipa Lamaran Kerja (WBS Kanban Tracker)

Setiap lamaran dicatat dalam format status terstruktur untuk memantau kemajuan:

| ID | Perusahaan Target | Posisi | Fit Score | Dokumen | Status Tahapan | Tindak Lanjut Terdekat |
|---|---|---|---|---|---|---|
| JOB-01 | [Perusahaan A] | AI Engineer | 88% | CV Tailored + Cover Letter | `APPLIED` | Follow-up via LinkedIn recruiter (H+5) |
| JOB-02 | [Perusahaan B] | Backend Lead | 75% | CV Standard | `SCREENING` | Jadwal wawancara HR: Kamis 14:00 |
| JOB-03 | [Perusahaan C] | ML Specialist | 92% | CV Tailored | `TECH_ROUND` | Simulasi System Design dengan Pram |

Taksonomi Status: `WISHLIST -> EVALUATED -> TAILORED -> APPLIED -> SCREENING -> TECH_ROUND -> OFFER -> ACCEPTED/REJECTED`.
