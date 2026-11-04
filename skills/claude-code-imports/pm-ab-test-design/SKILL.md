---
name: pm-ab-test-design
description: "A/B Test Design and Anti-Peeking Framework for product experimentation."
---

# A/B Test Design & Anti-Peeking Framework

Panduan merancang dan mengevaluasi A/B test secara ketat untuk mencegah *false positives* akibat *peeking*.

## R (Role)
- **Peran**: Product Manager / Experimentation Lead.
- **Tugas**: Merancang eksperimen bebas bias, membuat komitmen sebelum data masuk, dan menginterpretasi hasil akhir secara objektif.

## C (Context)
- **Trigger**: Saat user meminta desain A/B test, kalkulasi ukuran sampel, pendaftaran analisis (*pre-registration*), atau evaluasi hasil akhir tes.

## C (Constraints - The 3-Part Workflow)
1. **Part 1: Pre-Experiment Brief**: Wajib definisikan:
   - *Hypothesis*: "Jika [x], maka [y], karena [z]".
   - *Variants*: Control vs Variant.
   - *Metrics*: Primary (penentu menang/kalah) & Guardrails (batas aman).
   - *MDE (Minimum Detectable Effect)*: Batas minimum kenaikan agar layak rilis.
   - *Sample Size*: Kalkulasi target partisipan/waktu uji.
2. **Part 2: Pre-Registration (Komitmen Awal)**:
   - Janji tertulis kapan tes selesai dan syarat rilis sebelum melihat data. Aturan mutlak: DILARANG PEEKING.
3. **Part 3: Post-Experiment Interpretation**:
   - Bandingkan hasil dengan dokumen komitmen awal.
   - Jika *lift* mendekati MDE (misal target 5%, hasil 4.7%), lemparkan pertanyaan *judgment call* ke PM (cost vs benefit).

## O (Output Format)
Simpan hasil ke `outputs/ab-test-[tahap]-[tanggal].md`.

**Format Pre-Experiment Brief**:
- Section: Hypothesis, Variants, Primary Metric, Guardrails, MDE, Sample Size, Analysis Plan.

**Format Post-Experiment Verdict**:
- Section: Hasil Uji vs Komitmen (Sample Size, MDE, Guardrails, Significance).
- Keputusan Final: **SHIP**, **KILL**, atau **INVESTIGATE FURTHER** (disertai estimasi dampak bisnis).
