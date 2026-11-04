# LEKSIKON DAN TAKSONOMI ANTI-AI SLOP (ZERO SLOP STANDAR)

Dokumen referensi baku untuk mendeteksi, mengeliminasi, dan merekonstruksi kalimat yang terindikasi terjangkit *post-training register* (bahasa klise khas model bahasa AI).

---

## 1. Taksonomi 6 Kategori Pola AI Slop

### Kategori A: Pembuka Usang (Canned Openers)
Frasa pembuka template yang tidak membawa informasi baru:
- "Di era digital yang serba cepat ini..."
- "Dalam lanskap teknologi yang terus berkembang..."
- "Tahukah Anda bahwa..."
- "We are thrilled to announce..."
- "In today's fast-paced world..."
- "Here is the thing..."
- "It is worth noting that..."
- "Needless to say..."
**Tindakan**: HAPUS kalimat pembuka tersebut langsung. Mulai paragraf dari fakta konkret atau subjek utama kalimat.

### Kategori B: Formula Kontras Biner (Binary Contrast Formulas)
Pola retorika sintetis yang membandingkan dua hal klise:
- "Ini bukan sekadar alat, ini adalah revolusi."
- "Bukan tentang bagaimana kita bekerja, tetapi mengapa kita bekerja."
- "It is not just about X; it is about Y."
- "This is not merely a tool, but a paradigm shift."
**Tindakan**: Rekonstruksi menjadi pernyataan langsung mengenai fungsi riil dan kegunaan sistem tanpa dramatisasi.

### Kategori C: Atribusi Samar (Vague Attribution)
Mengklaim otoritas tanpa menyertakan sumber nyata:
- "Para ahli sepakat bahwa..."
- "Penelitian membuktikan bahwa..."
- "Banyak pihak menilai..."
- "Experts agree that..."
- "Studies have shown that..."
- "Industry leaders believe..."
**Tindakan**: Cantumkan nama ilmuwan/institusi/metrik secara eksplisit, atau hapus klaim tersebut jika tidak ada data pendukung faktual.

### Kategori D: Inflasi Signifikansi (Significance Inflation)
Membesar-besarkan peristiwa biasa menjadi momen kosmik:
- "Menandai babak baru dalam sejarah..."
- "Menjadi tonggak bersejarah..."
- "Bukti nyata dari dedikasi tiada henti..."
- "Marks a pivotal moment..."
- "Stands as a testament to..."
- "Serves as a beacon of innovation..."
**Tindakan**: Paparkan fakta mentah apa yang dicapai. Biarkan pembaca menilai sendiri signifikansinya.

### Kategori E: Kata Sifat Pemasaran Hampa (Hype Buzzwords)
Kata-kata sifat yang terlalu sering diobral hingga kehilangan makna:
- "Solusi mutakhir", "Revolusioner", "Komprehensif", "Holistik", "Kredibel"
- "Seamless", "Robust", "Leverage", "Synergy", "Delve", "Foster", "Cutting-edge", "Game-changer"
- "Tapestry", "Beacon", "Pinnacle", "Bedrock", "Supercharge", "Unleash"
**Tindakan**: Ganti dengan kata kerja operasional atau ukuran spesifikasi teknis (contoh: "cepat dan seamless" -> "waktu muat di bawah 200 ms").

### Kategori F: Kesimpulan Rekapitulasi Berulang (Repetitive Recap)
Paragraf penutup yang hanya mengulang poin sebelumnya tanpa kesimpulan baru:
- "Secara keseluruhan, dapat disimpulkan bahwa..."
- "Singkatnya, masa depan ada di tangan kita..."
- "In conclusion...", "To sum up...", "All in all..."
- "The bottom line is..."
**Tindakan**: Hapus paragraf penutup rekap jika tidak ada rekomendasi tindak lanjut (*action item*) yang nyata.

---

## 2. Matriks Penggantian Kata Klise (Quick Substitution Table)

| Kata/Frasa AI Slop | Masalah Utama | Alternatif Pengganti Konkret |
|---|---|---|
| Memanfaatkan (Leverage) | Klise korporat | Menggunakan, menerapkan, menjalankan |
| Solusi mutakhir | Melebih-lebihkan | Nama alat, framework, atau arsitektur spesifik |
| Robust | Abstrak | Tahan uji beban, toleran terhadap kegagalan (fault-tolerant) |
| Seamless | Janji palsu | Tanpa jeda, terintegrasi langsung, otomatis |
| Delve into | Klise GPT | Menganalisis, memeriksa, membedah |
| Foster collaboration | Jargon HR | Bekerja sama, mengoordinasikan tim |
| In today's digital era | Basa-basi kosong | (Hapus kalimat pembuka ini secara total) |
| It is worth noting | Interupsi penulis | (Hapus frasa transisi, langsung tulis pernyataannya) |
| A testament to | Dramatisasi | Menunjukkan bahwa, membuktikan bahwa |
| Game-changer | Hype berlebihan | Meningkatkan efisiensi sebesar X%, memangkas latensi |

---

## 3. Protokol Verifikasi Fidelitas (Fact-Checking Gate)
Setiap kali menjalankan revisi de-sloppify:
1. Hitung seluruh angka dan metrik sebelum dan sesudah edit (wajib identik 100%).
2. Periksa nama diri (orang, perusahaan, model, library) tidak boleh ada yang berubah atau tertukar.
3. Pastikan tautan URL dan path berkas tidak berubah.
4. Pastikan blok kode dan parameter konfigurasi tidak diubah strukturnya.
