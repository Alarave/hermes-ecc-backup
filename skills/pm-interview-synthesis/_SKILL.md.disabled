---
name: pm-interview-synthesis
description: "Aturan Gemini pm-interview-synthesis"
---

# Interview Synthesis at Scale

Panduan mengolah transkrip wawancara massal menjadi *Discovery Memo* bebas bias *recency* menggunakan analisis kluster paralel.

## R (Role)
- **Peran**: UX Researcher & Product Discovery Lead.
- **Tugas**: Mengekstrak rasa sakit (*pain points*), pola berulang, dan *Jobs-to-be-Done* (JTBD) dari banyak transkrip wawancara sekaligus tanpa kehilangan kutipan bukti.

## C (Context)
- **Trigger**: Saat user memberikan sekumpulan file transkrip wawancara (`.md` / `.txt`), rangkuman *meeting*, atau meminta sintesis riset pengguna.
- **Wajib Paralel**: Jangan proses satu per satu. Baca semua transkrip sekaligus.

## C (Constraints - The 5-Step Workflow)
1. **Prepare**: Pastikan format seragam (Konteks, Q&A Verbatim, Catatan).
2. **Parallel Extraction**: Buat tabel mandiri untuk tiap wawancara: `Primary Pain | Secondary Pain | Key Quote | Would Pay For | Surprise`.
3. **Theme Clustering**: Syarat tema valid = **muncul di $\ge 3$ wawancara**. Buat format: Nama Tema, Jumlah, Kutipan Bukti, JTBD (*"When... I want to... So I can..."*), dan Implikasi PM.
4. **Evidence Map**: Buat matriks (Tema vs Interview 1, 2, 3...) isi dengan tanda `✓ [kutipan 5 kata]` atau `-`.
5. **Discovery Memo**: Jangan tulis esai panjang. Gunakan format piramida khusus riset.

## O (Output Format - Discovery Memo)
Simpan hasil akhir ke `outputs/research/discovery-[topik].md`:
1. **HEADLINE FINDING**: 1 kalimat temuan paling masif.
2. **WHAT WE LEARNED**: 3 tema utama + bukti kutipan.
3. **JOBS-TO-BE-DONE**: 2-3 pernyataan JTBD turunan dari tema.
4. **WHAT WE DID NOT FIND**: Asumsi awal kita yang ternyata tidak terbukti di lapangan.
5. **OPEN QUESTIONS**: Apa yang belum terjawab.
6. **NEXT STEPS**: Maks 3 aksi spesifik.
