# Requirements Specification: Upgrade Esensial spesialis-frontend v3.0.0

## Document Information
- **ID Proyek**: SPEC-FE-UPGRADE-V3
- **Tanggal**: 2026-10-21
- **Arsitek**: Asep (spesialis-skills) via kiro-workflow
- **Target**: `skills/spesialis-frontend`
- **Status**: DRAFT (Reviewing)

---

## 1. Introduction
Dokumen ini mendefinisikan kebutuhan fungsional dan non-fungsional untuk upgrade arsitektural skill `spesialis-frontend` ke versi 3.0.0. Peningkatan ini menyuntikkan kapabilitas esensial yang sebelumnya terfragmentasi di berbagai skill periferal: aksesibilitas ketat (a11y/WCAG AA), optimasi performa Core Web Vitals (INP/LCP/CLS), paradigma modern React 19/Next.js 15+, orkestrasi animasi Framer Motion tahan aksesibilitas, dan pipeline token sistem desain Tailwind v3/v4.

---

## 2. Functional Requirements (EARS Format)

### FR-1: Aksesibilitas Tersemat (WCAG 2.1 AA Compliance)
- **WHEN** agen merancang atau mengimplementasikan elemen interaktif (modal, dropdown, dialog, tabs), **THE** `spesialis-frontend` **SHALL** menyertakan focus trap, penanganan tombol Keyboard (Escape, Tab, Arrow keys), dan role ARIA yang sesuai spesifikasi WAI-ARIA.
- **WHEN** agen membuat formulir masukan, **THE** `spesialis-frontend` **SHALL** menyematkan label eksplisit (`htmlFor`), status kesalahan (`aria-invalid`), dan pesan validasi dengan pengumuman screen reader (`aria-describedby` atau `role="alert"`).
- **IF** pengguna memiliki preferensi gerak berkurang (`prefers-reduced-motion`), **THEN THE** `spesialis-frontend` **SHALL** menonaktifkan atau menyederhanakan animasi Framer Motion ke fade instan.

### FR-2: Performa & Optimasi Core Web Vitals
- **WHEN** komponen memuat aset gambar atau media hero, **THE** `spesialis-frontend` **SHALL** menyertakan atribut prioritas pemuatan (`priority`, `loading="eager"`) dan dimensi eksplisit (mencegah CLS).
- **WHILE** merancang halaman dengan bundle besar atau komponen berat, **THE** `spesialis-frontend` **SHALL** memisahkan komponen non-kritis menggunakan dynamic import (`lazy`, `Suspense`, atau `next/dynamic`).
- **WHEN** menulis state interaksi frekuensi tinggi (slider, pencarian instan, filter), **THE** `spesialis-frontend` **SHALL** mengisolasi re-render ke leaf node atau menerapkan debouncing dan transisi concurrent (`useTransition`).

### FR-3: Paradigma Modern React 19 & Next.js 15
- **WHEN** merancang komponen berkonsumsi server, **THE** `spesialis-frontend` **SHALL** secara eksplisit menetapkan batas Server Component vs Client Component (`'use client'`) pada tingkat sekecil mungkin.
- **WHEN** menangani mutasi formulir atau aksi pengguna, **THE** `spesialis-frontend` **SHALL** menggunakan hook mutasi modern (`useActionState`, `useOptimistic`) dan feedback loading terintegrasi.

### FR-4: Pipeline Design Token & Brand Matching
- **WHEN** pengguna meminta adopsi gaya brand tertentu (contoh: Stripe, Apple, Vercel), **THE** `spesialis-frontend` **SHALL** mengonversi token warna, radius, dan shadow dari berkas referensi menjadi token semantik Tailwind (`bg-surface-elevated`, `border-subtle`).
- **IF** token yang diminta tidak memiliki kontras warna minimal 4.5:1 untuk teks normal, **THEN THE** `spesialis-frontend` **SHALL** menyesuaikan luminansi token guna memenuhi standar kontras AA.

### FR-5: Pengujian Komponen & Checklist Verifikasi
- **WHEN** kode komponen final disajikan, **THE** `spesialis-frontend` **SHALL** menyertakan cuplikan uji perilaku berbasis React Testing Library / Vitest tanpa menguji detail implementasi internal.

---

## 3. Non-Functional Requirements
- **NFR-1 (Efisiensi Konteks)**: File entrypoint `SKILL.md` wajib berada di bawah batas 5.000 token untuk menjaga efisiensi konteks agen.
- **NFR-2 (Modularitas Referensi)**: Rincian teknis mendalam wajib dipecah ke dalam berkas terpisah di subdirektori `references/`.
- **NFR-3 (Standar Bahasa & Tipografi)**: Instruksi bahasa Indonesia baku EYD V tanpa em dash atau en dash.
- **NFR-4 (Validasi Linter)**: Lolos 100/100 pada pengujian `validate_skill.py --strict`.

---

## 4. Constraints
- Dilarang menulis logika database/backend murni.
- Dilarang menambahkan dependensi paket NPM yang tidak lazim bila CSS native atau HTML semantik sudah mencukupi.

---

## 5. Success Criteria
1. Seluruh AC berbasis EARS terverifikasi dalam dokumen desain dan task eksekusi.
2. Tersedia 3 referensi modul inti baru di `spesialis-frontend/references/`:
   - `core-web-vitals-performance.md`
   - `wcag-accessibility-handbook.md`
   - `react19-next15-patterns.md`
3. Skor linter mencapai 100/100 pada `validate_skill.py`.

---

## 6. Glossary
- **EARS**: Easy Approach to Requirements Syntax.
- **a11y**: Singkatan numerik dari Accessibility (A + 11 huruf + Y).
- **CLS**: Cumulative Layout Shift (metrik kestabilan visual).
- **INP**: Interaction to Next Paint (metrik responsivitas interaksi).
- **WCAG**: Web Content Accessibility Guidelines.

---

## 7. Quality Gate Checklist (Requirements)
- [x] Kepatuhan EARS pada setiap AC
- [x] Batasan domain frontend terjaga
- [x] Kriteria penerimaan terukur
