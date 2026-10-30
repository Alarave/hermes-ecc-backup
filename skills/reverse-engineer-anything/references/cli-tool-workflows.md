# PANDUAN TEKNIS: ALUR KERJA CLI & ISOLASI BUKTI
> Tata cara pengoperasian utilitas CLI eksternal rea-agents secara deterministik dan aman untuk konteks agen AI.

---

## 1. Prinsip Isolasi Berkas Bukti (Evidence File Redirection)

Keluaran analisis biner atau aplikasi JavaScript dapat berukuran puluhan hingga ratusan megabyte jika mencakup ribuan modul. Memuat luaran ini secara langsung ke context window percakapan akan menghabiskan token budget dan memperlambat penalaran agen.

Aturan wajib:
1. Selalu alihkan luaran CLI ke berkas JSON lokal.
2. Gunakan mode ringkasan (`summary`) sebelum meminta detail per modul.
3. Gunakan filter jq atau skrip Python lokal untuk membaca bagian yang spesifik.

---

## 2. Perintah CLI Standar REA (npx rea-agents)

Berikut adalah perintah CLI yang dapat dijalankan secara mandiri pada host Windows:

### A. Analisis Aplikasi JavaScript / ASAR
```bash
# Analisis direktori aplikasi atau ASAR dan simpan bukti ke file
npx -y rea-agents@latest analyze-javascript-application "C:/jalur/ke/app" --json > cache/scratch/app-evidence.json

# Buat berkas tampilan ringkasan
node -e "const data = require('./cache/scratch/app-evidence.json'); console.log(JSON.stringify({source: {kind: 'inline', evidence: data}, view: {kind: 'summary'}}));" > cache/scratch/app-view.json

# Tampilkan ringkasan modul
npx -y rea-agents@latest inspect-analysis-view cache/scratch/app-view.json
```

### B. Inspeksi Biner Go
```bash
npx -y rea-agents@latest inspect-go-binary "C:/jalur/ke/target.exe" --json > cache/scratch/go-metadata.json
```

### C. Inspeksi Biner Rust
```bash
npx -y rea-agents@latest inspect-rust-binary "C:/jalur/ke/target.exe" --json > cache/scratch/rust-metadata.json
```

---

## 3. Fallback Tanpa Alat Eksternal

Jika paket npm tidak dapat diunduh (misal: koneksi offline atau pembatasan firewall):
1. **ASAR**: Gunakan Python untuk membaca header JSON pada berkas ASAR (header ASAR adalah JSON biner sederhana di awal berkas).
2. **Strings**: Jalankan skrip Python ringkas untuk mengekstrak string ASCII/UTF-16 dari berkas biner.
3. **PE Header**: Gunakan pustaka Python bawaan atau skrip inspeksi struct PE lokal.
