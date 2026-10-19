# Pola Arsitektur Diagram Vision-Language & OCR (vlm-ocr-architecture-patterns)

Dokumen rujukan visual dan tata letak diagram arsitektur kecerdasan buatan untuk *Vision-Language Encoders* (SigLIP 2) dan *Deep Scene-Text OCR* (PaddleOCR 3.0 / PP-OCRv4/v5/v6). Disusun untuk FigGenie agar mampu menggambar diagram arsitektur model multimodal berstandar publikasi konferensi top dunia (CVPR, ICCV, ECCV, NeurIPS, OSDI).

---

## 1. Analisis Tata Visual Arsitektur SigLIP 2 (Google DeepMind, arXiv:2502.14786)

### 1.1 Karakteristik Arsitektur & Anatomi Visual
SigLIP 2 merevolusi arsitektur *dual-tower* konvensional dengan mengintegrasikan multi-task learning multi-cabang tanpa mengorbankan sifat modular encoder:

```text
[Input Image] ──► [Patch Grid 16x16 / NaFlex] ──► [Vision Transformer (ViT)] ──┬──► [MAP Attention Head] ──► [Sigmoid Loss]
                                                                                ├──► [LocCa Decoder] ─────► [BBox & Captions]
                                                                                └──► [Student-Teacher] ──► [Self-Distillation]

[Input Text]  ──► [Multilingual Gemma Tokenizer] ─► [Text Transformer] ─────────┴──► [MAP Attention Head] ──► [Sigmoid Loss]
```

### 1.2 Komponen Visual Kunci & Representasi Grafis
1. **Representasi Patch Grid & NaFlex (Native Aspect-Ratio Flexible Resolution)**:
   - Digambar sebagai matriks kotak-kotak kecil (`16x16` piksel) di atas citra masukan dengan garis grid tipis (`stroke: #94a3b8`, `stroke-width: 0.5 pt`).
   - Penanda NaFlex: Panah interpolasi bilinear dwiarah yang menunjukkan adaptasi resolusi non-persegi tanpa distorsi *aspect ratio*.
2. **Dual-Tower Encoder (Backbone Utama)**:
   - Tower Citra: Blok bertingkat *Vision Transformer* (ViT-B, L, So400m, atau g) dengan warna latar netral sejuk (`fill: #f8fafc`, `stroke: #334155`).
   - Tower Bahasa: Blok *Text Transformer* dengan Gemma Multilingual Tokenizer (kosakata 256k), warna latar hijau sejuk (`fill: #f0fdf4`, `stroke: #166534`).
3. **Multi-Objective Loss Branching (Cabang Target Latihan)**:
   - *Cabang 1 - SigLIP Sigmoid Loss*: Matriks klasifikasi biner pasangan gambar-teks mini-batch tanpa normalisasi softmax global (`fill: #e0e7ff`, `stroke: #4338ca`).
   - *Cabang 2 - LocCa Decoder (Grounded Captioning & BBox)*: Decoder transformer dengan cross-attention ke representasi vision un-pooled untuk memprediksi koordinat bounding box dan frasa teks region (`fill: #ccfbf1`, `stroke: #0f766e`).
   - *Cabang 3 - Self-Distillation & Masked Prediction (SILC/TIPS)*: Cabang self-supervised untuk pembelajaran fitur padat dense prediction (`fill: #f3e8ff`, `stroke: #7e22ce`).

### 1.3 Palet Warna Standar Google Research untuk SigLIP 2
| Peran Komponen | Warna Garis (Stroke) | Warna Latar (Fill) | Warna Teks | Keterangan |
|---|---|---|---|---|
| Vision Tower | `#334155` (Slate-700) | `#f8fafc` (Slate-50) | `#0f172a` | Komponen visual dasar |
| Text Tower | `#166534` (Green-800) | `#f0fdf4` (Green-50) | `#14532d` | Komponen representasi teks |
| Sigmoid Loss Matrix | `#4338ca` (Indigo-700) | `#e0e7ff` (Indigo-100) | `#312e81` | Loss biner kontras |
| LocCa Grounding Head | `#0f766e` (Teal-700) | `#ccfbf1` (Teal-100) | `#134e4a` | Kepala deteksi bounding box |
| Self-Distillation Head| `#7e22ce` (Purple-700) | `#f3e8ff` (Purple-100) | `#581c87` | Pembelajaran fitur padat |

---

