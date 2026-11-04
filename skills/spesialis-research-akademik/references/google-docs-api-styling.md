# Google Docs Programmatic Typesetting & BatchUpdate Guide

Panduan manipulasi gaya paragraf, tipografi, dan tata letak Google Docs via Google Docs API (batchUpdate) atau Composio MCP (googledocs).

## 1. Pemetaan Struktur Dokumen & Karakter Indeks
- Ambil seluruh AST dokumen via GOOGLEDOCS_GET_DOCUMENT_BY_ID.
- Struktur bodi dokumen berada di body.content[]. Setiap elemen struktural berupa paragraph memiliki startIndex dan endIndex.
- Aturan Pergeseran Indeks: Seluruh operasi penambahan atau penghapusan teks mengubah indeks karakter di belakangnya. Lakukan perubahan teks sebelum pemformatan gaya, atau terapkan pemformatan dari indeks terbesar ke terkecil (urutan terbalik).

## 2. Pembaruan Gaya Paragraf (updateParagraphStyle)
### Skema Payload Baku
```json
{
  "updateParagraphStyle": {
    "range": {
      "startIndex": 100,
      "endIndex": 250
    },
    "paragraphStyle": {
      "alignment": "JUSTIFIED",
      "lineSpacing": 150,
      "indentFirstLine": {
        "magnitude": 36,
        "unit": "PT"
      },
      "indentStart": {
        "magnitude": 0,
        "unit": "PT"
      },
      "spaceAbove": {
        "magnitude": 0,
        "unit": "PT"
      },
      "spaceBelow": {
        "magnitude": 8,
        "unit": "PT"
      }
    },
    "fields": "alignment,lineSpacing,indentFirstLine,indentStart,spaceAbove,spaceBelow"
  }
}
```

### Pitfall Skema Paragraf
- Kunci Properti: Kunci di dalam updateParagraphStyle WAJIB bernama paragraphStyle, BUKAN style. Menggunakan style memicu galat API: Unknown name style at requests[0].update_paragraph_style.
- Mask fields Eksplisit: Google Docs API menolak pembaruan jika fields tidak didefinisikan. Sebutkan atribut persis yang diubah dipisahkan koma tanpa spasi: alignment,lineSpacing,indentFirstLine,indentStart.
- Nilai Perataan (alignment): Gunakan JUSTIFIED (rata kiri-kanan), START (rata kiri), CENTER (rata tengah), atau END (rata kanan).
- Nilai Spasi Baris (lineSpacing): Dinyatakan dalam persentase bilangan bulat (150 untuk 1,5 spasi; 100 untuk 1 spasi; 200 untuk 2 spasi).
- Satuan Indentasi: Gunakan objek unit poin { "magnitude": 36, "unit": "PT" } untuk indentasi 0,5 inci / 1,27 cm baku skripsi.

## 3. Pembaruan Gaya Huruf (updateTextStyle)
### Skema Payload Baku
```json
{
  "updateTextStyle": {
    "range": {
      "startIndex": 100,
      "endIndex": 150
    },
    "textStyle": {
      "bold": true,
      "italic": false,
      "fontSize": {
        "magnitude": 12,
        "unit": "PT"
      },
      "weightedFontFamily": {
        "fontFamily": "Times New Roman"
      }
    },
    "fields": "bold,italic,fontSize,weightedFontFamily"
  }
}
```

### Pitfall Rentang Teks (Range Guard)
- Kunci Properti: Kunci di dalam updateTextStyle WAJIB bernama textStyle, BUKAN style.
- Trailing Newline Pitfall: Pada range untuk pemformatan teks heading, kurangi endIndex sebanyak 1 karakter (endIndex - 1) agar karakter baris baru (\n) tidak ikut terpilih. Memformat karakter newline dapat menyebabkan gaya merembes ke paragraf berikutnya atau ditolak parser API.

## 4. Strategi Pembaruan Dokumen Skala Besar (Chunking)
- Batas Ukuran Payload: Jangan mengirim lebih dari 30 request updateParagraphStyle atau updateTextStyle dalam satu panggilan tunggal batchUpdate atau GOOGLEDOCS_UPDATE_EXISTING_DOCUMENT.
- Pembagian Chunk: Bagi daftar permintaan menjadi kumpulan batch berisi 20 sampai 25 request per eksekusi untuk mencegah HTTP 504 Gateway Timeout atau pemutusan koneksi MCP.

