# Business Understanding untuk Proyek LLM & Chatbot (Berdasarkan Literatur 2024-2025)

File ini merangkum *state-of-the-art* penggunaan *Large Language Models* (LLM) dan Chatbot di ranah bisnis, dipetakan secara spesifik ke dalam Fase 1 metodologi **CRISP-DM** (*Business Understanding*). Gunakan dokumen ini sebagai landasan penyusunan PRD, analisis proyek, dan perancangan *Agile Charter* yang tidak *ngawang*.

## 1. Referensi Jurnal Terkini (2024 - 2025)

1. **Musazade, N. (2024)** - *"Exploring the Performance of Large Language Models for Data Analysis Tasks Through the CRISP-DM Framework"*.
   - **Insight**: Menguji model LLM (seperti GPT) pada 6 fase CRISP-DM. Fase *Business Understanding* adalah langkah vital di mana LLM menerjemahkan tujuan organisasi menjadi kriteria teknis.
2. **Lähde, M. (2025)** - *"A Proposal for a Method to Systematically Integrate LLMs into Data Analytics"*.
   - **Insight**: Menyediakan metodologi untuk mengintegrasikan LLM ke dalam analitik data korporat (CRISP-DM). LLM tidak hanya dievaluasi pada kode, tapi pemahaman proses bisnis (parsing tabel kompleks, sintesis data bisnis).
3. **Universitas Leiden (2024)** - *"Using LLMs to extract key information from Dutch IT Assessments"*.
   - **Insight**: Implementasi *text-mining* LLM berbasis CRISP-DM. Menggunakan model *state-of-the-art* (Claude-3.5, GPT-4o) dengan penekanan pada akurasi *Business Understanding* saat mengekstrak regulasi pemerintah.
4. **Copenhagen Business School (2024)** - *"Distilling Intelligence of Large Language Models in Business Applications"*.
   - **Insight**: Meneliti biaya komputasi dan ROI lingkungan (*Knowledge Distillation*). Mengajarkan bahwa *Business Understanding* AI tidak hanya soal performa, tapi efisiensi *resource* di tingkat perusahaan.
5. **Universidade do Porto (2024)** - *"Application of AI in Information Extraction for Small Business"*.
   - **Insight**: Modifikasi CRISP-DM khusus untuk UMKM (SME) yang menerapkan NLP/LLM, di mana keterlibatan *stakeholder* di fase awal (Business Understanding) adalah penentu utama agar model *DistilBERT* tidak salah sasaran.

---

## 2. Fase "Business Understanding" untuk Proyek AI/Chatbot
Sebagai PM / Orchestrator, Anda TIDAK BOLEH langsung menyuruh spesialis untuk koding RAG. Anda wajib menanyakan dan mendefinisikan 4 pilar *Business Understanding* berikut:

### A. Penentuan Tujuan Bisnis (Business Objectives)
- Apa *pain point* utamanya? (Misal: CS lambat membalas, dokumen berantakan, biaya operasional tinggi).
- Apa metrik keberhasilannya (KPI)? (Contoh: Waktu respons turun dari 24 jam jadi 3 detik, *Cost-per-query* di bawah Rp 50).
- Apakah LLM adalah solusi yang tepat, atau *rule-based* biasa sudah cukup?

### B. Asesmen Situasi Bisnis (Assess Situation)
- **Sumber Daya & Data**: Apakah data untuk *knowledgebase* RAG sudah ada? Bersih atau kotor? Ada privasi data (PII) yang rentan bocor?
- **Batasan Komputasi**: Apakah bisnis mampu membayar API GPT-4/Claude-3.5, atau butuh LLM lokal skala kecil (Llama-3 8B) demi *Cost Efficiency* seperti diusulkan studi CBS (2024)?

### C. Penerjemahan ke Tujuan Data/AI (Data Mining Goals)
Tujuan bisnis harus diterjemahkan menjadi tujuan mesin.
- *Contoh Bisnis*: "Bantu staf penjualan jualan mobil."
- *Terjemahan AI*: "Membangun *vector database* spesifikasi mobil, menggunakan Cosine Similarity untuk pencarian katalog, dan membatasi (*guardrails*) agar bot tidak halusinasi menyebutkan merek kompetitor."

### D. Perancangan Rencana Proyek (Project Plan)
Membuat matriks tugas WBS (*Work Breakdown Structure*) berdasarkan alur AI:
1. Pengumpulan dataset (*Data Engineer*).
2. Pembersihan & *Embedding* (*ML Engineer*).
3. Pembuatan API & *Backend* RAG (*Backend Engineer*).
4. Pembuatan UI Chatbot (*Frontend Engineer*).
5. Pengujian LLM & Prompt Injection (*Security QA*).

**Pesan untuk Pram**: Gunakan matriks ini untuk memastikan Anda *Orchestrator* terbaik. Kalau *Business Understanding* belum selesai, TOLAK permintaan masuk ke tahap Koding.
