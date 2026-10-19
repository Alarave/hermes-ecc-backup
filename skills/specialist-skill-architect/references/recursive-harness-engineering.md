# Rekayasa Harness Rekursif Agen Cerdas (recursive-harness-engineering)

Dokumen rujukan operasional perancangan, optimalisasi, dan evolusi rekursif sistem lingkungan agen (*agent harness*) berbasis metodologi Google Research Harness² (arXiv:2610.14224, Oktober 2026). Disesuaikan untuk engine arsitek skill Asep (`specialist-skill-architect` dan `spesialis-skills`) pada ekosistem Hermes.

---

## 1. Landasan Konseptual: Mengapa Harnessing Rekursif?

Dalam pengembangan sistem agen cerdas (*agentic AI*), performa penyelesaian tugas kompleks tidak hanya ditentukan oleh ukuran atau bobot model dasar (*foundation model*). Ketika bobot model dibekukan (*frozen weights*), kapabilitas agen dioptimalkan secara dinamis melalui rekayasa sistem di sekeliling model, yang disebut sebagai **Harness**.

### Prinsip Inti Harness²
1. **Model Weights Fixed**: Inferensi mengandalkan model yang sudah ada tanpa fine-tuning berbiaya tinggi.
2. **Harnessing as Optimization**: Peningkatan performa dilakukan dengan merekayasa prompt, tools, memori, skrip, dan modul kapabilitas.
3. **Contrastive Feedback**: Evaluasi keberhasilan kandidat harness didasarkan pada perbandingan kontras jejak eksekusi (*behavioral traces*) antara solusi yang berhasil dan yang gagal, tanpa memerlukan anotasi kebenaran mutlak (*ground-truth labels*).

---

## 2. Taksonomi 8 Komponen Harness Agen (The C1-C8 Surface)

Berdasarkan spesifikasi arsitektur Google Harness², lingkungan kerja agen didekomposisi menjadi 8 komponen modular:

| Kode | Komponen | Peran Runtime | Implementasi pada Ekosistem Hermes / ECC |
|---|---|---|---|
| **C1** | `system_prompt` | Konstruksi Konteks Global | Persona dasar, instruksi peran (Role), dan batasan sistem utama. |
| **C2** | `guardrails` | Regulasi Keamanan & Integritas | Aturan pembatas tindakan berbahaya, fact-forcing gates (`gateguard`), dan filter linter sebelum commit. |
| **C3** | `memory` | Retensi Fakta Persisten | Memori jangka panjang lintas sesi (`MEMORY.md` untuk lingkungan dan `USER.md` untuk preferensi pengguna). |
| **C4** | `skills` | Pengetahuan Prosedural Domain | Modul keahlian berstandar format RCCO (`skills/<name>/SKILL.md` dan folder `references/`). |
| **C5** | `tool_guidance` | Kontrak Antarmuka Alat | Panduan pemanggilan tools, spesifikasi skema JSON parameter, dan alur fallback MCP. |
| **C6** | `scripts` | Eksekutor Deterministik | Skrip Python/Bash fisik mandiri di subdirektori `scripts/` untuk otomasi yang tidak boleh bergantung pada tebakan LLM. |
| **C7** | `subagents` | Orkestrasi Delegasi Tugas | Pembagian inisiatif kerja ke profil agen spesialis terisolasi (`agents/` atau delegasi multi-agen). |
| **C8** | `plugins` | Middleware & Interceptor | Skrip hook event-driven, pre-execution validator, dan parser laporan. |

---

## 3. Protokol Dua Tingkat Rekursi (Two-Level Recursion Protocol)

