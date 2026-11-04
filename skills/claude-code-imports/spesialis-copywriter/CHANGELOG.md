# CHANGELOG (CATATAN PERUBAHAN)

Seluruh perubahan penting pada skill `spesialis-copywriter` didokumentasikan di berkas ini. Format mengacu pada [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) dan mematuhi [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-14

### Added (Penambahan Baru)
- Inisialisasi perdana arsitektur skill `spesialis-copywriter` berbasis format baku RCCO (Role, Context, Constraints, Output).
- 5 Mode Operasional Mandiri: `LANDING_PAGE`, `DIRECT_RESPONSE_ADS`, `EMAIL_SEQUENCE`, `UX_MICROCOPY`, dan `SLIDE_DECK_AND_DEFENSE`.
- Panduan Penulisan Slide Presentasi Klien & Sidang Penguji (`references/presentation-deck-copywriting.md`): Prinsip "Titles are Claims, Not Topics", alur McKinsey SCR / Sequoia 10-Slide, alur sidang skripsi Gunadarma, formula Speaker Notes, dan kartu antisipasi sanggahan (Defense Q&A Cards).
- Kerangka Kerja Persuasi Teruji (`references/copywriting-frameworks.md`): AIDA, PAS, BAB, 4P, FAB, RMBC Method, dan StoryBrand SB7.
- Sistem Penegakan Mutu Anti-AI Slop (`references/anti-ai-slop-guidelines.md`): Daftar hitam kata klise pembuka, kata sifat superlatif kosong, uji penggantian konkret, dan variasi ritme kalimat.
- Panduan Ejaan Pemasaran Baku EYD V (`references/eyd-v-copywriting.md`): Aturan kata depan vs awalan, partikel pun, bentuk terikat, glosarium istilah pemasaran, dan kepatuhan Etika Pariwara Indonesia (EPI).
- Playbook Naskah Konversi (`references/conversion-copy-playbook.md`): Arsitektur laman landas, struktur iklan Meta/Google, urutan 3 email otomatis, dan teks mikro UX.
- SOP Copy Brief dan Matriks Audit Mutu 10 Poin (`references/copy-brief-and-audit.md`).
- Empat Berkas Percontohan Implementasi (`examples/`): `simple-microcopy.md`, `modular-email-sequence.md`, `complex-landing-page.md`, dan `presentation-client-and-defense.md`.
- Suite Pengujian Mutu (`tests/`): 14 skenario pengujian regresi (`regression-cases.md`) dan daftar periksa 30 butir validasi produksi (`validation-checklist.md`).
- Integrasi ke Chief AI Orchestrator (Pram) pada matriks audit keahlian sub-agent.
- Pembuatan alias perintah cepat slash command `/spesialis-copywriter`.