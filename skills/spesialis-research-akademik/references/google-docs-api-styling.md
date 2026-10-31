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