Evolusi harness beroperasi dalam dua horizon waktu yang saling menguatkan:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ TINGKAT 1: Task-Level Recursion (Propose - Probe - Compose)                 │
│                                                                             │
│  [Task Input]                                                               │
│       │                                                                     │
│       ▼                                                                     │
│  ┌───────────┐      ┌───────────┐      ┌───────────┐      ┌──────────────┐  │
│  │  PROPOSE  │ ──►  │   PROBE   │ ──►  │  CONTRAST │ ──►  │   COMPOSE    │  │
│  │ (Mutasi)  │      │ (Uji Coba)│      │ (Analisis)│      │ (Adopsi Fitur│  │
│  └───────────┘      └───────────┘      └───────────┘      └──────────────┘  │
│                             │                 ▲                             │
│                             └─────────────────┘                             │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ (Kandidat Unggul Terverifikasi)
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ TINGKAT 2: Harnessing-Level Recursion (Cumulative Memory & Skill Evolution) │
│ - Simpan temuan empiris ke dokumen referensi modular                        │
│ - Kunci stabilitas fungsional via validasi strict                           │
│ - Tugas masa depan mewarisi peningkatan secara permanen                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Task-Level Recursion: Siklus Propose-Probe-Compose (PPC)

#### Langkah 1: PROPOSE (Perumusan Kandidat Solusi)
- Analisis kegagalan atau kebutuhan baru pada tugas aktif (misal: teks terpotong, parsing tanggal gagal, linter terlalu longgar).
- Terapkan kontrak **omitted-is-inherited**: hanya formulasikan perubahan pada komponen yang bermasalah (misal: C6 skrip dan C4 referensi skill), jangan merombak komponen lain yang sudah stabil.

#### Langkah 2: PROBE (Pengujian Terisolasi Tanpa Efek Samping)
- Dilarang langsung mengubah kode di repositori produksi secara sembrono.
- Gunakan area kerja terisolasi (*scratchpad* / `cache/scratch/`).
- Jalankan skrip probe dan kumpulkan bukti perilaku nyata:
  * Apakah skrip berjalan tanpa error (exit code 0)?
  * Apakah output memenuhi batas toleransi matematis?
  * Apakah linter mendeteksi anomali?

#### Langkah 3: CONTRAST (Analisis Komparatif Perilaku)
- Bandingkan jejak eksekusi sebelum perbaikan (*baseline trace*) dengan jejak eksekusi kandidat baru (*candidate trace*).
- Identifikasi apakah perubahan menyelesaikan masalah tanpa menimbulkan regresi (*side-effects*) pada fitur lain.

#### Langkah 4: COMPOSE (Sintesis & Adopsi Solusi)
- Susun versi final berkas dengan menggabungkan perbaikan yang telah terbukti unggul secara objektif.
- Terapkan aturan *Token Budget Defense*: hapus kode atau teks instruksi yang redundan.

---

### 3.2 Harnessing-Level Recursion (Evolusi Kumulatif Jangka Panjang)

Setelah sebuah tugas berhasil diselesaikan dan diverifikasi:
1. **Refleksi Berbasis Bukti**: Ekstrak aturan deterministik yang dipelajari selama penanganan tugas (contoh: formula padding minimal kanvas, batas toleransi overlap teks).
2. **Dokumentasi Modular**: Simpan temuan ke dalam subfolder `references/` pada skill yang bersangkutan, bukan menumpuk teks raksasa di `SKILL.md` utama.
3. **Penyelarasan Pemicu (Trigger Alignment)**: Perbarui kata kunci deskripsi agar skill otomatis terpanggil saat menghadapi kasus serupa di masa mendatang.

---

## 4. Dua Mode Skalabilitas Rekursi (Scaling Recursion)

Google Harness² membuktikan bahwa eksplorasi rekursif dapat diskalakan melalui dua pendekatan:

### A. Parallel Recursion (Eksplorasi Melebar)
- *Kapan Digunakan*: Menghadapi domain atau format tugas baru yang belum pernah ditemui sebelumnya.
- *Mekanisme*: Menghasilkan $k$ variasi kandidat harness yang independen (misal: membandingkan pendekatan regex vs modul LLM vs detektor visual), menguji seluruh variasi secara paralel, lalu mengambil elemen terbaik dari masing-masing kandidat untuk dikomposisikan.
- *Karakteristik*: Menghindari jebakan optimum lokal (*local minima*), mengeksplorasi ruang solusi secara luas.

### B. Sequential Recursion (Penyempurnaan Mendalam)
- *Kapan Digunakan*: Mengoptimalkan atau memperbaiki bug pada alur kerja yang arsitekturnya sudah mapan.
- *Mekanisme*: Menjalankan siklus Propose-Probe-Compose bertahap secara berurutan. Setiap tahap $k$ membawa akumulasi bukti dan perbaikan dari tahap $k-1$.
- *Karakteristik*: Sangat presisi, minim gangguan terhadap sistem yang berjalan, dan hemat token komputasi.

---

## 5. Kaidah Anti-Overengineering (Anti-YAGNI Gates)

Untuk mencegah pemborosan token dan kompleksitas kode yang tidak perlu:

1. **Prinsip Tangga Solusi (The Solution Ladder)**:
   - Tingkat 1: Apakah masalah ini perlu dibuatkan solusi baru? (YAGNI).
   - Tingkat 2: Apakah pustaka standar Python/OS sudah menyediakannya? Gunakan stdlib terlebih dahulu.
   - Tingkat 3: Apakah pustaka yang sudah terpasang sudah bisa menyelesaikannya? Dilarang menambah dependensi baru jika 10 baris skrip Python mandiri sudah cukup.
   - Tingkat 4: Jika harus menambah kode, buat diff terpendek yang bekerja secara deterministik.
2. **Larangan Simulasi Fiktif**: Dilarang mengarang hasil eksekusi pengujian. Seluruh klaim keberhasilan harness wajib didukung oleh log eksekusi terminal atau artefak berkas fisik di disk.
3. **Pembersihan Berkas Temporer**: Berkas uji coba di `cache/scratch/` wajib dihapus setelah fase probe selesai agar lingkungan kerja tetap higienis.

---

## 6. Prosedur Audit Mutu Harness Baru

Sebelum sebuah harness atau pembaruan skill disahkan oleh Asep, jalankan checklist 5-titik:

- [ ] **Validasi Format RCCO**: Memiliki blok Role, Context, Constraints, dan Output Format yang tegas.
- [ ] **Uji Linter Ketat**: Lolos eksekusi `python skills/specialist-skill-architect/scripts/validate_skill.py <path> --strict`.
- [ ] **Uji Audit Kontributor**: Lolos eksekusi `python scripts/audit_incoming_skills.py <path>/SKILL.md`.
- [ ] **Kebersihan Tipografi**: Bebas dari karakter ilegal em-dash (`\u2014`) dan en-dash (`\u2013`).
- [ ] **Ketersediaan Fisik**: Seluruh skrip pembantu di `scripts/` dan dokumen rujukan di `references/` tersimpan secara nyata di disk.
