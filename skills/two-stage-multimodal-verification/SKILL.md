---
name: two-stage-multimodal-verification
description: "Use when verifying product attributes with YOLO and OCR."
---

# Two-Stage Multimodal Verification (YOLO + Scene-Text OCR)

## R (Role & Identity)
- **Peran**: Principal Multimodal AI Engineer & Computer Vision Systems Architect.
- **Tanggung Jawab**: Merancang dan mengimplementasikan pipeline hibrida kolaborasi dua tahap (*two-stage collaboration*) antara detektor objek spasial berkecepatan tinggi (YOLOv11) dan mesin pengenal teks optik (*scene-text OCR*, PaddleOCR PP-OCRv4) untuk verifikasi kepatuhan atribut kemasan fisik ritel dan *e-commerce*.
- **Prinsip Rekayasa**: Zero AI-slop, deterministik, latensi rendah (< 500 ms/produk), dan bebas kebocoran data (*anti-data leakage*).

---

## C (Context & Metodologi)
Pipeline ini mengadopsi arsitektur kolaboratif dua tahap (Richo, 2025; MDPI Mathematics KORIE, 2026; Jocher & Qiu, 2024):
1. **Kegagalan OCR Murni**: OCR berbasis deteksi teks tunggal (*end-to-end scene text*) mengalami degradasi akurasi drastis pada kemasan ritel padat akibat tipografi artistik, teks multi-baris, dan ketiadaan fokus area sasaran.
2. **Solusi Kolaboratif**:
   - Tahap 1: Deteksi objek spasial mengisolasi wilayah atribut target kemasan.
   - Tahap Antara: Pemotongan RoI beresolusi asli dengan margin adaptif mencegah pemotongan huruf tepi.
   - Tahap 2: Ekstraksi teks karakter terfokus pada potongan RoI.
   - Tahap 3: Fusi spasial mengaitkan token teks ke atribut sasaran.
   - Tahap 4 & 5: Normalisasi kanonikal dan pencocokan string/numerik terhadap klaim katalog.

---

## C (Constraints & Aturan Prosedural)

### 1. Deteksi Objek Spasial (Ultralytics YOLOv11m)
- Model: `Ultralytics YOLOv11m` (arsitektur C3k2, SPPF, Enhanced PAN, dynamic head, Depthwise Separable Convolutions / DSC, atensi C2PSA, loss CIoU + DFL).
- Kelas Target Tertutup (*Closed-Vocabulary Attributes*):
  - 0: `brand` (area logo/teks merek kemasan)
  - 1: `netto` (area kuantitas isi bersih dan satuan)
  - 2: `product_type` (area teks tipe sediaan produk, misal serum, toner, cleanser)
- Parameter: Citra masukan letterbox $640 \times 640$ px, ambang keyakinan deteksi $conf \ge 0.25$.
- Luaran: Koordinat kotak pembatas absolut piksel $[x_1, y_1, x_2, y_2]$ dan ternormalisasi $[0.0, 1.0]$.

### 2. Pemotongan RoI Ber-Margin Adaptif (Tahap Antara)
- Wajib memotong patch kemasan langsung dari citra beresolusi asli (*native resolution patch*), BUKAN dari citra terkompresi letterbox.
- Terapkan ekspansi margin adaptif $\delta = 10\% \text{ s.d. } 15\%$ terhadap dimensi kotak deteksi:
  $$\delta_x = (x_2 - x_1) \times \text{margin\_ratio}, \quad \delta_y = (y_2 - y_1) \times \text{margin\_ratio}$$
  $$x_{\min}' = \max(0, x_1 - \delta_x), \quad y_{\min}' = \max(0, y_1 - \delta_y)$$
  $$x_{\max}' = \min(W, x_2 + \delta_x), \quad y_{\max}' = \min(H, y_2 + \delta_y)$$
- Mengapa: Kemasan silindris/melengkung (*curved surface*) dan sudut kamera miring sering menyebabkan huruf awal atau akhir menempel tepat di garis batas deteksi. Tanpa margin adaptif, huruf tepi terpotong (*boundary truncation*) dan merusak pengenalan karakter.

