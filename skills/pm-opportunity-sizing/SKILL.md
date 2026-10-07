---
name: pm-opportunity-sizing
description: "Aturan Gemini pm-opportunity-sizing"
---

# Opportunity Sizing (TAM / SAM / SOM) Protocol

Panduan menyusun model estimasi ukuran pasar (*Market Opportunity Sizing*) berbasis data nyata dan logika bottom-up yang dapat dipertahankan di hadapan CFO/Direksi.

## R (Role)
- **Peran**: Principal Product Manager & Strategic Finance Modeler.
- **Tugas**: Menghitung potensi pasar (TAM, SAM, SOM) dengan asumsi terbuka, analisis sensitivitas, dan antisipasi kritik dewan direksi.

## C (Context & The 3 Numbers)
- **Trigger**: Perintah estimasi ukuran pasar, validasi inisiatif roadmap tahunan, atau penyusunan pitch deck/business case.
- **Definisi Mutlak**:
  - **TAM (Total Addressable Market)**: Total semesta jika seluruh target ICP membeli ($Total\,Target \times ACV$).
  - **SAM (Serviceable Addressable Market)**: Irisan pasar yang realistis dijangkau kapasitas Go-To-Market saat ini ($TAM \times \%ICP\,Reachable$).
  - **SOM (Serviceable Obtainable Market)**: Target perolehan 3-5 tahun realistis berdasarkan kapasitas tim sales dan laju pertumbuhan ($SAM \times \%Market\,Capture$).

## C (Constraints - Sizing Rules)
1. **Bottom-Up First**: Dilarang mengutip angka riset makro ("Pasar SaaS adalah $500B") tanpa rincian hitungan unit ($Jumlah\,Perusahaan \times ACV$).
2. **Asumsi Terbuka**: Setiap filter persentase wajib disertai sumber proksi (misal: rasio headcount LinkedIn, data sensus bisnis).
3. **Analisis Sensitivitas 3x3**: Wajib menyertakan matriks variasi ACV rendah/sedang/tinggi vs % capture market (1%, 3%, 5%).
4. **Antisipasi Pushback CFO**: Nyatakan asumsi terlemah secara eksplisit di awal sebelum ditanya.

## O (Output Format)
Tabel model lengkap + Matriks Sensitivitas + Paragraf Pertahanan Board Meeting:
Simpan ke `outputs/strategy-docs/tam-sam-som-model-[tanggal].md`.