## 5. Format Hanging Indent Daftar Pustaka Google Docs API
Untuk menyusun entri Daftar Pustaka (Bibliography) dengan format gantung (*hanging indent*) 1,27 cm (0,5 inci):
- Baris pertama berada di margin kiri ($0\text{ cm}$), baris kedua dan seterusnya menjorok $1,27\text{ cm}$ ($36\text{ pt}$).
- Rumus Google Docs API: `indentStart` bernilai positif ($+36\text{ pt}$), sedangkan `indentFirstLine` bernilai negatif relatif terhadap `indentStart` ($-36\text{ pt}$).
```json
{
  "updateParagraphStyle": {
    "range": {
      "startIndex": 34485,
      "endIndex": 34679
    },
    "paragraphStyle": {
      "alignment": "JUSTIFIED",
      "lineSpacing": 150,
      "spaceBelow": {
        "magnitude": 6,
        "unit": "PT"
      },
      "indentStart": {
        "magnitude": 36,
        "unit": "PT"
      },
      "indentFirstLine": {
        "magnitude": -36,
        "unit": "PT"
      }
    },
    "fields": "alignment,lineSpacing,spaceBelow,indentStart,indentFirstLine"
  }
}
```

## 6. Disambiguasi Penggantian Sitasi Berulang via GOOGLEDOCS_REPLACE_ALL_TEXT
Saat mengganti teks sitasi terprogram di mana sitasi yang sama muncul lebih dari satu kali (misal: kemunculan pertama wajib ditulis lengkap seluruh penulis, sedangkan kemunculan kedua dan seterusnya wajib disingkat `dkk.`):
- DILARANG menggunakan kata kunci nama penulis saja (`find_text: "(Dompeipen et al., 2021)"`) karena operasi penggantian global akan mengubah seluruh kemunculan menjadi teks yang sama persis.
- SERTAKAN klausa kalimat unik di sekitar sitasi tersebut sebagai jangkar:
  - Kemunculan Pertama: `find_text: "suatu citra atau gambar digital (Dompeipen et al., 2021)."` diganti ke `find_text: "suatu citra atau gambar digital (Dompeipen, Henderi, dan Rahardja, 2021)."`
  - Kemunculan Kedua: `find_text: "serta jenis obyek yang terlihat (Dompeipen et al., 2021)."` diganti ke `find_text: "serta jenis obyek yang terlihat (Dompeipen dkk., 2021)."`
- Pola ini menjamin kepatuhan First-Mention Rule 100% tanpa salah sasaran.

## 7. Pemformatan Cetak Miring Asli (Native Italics) vs Anti-Markdown Slop
- **Larangan Karakter Markdown Semu**: DILARANG KERAS mengganti teks menjadi `_teks_` atau `*teks*` via `GOOGLEDOCS_REPLACE_ALL_TEXT` saat pengguna meminta format cetak miring (*italic*). Pengolah kata Google Docs memperlakukan karakter garis bawah `_` sebagai teks biasa (literal character), menghasilkan teks kotor seperti `_e-commerce_`.
- **Prosedur Pemformatan Murni (Native Rich-Text)**:
  1. Petakan seluruh teks dan indeks karakter dokumen dari pohon AST `body.content` (elemen `paragraph` dan `table`).
  2. Cari posisi teks target dan tentukan batas indeks asli `[startIndex, endIndex)`.
  3. Bangun objek permintaan `updateTextStyle`:
     ```json
     {
       "updateTextStyle": {
         "range": {
           "startIndex": 8580,
           "endIndex": 8603
         },
         "textStyle": {
           "italic": true
         },
         "fields": "italic"
       }
     }
     ```
  4. Kirimkan dalam kumpulan batch (chunk) berisi 20 sampai 25 permintaan melalui `GOOGLEDOCS_UPDATE_EXISTING_DOCUMENT`.
  5. Verifikasi bahwa teks target memiliki properti `textStyle: {"italic": true}` tanpa ada karakter `_` literal di sekitarnya.