## 2. Analisis Tata Visual Arsitektur PaddleOCR (Baidu, arXiv:2507.05595 & arXiv:2606.13108)

### 2.1 Karakteristik Arsitektur Two-Stage Decoupled
Arsitektur PaddleOCR memisahkan proses deteksi fisik dengan pengenalan semantik karakter menjadi alur modular deterministik:

```text
[Dokumen / Foto Kemasan]
       │
       ▼
┌────────────────────────────────────────────────────────┐
│ TAHAP 1: Deteksi Teks (DBNet++ / PP-OCRv5 Detektor)    │
│ [PP-HGNetV2 / LCNetV4] ──► [LK-PAN] ──► [P / T / B Map]│
└────────────────────────────────────────────────────────┘
       │ (Bounding Polygons)
       ▼
┌────────────────────────────────────────────────────────┐
│ TAHAP 2: Rektifikasi Orientasi (Direction Classifier)  │
│ [Angle Net 0° / 180°] ──► [Rotated RoI Cropping]       │
└────────────────────────────────────────────────────────┘
       │ (Teks Tegak Terpotong)
       ▼
┌────────────────────────────────────────────────────────┐
│ TAHAP 3: Pengenal Teks Dual-Branch (PP-OCRv5 Rec)      │
│ ├── Fast Branch (Inference): SVTR-HGNet + CTC Loss     │
│ └── Heavy Branch (Training): GTC-NRTR Seq2Seq Decoder  │
└────────────────────────────────────────────────────────┘
       │ (Deretan String Karakter & Key Information)
       ▼
[KIE Extraction / PP-ChatOCRv4 / PaddleOCR-VL]
```

### 2.2 Komponen Visual Deteksi DBNet++
1. **Backbone & LK-PAN (Large Kernel Path Aggregation Network)**:
   - Digambar sebagai piramida fitur berlapis dengan panah *bottom-up* dan *top-down* yang menggabungkan fitur resolusi rendah bersemantik tinggi dengan fitur resolusi tinggi berdetail tepi.
2. **Tiga Peta Binerisasi Terdiferensiasi (Differentiable Binarization Maps)**:
   - *Probability Map ($P$)*: Peta probabilitas keberadaan teks (`fill: #dbeafe`, `stroke: #1d4ed8`).
   - *Threshold Map ($T$)*: Peta ambang batas dinamis permukaan kemasan (`fill: #fef3c7`, `stroke: #b45309`).
   - *Approximate Binary Map ($\hat{B}$)*: Hasil binerisasi menggunakan formula step function diferensiabel:
     $$\hat{B}_{i,j} = \frac{1}{1 + \exp(-k(P_{i,j} - T_{i,j}))}$$

### 2.3 Komponen Visual Pengenalan Dual-Branch SVTR
1. **Fast Inference Branch (SVTR-HGNet + CTC)**:
   - Digambar dengan garis panah tebal solid (`stroke-width: 1.2 pt`), menunjukkan jalur eksekusi inferensi ringan (<5 ms per kata).
2. **Training-Only Supervision Branch (GTC-NRTR)**:
   - Digambar dengan garis putus-putus (`stroke-dasharray: 4, 3`), mengindikasikan modul perhatian yang hanya aktif saat pelatihan untuk membimbing representasi student model.

---

## 3. Blueprint Arsitektur Hibrida VLM-OCR untuk E-Commerce & Skripsi

Menggabungkan keunggulan visual grounding SigLIP 2 dengan presisi karakter PaddleOCR ke dalam satu diagram sistem komprehensif:

```text
                               ┌───────────────────────────────────────────────────┐
                               │ Jalur Semantik Makro (Vision-Language SigLIP 2)   │
                        ┌─────►│ [ViT Patch Grid] ──► [Joint Embedding Space]      │
                        │      │ Memverifikasi Logo Merek & Varian Kemasan         │
                        │      └─────────────────────────┬─────────────────────────┘
[Katalog Shopee]        │                                │ (Cosine Similarity Score)
[Foto + Judul + Deskripsi]                               ▼
                        │      ┌───────────────────────────────────────────────────┐
                        │      │ Jalur Fisik Mikro (PaddleOCR DBNet++ & SVTR)      │
                        └─────►│ [DBNet RoI Polygon] ──► [SVTR Character Parsing]  │
                               │ Membaca Netto: "50 ml", BPOM: "NA18211900123"     │
                               └─────────────────────────┬─────────────────────────┘
                                                         │ (Exact String Tokens)
                                                         ▼
                               ┌───────────────────────────────────────────────────┐
                               │ Mesin Fusi & Discrepancy Gate                     │
                               │ [Pencocokan Atribut Seller vs Fakta Kemasan]      │
                               │ Output: MATCH (Valid) / MISMATCH (Inkonsisten)    │
                               └───────────────────────────────────────────────────┘
```

