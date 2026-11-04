# Blueprint Teknis 2 Paradigma Verifikasi Multimodal

Dokumen ini memuat spesifikasi teknis dan logika eksekusi lengkap untuk dua paradigma verifikasi kemasan produk kosmetik Sociolla sesuai dokumen `brief/design.md` dan `brief/requirements.md`.

---

## 1. Paradigma 1: Pipeline Multimodal Konvensional Hibrida (Kolaborasi Dua Tahap Mengadopsi Richo, 2025)

### Komponen Inti
1. **Model Lokalisasi Spasial Objek**: `Ultralytics YOLOv11m` (arsitektur C3k2, SPPF, PAN, DSC, C2PSA attention, anchor-free decoupled head, loss CIoU + DFL) untuk melokalisasi 3 kelas atribut target (`brand`, `netto`, `product_type`).
2. **Pemotongan RoI Atribut Ber-Margin Adaptif**: Memotong wilayah bounding box langsung dari citra resolusi asli dengan ekspansi margin adaptif 10% s.d. 15% guna mencegah pemotongan huruf tepi (*boundary truncation*) pada kemasan melengkung/silindris.
3. **Mesin Pembaca Karakter (OCR)**: `PaddleOCR PP-OCRv4` (DBNet++ detektor binarisasi diferensiabel 4.5M + detektor arah teks `use_angle_cls=True` + SVTR-LCNet rekognizer 12.8M dengan CTC Loss, total ~17.3M parameter).
4. **Penyelaras Spasial & Matching Engine**: Filter *Intersection over Area* (IoA >= 0.50), *Normalized Levenshtein Distance* (>= 0.85 untuk merek & tipe produk), dan *Exact Netto Match* (kuantitas dan satuan metrik baku MAVE).

### Alur Eksekusi Bertahap
```text
Citra Kemasan (640x640) + Metadata Katalog Toko (Sociolla)
         |
         v
[Ultralytics YOLOv11m Object Detection]
Deteksi 3 Kelas: brand, netto, product_type
BBox: [x1, y1, x2, y2] ternormalisasi [0.0, 1.0] (Conf >= 0.25)
         |
         v
[Adaptive RoI Cropping (Margin 10%-15%)]
Pemotongan Patch Resolusi Asli Tanpa Kompresi
         |
         v
[PaddleOCR PP-OCRv4 (DBNet++ + use_angle_cls + SVTR-LCNet)]
Deteksi Probabilitas Teks via Sigmoid DBNet + Rectification Sudut + CTC Loss
Token Teks Alfanumerik Fisik + Keyakinan (Conf >= 0.50)
         |
         v
[Spatial Fusion Filter: IoA >= 0.50]
IoA = Area(B_ocr ∩ B_yolo) / Area(B_ocr) >= 0.50
         |
         v
[Discrepancy Matcher & Canonicalizer]
Brand: Normalized Levenshtein >= 0.85
Product Type: Normalized Levenshtein >= 0.85
Netto: Exact Numerical & Unit Match (MAVE Canonicalization)
         |
         v
Keputusan: MATCH / MISMATCH / UNVERIFIED
```

### Logika Matematis & Ambang Batas
1. **Formulasi Binarisasi DBNet++ (Richo, 2025)**:
   $$P(i, j) = \frac{1}{1 + \exp(-k(X_{i,j} - \theta))}$$
   di mana $X_{i,j}$ merepresentasikan nilai piksel fitur prapemrosesan, $\theta$ adalah ambang batas binarisasi adaptif, dan $k$ adalah faktor pengontrol kelandaian (*steepness factor*) fungsi sigmoid untuk membedakan teks dari latar belakang kemasan.

2. **Probabilitas Rekognisi Karakter SVTR/CRNN & CTC Loss (Richo, 2025)**:
   Konvolusi visual $F = \text{Conv}(X, K)$, pemodelan urutan tanpa segmentasi eksplisit:
   $$p(l | X) = \sum_{\pi: \mathcal{B}(\pi) = l} p(\pi | X)$$
   serta aktivasi softmax probabilitas karakter:
   $$p(y_t = c | x) = \frac{\exp(W_c \cdot h_t)}{\sum_{c'} \exp(W_{c'} \cdot h_t)}$$

3. **Intersection over Area (IoA)**:
   $$\text{IoA}(B_{\text{ocr}}, B_{\text{yolo}}) = \frac{\text{Area}(B_{\text{ocr}} \cap B_{\text{yolo}})}{\text{Area}(B_{\text{ocr}})}$$
   Ambang batas: $\text{IoA} \ge 0.50$. Memastikan teks OCR benar-benar berada di dalam wilayah atribut yang dilokalisasi YOLOv11m.