### 3. Ekstraksi Teks (PaddleOCR PP-OCRv4)
- Arsitektur: Detektor teks DBNet++ binarisasi diferensiabel sigmoid $P(i, j) = \frac{1}{1 + \exp(-k(X_{i,j} - \theta))}$ dan rekognizer SVTR-LCNet / CRNN berbasis CTC loss.
- Wajib aktifkan orientasi sudut: `use_angle_cls=True` untuk merotasi teks vertikal atau terbalik pada kemasan melengkung ke orientasi $0^\circ$.
- Ambang batas keyakinan karakter: abaikan token dengan confidence $< 0.50$ sebagai gangguan visual (*graphic noise*).

### 4. Fusi Spasial IoA (Intersection over Area)
- Gunakan metrik tumpang tindih spasial *Intersection over Area* (IoA), DILARANG menggunakan IoU standar:
  $$\text{IoA}(B_{\text{ocr}}, B_{\text{yolo}}) = \frac{\text{Area}(B_{\text{ocr}} \cap B_{\text{yolo}})}{\text{Area}(B_{\text{ocr}})} \ge 0.50$$
- Mengapa IoA bukan IoU: Asimetri luas ekstrem $\text{Area}(B_{\text{yolo}}) \gg \text{Area}(B_{\text{ocr}})$. Kotak deteksi atribut mencakup blok luas kemasan, sedangkan kotak teks OCR hanya melingkupi baris huruf kecil di dalamnya. Pada kondisi ini, IoU jatuh mendekati 0 meskipun teks berada 100% di dalam kotak atribut. Normalisasi terhadap luas teks OCR menjamin pengaitan spasial yang akurat.

### 5. Format Adjustment & Mesin Pencocokan
- Nama Merek & Tipe Produk: Dihitung menggunakan *Normalized Levenshtein Similarity*:
  $$\text{NLSim}(s_1, s_2) = 1.0 - \frac{\text{Levenshtein}(s_1, s_2)}{\max(|s_1|, |s_2|)} \ge 0.85$$
- Kuantitas Netto: Wajib standardisasi kanonikal (taksonomi MAVE) volume ke `ml`, massa ke `g`, atau diskret (`pcs`, `sheet`, `patch`), diikuti pencocokan eksak numerik (*exact match*).

### 6. Higiene Notebook & Eksekusi Otomatis
- Saat membangun struktur sel notebook secara programatik dengan `nbformat`, pastikan menetapkan `nb["cells"] = cells` secara eksplisit sebelum memanggil `nbf.write(nb, f)`. Mengabaikan baris ini akan menghasilkan berkas JSON berstruktur kosong (0 cells).
- Jalankan notebook otomatis headless menggunakan `nbclient.NotebookClient(nb, timeout=600, kernel_name='python3').execute()` dengan menggunakan path interpreter Python lingkungan ML yang terverifikasi.

---

## O (Output Format & Contract)

Setiap sampel verifikasi wajib menghasilkan struktur JSON patuh kontrak:
```json
{
  "product_id": "SOC_TEST_001",
  "model_paradigm": "CONVENTIONAL_HYBRID",
  "brand_verification": {
    "claimed": "COSRX",
    "extracted": "COSRX",
    "status": "MATCH",
    "similarity": 1.0
  },
  "netto_verification": {
    "claimed": "150 ml",
    "extracted": "150ml",
    "status": "MATCH",
    "similarity": 1.0
  },
  "product_type_verification": {
    "claimed": "Toner",
    "extracted": "Clarifying Treatment Toner",
    "status": "MATCH",
    "similarity": 0.88
  },
  "overall_status": "MATCH",
  "confidence": 0.95,
  "latency_ms": 142.5,
  "vram_peak_mb": 420.0,
  "metadata": {
    "detections": [
      {
        "class_id": 0,
        "class_name": "brand",
        "bbox_norm": [0.15, 0.20, 0.45, 0.35],
        "confidence": 0.94
      }
    ]
  }
}
```
