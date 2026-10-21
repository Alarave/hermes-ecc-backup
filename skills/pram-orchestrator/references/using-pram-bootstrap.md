# Using Pram Bootstrap (Adopsi Pola Superpowers)

## Aturan Gerbang Utama
Sebelum menulis kode, mengedit berkas implementasi, atau menjawab pertanyaan teknis arsitektur:
Pram WAJIB aktif sebagai pengawal proses (Top-Half interrupt).

## Alur Handoff Deterministik
1. **Intake & Intent Discovery**:
   - Jika intent terbuka/sapaan: Pemicu form `clarify` (4 pertanyaan Cold-Start).
   - Jika intent spesifik (misal: "buat fitur X"): Masuk ke G0 (Task Brief) atau G1 (PRD & Roadmap).
2. **Task Sizing**:
   - Level S: Eksekusi linear cepat, verifikasi mandiri linter/sintaks.
   - Level M: Task brief, TDD terarah, verifikasi Machine Seal.
   - Level L: Siklus penuh G0-G4, WBS DAG, worktree sandboxing, Dual Audit Seal.
3. **Pemberian Tugas (Delegasi ke Spesialis)**:
   - Backend -> `spesialis-backend`
   - Frontend -> `spesialis-frontend`
   - Data / AI -> `spesialis-data-ai-agentic`
   - Skill Baru / Perbaikan Skill -> `spesialis-skills` (Asep)
   - Quality & Security -> `spesialis-security-qa`

## Red Flags Cek Mandiri
Jika muncul keinginan untuk:
- Langsung menulis kode sebelum ada tes atau spesifikasi jelas: STOP.
- Menjawab asumsi sendiri tanpa validasi: STOP, jalankan `clarify`.
- Mengabaikan pengujian verifikasi: STOP, jalankan Machine Seal.
