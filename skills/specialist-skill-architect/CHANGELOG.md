# CHANGELOG: SPECIALIST SKILL ARCHITECT

Format pencatatan perubahan berpedoman pada [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) dan menerapkan konvensi [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-14

### Added
- **Rilis Perdana `specialist-skill-architect`**: Arsitek rekayasa siklus hidup specialist skill AI berbasis format RCCO dan konvensi Agent Skills Open Specification.
- **4 Mode Operasional Utama**:
  - `Mode A (EXPLAIN)`: Membedah dan menjelaskan arsitektur serta cara kerja skill eksisting secara mendalam.
  - `Mode B (CREATE)`: Prosedur 12 langkah perancangan dan pembuatan skill baru dari nol.
  - `Mode C (EXTEND)`: Prosedur 10 langkah penambahan kapabilitas baru dengan jaminan backward compatibility.
  - `Mode D (IMPROVE)`: Audit 10 dimensi, refactoring instruksi, dan optimasi efisiensi konteks.
- **11 Modul Referensi Teknis Operasional di `references/`**:
  - `skill-discovery.md`: Prosedur inventarisasi lokal dan gap analysis.
  - `github-research.md`: Standar riset dan penyerapan SOTA dari repositori GitHub bereputasi tinggi.
  - `strategy-selection.md`: Matriks pembobotan pemilihan di antara 7 strategi rekayasa standar.
  - `skill-specification.md`: Spesifikasi teknis penulisan berkas dan konvensi penamaan direktori.
  - `skill-composition.md`: Tata kelola komposisi multi-agen dan konsolidasi skill yang terfragmentasi.
  - `context-engineering.md`: Arsitektur pemuatan bertahap 3-tingkat dan skema Context Pack.
  - `tool-routing.md`: Pemetaan kapabilitas ke tools fisik beserta matriks rantai fallback.
  - `quality-assurance.md`: Sistem 5 Gerbang Kendali Mutu (Gates G0 s.d. G4) dan standar kelulusan linter.
  - `testing-framework.md`: Kerangka pengujian perilaku dan deterministik untuk skill AI.
  - `security-governance.md`: Tata kelola hak akses terkecil, sensor 8-Class PII, dan proteksi prompt injection.
  - `versioning-evolution.md`: Konvensi SemVer untuk skill, evaluasi pasca-tugas, dan penghentian aman.
  - `implementation-workflows.md`: Prosedur operasional standar langkah demi langkah untuk seluruh mode kerja.
  - `troubleshooting.md`: Matriks diagnostik cepat dan prosedur investigasi akar masalah 5-Whys.
- **3 Contoh Desain Representatif di `examples/`**:
  - `simple-skill.md`: Implementasi skill sederhana berbasis instruksi tunggal.
  - `modular-skill.md`: Implementasi skill modular dengan pemisahan berkas referensi.
  - `complex-skill.md`: Implementasi skill kelas industri dengan skrip deterministik dan skema validasi.
- **Suite Pengujian & Validasi di `tests/`**:
  - `regression-cases.md`: 18 skenario pengujian regresi deterministik dan penanganan kasus batas.
  - `validation-checklist.md`: 30 butir daftar periksa kesiapan produksi sebelum rilis.

### Consolidated
- Menggabungkan seluruh kapabilitas `spesialis-laporan-akademik` ke dalam `spesialis-research-akademik` guna mengeliminasi fragmentasi domain dan tabrakan kata kunci pemicu.