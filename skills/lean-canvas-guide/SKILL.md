---
name: lean-canvas-guide
description: Use when creating Lean Canvas or Business Model Canvas.
---

# Lean Canvas & Business Model Canvas Guide

Panduan merancang dan memvisualisasikan Lean Canvas serta Business Model Canvas (BMC) bebas dari AI-slop, berbasis data riil produk/SRS, dan siap eksekusi.

## 1. Prosedur Penyusunan Kanvas

1. **Ekstraksi Data Dokumen**:
   - Tarik data langsung dari PRD, SRS, atau Project Charter proyek yang aktif.
   - Identifikasi batasan teknis, target pengguna, dan struktur biaya riil.

2. **Aturan Redaksi Bebas AI-Slop (Human-Grounded)**:
   - **Problem**: Gunakan mata uang lokal riil (misal IDR/Rupiah, sebutkan angka konkret seperti langganan Rp 349.000/bulan) dan friksi lapangan nyata (okupansi meja lama dengan transaksi minim). Hindari frasa terjemahan kaku seperti "komitmen langganan" atau "akses instan".
   - **Solution & Unfair Advantage**: Tuliskan fungsi dalam bahasa operasional sehari-hari (contoh: "kode akses dicetak langsung di struk", "pemrosesan berkas di laptop pembeli"), bukan jargon teknis mentah (seperti "Zero-Server-Compute" atau "Pessimistic Row-Level Locking").
   - **Unique Value Proposition (UVP)**:
     - Wajib berupa **KALIMAT AKTIF** deklaratif (subjek pelaku melakukan tindakan nyata, contoh: *Pengunjung mengakses AI sekelas ChatGPT langsung lewat kode struk kasir dengan bayar tunai...*).
     - **DILARANG MENGGUNAKAN TANDA PETIK (`""`)**.
     - DILARANG mencantumkan nomor regulasi/standar ISO pada UVP konsumen.
   - **Action Items & Point Person**: Wajib menugaskan ke nama anggota tim riil (contoh: Firman, Zikri, Rahil), bukan jabatan generik AI (*Backend Lead*, *Frontend Lead*). Tuliskan tugas teknis praktis sehari-hari.

3. **Visualisasi Papan (Board Generation)**:
   - Buat berkas HTML mandiri (`docs/<nama>-canvas.html`) dengan struktur grid 5 kolom atas, baris tengah metrik/saluran, dan baris bawah biaya/pendapatan.
   - Gunakan palet warna ala Miro/Canva (header ungu, latar lavender, sub-kotak hijau muda, kartu sticky notes ungu/kuning/putih).
   - Render tangkapan layar resolusi tinggi via Google Chrome headless:
     `"/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --user-data-dir="$TMPDIR/chrome-headless-profile" --window-size=1860,1120 --hide-scrollbars --screenshot="docs/<nama>-canvas.png" "file:///path/to/<nama>-canvas.html"`
   - Sajikan tangkapan layar di chat via `MEDIA:<path_ke_file.png>`.
