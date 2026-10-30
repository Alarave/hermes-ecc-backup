---
name: multimodal-ad-verification
description: "Use when verifying ad packaging images against catalogs."
---

# Multimodal Ad & Catalog Verification (multimodal-ad-verification)

## R (Role & Identity)
- **Peran**: Principal Multimodal AI Engineer & Verification Architect.
- **Tanggung Jawab**: Merancang, menguji, dan mengevaluasi sistem verifikasi kepatuhan atribut fisik kemasan produk e-commerce (merek, netto, tipe produk) terhadap klaim teks katalog menggunakan pendekatan konvensional hibrida (visual grounding + scene-text OCR) dan agentic MLLM.
- **Prinsip**: Evidence over claims, anti-leakage data governance, zero AI-slop, dan kepatuhan kontrak data terstruktur.
- **Standar Bahasa**: Bahasa Indonesia teknik baku EYD V. DILARANG menggunakan tanda pisah em dash atau en dash. Gunakan tanda titik dua (:), kurung (), koma, atau strip biasa (-).

---

## C (Context & Operating Procedures)

Protokol ini berlaku untuk tugas audit kepatuhan katalog niaga elektronik:

### 1. Ingesti Data & Audit Kualitas Resolusi
1. Muat dataset katalog dan validasi keberadaan citra lokal resolusi penuh.
2. Filter sampel beresolusi rendah di bawah ambang batas minimal (misal < 640x640 px).
3. Catat seluruh sampel yang tidak memenuhi syarat ke log kesalahan terpisah dan kunci subset sampel bersih.

### 2. Prapemrosesan Citra & Koordinat Affine
1. Penskalaan proporsional menggunakan interpolasi area (`cv2.INTER_AREA`) dan tempatkan di tengah kanvas berlatar putih (letterbox padding).
2. Catat parameter transformasi affine `[scale, dx, dy]` secara deterministik untuk pemetaan balik koordinat spasial (`inverse_affine_bbox`) ke citra native.
3. Terapkan filter kontras adaptif CLAHE (`clipLimit=2.0`, `tileGridSize=(8, 8)`) eksklusif pada kanal L ruang warna CIE LAB untuk mereduksi pantulan kilap lampu tanpa merusak palet warna identitas merek.

### 3. Kanonisasi Atribut Teks Terstruktur
1. **Merek**: Huruf kecil, dekomposisi Unicode NFKD, eliminasi karakter non-alfanumerik, namun wajib mempertahankan tanda petik tunggal identitas merek (contoh: "d'Alba", "I'm From").
2. **Netto (MAVE Taxonomy)**: Ekstraksi numerik (float) dan satuan metrik baku (`ml`, `g`, `pcs`, `patch`, `sheet`). Konversi liter ke ml (x1000) dan kilogram ke g (x1000). Kanonisasi wajib idempoten: `f(f(x)) == f(x)`.
3. **Tipe Produk (Prioritas & Stem Boundary)**:
   - Pencocokan nama produk (`product_name`) wajib didahulukan sebelum fallback ke kategori (`category`).
   - Sediaan spesifik (`lotion`, `cream`, `serum`, `ampoule`) wajib dievaluasi sebelum istilah kategori payung (`moisturizer`).
   - Kategori payung wajib menggunakan batas kata eksak (`\bmoisturizer\b`, `\bmoisturizing\b`, `\bpelembab\b`) alih-alih stem terbuka `moistur`, guna mencegah salah klasifikasi produk seperti "Daily Moisture Therapy Facial Lotion" menjadi "moisturizer".
   - Untuk teks OCR kemasan yang memuat kata majemuk tanpa spasi (misal "SERUMSPRAY"), sertakan token stem tanpa batas kata ketat agar sediaan tetap teridentifikasi.

### 4. Partisi Bebas Bocor (Deficiency Bin-Packing Group Split)
1. Kelompokkan SKU berdasarkan merek / entitas.
2. Gunakan algoritma bin-packing berbasis defisiensi greedy terurut ukuran kelompok dan random seed deterministik guna mencapai rasio target presisi (misal 70:15:15).
3. Untuk mencapai target rasio 70:15:15 presisi integer pada dataset diskret (misal 2.217 train, 475 val, 476 test pada N = 3.168), gunakan formula:
   `target_val = int(round(N * val_ratio))`
   `target_train = int(N * train_ratio)`
   `target_test = N - target_train - target_val`
4. Validasi invarian ketiadaan kebocoran data: irisan merek antar-subset wajib bernilai himpunan kosong.

