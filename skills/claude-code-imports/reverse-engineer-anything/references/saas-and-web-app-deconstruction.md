# Panduan Teknis: Dekonstruksi Arsitektur Web SaaS dan AI Application (SaaS REA)
> Standar operasional rekayasa balik arsitektur aplikasi berbasis web, platform SaaS tertutup di balik login wall, pohon instruksi AI (prompt tree), dan editor rich-text.

---

## 1. Landasan Rekayasa Balik Aplikasi SaaS & Web SPA

Aplikasi SaaS modern (termasuk AI writing assistant seperti Jenni AI, Notion AI, atau Linear) umumnya menempatkan antarmuka editor di balik gerbang autentikasi (*login wall*) dan memproses inferensi AI di sisi server privat.

Dekonstruksi arsitektur (*Reverse Engineering Architecture / REA*) pada aplikasi SaaS bertujuan untuk memahami:
1. **Pola Manajemen Konteks**: Bagaimana prompt dan batasan dokumen dirakit secara hierarkis sebelum dikirim ke model LLM.
2. **Skema Antarmuka Editor**: Bagaimana editor teks (ProseMirror, TipTap, Slate) menstrukturkan node dokumen, slash commands, dan caption.
3. **Mekanisme Verifikasi & Guardrails**: Bagaimana sistem mendeteksi inkonsistensi fakta, sitasi tidak valid, atau halusinasi teks.
4. **Pola Bersih Rekonstruksi (Clean-Room Design)**: Mengambil prinsip arsitektural terbaik tanpa menyalin kode berhak cipta atau mengekfiltrasi rahasia komersial.

---

## 2. Prosedur Investigasi 5 Tahap (SaaS REA Workflow)

### Tahap 1: Sanitasi URL dan Triage Permukaan
- Bersihkan URL target dari parameter pelacakan iklan (`utm_*`, `gclid`, `gbraid`, `_gl`).
- Tentukan apakah rute target bersifat publik (*marketing/docs page*) atau privat (*authenticated SPA dashboard*).
- Jika halaman privat memantul ke formulir masuk (*login wall*), jangan menebak kredensial. Beralih ke metode triangulasi bukti lapis 2 dan 3.

### Tahap 2: Triangulasi Tiga Lapis Bukti (Evidence Triangulation)
Jika kode sumber backend tidak dapat diakses, kumpulkan bukti fisik dari 3 lapis permukaan publik:
1. **Lapis A (Landing Shell & Asset Bundle)**: Inspeksi berkas manifest web publik, bundel JavaScript vendor, dan skema CSS untuk mengidentifikasi pustaka UI (Tailwind, Radix, Lucide) dan engine editor (TipTap/ProseMirror).
2. **Lapis B (Subdomain Dokumentasi Teknis `docs.<domain>`)**: Telusuri dokumentasi resmi, panduan troubleshooting, dan changelog API untuk mengekstrak definisi parameter, taksonomi galat, batas karakter prompt, dan alur kerja bawaan.
3. **Lapis C (Bantuan & API Help Center)**: Ekstraksi FAQ teknis untuk memetakan nama internal fitur, limit kuota komputasi, dan integrasi pihak ketiga (Zotero, BibTeX, Crossref).

### Tahap 3: Pemetaan Pohon Konteks & Hierarki Prompt (Cascading Context Tree)
- Analisis bagaimana aplikasi menyusun ruang lingkup penulisan:
  - *Document Prompt*: Instruksi tingkat global (tema, audiens, batasan gaya).
  - *Section / Heading Prompts*: Instruksi lokal per bab yang membatasi wilayah jelajah model.
  - *Selection Context*: Instruksi bedah teks terpilih (*rewrite, simplify, hedge*).
- Catat format passing parameter antar-level untuk diadaptasi ke dalam modul skill lokal.

### Tahap 4: Dekonstruksi Verification Gates & Claim Confidence
- Petakan bagaimana platform mengevaluasi luaran AI:
  - Apakah klaim ditautkan ke berkas sumber (PDF / Zotero / URL)?
  - Apa taksonomi cacat klaim yang digunakan? (Misal: *Unsupported, Weakly Supported, Overstated, Misrepresented, Contradicted, Unverifiable*).
  - Bagaimana mekanisme *hedging* diterapkan pada pernyataan yang belum terbukti secara empiris.

### Tahap 5: Penyusunan Matriks Rekonstruksi Bersih (Clean-Room Mapping)
Sajikan tabel konversi yang membandingkan:
- Fitur Asli SaaS
- Mekanisme Kerja Internal Hasil Observasi
- Kelemahan / Batasan yang Ditemukan
- Rancangan Implementasi Rekonstruksi di Repositori Lokal

---

## 3. Matriks Pelaporan Temuan SaaS REA

Format laporan baku untuk dekonstruksi SaaS:

```markdown
### LAPORAN SAAS REA: [Nama Aplikasi / Fitur]
- **Target URL**: [URL kanonikal bersih]
- **Metode Pembuktian**: [Triangulasi Dokumentasi / Inspeksi Manifest SPA / Tracing API]
- **Pohon Konteks & Prompt**: [Struktur injeksi konteks global vs lokal]
- **Engine Editor & State**: [Pustaka rich-text dan format payload]
- **Verification & Guardrails**: [Aturan filter sitasi, confidence, dan anti-halusinasi]
- **Rekomendasi Rekonstruksi**: [Pola adopsi bersih ke skill / kode lokal]
```
