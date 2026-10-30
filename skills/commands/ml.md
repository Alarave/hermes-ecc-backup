---
description: Komando cepat eksekusi, rekayasa, dan evaluasi pipeline multimodal (Florence-2 + PaddleOCR vs Qwen2-VL) untuk skripsi Sociolla.
---

# /ml

Alias komando cepat untuk memicu spesialis **multimodal-attribute-extraction** (MAVE-Sociolla) di bawah orkestrasi **Pram Orchestrator** dan **Asep (spesialis-skills)**.

## Ruang Lingkup & Kemampuan
1. **EDA & Data Understanding**: Eksplorasi 3.224 produk Sociolla, eliminasi 56 sampel beresolusi rendah (<640px) ke `logs/preprocessing_errors.log`.
2. **Prapemrosesan & Anti-Leakage**: CLAHE LAB, letterbox 640x640, stratified group split by brand (70:15:15) pada 3.168 sampel bersih.
3. **Pipeline Konvensional Hibrida**: `microsoft/Florence-2-base` visual grounding + `PaddleOCR PP-OCRv4` (DBNet++ dan SVTR) + IoA >= 0.50 + Normalized Levenshtein >= 0.85 + exact match netto.
4. **Pipeline Agentic MLLM**: `Qwen/Qwen2-VL-7B-Instruct` ReAct reasoning loop (<= 5 langkah) + micro-tools (`crop_roi`, `enhance_patch`, `finalize_verdict`) + pencatatan jejak ke `outputs/agent_traces/{product_id}_trajectory.json`.
5. **Evaluasi & Benchmark**: Akurasi, Precision, Recall, Macro/Micro F1, CER, WER, Latensi (ms), VRAM (MB), dan Uji Signifikansi McNemar (alpha = 0.05).
6. **Dasbor Peraga**: Streamlit side-by-side verification interface.

## Penggunaan

```bash
/ml <tugas-atau-fase-spesifik>
```
Contoh:
- `/ml eda`: Eksplorasi dataset katalog dan audit resolusi citra.
- `/ml preprocess`: Eksekusi filter 640px, CLAHE LAB, dan group split 70:15:15.
- `/ml conventional`: Bangun dan uji pipeline Florence-2 + PaddleOCR.
- `/ml agentic`: Bangun dan uji pipeline penalaran otonom Qwen2-VL ReAct.
- `/ml benchmark`: Hitung metrik komparasi dan jalankan uji McNemar.
- `/ml demo`: Bangun dasbor interaktif Streamlit.