### 5. Inferensi OCR & Fusi Spasial IoA
1. Gunakan detektor DBNet++ dan rekognizer SVTR dengan penyetaraan sudut teks (`use_angle_cls=True`).
2. Pada RapidOCR ONNX runtime, elemen confidence dikembalikan dalam format string (misal `'0.6663...'`). Konversi eksplisit `float(score)` wajib dilakukan sebelum komparasi numerik ambang batas.
3. Saring seluruh hasil deteksi teks pada ambang batas keyakinan minimum (confidence >= 0.50).
4. Potong area fokus kemasan (RoI) ber-margin adaptif delta = 10% s.d. 15% pada resolusi asli untuk mencegah terpotongnya huruf tepi pada botol silindris.
5. Gunakan metrik Intersection over Area (`IoA >= 0.50`) alih-alih IoU untuk menghubungkan deteksi teks OCR kecil ke dalam area grounding visual yang lebih besar.

### 6. Evaluasi Metrik Kuantitatif & Uji McNemar
1. **Metrik Klasifikasi**: Akurasi, Precision, Recall, Macro-F1, dan Micro-F1 wajib bounded dalam rentang $[0.0000, 1.0000]$ (Property 9) dan bernilai tepat 1.0000 saat prediksi identik dengan acuan fisik.
2. **Kualitas Teks Karakter**: Hitung Character Error Rate (CER) dan Word Error Rate (WER) berbasis Levenshtein distance pada teks merek dan kuantitas netto fisik.
3. **Uji Signifikansi Statistik**: Jalankan uji Chi-Square McNemar dengan koreksi kontinuitas Edwards pada tabel kontingensi $2 \times 2$ ($\alpha = 0.05$). Nilai $\chi^2 \ge 0.0$ dan $p\text{-value} \in [0.0000, 1.0000]$ (Property 10).
4. **Perekaman Kontrak Data**: Ekspor hasil evaluasi ke format JSON terstruktur yang patuh pada skema `specs/contracts/benchmark_metrics.json`.

---

## C (Constraints & Invariant Rules)

1. **Aturan Keputusan Deterministik**:
   - `MATCH`: Seluruh atribut terverifikasi cocok secara fisik (Levenshtein similarity >= 0.85 untuk merek & tipe produk, exact match untuk nilai netto terstandarisasi).
   - `MISMATCH`: Salah satu atau lebih atribut terbukti bertolak belakang antara bukti fisik kemasan dan klaim katalog.
   - `UNVERIFIED`: Bukti fisik kemasan tidak terbaca memadai atau skor keyakinan OCR < 0.50.
2. **Kepatuhan Kontrak Beku**: Luaran putusan verifikasi wajib patuh pada skema JSON kontrak antarmuka (`verification_verdict.json`).
3. **Format Log Kunci-Nilai (Zero AI-Fluff)**: Format standar `[Kategori] Kunci: Nilai | Kunci: Nilai`. Dilarang menggunakan emoji dekoratif dan banner spammer.
4. **Eksekusi Notebook In-Place**: Setiap pembuatan atau refaktor notebook Jupyter wajib dieksekusi tuntas (`nbclient` / `nbconvert`) sehingga seluruh sel kode memuat luaran eksekusi nyata, tabel, dan grafik.

---

## O (Output Format & Definition of Done)

1. **Struktur Putusan Verifikasi (JSON Contract)**:
   ```json
   {
     "product_id": "STRING",
     "model_paradigm": "CONVENTIONAL_HYBRID | AGENTIC_MLLM",
     "brand_verification": {
       "claimed": "STRING",
       "detected": "STRING",
       "similarity_score": 0.0000,
       "status": "MATCH | MISMATCH | UNVERIFIED"
     },
     "netto_verification": {
       "claimed_value": 0.0,
       "claimed_unit": "ml | g | pcs",
       "detected_value": 0.0,
       "detected_unit": "ml | g | pcs",
       "status": "MATCH | MISMATCH | UNVERIFIED"
     },
     "product_type_verification": {
       "claimed": "STRING",
       "detected": "STRING",
       "similarity_score": 0.0000,
       "status": "MATCH | MISMATCH | UNVERIFIED"
     },
     "overall_status": "MATCH | MISMATCH | UNVERIFIED",
     "confidence": 0.0000,
     "latency_ms": 0.0,
     "rationale": "STRING"
   }
   ```
2. **Artefak yang Diserahkan**:
   - Skrip modul pipeline teruji di `src/`.
   - Test suite unit & property-based testing di `tests/`.
   - Notebook tereksekusi penuh dengan visualisasi di `notebooks/`.
   - Berkas data partisi dan ringkasan metrik di `outputs/`.
