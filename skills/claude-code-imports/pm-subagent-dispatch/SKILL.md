---
name: pm-subagent-dispatch
description: "Dispatch parallel sub-agents for heavy PM workloads such as multi-source analysis."
---

# Parallel Sub-Agent Dispatch Protocol

Panduan mendistribusikan beban kerja PM berat (sintesis 10+ wawancara, audit kompetitor simultan, review 3-kacamata) menjadi tugas paralel terisolasi menggunakan sub-agent.

## R (Role)
- **Peran**: Multi-Agent Orchestrator & Delivery Lead PM.
- **Tugas**: Memecah 1 tugas raksasa menjadi 3-5 sub-task paralel yang berjalan bersamaan, lalu merangkum laporannya menjadi ringkasan eksekutif 5-poin.

## C (Context & Eksekusi)
- **Trigger**: Tugas riset bervolume besar, analisis multi-kompetitor, atau simulasi audit multi-kacamata.
- **Wajib Sub-Agent**: Gunakan alat bawaan `delegate_task` pada sistem untuk menjalankan tugas secara terpisah agar tidak membanjiri memori konteks percakapan utama.

## C (Constraints - 3 Pola Delegasi Paralel)
1. **Multi-Transcript Synthesis**: Delegasikan pembacaan berkas wawancara per sub-agent $\rightarrow$ kumpulkan tabel perbandingan.
2. **Competitor Multi-Scan**: 1 sub-agent per kompetitor (misal: Sub-agent A selidiki Zapier, Sub-agent B selidiki Make, Sub-agent C selidiki ServiceNow) $\rightarrow$ kumpulkan tabel komparasi.
3. **Multi-Perspective PRD Audit**: 1 sub-agent per kacamata ahli (Engineer, UX, CFO).

## O (Output Format - Executive Synthesis)
Setelah semua sub-agent melapor, hasilkan Executive Summary (Maksimal 5 bullet points):
1. Temuan paling krusial lintas analisis.
2. Kontradiksi data yang ditemukan antar sub-agent.
3. Rekomendasi tindakan selanjutnya yang paling masuk akal.
Simpan hasil ke `outputs/research/parallel-synthesis-[tanggal].md`.
