# CHANGELOG

Semua perubahan pada skill `reverse-engineer-anything` dicatat di berkas ini.

## [1.0.0] - 2026-10-17
### Added
- Inisialisasi rilis modul hasil adaptasi framework terbuka morluto/rea.
- Arsitektur 4 pilar RCCO (Role, Context, Constraints, Output).
- 4 Mode Operasional: Analisis JS/Electron/ASAR, Metadata Biner (Go/Rust/PE), Dekompiler Handoff, dan Alur Kerja CLI Terisolasi.
- Dokumen referensi: `javascript-and-electron.md`, `native-binaries-and-pe.md`, dan `cli-tool-workflows.md`.
- Skenario pengujian regresi dan daftar periksa validasi kesiapan produksi.
- Dataset evaluasi empiris `evals/evals.json`.
- Kepatuhan penuh terhadap standar mutu anti-leakage PII dan larangan em/en dash.
