# Tasks: Eksekusi Upgrade spesialis-frontend v3.0.0

## Fase 1: FOUNDATION (Referensi & Infrastruktur)

### Task 1.1 - Tulis modul `wcag-accessibility-handbook.md`
_Requirements: FR-1 (a11y)_
**Langkah**:
- Sumber: Ekstrak pola dari skill lokal `frontend-a11y` (pola form, focus trap, keyboard nav)
- Tambah pola ARIA live region, reduced-motion safeguard dari `motion-foundations`
- Simpan ke `references/wcag-accessibility-handbook.md`

**Acceptance (pass/fail)**:
- PASS: Berisi pola ARIA minimal: `role="dialog"`, `aria-modal`, live region, focus trap
- FAIL: Tidak ada contoh kode React/TypeScript siap pakai

---

### Task 1.2 - Tulis modul `core-web-vitals-performance.md`
_Requirements: FR-2 (performa)_
**Langkah**:
- Sumber: Adaptasi dari skill lokal `react-performance` dan `nextjs-turbopack`
- Cakupan: LCP image priority, CLS prevention skeleton, INP via `startTransition`, dynamic import
- Simpan ke `references/core-web-vitals-performance.md`

**Acceptance (pass/fail)**:
- PASS: Ada checklist pre-deploy CWV dan pattern kode dengan anotasi metrik
- FAIL: Hanya teori tanpa snippet implementasi spesifik Next.js

---

### Task 1.3 - Tulis modul `react19-next15-patterns.md`
_Requirements: FR-3 (paradigma modern)_
**Langkah**:
- Sumber: Adaptasi dari skill lokal `react-patterns`, `nextjs-turbopack`
- Cakupan: Server/Client Component discipline, `useActionState`, `useOptimistic`, Error Boundary
- Simpan ke `references/react19-next15-patterns.md`

**Acceptance (pass/fail)**:
- PASS: Ada pola `use client` boundary decision tree + contoh `useActionState`
- FAIL: Tidak ada contoh Server Action konkret

---

## Fase 2: UPGRADE SKILL.md INTI

### Task 2.1 - Upgrade entrypoint `SKILL.md` ke v3.0.0
_Requirements: FR-1, FR-2, FR-3, FR-4, FR-5; NFR-1, NFR-3, NFR-4_
**Langkah**:
- Perluas deskripsi trigger untuk menyertakan kata kunci a11y, performa, React 19
- Tambah Mode Operasional baru: "Audit Mode" (FR-5) untuk verifikasi aksesibilitas dan performa
- Perbarui Linked References dengan 3 modul baru
- Pastikan entrypoint tetap di bawah 4.000 token

**Acceptance (pass/fail)**:
- PASS: Lolos `validate_skill.py --strict` dengan skor 100/100

---

## Fase 3: QUALITY GATE

### Task 3.1 - Jalankan Linter Validasi
_Requirements: NFR-4_
```bash
python skills/specialist-skill-architect/scripts/validate_skill.py \
    C:\Users\HP\.gemini\antigravity\skills\spesialis-frontend --strict
```
- PASS: [PASS 100/100]
- FAIL: Ada error atau warnings = perbaiki sebelum merge

### Task 3.2 - Periksa em dash & en dash
```bash
Select-String -Path "...\spesialis-frontend\**\*.md" -Pattern "[-]{2}|[--]"
```
- PASS: 0 hasil, tidak ada tipografi terlarang

---

## Definition of Done
- [x] 3 modul referensi baru tersimpan di `references/`
- [x] `SKILL.md` v3.0.0 lolos validator 100/100 strict
- [x] Semua FR dan NFR tercakup dalam referensi dan trigger
