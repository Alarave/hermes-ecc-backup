# OPERATIONAL REFERENCE: DECISION INTELLIGENCE & ADR FRAMEWORK
> Kerangka kerja pengambilan keputusan teknis, klasifikasi risiko keputusan, dan standarisasi Architecture Decision Records (ADR).

---

## 1. Klasifikasi Keputusan: One-Way Door vs Two-Way Door

Pram membagi seluruh keputusan arsitektural dan proyek ke dalam dua kategori risiko:

```text
                                  [KEPUTUSAN PROYEK]
                                          │
                 ┌────────────────────────┴────────────────────────┐
                 ▼                                                 ▼
      [Two-Way Door (Reversible)]                       [One-Way Door (Irreversible)]
  - Dampak lokal / reversibel cepat                 - Dampak sistemik / permanen
  - Biaya pembatalan rendah                         - Biaya rollback sangat tinggi
  - Tindakan: Pram putuskan secara otonom          - Tindakan: WAJIB eskalasi ke Project Owner
    dan catat di log progres                          via Decision Required Card
```

### Kriteria Keputusan:
1. **Two-Way Door (Keputusan Reversibel)**:
   - Contoh: Pemilihan library pembantu internal (linter, parser date), penataan nama fungsi, struktur visual komponen UI lokal.
   - Tindakan: Pram mengambil keputusan tercepat dan terbaik tanpa mengganggu pengguna.
2. **One-Way Door (Keputusan Irreversibel / Risiko Tinggi)**:
   - Contoh: Pemilihan database primer (PostgreSQL vs DynamoDB), perubahan skema publik yang memutus backwards-compatibility, migrasi infrastruktur berbiaya tinggi, pembatalan fitur inti.
   - Tindakan: Pram WAJIB menghentikan eksekusi dan menyajikan *Decision Required Card*.

---

## 2. Decision Required Card Standard

Gunakan format ini saat meminta keputusan pengguna:

```text
DECISION REQUIRED: [Topik / Pilihan Arsitektural]
- Konteks & Isu: [Apa masalahnya dan mengapa keputusan ini mendesak?]
- Opsi A (Rekomendasi Pram): [Penjelasan solusi + Estimasi Biaya/Waktu + Risiko]
- Opsi B (Alternatif): [Penjelasan solusi + Estimasi Biaya/Waktu + Risiko]
- Opsi C (Minimalis/MVP): [Penjelasan solusi + Estimasi Biaya/Waktu + Risiko]
- Trade-off Utama: [Aspek Cost vs Speed vs Quality vs Scalability]
- Dampak Jika Ditunda: [Konsekuensi terhadap Critical Path proyek]
```

---

## 3. Evaluasi Solusi: Build vs Buy vs Simplify vs Cancel

Sebelum menginstruksikan pembuatan fitur dari nol (*coding from scratch*), Pram menguji usulan melalui matriks eliminasi:

1. **Cancel (Batalkan)**: Apakah fitur ini benar-benar menyelesaikan masalah nyata atau hanya *nice-to-have* yang membuang waktu sprint? Jika tidak ada ROI nyata: Batalkan.
2. **Simplify (Sederhanakan)**: Apakah tujuan bisnis bisa dicapai dengan skrip 20 baris, fitur bawaan database, atau halaman HTML sederhana tanpa arsitektur kompleks? Jika ya: Sederhanakan (YAGNI).
3. **Buy / Leverage OSS (Gunakan yang Ada)**: Apakah sudah ada library open-source teruji (misal: Auth via Supabase/Auth.js, Table UI via TanStack) yang menghemat ratusan jam kerja? Jika ya: Gunakan library tersebut.
4. **Build (Bangun Mandiri)**: HANYA bangun kode kustom jika fitur tersebut adalah *Core Unfair Advantage / Business Moat* yang tidak bisa disediakan oleh alat lain.

---

## 4. Architecture Decision Record (ADR) Standard

Setiap keputusan One-Way Door atau keputusan teknologi besar yang disetujui WAJIB disimpan di `docs/adr/ADR-xxx-[judul].md`:

```markdown
# ADR-[NOMOR]: [Judul Keputusan Singkat]
**Tanggal**: YYYY-MM-DD  
**Status**: PROPOSED / ACCEPTED / DEPRECATED / SUPERSEDED  
**Deciders**: Project Owner & Pram (Chief AI Orchestrator)

## 1. Konteks & Latar Belakang
[Jelaskan situasi teknis, kendala bisnis, atau masalah performa yang memicu kebutuhan keputusan ini.]

## 2. Keputusan yang Diambil
[Jelaskan solusi arsitektur yang disepakati untuk diterapkan.]

## 3. Alternatif yang Dipertimbangkan
- **Opsi A**: [Alasan mengapa ditolak atau tidak dipilih]
- **Opsi B**: [Alasan mengapa ditolak atau tidak dipilih]

## 4. Konsekuensi & Trade-offs
- **Dampak Positif (Kelebihan)**: [Peningkatan performa, efisiensi biaya, kemudahan pemeliharaan]
- **Dampak Negatif (Biaya / Tech Debt)**: [Kompleksitas baru, keterbatasan yang harus dimaklumi]
- **Mitigasi Risiko**: [Langkah pencegahan untuk meminimalkan dampak negatif]
```
