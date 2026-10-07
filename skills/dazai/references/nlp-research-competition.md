# NLP Research Competition Skill

## Scope
Advisory skill for NLP/ML research projects submitted to academic competitions (USB, GEMASTIK, or similar). Covers: repo analysis, competition requirement mapping, team planning, model architecture explanation, hyperparameter strategy, and data collection.

---

## 1. Repo Gap Analysis (First Step)

When given a GitHub repo, fetch via API — do NOT rely on `@url` mentions (they often return no content):

```python
# Get file tree
curl https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1

# Get raw file content
curl https://raw.githubusercontent.com/{owner}/{repo}/main/{path}
```

Map repo state against deliverable checklist:
- Specs written vs implemented (`specs/` vs `src/`)
- Data files populated vs placeholder (`data/video_list.txt` empty = blocking)
- `project_state.md` filled vs header-only = signals early stage
- `requirements.txt` complete vs missing ML deps

**Pitfall:** `video_list.txt` containing only comment lines (`#`) is EMPTY — check actual URL count, not file existence.

---

## 2. Competition Deliverable Mapping (USB / GEMASTIK Data Mining)

Standard deliverables for Implementasi Data Mining category:

| # | File | Format | Naming |
|---|---|---|---|
| 1 | Proposal | PDF max 20 hal, A4, 1.5 spasi, TNR 12 | `Proposal_DataMining_NamaTim_NamaProduk.pdf` |
| 2 | Poster | PDF A3 (29.7×42cm), max 150MB, 1 halaman | `Poster_DataMining_NamaTim_NamaProduk.pdf` |
| 3 | Presentasi | PPT max 8 slide, max 100MB, **no video/external link** | `Presentasi_DataMining_NamaTim_NamaProduk.ppt` |
| 4 | Video | YouTube Unlisted, max 10 menit, min 1920×1080 FHD 16:9 | `USB 2026 \| Penambangan Data \| NamaTim \| NamaProduk` |
| 5 | Surat Orisinalitas | Materai Rp10.000, tanda tangan ketua | Lampiran 2 |

**Poster wajib: 2 QR code** di footer — (1) link prototype/Streamlit, (2) link video YouTube.

**Video opening wajib:** Logo USB, Logo Universitas, logo produk, nama tim, semua anggota.

**Source code harus siap** — juri bisa minta lihat saat tanya jawab.

### Grading Weights (Penilaian)
| Bobot | Kriteria |
|---|---|
| 25% | Kualitas dataset & ketepatan metode |
| 25% | Implementasi & hasil analisis |
| 20% | Kebaruan & relevansi permasalahan |
| 15% | Manfaat & potensi implementasi nyata |
| 15% | Kemampuan presentasi & penguasaan materi |

**Focus highest-effort on the two 25% criteria.** Systematic hyperparameter tables and confusion matrix per aspect = strong signal for both.

---

## 3. Team Role Assignment (3-Person Team)

| Orang | Peran | Tanggung Jawab |
|---|---|---|
| Ketua (SI) | Lead + ML Engineer | Pipeline model, evaluasi metrik, pimpin presentasi & Q&A |
| Anggota 1 | Data + Preprocessing | Kumpul URL video, run extractor, cleaning/normalisasi, labeling |
| Anggota 2 | Frontend + Deliverables | Streamlit dashboard, poster A3, PPT, edit video YouTube |

Proposal sections dibagi sesuai domain masing-masing.

---

## 4. Hyperparameter Strategy

For small datasets (1k–5k samples), **minimal systematic tuning** is sufficient and safer than exhaustive grid search.

### Wajib di-tune (3×2 grid minimum)
```
Learning rate: [2e-5, 3e-5, 5e-5]
Epochs:        [3, 5]  (tambah 10 jika data > 3k)
Batch size:    [8, 16] tergantung VRAM
```

### Cukup default
```python
weight_decay = 0.01
warmup_ratio = 0.1
scheduler = "linear"
random_seed = 42  # WAJIB — per AGENTS.md
max_seq_length = 128  # komentar YouTube pendek
```

### LoRA (jika Sahabat-AI)
```python
lora_r = [8, 16]   # rank variants
lora_alpha = 32
lora_dropout = 0.1
```

**Pitfall:** Overtune pada dataset kecil = overfit. 3–4 eksperimen dengan tabel metrik lebih convincing ke juri daripada 20+ run tanpa analisis.

### Wajib catat di `outputs/EXPERIMENT_LOGS.md`
```
| Eksperimen | LR   | Epoch | Macro F1 | Precision | Recall | Latency |
|---|---|---|---|---|---|---|
| IndoRoBERTa-A | 2e-5 | 5 | ... | ... | ... | ... |
```

---

## 5. Model Architecture Quick Reference

Full detail in `references/models-absa.md`.

| Dimensi | IndoRoBERTa | Sahabat-AI |
|---|---|---|
| Arsitektur | Encoder-only (BERT family) | Decoder-only (GPT/LLaMA) |
| Ukuran | ~125M params | ~7B params |
| Butuh data berlabel? | Ya (fine-tune) | Tidak (few-shot) |
| GPU minimum | T4 16GB (Colab gratis) | A100 / T4 + 4-bit quant |
| Kecepatan inferensi | Cepat (~10ms/komentar) | Lambat (~500ms–2s) |
| Konsistensi output | Tinggi | Rendah (perlu output parsing) |

**Pipeline yang direkomendasikan:**
1. Sahabat-AI few-shot → label awal (weak supervision)
2. Human audit 20–30% → hitung Cohen's Kappa ≥ 0.61
3. Fine-tune IndoRoBERTa → model produksi
4. Bandingkan keduanya di test set yang sama
5. Deploy model terbaik ke Streamlit

---

## 6. Data Collection: YouTube Comment Extraction

### Target Video Sources
Prioritize high-view videos with many Indonesian comments per brand:
- **Wuling Air EV** — Fitra Eri, OtoDriver, channel resmi Wuling
- **BYD** (M6, ATTO 1) — Om Mobi, Ridwan Hanif, OtoDriver
- **Chery Omoda E5** — OtoDriver, user reviews
- **Neta / SERES** — independent review channels

Target: **≥3.000 komentar total**, distribusi merata antar brand.

To find videos, search YouTube directly via browser tool — web search API often blocked.

**Pitfall:** Juri minta lihat distribusi aspek — pastikan 4 aspek terwakili. Kalau imbalanced, catat di proposal dan gunakan Macro F1 bukan Accuracy.

---

## 7. Meeting Preparation (Rapat Tim)

For first team meeting, prioritize blocking decisions:

1. **API Key** — siapa yang buat di Google Cloud Console?
2. **Target komentar** — berapa minimum? (1k min, 3k ideal)
3. **Single-label atau multi-label?** — menentukan seluruh arsitektur model
4. **Siapa pegang GPU?** — bottleneck training
5. **Siapa isolasi test set?** — kalau bocor, semua hasil tidak valid

Action item langsung: buka `video_list.txt`, tiap anggota cari 5–10 URL video, jalankan extractor, verifikasi CSV.

---

## 8. Sprint Planning (17-Day Example)

```
Hari 1-3:   Kumpul URL, run extractor, kumpulkan raw data
Hari 4-7:   Preprocessing + labeling (weak supervision + manual audit)
Hari 8-11:  Eksperimen model, catat metrik
Hari 12-14: Streamlit dashboard, deploy
Hari 15-17: Tulis proposal, poster, PPT, rekam video, tanda tangan materai
```
