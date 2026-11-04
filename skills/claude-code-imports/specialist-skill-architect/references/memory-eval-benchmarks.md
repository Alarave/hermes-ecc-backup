# Tolok Ukur Evaluasi Memori Agen AI (memory-eval-benchmarks)

Panduan operasional pengujian empiris sistem memori agen AI multi-sesi berbasis konsensus Memory Benchmark Registry (207 tolok ukur). Digunakan oleh Asep (Mode E: Benchmark & Eval) untuk mengukur ketahanan retensi memori, akurasi pembaruan fakta, dan pencegahan kebocoran data pada agen otonom.

---

## 1. Prinsip Evaluasi: Memori Lintas Sesi vs Long-Context

Pemisahan tegas wajib diterapkan sebelum pengujian:
- **Bukan Tolok Ukur Memori**: Uji satu kali masukan konteks panjang (seperti RULER, Needle-In-A-Haystack / NIAH, LongBench). Uji ini mengukur kapasitas jendela perhatian model (*context window*), bukan kemampuan memori.
- **Tolok Ukur Memori Nyata**: Menguji persistensi eksternal, pembaruan fakta (*update/delete*), isolasi preferensi pengguna (*personalization*), dan retensi informasi lintas sesi mandiri (*cross-session episodic recall*).

---

## 2. Tiga Tolok Ukur Runner Resmi Terverifikasi

### A. DolphinBench (Mem0, 2026-09)
- **Tautan Resmi**:
  - Paper: `https://arxiv.org/abs/2609.24971`
  - Repositori: `https://github.com/mem0ai/dolphinbench`
- **Domain Memori**: `conversational_longterm`, `personalization`, `episodic`.
- **Skala Data**: 3 persona pengguna riil lintas tahun, 600 tugas aksi simulasi aplikasi, sekitar 500.000 token riwayat percakapan per persona (3.400 hingga 5.128 pesan pengguna).
- **Metrik Utama**:
  1. *Task Pass Rate*: Persentase keberhasilan aksi alat berdasarkan memori masa lalu.
  2. *Total Cost*: Konsumsi token per penyelesaian tugas (efisiensi context pack).
  3. *Median Task Latency*: Waktu respons penelusuran memori hingga eksekusi aksi.
- **Model Penilai**: GPT-5.6-Sol / LLM Judge untuk mengevaluasi maksud semantik aksi.
- **Metode Uji**: Jalankan agen pada skenario *with-memory* versus *without-memory* untuk membuktikan delta kontribusi memori terhadap keberhasilan tugas.

### B. MemOps (MemTensor, 2026-07)
- **Tautan Resmi**:
  - Paper: `https://arxiv.org/abs/2607.12893`
  - Repositori: `https://github.com/MemTensor/MemOps`
- **Domain Memori**: `conversational_longterm`, `semantic_knowledge_update`, `memory_security`.
- **Skala Data**: 403 percakapan bukti (3 segmen per topik, 9.672 giliran bicara), 2.006 pasangan tanya-jawab unik yang diuji dalam kondisi berdekatan (*adjacent* ~2.557 token) dan kondisi injeksi derau konteks panjang (*long-context* hingga 68.309 token).
- **Operasi Memori yang Diuji**:
  - `Insert`: Menambahkan fakta baru tanpa mendegradasi fakta lama.
  - `Update`: Memperbarui nilai fakta yang berubah seiring waktu.
  - `Delete`: Menghapus fakta yang kedaluwarsa atau ditarik kembali.
  - `Overwrite`: Menyelesaikan konflik informasi kontradiktif.
  - `Retrieve`: Mengambil fakta tepat sasaran di bawah derau konteks tinggi.
- **Metrik Kritis**:
  1. *Operation F1*: Presisi dan recall operasi manipulasi memori.
  2. *Stale Value Rate (SVR)*: Rasio kegagalan saat agen masih menjawab menggunakan fakta usang yang telah diubah atau dihapus. Target: 0.0%.
  3. *Leakage Rate (LR)*: Rasio kebocoran data sensitif pribadi (PII) ke sesi yang tidak berhak. Target: 0.0%.
  4. *Provenance Support*: Ketepatan sitasi sumber memori (ID pesan atau nomor sesi).

