# Metodologi & Tolok Ukur Evaluasi Memori Agen AI (agent-memory-benchmarks)

Dokumen rujukan metodologi penelitian akademik dan perancangan eksperimen evaluasi sistem memori agen cerdas (*Agentic Memory Systems*). Disusun untuk integrasi Bab 2 (Tinjauan Pustaka) dan Bab 3 (Metodologi Penelitian) pada skripsi, tesis, dan makalah ilmiah bidang Ilmu Komputer dan Kecerdasan Buatan.

---

## 1. Landasan Konseptual: Memori Agen vs Jendela Konteks

Dalam literatur rekayasa sistem agen otonom, terdapat distingsi fundamental antara kapasitas jendela konteks (*context window*) dan arsitektur memori:

### A. Jendela Konteks Statis (Bukan Tolok Ukur Memori)
Pengujian seperti *Needle In A Haystack* (NIAH), RULER, dan LongBench hanya mengukur kemampuan mekanisme atensi model memproses deretan token panjang dalam satu kali inferensi (*single-turn inference*). Pengujian ini tidak mengevaluasi:
- Bagaimana informasi diperbarui saat terjadi perubahan fakta di dunia nyata.
- Bagaimana informasi lama dihapus (*forgetting mechanism* / *unlearning*).
- Bagaimana agen mengingat fakta lintas sesi yang terpisah waktu dan ruang.

### B. Arsitektur Memori Agen Otonom (Tujuan Evaluasi Riil)
Sistem memori agen mencakup penyimpanan eksternal persisten yang terhubung ke model melalui protokol baca-tulis terstruktur (seperti RAG bertingkat, basis data vektor, graf pengetahuan, atau log keadaan terstruktur). Memori ini berfungsi melintasi berbagai sesi independen tanpa bergantung penuh pada pemuatan seluruh riwayat ke dalam jendela konteks.

---

## 2. Taksonomi 11 Tipe Memori Agen AI

Berdasarkan konsensus registri tolok ukur memori agen (207 benchmark ilmiah), evaluasi memori dibagi ke dalam 11 dimensi operasional:

| No | Tipe Memori | Definisi Operasional | Contoh Tolok Ukur Teruji |
|---|---|---|---|
| 1 | `conversational_longterm` | Kemampuan memanggil kembali dan bernalar atas riwayat percakapan panjang multi-sesi | LoCoMo, DolphinBench, LongMemEval |
| 2 | `personalization` | Pemanfaatan preferensi, persona, atau profil unik pengguna untuk mempersonalisasi tindakan | PersonaMem, RealPref, PrefEval |
| 3 | `episodic` | Rekonstruksi urutan peristiwa masa lalu dengan dimensi waktu, lokasi, dan kausalitas | DyadMem, MemTrace, TimeMem |
| 4 | `semantic_knowledge_update` | Pembaruan fakta eksternal saat informasi berubah tanpa merusak bobot dasar model | MemOps, MemAudit, K-Update |
| 5 | `procedural_workflow` | Ekstraksi keahlian, SOP kerja, atau urutan pemanggilan alat dari tugas lama ke tugas baru | ToolBench-Mem, ProcEval |
| 6 | `coding_cross_session` | Retensi struktur basis kode, dependensi, dan keputusan arsitektur lintas sesi koding mandiri | SWE-bench Long, CrossCode |
| 7 | `parametric` | Penanaman memori langsung ke dalam bobot model melalui fine-tuning atau editing pengetahuan | ROME, MEMIT, Test-Time Training |
| 8 | `multi_agent_group` | Sinkronisasi memori bersama (*shared state*) antar-agen dalam percakapan kelompok | GroupMemBench, MultiMem |
| 9 | `multimodal` | Penyimpanan dan penelusuran konten non-teks (citra, audio spektrogram, video) | SuperMemory-VQA, VoxMem |
| 10 | `embodied` | Memori aksi pada agen robotik atau lingkungan simulasi spasial berbasis navigasi | RoboMemArena, WorldMemArena |
| 11 | `memory_security` | Ketahanan memori terhadap serangan injeksi, keracunan data (*poisoning*), dan audit privasi PII | MemOps (Security Probe), HUSH-Bench |

