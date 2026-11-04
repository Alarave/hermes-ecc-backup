---
name: anti-parenthesis-slop
description: "Use when editing or refining Indonesian academic prose. Eliminates redundant bilingual parentheses, double-term slop, and bloated subheadings."
---

# Anti-Parenthesis Slop & Single-Term Selection Rule

## R (Role & Purpose)
Aturan penulisan ilmiah bahasa Indonesia baku untuk mengeliminasi residu kebiasaan AI yang gemar membuka tanda kurung secara berlebihan, menjejerkan istilah ganda, dan menulis judul sub-bab bertele-tele.

## C (Context & Pitfall Utama)
- **Penyakit Naif Penghapusan Kurung**: Ketika model AI diinstruksikan menghapus tanda kurung, model kerap hanya membuang karakter `(` dan `)` tetapi membiarkan kedua kata yang bertumpuk makna tetap berdampingan (contoh rusak: `kelapa sawit Elaeis guineensis`, `kotak pembatas bounding box`, `buah kecil spikelet`).
- **Prinsip Seleksi Tunggal (Single-Term Selection)**:
  1. DILARANG KERAS menjejerkan dua istilah yang maknanya sama, baik dengan kurung maupun tanpa kurung.
  2. Pilih salah satu secara tegas:
     - Gunakan istilah teknis universal langsung dalam cetak miring (*bounding box*, *backbone*, *region proposal*, *real-time*, *deep learning*, *anchor-free*, *frames per second* / FPS) tanpa embel-embel padanan Indonesia di depannya.
     - ATAU gunakan istilah bahasa Indonesia murni tanpa istilah asing di sampingnya (kotak pembatas, brondolan, rendemen minyak, stasiun sortasi).
     - Jangan menyandingkan nama ilmiah Latin jika nama komoditasnya sudah baku (tulis 'kelapa sawit', bukan 'kelapa sawit Elaeis guineensis').
  3. Tanda kurung HANYA sah untuk 4 kategori:
     - Tahun sitasi: `(Ramadhani dkk., 2026)` atau `Lai dkk. (2023)`.
     - Singkatan akronim saat pertama kali didefinisikan: `Stock Keeping Unit (SKU)` atau `Optical Character Recognition (OCR)`.
     - Rujukan pasal atau ayat perundang-undangan: `Pasal 8 ayat (1) huruf f`.
     - Penomoran persamaan matematika: `Persamaan (2.1)` atau `(2.1)`.
     - Koordinat dan notasi matematika: $[x_c, y_c, w, h]$.
  4. Kepadatan tanda kurung non-sitasi wajib ditekan hingga 0 pasang, dan kepadatan kurung editorial non-ilmiah ditekan di bawah 5 sampai 7 pasang per 1.000 kata. Dilarang mengeliminasi kurung tahun sitasi ilmiah hanya demi mengejar target rasio kurung.
- **Standar Penamaan Judul Sub-Bab Bab 2 (Aturan 1 Sampai 2 Kata Korpus UPNVJ)**:
  1. Judul sub-bab Bab 2 (`Heading 2` dan `Heading 3`) wajib terdiri dari **1 sampai 2 kata benda entitas murni** (contoh baku: `2.1 Tanaman Selada`, `2.2 Citra Digital`, `2.3 *Deep Learning*`, `2.4.1 *Convolutional Layer*`, `2.4.2 *Pooling Layer*`, `2.4.3 *Softmax*`, `2.5 MobileNetV2`, `2.6 Python`, `2.7 Evaluasi Model`, `2.8 Penelitian Terdahulu`). Maksimal 3 kata hanya untuk nama algoritma baku yang tidak dapat dipenggal (`2.4 *Convolutional Neural Network*`).
  2. DILARANG KERAS menulis judul sub-bab panjang ala AI slop (`2.1 Tinjauan Komprehensif Mengenai...`) atau menggabungkan dua topik dengan kata hubung `dan` / `&` / `/` (`2.3 Arsitektur Model dan Fungsi Objektif`).
  3. Pada tata letak fisik PDF/Word, judul sub-bab menggunakan `Times New Roman 12 pt Bold` (*Bold Italic* untuk istilah bahasa Inggris) dengan *Hanging Indent* 36.0 pt (nomor di `x = 113.4 pt`, teks judul di `x = 149.4 pt` sejajar vertikal dengan awal baris pertama paragraf).
- **Standar Penamaan Judul Tabel dan Gambar (Korpus UPNVJ & Gunadarma)**:
  1. Penomoran tabel dan gambar menggunakan format `Tabel X.Y Judul Tabel` dan `Gambar X.Y Judul Gambar` tanpa titik setelah nomor sub-bab (DILARANG `Tabel X.Y.` atau `Gambar X.Y.`).
  2. DILARANG KERAS membubuhkan tanda kurung istilah asing pada judul tabel dan gambar (contoh salah AI slop: `Tabel 2.3. Matriks Perbandingan Penelitian Terdahulu (State-of-the-Art)`).
  3. Gunakan judul yang singkat, padat, dan lugas sesuai korpus riil UPNVJ (contoh baku: `Tabel 2.1 Kajian Pustaka`, `Tabel 2.3 Penelitian Terdahulu`, `Tabel 2.1 Dekomposisi Variabel Faster R-CNN`, `Tabel 4.1 Jadwal Pelaksanaan Penelitian`).
  4. Posisi caption: judul tabel di atas tabel, judul gambar di bawah gambar.

- **Prosedur Baku Perapihan Bab 2 (Tinjauan Pustaka)**:
  1. *Audit Judul Sub-Bab 1-2 Kata*: Pangkas seluruh judul sub-bab Bab 2 yang lebih dari 2-3 kata atau yang mengandung preposisi/kata hubung menjadi nama entitas murni 1-2 kata, lalu jadikan kata judul tersebut sebagai subjek kalimat pertama pada paragraf di bawahnya.
  2. *Audit Istilah Bertumpuk*: Telusuri teks untuk menemukan jejeran kata ganda padanan (seperti *buah spikel*, *lapisan mesokarp daging buah*, *grader petugas sortasi*). Ganti menjadi satu istilah tunggal yang baku dan presisi.
  3. *Audit Kurung Liar*: Buang seluruh tanda kurung terjemahan bahasa Inggris pada nama fraksi atau istilah umum (misal ubah `Mentah (*Unripe*)` menjadi `Mentah`). Sisakan kurung hanya untuk tahun sitasi, akronim awal, dan nomor persamaan.
  4. *Penegakan First-Mention Sitasi*: Untuk 3 sampai 5 penulis, pemunculan pertama sebutkan seluruh nama belakang disambung kata 'dan' (misal `Ramadhani, Dewanta, dan Gunawan, 2026`). Pemunculan kedua dan seterusnya gunakan `dkk.`
  5. *Verifikasi Kuantitatif Jurnal*: Pastikan seluruh angka akurasi, mAP, FPS, dan parameter model di tabel penelitian terdahulu diverifikasi langsung dari berkas asli jurnal rujukan (zero hallucination).
  6. *Sinkronisasi Multi-Format*: Jika proyek mengelola dokumen multi-format, lakukan patch langsung pada file teks master (`.md`), selaraskan pada naskah layout (`.typ` dikompilasi ke `.pdf`), dan simpan pembaruan pada berkas Word (`.docx`) secara in-place via WordCraft MCP.

## O (Definition of Done)
Naskah mengalir dingin, lugas, alami, dengan judul sub-bab 1-2 kata entitas murni serta bebas dari kejanggalan kata bertumpuk maupun residu kurung AI. Seluruh format tabel, sitasi, dan formula sinkron lintas format dokumen.
