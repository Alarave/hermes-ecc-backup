# OPERATIONAL REFERENCE: CONTEXT ENGINEERING & PROGRESSIVE DISCLOSURE
> Panduan operasional komprehensif Specialist Skill Architect untuk mengoptimalkan efisiensi context window, menerapkan teknik pemuatan bertahap (Progressive Disclosure), dan mengelola Task Ledger terstruktur.

---

## 1. Tantangan Efisiensi Jendela Konteks (Context Window Optimization)

Jendela konteks (*Context Window*) model bahasa besar adalah sumber daya yang terbatas dan berbiaya mahal. Memuat instruksi teknis ribuan kata ke dalam konteks pada setiap giliran obrolan memicu tiga dampak buruk:
1. **Biaya Token Membengkak**: Setiap giliran percakapan menghitung ulang token instruksi panjang yang tidak relevan.
2. **Degradasi Perhatian Model (Attention Dilution)**: Semakin panjang teks yang tidak relevan di dalam konteks, semakin rentan model mengabaikan instruksi penting atau mengalami halusinasi.
3. **Kompaksi Konteks Prematur**: Runtime terpaksa memangkas riwayat obrolan (*context compaction*) lebih cepat, menghapus fakta berharga dari percakapan sebelumnya.

Specialist Skill Architect menerapkan prinsip **Pemuatan Bertahap Berbasis Kebutuhan (*Just-In-Time Progressive Disclosure*)**.

---

## 2. Arsitektur Pemuatan 3 Tingkat (3-Tier Progressive Loading)

Mengadopsi standar arsitektur Agent Skills dan riset Vibe-Skills (penghematan token hingga 29.6%):

```text
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 1: METADATA FILTER RINGKAS (~100 token)                           │
│ - Selalu ada di context window utama.                                  │
│ - Memuat atribut 'name' dan 'description' (frasa pemicu).              │
│ - Digunakan oleh Intent Translator untuk memilih kandidat skill.       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                         (Jika Skill Terpilih)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 2: SKILL.md KERNEL UTAMA (< 5.000 token)                          │
│ - Dimuat ke dalam context HANYA saat skill aktif dipicu.               │
│ - Memuat identitas Role, ringkasan mode kerja, aturan inti (RCCO),     │
│   dan daftar modul referensi yang tersedia.                            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                         (Jika Butuh Prosedur Spesifik)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ TIER 3: MODUL REFERENSI MENDALAM (On-Demand References)                 │
│ - Berkas di direktori `references/*.md`.                               │
│ - Dimuat HANYA saat agen menjalankan fase kerja spesifik               │
│   (misal: `quality-assurance.md` hanya dimuat saat fase verifikasi).   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Spesifikasi Paket Konteks Tugas (Context Pack Schema)

Ketika agen spesialis didelegasikan sebuah tugas oleh Orchestrator, agen tersebut TIDAK BOLEH dikirimi tumpukan riwayat chat mentah (*chat history dump*). Arsitek menetapkan format baku **Context Pack** mandiri:

```markdown
# CONTEXT PACK: [TASK-ID] - [NAMA TUGAS]

## 1. Identitas & Tujuan Inti
- **Task ID**: TSK-001
- **Skill Spesialis**: specialist-skill-architect
- **Objektif**: Bangun modul referensi tool routing untuk integrasi terminal.

## 2. Batasan Ruang Lingkup
- **In-Scope**: Menulis panduan tool-routing.md dengan tabel fallback dan prinsip zero-fabrication.
- **Hard Out-of-Scope**: Tidak boleh mengubah konfigurasi linter global scripts/audit_incoming_skills.py.

## 3. Input Artefak & Kontrak Data
- **Berkas Masukan**: `skills/specialist-skill-architect/SKILL.md`
- **Hash Kontrak**: [SHA-256 terverifikasi jika ada]

## 4. Batasan Teknis & Lingkungan
- Host Windows 11, terminal MSYS bash, dilarang tanda pisah em dash atau en dash.
- Bahasa Indonesia baku mematuhi EYD V dan KBBI.

## 5. Kriteria Penerimaan & Definition of Done (DoD)
- Berkas fisik `references/tool-routing.md` terbit di disk.
- Lolos audit linter skor 100/100.
```

---

## 4. Pengelolaan Buku Besar Tugas (Task Ledger Architecture)

Untuk menjaga kesinambungan progres kerja lintas compactions atau lintas giliran obrolan yang panjang, status pekerjaan disimpan dalam berkas status lokal `Task Ledger` (`.task_ledger.json` atau `TASK_STATE.md`).

Parameter yang wajib dicatat di Task Ledger:
1. **Fakta Terverifikasi (Verified Facts)**: Informasi yang telah dibuktikan lewat eksekusi terminal atau inspeksi berkas nyata.
2. **Asumsi Kerja (Working Assumptions)**: Asumsi sementara yang digunakan agen namun belum dibuktikan secara empiris.
3. **Keputusan Disetujui (Approved Decisions)**: Keputusan arsitektur yang telah disahkan pengguna.
4. **Isu Terbuka (Unresolved Issues / Blockers)**: Kendala yang masih menunggu data atau tindakan perbaikan.