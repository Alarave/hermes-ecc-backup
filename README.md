# ⚡ Agent Harness OS (Hermes ECC)
> **Sistem Operasi Multi-Agen, Orkestrasi WBS DAG, dan Gudang Skill Berstandar RCCO.**  
> *Kompatibel lintas toolchains: Hermes Desktop, Claude Code, Codex CLI, Kiro, dan Gemini / Antigravity CLI.*

---

## 🔒 Catatan Akses Repositori (Private Repo)
Repositori ini bersifat **Private**. Sebelum teman atau anggota tim Anda dapat menginstal atau memperbarui skill, pastikan Anda telah memberikan akses kolaborator:
1. Buka repositori di GitHub: `Settings` -> `Collaborators` -> `Add people`.
2. Masukkan username atau email GitHub teman Anda.
3. Setelah mereka menerima undangan kolaborasi, mereka dapat langsung menginstal repositori menggunakan instruksi di bawah.

---

## 🚀 Panduan Instalasi (Untuk Teman / Device Baru)

### A. Windows (PowerShell)
Buka PowerShell, lalu jalankan perintah berikut:

```powershell
# 1. Clone repositori ke komputer lokal
git clone https://github.com/Alarave/hermes-ecc-backup.git "$env:LOCALAPPDATA\hermes-ecc"

# 2. Masuk ke direktori dan jalankan setup otomatis
cd "$env:LOCALAPPDATA\hermes-ecc"
.\setup.ps1
```

> **Apa yang dilakukan `setup.ps1` secara otomatis?**
> - Menginisialisasi konfigurasi profil tanpa menimpa data kredensial.
> - Membuat *directory junction (symlink)* global ke `.hermes`, `.claude`, `.codex`, `.kiro`, dan `.gemini\antigravity`.
> - Menginjeksi aturan ke Antigravity / Gemini CLI (`~/.gemini/config/rules/`).

---

### B. Linux & macOS (Bash)
Buka terminal:

```bash
# 1. Clone repositori
git clone https://github.com/Alarave/hermes-ecc-backup.git "$HOME/.hermes-ecc"

# 2. Masuk direktori dan jalankan script update
cd "$HOME/.hermes-ecc"
chmod +x update_skills.sh
./update_skills.sh
```

---

## 🔄 Cara Memperbarui Skill (Auto-Update 1-Klik)

Setiap kali ada pembaruan skill baru di repositori ini, teman Anda tidak perlu instalasi ulang. Cukup jalankan:

### Di Windows (PowerShell):
```powershell
cd "$env:LOCALAPPDATA\hermes-ecc"
.\update_skills.ps1
```

### Di Linux / macOS (Bash):
```bash
cd "$HOME/.hermes-ecc"
./update_skills.sh
```

---

## 🧬 Berbagi Pengalaman & Evolusi Kolektif (Team Instincts)

Ketika teman Anda menyelesaikan masalah rumit atau menemukan trik baru di komputernya, mereka bisa langsung membagikannya ke repositori bersama dalam 1 perintah:

```bash
python scripts/share_experience.py "Pola baru optimasi query PostgreSQL"
```

Skrip ini otomatis:
1. Membuat file pengalaman terisolasi di `instincts/shared/<nama_user>/`.
2. Menyensor kredensial dan path lokal secara otomatis.
3. Melakukan git commit dan push ke repositori tim.

Saat Anda menjalankan `.\update_skills.ps1`, AI Anda akan mendeteksi pengalaman tersebut dan menyerap ilmunya secara otomatis!

Skrip ini akan otomatis:
1. Menarik commit terbaru via `git pull origin main`.
2. Menyinkronkan seluruh skill ke memori lokal Antigravity CLI.
3. Memverifikasi seluruh tautan symlink global agar selalu terhubung.

---

## 🧠 Daftar Komando & Spesialis Utama

| Agen / Skill | Peran Utama | Standar Metodologi |
| :--- | :--- | :--- |
| **`pram-orchestrator`** | **Chief AI Orchestrator & TPM** | Sistem RCCO, WBS DAG Engine, Quality Gate G0-G4, Dual Audit Seal, Frozen Contracts, Postmortem SRE, dan Zero Cognitive Load. |
| **`spesialis-data-ai-agentic`** | **Principal Data & MLOps Engineer** | Pipeline DAG, Great Expectations Quality Gate, Parquet/Arrow, DVC Data Lineage, Hybrid Search RAG + Reranker. |
| **`spesialis-research-akademik`** | **Peneliti Akademik (Q1/Q2)** | Protokol PRISMA, Falsifiability Popper, Template Bab 1-5 Skripsi, Sitasi Markdown Keys `[@citekey]`, Anti-Slop Writing. |
| **`academic-note-coach`** / **`note`** | **Tutor 0-ke-100 & Zettelkasten** | Pedagogi 0-100, Analogi Dunia Nyata, LaTeX + Simulasi Hitungan Manual, Mermaid Mindmap, Collapsible Active Recall `> [!question]-`. |
| **`ceemdan-lstm-forecasting`** | **Time-Series Deep Learning** | Anti-Leakage Split (Train-first), Sample Entropy Grouping, Bi-LSTM, Huber Loss, Validasi Diebold-Mariano vs Naive Baseline. |
| **`spesialis-product-bisnis`** | **Product Lead & Strategist** | PRD FAANG (Rubrik 0-40), RICE Scoring, Incident Postmortem, Executive RAG Updates, Competitive Parity Matrix. |

---

## 💬 Cara Memanggil Agen (Zero Cognitive Load)

Tidak perlu menghafal nama file atau perintah slash command. Cukup ketik maksud Anda di kolom chat:
- *"Pram, rancang arsitektur dan timeline WBS untuk aplikasi baru ini."*
- *"Pram, bantu tuliskan Bab 1 Pendahuluan untuk skripsi saya."*
- *"Bikin catatan belajar materi Machine Learning ini dari level 0 sampai 100 ke Obsidian."*
- *"Prediksi time series saham ini menggunakan CEEMDAN-LSTM."*
- *"Bikinin PRD dan analisis kompetitor untuk fitur baru."*

---

## 🛡️ Kebijakan Privasi & Kontribusi (Zero Leakage)
- Dilarang keras melakukan hardcode path komputer pribadi. Selalu gunakan format variabel dinamis:  
  `${OBSIDIAN_VAULT_PATH:-~/notes}`.
- Seluruh kredensial sensitif wajib disamarkan menjadi `[REDACTED]`.
- Pesan Git commit wajib berbahasa Indonesia terstruktur: `fitur:`, `perbaikan:`, `dokumen:`, `rapihan:`, `koreografi:`.
