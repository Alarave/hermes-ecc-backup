# PANDUAN TEKNIS: INSPEKSI BINER NATIVE & PE WINDOWS
> Prosedur pemeriksaan biner terkompilasi (PE Windows, Go, Rust, ELF) dan integrasi dekompiler native.

---

## 1. Biner Bahasa Go (Go Executables)

Biner yang dikompilasi dengan Go menyertakan metadata tabel modul dan build settings secara statis di dalam segmen biner:
1. **Identifikasi Versi Kompiler**: Biner memuat string versi runtime seperti `go1.22.x`.
2. **Daftar Modul & Dependensi**: Dapat diekstrak menggunakan perintah standar Go jika terpasang (`go version -m biner.exe`) atau melalui parser header REA (`inspect_go_binary`).
3. **Rekonstruksi Simbol**: Walaupun biner di-strip, tabel nama paket dan fungsi sering kali masih dapat dipetakan dari struktur pclntab internal Go.

---

## 2. Biner Bahasa Rust (Rust Executables)

Biner Rust modern yang dikompilasi dengan opsi audit menyimpan dependensi crate di dalam section `.dep-v0`:
1. Metadata memuat nama crate, nomor versi, dan hash repositori crates.io.
2. Identifikasi compiler hash commit rustc sering terdapat di string jalur `/rustc/<commit-hash>/`.

---

## 3. Biner Windows Portable Executable (PE)

Pada sistem operasi Windows, biner berekstensi `.exe` atau `.dll` memuat struktur PE yang kaya:
1. **Import Address Table (IAT)**: Menunjukkan fungsi API Windows apa saja yang dipanggil (contoh: `CryptProtectData`, `CreateFileW`, `RegOpenKeyExW`).
2. **Export Table**: Fungsi publik yang diekspos oleh berkas DLL.
3. **Resource Section (.rsrc)**: Memuat icon, string table, dialog box, dan manifest aplikasi.

---

## 4. Alur Kerja Dekompilasi Lanjut (Ghidra / IDA)

Jika algoritma internal membutuhkan rekonstruksi mendalam hingga tingkat instruksi CPU:
1. **Pilihan Engine**: Prioritaskan Ghidra (open source NSA, membutuhkan Java JDK) atau IDA Pro (jika pengguna memiliki lisensi).
2. **Alur Analisis**:
   - Impor biner dan jalankan Auto-Analysis awal (identifikasi fungsi, call graph, string).
   - Cari string kunci (misal: endpoint URL, pesan error, header autentikasi).
   - Temukan fungsi yang merujuk string tersebut (*Cross-References / Xrefs*).
   - Buka Decompiler View untuk membaca pseudocode representasi C/C++.
