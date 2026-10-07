---
name: workspace-repo-template
description: "Prosedur pembersihan PII dan template repo workspace."
---

# Prosedur Pembersihan PII & Pembuatan Template Workspace

Gunakan panduan ini saat membagikan atau mem-backup workspace ke Git publik atau tim lain untuk mencegah kebocoran informasi pribadi (PII), kredensial, dan jadwal tugas otomatis.

## 1. File Sensitif Wajib Anonymize
- `config.yaml`, `profile.yaml`: Berisi API Key dan endpoint internal.
- `memories/USER.md`, `memories/MEMORY.md`: Berisi identitas, kontak, dan preferensi kerja user.
- `cron/`: Berisi target delivery (misalnya nomor WhatsApp/LID) dan riwayat tugas.
- `.env`, `auth.json`: Berisi token rahasia.

## 2. Prosedur Anonymization (Clean Slate Git History)
Jika file sensitif pernah ter-commit, menghapus file di commit baru tidak menghapus data dari `git log`. Riwayat commit lama wajib dihancurkan.

```bash
# 1. Buat versi .example
cp config.yaml config.example.yaml
cp profile.yaml profile.example.yaml

# 2. Siapkan template placeholder netral
mkdir -p memories-template cron-template
# Isi USER.example.md dan MEMORY.example.md dengan placeholder [Nama], [Role]
# Isi jobs.example.json dengan job nonaktif (enabled: false)

# 3. Update .gitignore untuk ignore file asli & include template
# Pastikan config.yaml, profile.yaml, memories/, cron/ diabaikan

# 4. Hancurkan riwayat lama menggunakan orphan branch
git checkout --orphan clean_branch
git add .
git commit -m "inisialisasi: rilis template repo bersih"
git branch -D main
git branch -m main
git push -f origin main
```

## 3. Otomasi Pengguna Baru
Sediakan `setup.ps1` untuk menyalin template `.example` ke konfigurasi aktif saat pengguna pertama kali clone:
```powershell
if (-Not (Test-Path "config.yaml")) { Copy-Item "config.example.yaml" "config.yaml" }
if (-Not (Test-Path "memories")) {
    New-Item -ItemType Directory -Force -Path "memories"
    Copy-Item "memories-template/USER.example.md" "memories/USER.md"
}
```