---

## 4. Template Kode SVG Siap Pakai (Anti-Clipping & Anti-Overlap)

Template SVG vektor murni berikut mengikuti standar baku FigGenie untuk visualisasi pipeline hibrida:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 504 180" width="504pt" height="180pt" font-family="Helvetica, Arial, sans-serif">
  <!-- Definisi Marker Panah Standar -->
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 1 2 L 7 5 L 1 8 z" fill="#334155"/>
    </marker>
    <marker id="arrow-teal" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 1 2 L 7 5 L 1 8 z" fill="#0f766e"/>
    </marker>
  </defs>

  <!-- Container 1: Input Layer -->
  <g id="c:input" data-kind="container">
    <rect x="16" y="24" width="96" height="132" rx="4" ry="4" fill="#f8fafc" stroke="#94a3b8" stroke-width="0.8"/>
    <text x="64" y="40" font-size="7" font-weight="bold" fill="#0f172a" text-anchor="middle">Input Data Shopee</text>
    <!-- Node Foto Kemasan -->
    <g id="n:input-img" data-kind="node">
      <rect x="24" y="52" width="80" height="44" rx="3" ry="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.6"/>
      <text x="64" y="72" font-size="6.5" fill="#334155" text-anchor="middle">Foto Kemasan Fisik</text>
      <text x="64" y="82" font-size="5.5" fill="#64748b" text-anchor="middle">(Patch Grid 16x16)</text>
    </g>
    <!-- Node Teks Katalog -->
    <g id="n:input-txt" data-kind="node">
      <rect x="24" y="104" width="80" height="40" rx="3" ry="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.6"/>
      <text x="64" y="122" font-size="6.5" fill="#334155" text-anchor="middle">Klaim Teks Seller</text>
      <text x="64" y="132" font-size="5.5" fill="#64748b" text-anchor="middle">(Judul, Netto, BPOM)</text>
    </g>
  </g>

  <!-- Konektor Input ke Dua Jalur -->
  <path d="M 112 74 L 144 54" fill="none" stroke="#334155" stroke-width="0.8" marker-end="url(#arrow)"/>
  <path d="M 112 80 L 144 114" fill="none" stroke="#334155" stroke-width="0.8" marker-end="url(#arrow)"/>

  <!-- Container 2: Jalur VLM (SigLIP 2) -->
  <g id="c:vlm-branch" data-kind="container">
    <rect x="148" y="24" width="168" height="60" rx="4" ry="4" fill="#f0fdf4" stroke="#86efac" stroke-width="0.8"/>
    <text x="232" y="38" font-size="7" font-weight="bold" fill="#166534" text-anchor="middle">Jalur Semantik Visual: SigLIP 2</text>
    <g id="n:vlm-encoder" data-kind="node">
      <rect x="156" y="46" width="70" height="30" rx="3" ry="3" fill="#ffffff" stroke="#22c55e" stroke-width="0.6"/>
      <text x="191" y="60" font-size="6.5" fill="#14532d" text-anchor="middle">ViT NaFlex Encoder</text>
      <text x="191" y="69" font-size="5.5" fill="#15803d" text-anchor="middle">(Dynamic Aspect)</text>
    </g>
    <g id="n:vlm-head" data-kind="node">
      <rect x="234" y="46" width="74" height="30" rx="3" ry="3" fill="#ffffff" stroke="#22c55e" stroke-width="0.6"/>
      <text x="271" y="60" font-size="6.5" fill="#14532d" text-anchor="middle">LocCa Grounding</text>
      <text x="271" y="69" font-size="5.5" fill="#15803d" text-anchor="middle">(BBox Region Match)</text>
    </g>
  </g>

  <!-- Container 3: Jalur OCR (PaddleOCR 3.0) -->
  <g id="c:ocr-branch" data-kind="container">
    <rect x="148" y="96" width="168" height="60" rx="4" ry="4" fill="#eff6ff" stroke="#93c5fd" stroke-width="0.8"/>
    <text x="232" y="110" font-size="7" font-weight="bold" fill="#1e40af" text-anchor="middle">Jalur Teks Eksak: PaddleOCR 3.0</text>
    <g id="n:ocr-dbnet" data-kind="node">
      <rect x="156" y="118" width="70" height="30" rx="3" ry="3" fill="#ffffff" stroke="#3b82f6" stroke-width="0.6"/>
      <text x="191" y="132" font-size="6.5" fill="#1e3a8a" text-anchor="middle">Detektor DBNet++</text>
      <text x="191" y="141" font-size="5.5" fill="#2563eb" text-anchor="middle">(Curve Scene Text)</text>
    </g>
    <g id="n:ocr-svtr" data-kind="node">
      <rect x="234" y="118" width="74" height="30" rx="3" ry="3" fill="#ffffff" stroke="#3b82f6" stroke-width="0.6"/>
      <text x="271" y="132" font-size="6.5" fill="#1e3a8a" text-anchor="middle">Pengenal SVTR-HG</text>
      <text x="271" y="141" font-size="5.5" fill="#2563eb" text-anchor="middle">(Fast CTC Infer)</text>
    </g>
  </g>

  <!-- Konektor ke Fusi -->
  <path d="M 316 54 L 348 76" fill="none" stroke="#0f766e" stroke-width="0.8" marker-end="url(#arrow-teal)"/>
  <path d="M 316 126 L 348 104" fill="none" stroke="#0f766e" stroke-width="0.8" marker-end="url(#arrow-teal)"/>

  <!-- Container 4: Discrepancy Gate & Decision -->
  <g id="c:gate" data-kind="container">
    <rect x="352" y="44" width="136" height="92" rx="4" ry="4" fill="#fdf4ff" stroke="#d8b4fe" stroke-width="0.8"/>
    <text x="420" y="58" font-size="7" font-weight="bold" fill="#6b21a8" text-anchor="middle">Discrepancy Gate (Audit)</text>
    
    <g id="n:gate-verify" data-kind="node">
      <rect x="360" y="66" width="120" height="30" rx="3" ry="3" fill="#ffffff" stroke="#a855f7" stroke-width="0.6"/>
      <text x="420" y="79" font-size="6.5" fill="#581c87" text-anchor="middle">Pencocokan Deterministik</text>
      <text x="420" y="89" font-size="5.5" fill="#7e22ce" text-anchor="middle">Regex BPOM + Unit Netto</text>
    </g>

    <g id="n:gate-out" data-kind="node">
      <rect x="360" y="102" width="120" height="26" rx="3" ry="3" fill="#ffffff" stroke="#a855f7" stroke-width="0.6"/>
      <text x="420" y="114" font-size="6.5" font-weight="bold" fill="#0f766e" text-anchor="middle">Valid (Match) / Mismatch</text>
      <text x="420" y="123" font-size="5.5" fill="#6b21a8" text-anchor="middle">Laporan Audit Interaktif</text>
    </g>
  </g>
