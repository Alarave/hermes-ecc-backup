# OPERATIONAL REFERENCE: EVAL-DRIVEN SKILL BENCHMARKING (A/B TESTING & EMPIRICAL EVALS)
> Panduan operasional Specialist Skill Architect untuk pengujian empiris specialist skill berbasis standar terbuka agentskills.io, perbandingan A/B terisolasi, skema evals.json, dan pengukuran presisi pemicu.

---

## 1. Filosofi Pengujian Empiris (Empirical Verification Over Assumptions)

Sebuah specialist skill tidak boleh dirilis ke lingkungan produksi hanya berdasarkan asumsi bahwa instruksi sudah ditulis dengan baik. Sesuai standar industri terbuka (agentskills.io dan Anthropic Agent Skills Specification), mutu sebuah skill diuji pada dua sumbu terpisah:
1. **Presisi Pemicu (Trigger Precision & Leakage)**:
   - *Hit Rate*: Persentase skill terpicu saat menerima prompt yang seharusnya mengaktifkan skill.
   - *Leakage Rate (False Positive)*: Persentase skill terpicu secara salah saat prompt di luar lingkup domain (adversarial negative prompts).
2. **Mutu Luaran & Efisiensi Biaya (Output Quality & Context ROI)**:
   - *Pass Rate Delta*: Peningkatan keberhasilan tugas dengan skill (with-skill) dibandingkan tanpa skill (without-skill / baseline).
   - *Token & Time Overhead*: Biaya tambahan konsumsi token dan durasi eksekusi yang dibutuhkan untuk memuat instruksi dan berkas referensi.

---

## 2. Struktur Direktori Standar Evals

Setiap skill berbobot tinggi menyimpan dataset evaluasi pada folder `evals/`:

```text
skills/<nama-skill>/
├── SKILL.md
├── references/
├── evals/
│   ├── evals.json             # Dataset uji: prompt, masukan, ekspektasi, dan asersi
│   └── iterations/            # Laporan artefak hasil run A/B testing
│       ├── iteration-1/
│       │   ├── benchmark.json # Rekapitulasi pass rate, token, dan durasi
│       │   ├── grading.json   # Skor detail per kasus uji
│       │   ├── with_skill/    # Log eksekusi dengan skill aktif
│       │   └── without_skill/ # Log eksekusi baseline tanpa skill
```

---

## 3. Skema Baku Berkas `evals/evals.json`

Berkas `evals/evals.json` memuat kasus uji representatif dengan asersi terverifikasi:

```json
{
  "skill_name": "spesialis-skills",
  "version": "2.0.0",
  "evals": [
    {
      "id": "EVAL-01",
      "name": "trigger-accuracy-happy-path",
      "prompt": "tolong buatkan skill baru untuk ekstraksi laporan keuangan bank",
      "type": "trigger_positive",
      "expected_activation": true,
      "assertions": [
        {
          "id": "A1",
          "text": "Skill terpicu otomatis dari intent pembuatan skill baru",
          "weight": 1.0
        },
        {
          "id": "A2",
          "text": "Mengaktifkan Mode B (CREATE) dan menerapkan standar RCCO",
          "weight": 1.0
        }
      ]
    },
    {
      "id": "EVAL-02",
      "name": "trigger-leakage-negative-test",
      "prompt": "buatkan kode python sederhana untuk menjumlahkan dua angka",
      "type": "trigger_negative",
      "expected_activation": false,
      "assertions": [
        {
          "id": "A1",
          "text": "Skill TIDAK terpicu karena permintaan hanya berupa koding matematika sepele",
          "weight": 1.0
        }
      ]
    },
    {
      "id": "EVAL-03",
      "name": "output-conformance-rcco",
      "prompt": "desain skill validator data csv",
      "type": "output_quality",
      "expected_activation": true,
      "assertions": [
        {
          "id": "A1",
          "text": "Menghasilkan berkas SKILL.md fisik dengan struktur RCCO lengkap",
          "weight": 1.0
        },
        {
          "id": "A2",
          "text": "Frontmatter YAML valid dengan name kebab-case dan deskripsi tajam",
          "weight": 1.0
        },
        {
          "id": "A3",
          "text": "Bebas karakter tipografi tanda pisah em-dash atau en-dash",
          "weight": 1.0
        }
      ]
    }
  ]
}
```

---

## 4. Protokol Pengujian A/B Terisolasi (Isolated A/B Testing Protocol)

Langkah eksekusi evaluasi empiris:
1. **Pemisahan Konteks**: Setiap pengujian dijalankan pada sesi runtime bersih tanpa memori sisa dari percakapan sebelumnya.
2. **Eksekusi Ganda (Paired Runs)**:
   - *Run 1 (Baseline / Without-Skill)*: Kirim prompt ke agen tanpa menginjeksikan berkas SKILL.md.
   - *Run 2 (Intervensi / With-Skill)*: Kirim prompt yang sama dengan SKILL.md aktif.
3. **Penilaian Asersi (Assertion Grading)**:
   - Evaluasi setiap butir asersi dengan status PASS atau FAIL berdasar bukti fisik.
   - Hitung nilai agregat: `Pass Rate = (Total Asersi PASS) / (Total Asersi Diuji)`.
4. **Kompilasi Metrik `benchmark.json`**:

```json
{
  "timestamp": "2026-10-17T12:00:00Z",
  "configurations": {
    "without_skill": {
      "pass_rate": 0.35,
      "avg_tokens": 1200,
      "avg_duration_sec": 8.5
    },
    "with_skill": {
      "pass_rate": 0.95,
      "avg_tokens": 2800,
      "avg_duration_sec": 14.2
    }
  },
  "delta": {
    "pass_rate_uplift": "+0.60",
    "token_overhead": "+1600",
    "verdict": "SHIPPABLE"
  }
}
```

---

## 5. Ambang Batas Kelulusan Rilis (Shipping Gate Criteria)

Sebuah skill dinyatakan layak rilis (SHIPPABLE) jika memenuhi kriteria empiris minimum:
1. **Trigger Hit Rate** >= 90% pada set prompt positif representatif.
2. **Trigger Leakage Rate** <= 5% pada set prompt negatif adversarial.
3. **Pass Rate Uplift** >= +0.30 (30 persen peningkatan akurasi dibanding baseline).
4. **Linter Mutu** 100/100 pada skrip audit proyek (`scripts/audit_incoming_skills.py`).
5. **Zero Typography Violation**: Tidak ada tanda pisah em-dash atau en-dash.
