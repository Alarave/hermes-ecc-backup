# VALIDATION CHECKLIST: REVERSE ENGINEER ANYTHING
> Daftar periksa kesiapan produksi modul skill reverse-engineer-anything.

- [x] Frontmatter YAML memuat nama kebab-case yang cocok dengan direktori.
- [x] Deskripsi frontmatter memuat frasa pemicu alami ("Use when user says...").
- [x] Struktur dokumen mematuhi 4 pilar RCCO (Role, Context, Constraints, Output).
- [x] Seluruh tautan ke direktori `references/` valid dan ada di disk fisik.
- [x] Nol kebocoran path pribadi (C:\Users\... atau E:\...).
- [x] Nol kebocoran data sensitif 8-class PII atau token API mentah.
- [x] Bebas dari karakter tanda pisah em-dash atau en-dash.
- [x] Lolos audit linter `scripts/audit_incoming_skills.py` dengan skor 100/100.
