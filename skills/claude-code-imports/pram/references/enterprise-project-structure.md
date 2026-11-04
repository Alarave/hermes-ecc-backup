# Standar Arsitektur Folder Proyek AI & Chatbot (LLMOps & Enterprise Grade)

Sebagai Orchestrator, Anda (Pram) wajib menggunakan struktur folder ini saat menginisialisasi proyek berbasis AI / RAG Chatbot. Struktur ini memadukan **Manajemen Proyek Ketat (PMO)** di dalam `/docs` dan **Siklus Hidup AI (LLMOps)** di dalam `/ai_engine`.

## 1. Pohon Direktori (Directory Tree)

```text
my-ai-project/
├── .github/                  # CI/CD Workflows, Prompt Evaluation Actions
├── docs/                     # 🛡️ ZONA PM & SYSTEM ANALYST (Hak Akses Pram)
│   ├── 01_management/        # Project Charter, Timeline, RAB, NDA
│   ├── 02_requirements/      # PRD (Bisnis & JTBD), SRS (Fungsional EARS, IEEE 830)
│   ├── 03_architecture/      # SDD, ERD, Arsitektur AI (LangChain/LlamaIndex DAG)
│   ├── 04_eval_reports/      # Laporan Evaluasi RAGAS & Metrik Halusinasi AI
│   └── 05_assets/            # Mockup UI Chatbot, Diagram Gambar
├── src/                      # 💻 ZONA REKAYASA PERANGKAT LUNAK (Software Engineering)
│   ├── backend/              # API Gateway, WebSocket/SSE Server (Node.js/Go/FastAPI)
│   ├── frontend/             # Antarmuka Chatbot UI (React/Vue/Svelte)
│   └── shared/               # Tipe data, utilities bersama
├── ai_engine/                # 🧠 ZONA AI & DATA ENGINEER (LLMOps)
│   ├── data/                 # Penyimpanan Data (Di-.gitignore untuk privasi)
│   │   ├── raw/              # PDF Mentah, CSV asli (Sumber Knowledgebase)
│   │   └── processed/        # Chunked text, JSONL untuk vektor
│   ├── notebooks/            # Jupyter Notebooks (Eksperimen, EDA, Chunking Test)
│   │                         # Aturan Mutlak: 1 Notebook Cell = 1 Tugas Atomik!
│   ├── prompts/              # Manajemen Prompt (Pisahkan prompt dari hardcode backend!)
│   │   ├── system_prompts/   # Instruksi Sistem Utama
│   │   └── few_shot_examples/# Contoh QA untuk grounding model
│   ├── retrievers/           # Logika integrasi Vector Database (Chroma/Supabase pgvector)
│   └── eval/                 # Skrip Evaluasi Model (RAGAS, Groundedness test)
├── tests/                    # Pengujian Perangkat Lunak (Unit Test Backend/Frontend, E2E)
├── scripts/                  # Otomasi (Seeding Vektor DB, Build Docker, Scraping)
├── .env.example              # Template Environment Variables (OPENAI_API_KEY, dll)
├── .gitignore                # Pengecualian Git (node_modules, /data, /models, .env)
└── README.md                 # Entry point dokumentasi untuk tim engineer
```

## 2. Aturan Operasi & Kepatuhan Proyek
1. **Pemisahan Logika AI & Backend**: Prompt **TIDAK BOLEH** di-*hardcode* di dalam kode `src/backend`. Semua instruksi LLM harus berupa file `.md` atau `.txt` yang tersimpan di dalam folder `ai_engine/prompts/`. Ini agar System Analyst dapat mengubah instruksi AI tanpa harus mengerti kode backend.
2. **Aturan Notebooks AI**: DILARANG membuat Jupyter Notebook berantakan (*spaghetti code*). Setiap sel harus atomik dan ditujukan hanya untuk eksperimen (*chunking*, koneksi DB, cek kualitas OCR). Jika sudah matang, pindahkan ke *script* Python di `ai_engine/retrievers/`.
3. **Data Privacy**: Folder `ai_engine/data/raw/` dan `.env` mutlak harus dimasukkan ke `.gitignore` pada inisialisasi pertama untuk menghindari kebocoran data klien.