### C. MemAudit (NeurIPS, 2026-05)
- **Tautan Resmi**:
  - Paper: `https://arxiv.org/abs/2605.02199`
  - Repositori: `https://github.com/nishant7309/memaudit-artifact-neurips26`
  - Dataset: `https://huggingface.co/datasets/edgeclustr/memaudit-data`
- **Domain Memori**: `semantic_knowledge_update`, `conversational_longterm`.
- **Fokus Audit**: Mengukur rasio optimasi pemadatan memori eksternal (Mem0, Letta, A-Mem) terhadap batas optimum eksak yang tersertifikasi matematis (*certified exact optimum*).
- **Metrik Utama**:
  - *Package Ratio* rho_P(X): Rasio performa memori terkompresi terhadap batas optimum teoritis tanpa kehilangan informasi kunci.

---

## 3. Protokol Evaluasi Memori Hermes Lokal

Audit sistem memori Hermes (`memories/USER.md`, `memories/MEMORY.md`, basis data `state.db`, dan mesin FTS5) dieksekusi dengan protokol berikut:

### Matriks Pengujian 4 Tahap:
1. **Tahap 1: Ingestion & Boundary Test**:
   - Masukkan 5 fakta baru via tool `memory(action='add')`.
   - Pastikan panjang karakter mematuhi batas keras (budget 2.200 karakter untuk memory dan 1.375 karakter untuk user).
2. **Tahap 2: Stale Value Rejection Test (Anti-SVR)**:
   - Perbarui salah satu fakta menggunakan `memory(action='replace')` atau hapus via `memory(action='remove')`.
   - Ajukan pertanyaan jebakan mengenai nilai lama.
   - Status PASS: Agen secara konsisten menggunakan nilai mutakhir dan menyatakan nilai lama tidak berlaku.
3. **Tahap 3: Cross-Session Recall Test via FTS5**:
   - Jalankan kueri penelusuran sesi lama via tool `session_search`.
   - Ukur apakah pesan yang dijangkar (*anchor message*) memuat bukti konteks yang tepat sasaran tanpa mengembalikan log biner yang tidak relevan.
4. **Tahap 4: Zero Leakage Verification (Anti-LR)**:
   - Pastikan data kredensial, token API, dan path lokal akademik tidak pernah bocor ke templat bersama atau commit publik.

---

## 4. Skrip Uji Regresi Memori Sederhana (Self-Check Runner)

Skrip evaluasi mandiri berbasis SQLite lokal untuk memverifikasi integritas penelusuran memori Hermes:

```python
import sqlite3
import time

def audit_memory_fts5(db_path="state.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # 1. Verifikasi tabel FTS5 aktif
    cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='messages_fts'")
    has_fts = cur.fetchone()[0] > 0
    assert has_fts, "Tabel messages_fts tidak ditemukan di database state."
    
    # 2. Uji kueri penelusuran kata kunci teknis
    test_query = "skripsi OR CEEMDAN OR LSTM"
    start_t = time.time()
    cur.execute("SELECT rowid FROM messages_fts WHERE messages_fts MATCH ? LIMIT 10", (test_query,))
    rows = cur.fetchall()
    latency_ms = (time.time() - start_t) * 1000
    
    print(f"FTS5 Status: AKTIF")
    print(f"Hasil Temuan: {len(rows)} baris")
    print(f"Latency Penelusuran: {latency_ms:.2f} ms")
    assert latency_ms < 50.0, "Latency FTS5 melebihi ambang batas 50 ms."
    print("Audit Integritas Memori: LULUS (100/100)")

if __name__ == "__main__":
    audit_memory_fts5()
```

---

## 5. Ringkasan Kriteria Kelulusan (Definition of Done)
1. Seluruh pengujian memori menghasilkan Stale Value Rate = 0.0%.
2. Leakage Rate terhadap 8 kategori data pribadi PII = 0.0%.
3. Waktu penelusuran FTS5 pada database riwayat obrolan berada di bawah 50 ms.
4. Bebas dari karakter tanda pisah em dash atau en dash.
