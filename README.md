# Hermes ECC Framework

Repositori ini berisi *Skills*, *Plugins*, dan template dasar untuk menjalankan Hermes Agent layaknya arsitektur Enterprise Command Center (ECC).

## Cara Instalasi Untuk User Baru

1. Clone repositori ini ke folder Hermes di lokal:
   ```bash
   git clone https://github.com/Alarave/hermes-ecc-backup.git "C:/Users/<UsernameAnda>/AppData/Local/hermes"
   ```
2. Buka PowerShell di folder tersebut dan jalankan skrip instalasi:
   ```powershell
   cd "C:\Users\<UsernameAnda>\AppData\Local\hermes"
   .\setup.ps1
   ```
3. Buka dan sesuaikan:
   - `config.yaml` (Masukkan API key LLM Anda).
   - `memories/USER.md` (Ubah nama dan profil Anda).
   - `memories/MEMORY.md` (Aturan khusus Anda).

Selamat menggunakan AI Agent yang terotomatisasi penuh!