## 8. Penyuntingan In-Place Dokumen Google Docs via Composio MCP (Zero-Layout Drift)
Saat pengguna meminta penyuntingan dokumen Google Docs langsung di tautan (`docs.google.com/document/d/...`) dengan mandat menjaga *paragraph styles*, *table structure*, dan *formatting*:
- **Pemanfaatan GOOGLEDOCS_REPLACE_ALL_TEXT**: Operasi find-and-replace Google Docs API mempertahankan seluruh *paragraph styles*, *heading styles*, pewarnaan sel tabel, dan jenis font asli (misal: Times New Roman 12 pt, 1.5 spasi). Jangan merombak dokumen secara total jika perubahan berfokus pada pembaruan entitas, angka, dan narasi.
- **Aturan Prioritas Jangkar Spesifik (Anchor Specificity First)**: Selalu jalankan penggantian frasa yang lebih panjang dan spesifik terlebih dahulu sebelum frasa pendek yang merupakan substring-nya (contoh: ganti `31 dari 40 PC siap pakai` sebelum `31 dari 40`). Menjalankan frasa pendek terlebih dahulu menyebabkan duplikasi teks liar (contoh kegagalan: `37 dari 4637 dari 46`).
- **Penanganan Tab Dokumen (Multi-Tab Documents)**: Periksa properti `tabs` via `GOOGLEDOCS_GET_DOCUMENT_BY_ID`. Jika dokumen memiliki multiple tabs (misal `t.0` dan `t.xxx`), tentukan apakah penggantian dilakukan pada tab tertentu (`tab_ids: ["t.0"]`) atau pada seluruh tab (default jika `tab_ids` diabaikan).
- **Verifikasi Hasil via Export API (Bukan Browser DOM)**: Antarmuka Google Docs di peramban web modern menggunakan canvas rendering, sehingga `document.body.innerText` pada browser headless tidak memuat teks dokumen. Verifikasi keberhasilan modifikasi wajib dilakukan melalui endpoint ekspor teks (`https://docs.google.com/document/d/<ID>/export?format=txt`) atau `GOOGLEDOCS_GET_DOCUMENT_PLAINTEXT`.

## 9. Protokol Sinkronisasi Total & Mitigasi Kebocoran Gaya Heading
- **Pencadangan Wajib (Safety Backup)**: Sebelum mengeksekusi operasi penggantian atau pembersihan skala besar pada Google Docs, WAJIB buat salinan cadangan menggunakan `GOOGLEDOCS_COPY_DOCUMENT` dengan judul berawalan `[BACKUP SEBELUM SYNC TOTAL]`.
- **Mitigasi Kebocoran Gaya Heading (Markdown Heading Leakage)**:
  - *Mekanisme*: Ketika menggunakan `GOOGLEDOCS_UPDATE_DOCUMENT_SECTION_MARKDOWN`, tag heading markdown (contoh `## 2.1 Judul Sub-bab`) rentan membuat seluruh paragraf teks bodi di bawahnya terformat sebagai `HEADING_2` (font tebal dan besar).
  - *Solusi Baku*: Segera setelah injeksi markdown selesai, jalankan batch `updateParagraphStyle` melalui `GOOGLEDOCS_UPDATE_EXISTING_DOCUMENT` pada rentang indeks karakter bodi narasi `[startIndex, endIndex)` dengan parameter:
    ```json
    {
      "updateParagraphStyle": {
        "range": { "startIndex": start, "endIndex": end },
        "paragraphStyle": { "namedStyleType": "NORMAL_TEXT" },
        "fields": "namedStyleType"
      }
    }
    ```
- **Audit Keseluruhan Bab (Anti-Legacy Orphaned Content)**:
  - *Mekanisme*: Perintah "ganti total" pengguna sering kali gagal jika agen hanya memperbarui bab yang sedang dibahas (misal Bab 2), sementara bab-bab di bagian akhir dokumen (seperti Bab 4 dan Bab 5) masih menyimpan konten naskah lama atau template berbeda.
  - *Solusi Baku*: Pindai seluruh heading dokumen dari awal hingga akhir via `GOOGLEDOCS_GET_DOCUMENT_BY_ID`. Bandingkan struktur bab dengan naskah WordCraft aktif (`.docx`). Jika ditemukan bab usang yang tidak relevan, bersihkan rentang indeks tersebut (`deleteContentRange`) atau lakukan sinkronisasi bab lanjutan secara berurutan.
- **Pencegahan Kerusakan Substring (Substring Collision Guard)**:
  - DILARANG melakukan replace global via `GOOGLEDOCS_REPLACE_ALL_TEXT` menggunakan kata kunci pendek tanpa nomor sub-bab (contoh: mengganti `Verifikasi Katalog` saja).
  - Hal ini memicu kerusakan teks seperti `2.1 Ve2.1 Penelitian Terdahulu` dan memotong huruf awal heading tetangga (contoh `2.2 Prapemrosesan Citra Kemasan` terpotong menjadi `n Citra Kemasan`). Selalu gunakan string jangkar lengkap beserta nomor sub-bab.

