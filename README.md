# ⚡ Hermes ECC (Enterprise Command Center)
> **The All-in-One Multi-Agent Orchestration & Skill Framework**  
> *Kompatibel penuh dengan Hermes Agent, Antigravity CLI, dan Gemini CLI.*

Repositori ini adalah sistem otak AI terpadu (Enterprise Command Center) yang mengadopsi metodologi *Superpowers* dan *Meta-Skills*. Dilengkapi dengan peran agen spesialis yang terstruktur (Orchestrator, Research Akademik, Arsitek UI, Backend, Frontend, hingga Trading).

---

## 🚀 One-Click Install (Plug-and-Play)
Cukup buka **PowerShell** di Windows Anda dan jalankan perintah satu baris ini:

```powershell
irm https://raw.githubusercontent.com/Alarave/hermes-ecc-backup/main/install.ps1 | iex
```

### 🛠️ Apa yang Dilakukan Skrip Ini Secara Otomatis?
1. **Clone & Sinkronisasi Repo**: Mengunduh seluruh pustaka ke direktori `%LOCALAPPDATA%\hermes-ecc`.
2. **Penyambungan ke Hermes Agent**: Membuat *directory junction* (symlink) dari semua folder `skills/` langsung ke Hermes, sehingga penambahan fitur baru langsung aktif tanpa install ulang.
3. **Injeksi ke Antigravity / Gemini CLI**: Menjalankan konversi otomatis agar aturan dan meta-skill dikenali oleh Antigravity CLI (`~/.gemini/config/rules/`).
4. **Keamanan Data Terjamin**: Konfigurasi pribadi, memori profil, kredensial, dan API Key tidak akan bocor karena menggunakan sistem *template*.

---

## 🧠 Daftar Meta-Skills Utama

| Skill | Role / Deskripsi | Standar Metodologi |
| :--- | :--- | :--- |
| **`pram`** | **Chief AI Orchestrator & PM** | WBS, DAG Dependency Gating, Trinitas Dokumen (PRD, Charter, SRS), Anti-Bego Verification Protocol. |
| **`dazai`** | **Spesialis Riset Akademik** | Literature Review, Piramida Terbalik (Bab I), Audit DOI, Penulisan LaTeX/Typst, 1 Task 1 Cell Notebook. |
| **`spesialis-ui-templates`** | **Arsitek Design System & UI** | 50+ Referensi Brand Dunia (Stripe, Linear, Apple), Design Tokens, Anti-UI Generik. |
| **`spesialis-frontend`** | **Senior Frontend Engineer** | Next.js, React, Tailwind, Micro-animations, Aksesibilitas (WCAG/a11y). |
| **`spesialis-backend`** | **Backend & Systems Architect** | API Contract, Database Indexing, Unit Testing wajib (Anti-Mocking). |
| **`trading-agent`** | **Algo & Quantitative Trading** | Analisis tren, sintesis sinyal pasar, mitigasi risiko keuangan. |

---

## 📖 Cara Pemakaian Cepat

### 1. Di Hermes Desktop
Setelah instalasi selesai, cukup panggil agen yang Anda butuhkan di kolom chat:
- *"Pram, rancang spesifikasi dan arsitektur aplikasi e-commerce baru."*
- *"Dazai, cari celah penelitian dari jurnal-jurnal metode LSTM terbaru."*
- *"Buatkan antarmuka dashboard admin dengan tema ala Stripe."*

### 2. Di Antigravity / Gemini CLI
Buka terminal dan gunakan *command* biasa. Aturan dari skill-skill di atas sudah otomatis terinjeksi ke dalam memori CLI:
```bash
agy "Analisis bug autentikasi ini menggunakan standar spesialis-backend"
```

---

## 🔄 Pembaruan (Update)
Jika ada pembaruan skill di repositori ini, Anda cukup menjalankan perintah install satu baris di atas kembali, atau masuk ke folder dan lakukan:
```powershell
cd $env:LOCALAPPDATA\hermes-ecc
git pull origin main
python sync_skills.py
```

Selamat berkarya dengan AI yang terotomatisasi penuh!