4. **Normalized Levenshtein Similarity (Brand & Product Type)**:
   $$\text{Sim}(s_1, s_2) = 1.0 - \frac{\text{Levenshtein}(s_1, s_2)}{\max(|s_1|, |s_2|)}$$
   Ambang batas kelulusan: $\ge 0.85$. Mentoleransi kesalahan baca kecil akibat teks melengkung atau pantulan cahaya botol.

5. **Pencocokan Netto Eksak**:
   Nilai numerik `value_catalog == value_ocr` dan satuan baku `unit_catalog == unit_ocr` (`ml`, `g`, `pcs`, `patch`, `sheet`).

6. **Kaidah Status Verifikasi**:
   - `MATCH`: $\text{Sim}_{\text{brand}} \ge 0.85$ DAN $\text{Sim}_{\text{type}} \ge 0.85$ DAN nilai netto cocok persis.
   - `MISMATCH`: Salah satu atribut bertentangan secara definitif.
   - `UNVERIFIED`: Citra tidak terbaca, teks tidak terdeteksi, atau keyakinan OCR $< 0.50$. Batas waktu inferensi $\le 5.0$ detik per sampel.

---

## 2. Paradigma 2: Pipeline Agentic MLLM (Qwen2-VL ReAct Loop)

### Komponen Inti
1. **Model Fondasi Visual-Bahasa**: `Qwen/Qwen2-VL-7B-Instruct` (7.61B parameter, Native Dynamic Resolution ViT + Qwen2 Causal LM) dalam format FP16 (~15 GB VRAM) atau AWQ 4-bit (~5.8 GB VRAM).
2. **Arsitektur Siklus Penalaran**: ReAct (*Reasoning-Action-Observation*) otonom maksimal 5 langkah per sampel.
3. **Ruang Alat Mikro (Micro-Tools Space)**:
   - `crop_roi(ymin, xmin, ymax, xmax)`: Memotong wilayah fokus (*Region of Interest*) dari citra asli tanpa downsampling (koordinat normalisasi $[0.0, 1.0]$) guna membaca teks kecil/netto.
   - `enhance_patch(ymin, xmin, ymax, xmax, clip_limit=2.0)`: Menerapkan penajaman kontras adaptif lokal CLAHE jika ada pantulan cahaya atau gradien warna pudar pada kemasan.
   - `finalize_verdict(status, brand_match, netto_match, bboxes, confidence, rationale)`: Menghentikan penalaran seketika saat bukti visual memadai.

### Alur Siklus Penalaran ReAct
```text
[Input: Citra Asli + Klaim Katalog + System ReAct Prompt]
                      |
                      v
     +-----------> [Thought] (Analisis Tata Letak & Bukti Visual)
     |                |
     |                v
     |             [Action] (Pilih Alat: crop_roi / enhance_patch / finalize)
     |                |
     |         +------+------+
     |         |             |
     |    (Alat Inspeksi)  (finalize_verdict)
     |         |             |
     |         v             v
     |    [Observation]   [Validasi JSON & Bounding Box]
     |    (Kirim Patch)      |
     |         |             v
     +---------+      [Status Akhir & Trajectory JSON]
```

### Batasan Keras & Mekanisme Pengaman
1. **Batas Langkah**: Maksimal 5 siklus penalaran. Jika langkah ke-5 tercapai tanpa putusan, sistem memutus paksa ke status `UNVERIFIED`.
2. **Batas Waktu (Timeout)**: Maksimal 30.0 detik per sampel. Jika timeout, langsung fallback ke `UNVERIFIED`.
3. **Manajemen Memori Konteks**: Menyimpan riwayat maksimal 2 eksekusi alat terakhir (`last_k=2`) untuk mencegah context drift dan ledakan konsumsi token.
4. **Pencatatan Jejak Keputusan**: Setiap langkah penalaran dicatat secara berurutan dan disimpan ke `outputs/agent_traces/{product_id}_trajectory.json` untuk pembuktian auditabilitas 100%.

---

## 3. Skema Kontrak Keluaran JSON (verification_verdict.json)

```json
{
  "product_id": "SOC_SKIN_0001",
  "method": "conventional_hybrid",
  "overall_status": "MATCH",
  "confidence": 0.9250,
  "execution_time_ms": 235.4,
  "attributes": {
    "brand": {
      "claimed": "cosrx",
      "extracted": "cosrx",
      "similarity": 1.0000,
      "status": "MATCH",
      "bbox": [0.2540, 0.1200, 0.4500, 0.2800]
    },
    "netto": {
      "claimed_value": 150.0,
      "claimed_unit": "ml",
      "extracted_value": 150.0,
      "extracted_unit": "ml",
      "status": "MATCH",
      "bbox": [0.6500, 0.7200, 0.8200, 0.8500]
    }
  },
  "rationale": "Nama merek cocok persis dan nilai isi bersih 150 ml terverifikasi pada label depan kemasan."
}
```