## 10. Pencegahan Galat Hapus Paragraf Pre-Table (Invalid Deletion Range) & Netralisasi Outline
- Setiap elemen tabel pada Google Docs API wajib didahului oleh pembatas paragraf (newline). Mencoba menghapus baris kosong tepat sebelum tabel via `deleteContentRange` akan ditolak dengan galat: `Invalid requests[0].deleteContentRange: Invalid deletion range. Cannot delete the requested range.`
- Solusi: Alih-alih menghapusnya, netralkan gaya paragraf tersebut via `updateParagraphStyle`:
```json
{
  "updateParagraphStyle": {
    "range": {
      "startIndex": 37298,
      "endIndex": 37299
    },
    "paragraphStyle": {
      "namedStyleType": "NORMAL_TEXT",
      "spaceAbove": { "magnitude": 0, "unit": "PT" },
      "spaceBelow": { "magnitude": 0, "unit": "PT" },
      "lineSpacing": 100
    },
    "fields": "namedStyleType,spaceAbove,spaceBelow,lineSpacing"
  }
}
```
Langkah ini mengeliminasi celah vertikal kosong sebelum tabel dan mencegah paragraf kosong berstatus `HEADING_2` muncul sebagai entri hantu di Document Outline / Daftar Isi.

## 11. Penguncian Lebar Kolom Tabel Akademik (updateTableColumnProperties)
- Tabel yang baru disisipkan secara bawaan memiliki `tableColumnProperties.widthType: "EVENLY_DISTRIBUTED"`. Pada naskah A4 ber-margin 4-4-3-3 cm (lebar bidang teks efektif 14,0 cm = 396.86 PT), pembagian rata menyebabkan kolom nomor ("No") terlalu lebar (3,5 cm) dan kolom deskripsi teks sempit serta berisiko melar melampaui batas margin kanan.
- Terapkan `updateTableColumnProperties` berbobot `FIXED_WIDTH` dengan total akumulasi tepat 14,0 cm (396.86 PT):
```json
[
  {
    "updateTableColumnProperties": {
      "tableStartLocation": { "index": 37299 },
      "columnIndices": [0],
      "tableColumnProperties": {
        "widthType": "FIXED_WIDTH",
        "width": { "magnitude": 28.35, "unit": "PT" }
      },
      "fields": "widthType,width"
    }
  },
  {
    "updateTableColumnProperties": {
      "tableStartLocation": { "index": 37299 },
      "columnIndices": [1],
      "tableColumnProperties": {
        "widthType": "FIXED_WIDTH",
        "width": { "magnitude": 90.71, "unit": "PT" }
      },
      "fields": "widthType,width"
    }
  },
  {
    "updateTableColumnProperties": {
      "tableStartLocation": { "index": 37299 },
      "columnIndices": [2],
      "tableColumnProperties": {
        "widthType": "FIXED_WIDTH",
        "width": { "magnitude": 138.9, "unit": "PT" }
      },
      "fields": "widthType,width"
    }
  },
  {
    "updateTableColumnProperties": {
      "tableStartLocation": { "index": 37299 },
      "columnIndices": [3],
      "tableColumnProperties": {
        "widthType": "FIXED_WIDTH",
        "width": { "magnitude": 138.9, "unit": "PT" }
      },
      "fields": "widthType,width"
    }
  }
]
```

## 12. Penyeragaman Font dan Ukuran Massal Tanpa Merusak Format Cetak Miring
- Saat menyeragamkan tipografi (Times New Roman 12 pt) pada blok teks besar yang sudah memuat istilah asing berformat miring (*e-commerce*, *skincare*, *product_id*, dsb.), KELUARKAN atribut `italic` dan `bold` dari `fields` mask:
```json
{
  "updateTextStyle": {
    "range": { "startIndex": 32925, "endIndex": 37232 },
    "textStyle": {
      "fontSize": { "magnitude": 12, "unit": "PT" },
      "weightedFontFamily": { "fontFamily": "Times New Roman" }
    },
    "fields": "fontSize,weightedFontFamily"
  }
}
```
Google Docs API hanya akan menyentuh jenis font dan ukuran font tanpa menyentuh status `italic` dan `bold` karakter yang ada di dalamnya.
