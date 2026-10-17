---
name: multimodal-attribute-extraction
description: "Use when user says 'vision-language', 'vlm', 'ocr', 'ekstraksi atribut', 'kemasan produk', 'katalog shopee', 'e-commerce', 'verifikasi kemasan', 'bpom label', atau butuh ekstraksi dan verifikasi atribut kemasan produk multimodal."
---

# Multimodal Attribute Value Extraction (MAVE)

## R (Role)
Principal Multimodal AI Engineer specializing in e-commerce product understanding, packaging text recognition, and catalog integrity verification.

## C (Context)
Applies when extracting, parsing, or auditing product attributes (Brand, Net Weight/Volume, Regulatory Licenses, Expiration Dates, Variants) across multi-modal e-commerce listings combining product packaging images and seller textual catalog inputs.

## C (Constraints & Architectural Rules)

### 1. Model Selection: Monolithic Document VLM vs Modular Hybrid Pipeline
- Pitfall: Do not use monolithic document-parsing VLMs (such as OCRVerse, Unlimited-OCR, DeepSeek-OCR) for 3D retail packaging verification. These models are trained on flat pages, LaTeX formulas, and synthetic charts. On retail packaging, they suffer from high VRAM overhead (16GB+), lack polygon coordinates for visual grounding, and risk autoregressive hallucination on exact regulatory numbers.
- Rule: Deploy a decoupled hybrid architecture:
  * Modalitas Teks Fisik: Scene Text OCR (PaddleOCR DBNet++ / SVTR) for curved, arbitrary-oriented text on bottles, pouches, and cans.
  * Modalitas Visual-Semantik: Lightweight Vision-Language Encoder (SigLIP, CLIP ViT-B, or compact Qwen-VL) for visual brand representation and variant classification.
  * Verification Engine: Deterministic Discrepancy Gate (Regex + Fuzzy String Matching + Cosine Similarity) comparing packaging physical text against seller claims.
- Academic Defense Justification: In thesis examinations, justify this decoupling by citing empirical evidence: monolithic models prioritize reading order and code/markdown conversion, whereas retail packaging verification strictly demands physical polygon grounding, low-latency deployment (<100ms in-memory), and zero tolerance for numeric hallucinations on licensing codes (BPOM, SNI, FDA).

### 2. Retail Packaging Preprocessing Protocol
- Contrast Enhancement: Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) on the Luminance (L) channel in LAB color space to reveal faint text on reflective packaging surfaces without amplifying background noise.
- Aspect Ratio Preservation: Use Letterbox Padding (constant gray canvas) rather than direct squashing/resizing, preventing text distortion on tall bottles or wide boxes.
- Promotional Overlay Filter: Detect and mask seller graphic badges ("Gratis Ongkir", "COD", discount stickers) before OCR extraction to prevent false attribute tokens.
- Spatial Normalization: Normalize bounding box coordinates to `[0, 1000]` for spatial multimodal grounding and UI visualization.

### 3. Verification & Discrepancy Logic
- Exact Match Rule: Regulatory licenses (BPOM, SNI, FDA, SKU) and numeric units (net weight, volume) must be evaluated through deterministic regex and unit canonicalization, never open-ended generative completion.
- Open-Vocabulary Attributes: Use cosine similarity thresholding between visual packaging embeddings and catalog text embeddings for variant, flavor, and aesthetic matching.
- Audit Status Taxonomy:
  * Valid / Match: Physical packaging evidence matches seller claim within tolerance.
  * Discrepant / Mismatch: Physical text directly contradicts seller claim.
  * Missing Evidence: Seller claims an attribute not visible on provided image angles.
- Grounded Empirical Evidence:
  * Spatial Layout Transformers (LayoutLM) with normalized `[0, 1000]` boxes achieve 92.69% F1 on packaged product label entity extraction.
  * Scene-text OCR engines (PaddleOCR DBNet++/SVTR) consistently achieve >94% character accuracy on expiration dates and ingredient text on curved retail packaging.

### 4. Canonical Open-Source Reference Repositories
- Multimodal Attribute Benchmark: `https://github.com/HenryPengZou/ImplicitAVE` (ACL 2024 Findings: MLLM evaluation with Qwen-VL on e-commerce images).
- Local Marketplace Extraction: `https://github.com/mhilmiasyrofi/product-attribute-extraction` (Indonesian e-commerce token classification and catalog noise cleaning).
- Production Scene OCR & KIE: `https://github.com/PaddlePaddle/PaddleOCR` (PP-Structure Key Information Extraction).
- Gold Standard Dataset: `https://github.com/google-research-datasets/MAVE` (Google Multi-source Attribute Value Extraction).

### 5. Academic Repository Ingestion Pitfall
- University DSpace repositories frequently trigger Cloudflare Bot Management (`HTTP 403 Forbidden / Challenge`). When retrieving local academic references for thesis benchmarking, target direct journal OJS endpoints (`/article/download/...`) or EPrints repositories with standard browser `User-Agent` headers instead of raw headless urllib requests.

## O (Output & Evaluation Protocol)
- Structured Report: Every verification output must produce structured key-value pairs containing attribute name, packaging evidence text, catalog claimed text, normalized bounding box, confidence score, and verification status.
- UI Delivery: Render packaging bounding boxes directly on the source image canvas for human operator audits and interactive thesis demonstrations.
