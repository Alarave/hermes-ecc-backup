# Blueprint Skripsi Gunadarma: Pengembangan Sistem AI/RAG & Chatbot

Panduan mutlak untuk format penulisan akademik (Tugas Akhir/Skripsi) mahasiswa Sistem Informasi / Informatika Universitas Gunadarma, dianalisis dari referensi e-paper: *"PENGEMBANGAN SISTEM INFORMASI SHOWROOM MOBIL BERBASIS WEB DENGAN CHATBOT BERBASIS RETRIEVAL-AUGMENTED GENERATION UNTUK LAYANAN INFORMASI KENDARAAN" (M. Hafizh Naufal, 2026)*.

## 1. Sistematika Penulisan Baku (Heading Numerik Arab)
Gunadarma TIDAK menggunakan format "BAB I" melainkan format *numerik bergradasi* (Contoh: `1. PENDAHULUAN`, `1.1. Latar Belakang`). Sub-bab tidak menggunakan huruf Romawi.

- **1. PENDAHULUAN**
  - **1.1. Latar Belakang** (Dimulai dengan lanskap digital makro, lalu mengerucut ke masalah teknis institusi, lalu usulan solusi teknologi & justifikasinya).
  - **1.2. Ruang Lingkup** (*Catatan: Gunadarma menggunakan istilah "Ruang Lingkup", bukan "Batasan Masalah"*).
  - **1.3. Tujuan Penelitian**
  - **1.4. Sistematika Penulisan** (Berupa paragraf naratif yang menjelaskan isi setiap Bab dari 1 sampai 5).

- **2. LANDASAN TEORI**
  - Konsep sistem, LLM, RAG, *Vector Database*, *Embedding*, Algoritma Kemiripan (*Cosine Similarity*), Framework (React.js, Express.js), Database (PostgreSQL, Supabase), Gemini, Metrik Evaluasi RAGAS, dan Penelitian Terdahulu.

- **3. METODOLOGI PENELITIAN**
  - WAJIB menggunakan kerangka kerja spesifik. Untuk proyek AI/Data, gunakan **CRISP-DM (Cross Industry Standard Process for Data Mining)**:
    1. *Business Understanding*
    2. *Data Understanding*
    3. *Data Preparation*
    4. *Modeling* (Pembentukan *knowledgebase*, *embedding*, *query normalization*, *retrieval*, *augmentation*, *generation*, dan arsitektur sistem)
    5. *Evaluation*
    6. *Deployment*

- **4. HASIL DAN PEMBAHASAN**
  - Implementasi Antarmuka (*Frontend*) & *Backend*.
  - Implementasi Basis Data & Chatbot AI.
  - Hasil Evaluasi/Pengujian menggunakan RAGAS (*Retrieval-Augmented Generation Assessment*).
  - *Black-box testing* untuk fungsi-fungsi utama sistem.

- **5. PENUTUP**
  - Kesimpulan.
  - Saran.

## 2. Poin Penting dalam `1.2. Ruang Lingkup`
Dalam proyek berbasis AI Chatbot / RAG, Ruang Lingkup harus dirincikan dalam format daftar angka yang menyebutkan secara vulgar:
1. Objek penelitian (Contoh: Chatbot RAG terintegrasi web).
2. Sumber dataset awal (Kaggle) dan sumber data dinamis (Knowledgebase Admin).
3. Batasan informasi (Atribut data spesifik yang bisa dijawab chatbot).
4. Alur proses pencarian (*Query Normalization*, *Embedding*, pencarian dokumen via PostgreSQL `pgvector`, dan *Cosine Similarity*).
5. Model yang digunakan (Contoh: *Gemini Embedding* untuk vektor, *Gemini LLM* untuk generator teks).
6. Tumpukan teknologi (*Tech Stack*: React.js, Express.js, Supabase).
7. Pengecualian mutlak: "Penelitian ini TIDAK membahas proses pelatihan (fine-tuning) LLM..."
8. Batas metrik evaluasi: Akurasi jawaban chatbot diukur menggunakan metrik RAGAS dan fungsionalitas diukur via *Black-Box Testing*.

## 3. Gaya Bahasa Anti-Slop (Lugas, EYD V, KBBI)
- Menggunakan kalimat pasif objektif ("Model Gemini digunakan sebagai...", "Penelitian difokuskan pada...").
- JANGAN PERNAH gunakan kalimat tanya retoris di dalam paragraf ("Lantas, bagaimana cara sistem bekerja?").
- Istilah serapan dicetak miring (*italic*): *Chatbot, Retrieval-Augmented Generation, frontend, backend, knowledgebase, vector database*.