---

## 3. Metrik Evaluasi Komparatif & Rumus Formal

Untuk pengujian saintifik di Bab 4 (Hasil dan Pembahasan), gunakan metrik matematis baku berikut:

### A. Tingkat Akurasi Operasi (*Operation F1-Score*)
Mengukur keseimbangan antara presisi dan recall pada aksi manipulasi memori (*Insert, Update, Delete*):
$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

### B. Rasio Nilai Kedaluwarsa (*Stale Value Rate - SVR*)
Mengukur frekuensi kegagalan sistem ketika agen menjawab menggunakan fakta lama yang telah diperbarui atau dihapus:
$$\text{SVR} = \frac{\sum_{i=1}^{N} \mathbb{I}(\hat{y}_i = y_{\text{stale}})}{N}$$
Di mana $\mathbb{I}$ adalah fungsi indikator, $\hat{y}_i$ adalah jawaban model, dan $y_{\text{stale}}$ adalah nilai lama. Nilai optimal adalah 0.0%.

### C. Rasio Kebocoran Informasi (*Leakage Rate - LR*)
Mengukur probabilitas data sensitif pribadi (PII) dari sesi A muncul pada respons sesi B yang tidak berwenang:
$$\text{LR} = \frac{\text{Jumlah Pelanggaran Privasi Terdeteksi}}{\text{Total Kueri Lintas Sesi}}$$

### D. Skor Validitas Atribusi (*Provenance Support Score*)
Mengukur apakah fakta yang ditarik disertai bukti ID sesi atau ID pesan yang sah secara deterministik:
$$\text{Provenance} = \frac{\text{Fakta Terverifikasi dengan ID Sah}}{\text{Total Fakta yang Diklaim}}$$

---

## 4. Matriks Tingkat Keterulangan Riset (*Reproducibility Hierarchy*)

Saat menyusun tinjauan pustaka dan memilih baseline pembanding, klasifikasikan paper rujukan berdasarkan 4 tingkatan keterulangan bukti:

1. **Tingkat 1 - official_script (Standar Emas)**: Repositori resmi menyediakan skrip runner otomatis lengkap, data evaluasi, dan modul penilaian. Sangat disarankan sebagai baseline utama.
2. **Tingkat 2 - data_public**: Dataset pengujian tersedia publik di repositori terbuka (HuggingFace / Zenodo), namun skrip eksekusi agen harus direkonstruksi mandiri.
3. **Tingkat 3 - paper_only**: Metodologi hanya dijelaskan di naskah paper tanpa rilis data atau kode sumber. Hanya boleh dijadikan rujukan konseptual, bukan baseline numerik langsung.
4. **Tingkat 4 - unverified**: Klaim performa belum memiliki bukti artefak yang dapat diaudit secara independen.

---

## 5. Panduan Penulisan Bab 2 dan Bab 3 Skripsi

### Format Integrasi Bab 2 (Landasan Teori):
- Uraikan evolusi sistem memori dari arsitektur *Vector-Only RAG* (2023) menuju *Episodic-Semantic Hybrid Memory* (2025-2026).
- Sajikan tabel komparasi pendekatan memori berbasis parameter (*fine-tuning*) versus memori eksternal terstruktur (*state database* / *Zettelkasten*).

### Format Integrasi Bab 3 (Metodologi Penelitian):
- Definisikan alur eksperimen: *Data Preprocessing -> Ingestion Phase -> Memory Modification Phase (Insert/Update/Delete) -> Evaluation Probing*.
- Sertakan uji ablasi (*Ablation Study*): bandingkan performa agen pada 3 konfigurasi:
  1. *Baseline*: Agen tanpa memori eksternal (mengandalkan prompt awal saja).
  2. *Naive Long-Context*: Agen dengan seluruh riwayat dimasukkan ke konteks.
  3. *Proposed Architecture*: Agen dengan sistem manajemen memori dinamis terindeks.
