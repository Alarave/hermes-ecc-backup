---
name: jupyter-crisp-dm-workflow
version: 1.1.0
author: Firman
license: MIT
description: "Pola sel tripartit dan dual-environment notebook CRISP-DM."
metadata:
  hermes:
    tags: [jupyter, crisp-dm, notebook, machine-learning, mlops]
    related_skills: [pram-orchestrator, mle-workflow, ml-data-leakage-guard]
---

# Jupyter CRISP-DM Workflow & Dual-Environment Adaptation

## When to Use
Gunakan skill ini saat membuat, mengedit, atau mengevaluasi Jupyter Notebook (`.ipynb`) untuk penelitian machine learning, visi komputer, deep learning, dan MLOps berbasis metodologi CRISP-DM.

## 1. Pola Tripartit Sel Notebook (CRISP-DM Standard)
Setiap notebook riset (`.ipynb`) wajib mematuhi Pola Tripartit untuk mencegah AI-slop dan menjaga mutu dokumentasi ilmiah:
1. **Markdown Cell (Tujuan & Landasan Teori)**: Uraikan konteks teknis, tujuan sel, dan sitasi literatur primer (misal MAVE, Amazon CPG, ViOC-AG).
2. **Code Cell (Eksekusi Atomik & Key-Value Logging)**:
   - Satu aksi per sel (single responsibility).
   - Format print kunci-nilai terstandarisasi: `[Kategori] Kunci: Nilai | Kunci: Nilai`.
   - Dilarang keras menggunakan emoji atau banner pembatas berulang (`print("="*80)`).
   - Dilarang print di dalam perulangan ribuan sampel (gunakan `tqdm`).
3. **Markdown Cell (Interpretasi Saintifik Fakta Numerik)**:
   - Interpretasi hasil komputasi secara objektif dan kuantitatif.
   - Dilarang hanya mengulang baris kode atau memberikan komentar naratif generik.

## 2. Dual-Environment Runtime Guard (Cloud GPU vs Local CPU)
Untuk notebook deep learning / visi-bahasa yang dijalankan lintas lingkungan (Colab/Kaggle GPU vs Workstation Lokal CPU):
1. **Deteksi Perangkat Otomatis**:
   ```python
   device = "cuda" if torch.cuda.is_available() else "cpu"
   ```
2. **Komentar Ponytail untuk Fallback Terencana**:
   Gunakan format komentar baku untuk menyederhanakan eksekusi lokal:
   ```python
   # ponytail: fallback ke CPU dan mock inferensi jika CUDA nihil, upgrade ke GPU T4 saat di Colab
   ```
3. **Pin Versi Library Kritis di Lingkungan Colab**:
   Untuk mencegah konflik C-API (misal PaddlePaddle dengan NumPy 2.x):
   ```bash
   !pip install "numpy<2.0.0" "paddleocr>=2.7.0" "transformers>=4.45.0"
   ```

## 3. Pytest Scope Isolation pada Repositori Riset
Saat root repositori memuat folder referensi luar (seperti `REFERENSI CODE/` atau submodule):
- Dilarang menjalankan bare `pytest` tanpa argumen karena akan memindai seluruh folder asing dan memicu `ModuleNotFoundError`.
- Wajib eksekusi `pytest tests/` secara spesifik atau atur `testpaths = ["tests"]` pada konfigurasi `pytest.ini`.

## 4. Specification Parity & Split Guard
Sebelum mengeksekusi benchmark evaluasi batch:
- Wajib verifikasi jumlah baris `dataset/splits/test.csv` sama persis dengan angka data uji pada dokumen rencana dan spesifikasi.
- Jika terjadi perluasan master dataset, amankan partisi lama ke `dataset/archive/`, lakukan re-split anti-bocor (70:15:15), dan sinkronkan seluruh dokumen secara atomik sebelum tahap evaluasi dimulai.

## 5. Pencegahan Kebocoran Data Prapemrosesan (Stateless Preprocessing Invariant)
- Seluruh tahapan prapemrosesan dan pembersihan string (kanonisasi merek, parsing regex kuantitas netto, taksonomi tipe produk) yang dieksekusi sebelum fungsi splitting wajib bersifat *stateless* (murni fungsi baris-per-baris).
- Dilarang menghitung atau menerapkan statistik agregat korpus (seperti frekuensi kosakata, IDF, atau mean/std scaling) pada seluruh dataset sebelum partisi train/val/test dipisahkan.

## 6. Multi-Environment Python Toolchain Discovery
- Pada workstation Windows multi-environment, selalu verifikasi path Python yang memuat pustaka domain (seperti `cv2`, `torch`, `rapidocr`) via command probe `python.exe -c "import cv2..."` sebelum mengeksekusi pipeline atau test runner, bukan berasumsi pada python default shell.
