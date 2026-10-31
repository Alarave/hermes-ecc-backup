---
name: anti-parenthesis-slop
description: "Use when editing or refining Indonesian academic prose."
---

# Anti-Parenthesis Slop & Single-Term Selection Rule

## R (Role & Purpose)
Aturan penulisan ilmiah bahasa Indonesia baku untuk mengeliminasi residu kebiasaan AI yang gemar membuka tanda kurung secara berlebihan dan menjejerkan istilah ganda.

## C (Context & Pitfall Utama)
- **Penyakit Naif Penghapusan Kurung**: Ketika model AI diinstruksikan menghapus tanda kurung, model kerap hanya membuang karakter `(` dan `)` tetapi membiarkan kedua kata yang bertumpuk makna tetap berdampingan (contoh rusak: `kelapa sawit Elaeis guineensis`, `kotak pembatas bounding box`, `buah kecil spikelet`).
- **Prinsip Seleksi Tunggal (Single-Term Selection)**:
  1. DILARANG KERAS menjejerkan dua istilah yang maknanya sama, baik dengan kurung maupun tanpa kurung.
  2. Pilih salah satu secara tegas:
     - Gunakan istilah teknis universal langsung dalam cetak miring (*bounding box*, *backbone*, *region proposal*, *real-time*, *deep learning*, *anchor-free*, *frames per second* / FPS) tanpa embel-embel padanan Indonesia di depannya.
     - ATAU gunakan istilah bahasa Indonesia murni tanpa istilah asing di sampingnya (kotak pembatas, brondolan, rendemen minyak, stasiun sortasi).
     - Jangan menyandingkan nama ilmiah Latin jika nama komoditasnya sudah baku (tulis 'kelapa sawit', bukan 'kelapa sawit Elaeis guineensis').
  3. Tanda kurung HANYA sah untuk:
     - Tahun sitasi: `(Ramadhani dkk., 2026)` atau `Lai dkk. (2023)`.
     - Singkatan akronim saat pertama kali didefinisikan: `Tandan Buah Segar (TBS)` atau `Free Fatty Acid (FFA)`.
     - Nilai persentase/kadar: `(di atas 20%)` atau `(5%)`.
     - Penomoran persamaan matematika: `Persamaan (2.1)`.
     - Koordinat dan notasi matematika: $[x_c, y_c, w, h]$.
  4. Kepadatan tanda kurung wajib ditekan hingga di bawah 5 sampai 7 pasang per 1.000 kata.
- **Standar Penamaan Judul Tabel dan Gambar (Korpus UPNVJ & Gunadarma)**:
  1. Penomoran tabel dan gambar menggunakan format `Tabel X.Y Judul Tabel` dan `Gambar X.Y Judul Gambar` tanpa titik setelah nomor sub-bab (DILARANG `Tabel X.Y.` atau `Gambar X.Y.`).
  2. DILARANG KERAS membubuhkan tanda kurung istilah asing pada judul tabel dan gambar (contoh salah AI slop: `Tabel 2.3. Matriks Perbandingan Penelitian Terdahulu (State-of-the-Art)`).
  3. Gunakan judul yang singkat, padat, dan lugas sesuai korpus riil UPNVJ (contoh baku: `Tabel 2.1 Kajian Pustaka`, `Tabel 2.3 Penelitian Terdahulu`, `Tabel 2.1 Dekomposisi Variabel Faster R-CNN`, `Tabel 4.1 Jadwal Pelaksanaan Penelitian`).
  4. Posisi caption: judul tabel di atas tabel, judul gambar di bawah gambar.

- **Prosedur Baku Perapihan Bab 2 (Tinjauan Pustaka)**:
  1. *Audit Istilah Bertumpuk*: Telusuri teks untuk menemukan jejeran kata ganda padanan (seperti *buah spikel*, *lapisan mesokarp daging buah*, *grader petugas sortasi*). Ganti menjadi satu istilah tunggal yang baku dan presisi.
  2. *Audit Kurung Liar*: Buang seluruh tanda kurung terjemahan bahasa Inggris pada nama fraksi atau istilah umum (misal ubah `Mentah (*Unripe*)` menjadi `Mentah`). Sisakan kurung hanya untuk tahun sitasi, akronim awal, dan nomor persamaan.
  3. *Penegakan First-Mention Sitasi*: Untuk 3 sampai 5 penulis, pemunculan pertama sebutkan seluruh nama belakang disambung kata 'dan' (misal `Ramadhani, Dewanta, dan Gunawan, 2026`). Pemunculan kedua dan seterusnya gunakan `dkk.`
  4. *Verifikasi Kuantitatif Jurnal*: Pastikan seluruh angka akurasi, mAP, FPS, dan parameter model di tabel penelitian terdahulu diverifikasi langsung dari berkas asli jurnal rujukan (zero hallucination).
  5. *Sinkronisasi Multi-Format*: Jika proyek mengelola dokumen multi-format, lakukan patch langsung pada file teks master (`.md`), selaraskan pada naskah layout (`.typ` dikompilasi ke `.pdf`), dan simpan pembaruan pada berkas Word (`.docx`) secara in-place via WordCraft MCP.

## O (Definition of Done)
Naskah mengalir dingin, lugas, alami, dan bebas dari kejanggalan kata bertumpuk maupun residu kurung AI. Seluruh format tabel, sitasi, dan formula sinkron lintas format dokumen.