</svg>
```

---

## 5. Kaidah Perancangan Anti-Clipping Khusus Model AI

1. **Jarak Antar-Layer Neural Network**:
   - Selalu pertahankan jarak horizontal minimal 24-32 pt antar-tahap (Stage) untuk memberi ruang bagi panah konektor dan label dimensi tensor tanpa tumpang tindih.
2. **Backdrop Rect pada Garis Konektor (Anti-Line Strike)**:
   - Setiap kali garis panah melewati teks keterangan (misal: koordinat bounding box atau skor probabilitas), selalu gunakan `place_text.py --backdrop` atau buat elemen `<rect fill="#ffffff" fill-opacity="0.9" rx="2" ry="2"/>` di bawah elemen teks.
3. **Penyebutan Dimensi Tensor**:
   - Tulis dimensi tensor (seperti `[B, 3, 256, 256]` atau `[B, L, D]`) dengan font 5.5 pt dan warna abu-abu netral (`#64748b`) tepat di atas atau di bawah panah dengan jarak vertikal 3 pt.
4. **Batas Margin Kanvas 15-20 pt**:
   - Titik paling kiri tidak boleh kurang dari `x=16 pt` dan titik paling kanan tidak boleh melebihi `W - 16 pt`.
   - Titik paling atas tidak boleh kurang dari `y=16 pt` dan titik paling bawah tidak boleh melebihi `H - 16 pt`.
