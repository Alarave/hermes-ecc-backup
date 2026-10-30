# PANDUAN TEKNIS: ANALISIS APLIKASI JAVASCRIPT & ELECTRON (ASAR)
> Standar operasional untuk membongkar, membaca struktur modul, dan menelusuri boundary IPC aplikasi desktop berbasis Electron dan Node.js.

---

## 1. Anatomi Aplikasi Electron

Aplikasi Electron umumnya dikemas dalam arsip ASAR (`app.asar`) yang memuat hierarki berkas terstruktur:
1. `package.json`: Manifest utama berisi entrypoint berkas `main` (proses utama), dependencies, dan script.
2. `main.js`: Proses utama Node.js yang mengontrol siklus hidup jendela aplikasi (`BrowserWindow`), menu native, dan handler IPC (`ipcMain.handle`, `ipcMain.on`).
3. `preload.js`: Jembatan konteks (`contextBridge.exposeInMainWorld`) yang mengekspos API aman dari proses utama ke proses renderer.
4. `renderer/`: Antarmuka visual berbasis web (HTML, CSS, Webpack/Vite bundles) yang memanggil API via `ipcRenderer.invoke` atau objek `window.electronAPI`.

---

## 2. Langkah Pembongkaran & Ekstraksi ASAR

Jika arsip ASAR belum diekstrak, gunakan modul npx asar standar:

```bash
# Ekstraksi arsip ASAR ke folder kerja
npx --yes asar extract /jalur/ke/app.asar ./extracted-app

# Inspeksi daftar berkas dalam arsip tanpa ekstraksi penuh
npx --yes asar list /jalur/ke/app.asar > asar-files.txt
```

---

## 3. Penelusuran Alur Fitur (Feature Tracing)

Untuk menelusuri fitur tertentu (misal: mekanisme enkripsi lokal atau sinkronisasi data):
1. **Titik Awal (Renderer)**: Cari teks antarmuka atau tombol aksi di bundle renderer untuk menemukan event handler yang dipanggil pengguna.
2. **Jembatan (Preload & IPC Channels)**: Cari nama saluran IPC (contoh: `app:save-data`, `vault:decrypt`) pada berkas preload.js.
3. **Logika Inti (Main Process)**: Cari handler saluran tersebut di `main.js` atau modul pendukung di proses utama (`ipcMain.handle('app:save-data', ...)`).
4. **Isolasi Logika Bisnis**: Ambil algoritma atau alur data murni, lalu rancang ulang implementasi serupa yang bersih (clean-room design) tanpa menyalin kode berhak cipta secara ilegal.
