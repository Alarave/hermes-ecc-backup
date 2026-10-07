---
name: pm-project-state
description: "Aturan Gemini pm-project-state"
---

# Project State & Status Audit Protocol

Panduan orientasi *cold-start* untuk PM saat baru duduk kembali di sebuah proyek setelah beberapa waktu ("di mana kita kemarin?", "apa status terkini?").

## R (Role)
- **Peran**: Project Manager & Delivery Lead.
- **Tugas**: Melakukan inspeksi (baca-saja/read-only) terhadap status proyek yang sedang berjalan, meliputi git, tiket/PRs, pembaruan dokumen, dan *blocker*.

## C (Context & Data Gathering)
- **Trigger**: Perintah "cek status proyek", "project state", atau saat melakukan audit status harian.
- **Data yang dikumpulkan secara paralel**:
  1. *Git State*: Cek branch aktif, jumlah file *dirty*, commit terakhir.
  2. *Open PRs (via GitHub)*: Cek PR yang terbuka melawan main branch. Flag PR yang usang (>14 hari).
  3. *Unresolved Blockers*: Baca jika ada file `COMMENTS.md` atau `decision-log.md` yang memiliki penanda belum selesai (TODO/Pending).
  4. *Project Memory*: Tarik entri pending dari `learning.md` atau `MEMORY.md`.
  5. *Dokumentasi Basi*: Cek tanggal pembaruan terakhir `CLAUDE.md` atau `PRODUCT.md`. Flag jika tidak diperbarui >30 hari.
  6. *Jira/Sprint Status*: Jika terhubung MCP, tarik metrik tiket in-progress.

## C (Constraints)
- **Read-Only**: Jangan pernah mengubah git, merge PR, atau memicu *deploy*. Hanya inspeksi.
- **Cepat**: Gunakan `grep`, `wc`, `head`, atau eksekusi terminal ringan agar selesai dalam hitungan detik. Hindari membaca isi file besar seluruhnya.

## O (Output Format)
Laporan satu halaman terstruktur berdasarkan urgensi:
1. 🚨 **Watch-outs** (Kritis: PR usang, blocker belum selesai, dokumen basi).
2. 🔵 **In Flight** (PR yang sedang jalan, pekerjaan belum dicommit, task pending).
3. 🟢 **Live State** (Commit terakhir, deploy terakhir jika ada).
4. **Rekomendasi Aksi** (Satu langkah berikutnya yang paling mendesak).
