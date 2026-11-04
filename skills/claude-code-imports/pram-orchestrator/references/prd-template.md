# STANDAR OPERASIONAL & TEMPLATE: PRD (PRODUCT REQUIREMENTS DOCUMENT)
> Dokumen spesifikasi kebutuhan produk berstandar FAANG/Stripe dengan rubrik kelayakan 0-40.

---

## 🏛️ RUBRIK EVALUASI PRD (SKOR 0 - 40)
Sebelum diserahkan ke tim engineering, PRD wajib dinilai berdasarkan 4 pilar:
1. **Kejelasan Problem Statement (0-10)**: Apakah masalah nyata pengguna terdefinisi dengan metrik kerugian/inefisiensi terukur?
2. **Kelengkapan User Flow & Edge Cases (0-10)**: Apakah alur ideal (*Happy Path*) dan skenario kegagalan (*Error Handling*) dijabarkan tuntas?
3. **Ketegasan Out-of-Scope (0-10)**: Apakah batasan fitur yang TIDAK dibuat dikunci secara tegas untuk mencegah *Scope Creep*?
4. **Feasibilitas & Metrik Sukses (0-10)**: Apakah *North Star Metric* dan kebutuhan non-fungsional (NFR) realistis?
*Syarat Lulus (Ready for Engineering): Skor minimal 32/40.*

---

## 📝 TEMPLATE STRUKTUR PRD

```markdown
# PRD: [Nama Fitur / Produk]

## 1. Executive Summary & Problem Framing
- **Latar Belakang**: [Mengapa masalah ini mendesak untuk diselesaikan?]
- **Problem Statement**: [Pengguna mengalami kesulitan X yang menyebabkan dampak Y.]
- **Target Persona & JTBD**: 
  - *Persona*: [Siapa pengguna utama?]
  - *Jobs-to-be-Done (JTBD)*: Ketika [kondisi/situasi], saya ingin [tindakan/motivasi], agar saya dapat [hasil/manfaat yang terukur].

## 2. Success Metrics (North Star & Guardrails)
- **Primary Metric (North Star)**: [Contoh: 7-Day Active Users yang menyelesaikan alur checkout > 60%]
- **Secondary Metrics**: [Contoh: Rata-rata waktu penyelesaian transaksi < 45 detik]
- **Guardrail Metric**: [Contoh: Crash-free sessions tetap >= 99.9%, CS ticket tidak naik > 5%]

## 2.1 Tech Stack Matrix & Feature Roadmap Tree
- **Matriks Tech Stack**:
  - *Frontend*: [Contoh: Next.js 15 App Router / Tailwind CSS]
  - *Backend*: [Contoh: Go Gin / Node.js Express / Python FastAPI]
  - *Database*: [Contoh: PostgreSQL + Prisma / Drizzle]
  - *Deployment*: [Contoh: Docker / Vercel / VPS Linux]
- **Pohon Hierarki Fitur (Roadmap)**:
  1. **[Fitur P0 - Core System]**:
     - *Sub-Fitur 1.1*: Deskripsi fungsi, input/output, dan user journey.
     - *Sub-Fitur 1.2*: Deskripsi fungsi, validasi, dan integrasi data.
  2. **[Fitur P1 - Advanced / Secondary]**:
     - *Sub-Fitur 2.1*: Deskripsi optimasi atau automasi pendukung.

## 3. Scope & Prioritas (RICE Scoring)
| Fitur / Komponen | Reach | Impact | Confidence | Effort | RICE Score | Status |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Core Feature A | 1000 | 3 | 80% | 2 | 1200 | P0 (Must Have) |
| Optimization B | 500 | 2 | 70% | 1 | 700 | P1 (Should Have) |

### 3.1 Hard Out-of-Scope (DILARANG DIBUAT PADA RILIS INI)
- Fitur X (Ditunda ke Fase 2)
- Integrasi Payment Gateway Pihak Ketiga Tambahan
- Dukungan Multi-Bahasa selain ID dan EN

## 4. User Journey & Functional Specifications
### 4.1 Happy Path
1. Pengguna membuka halaman [X].
2. Pengguna mengisi formulir [Y] dengan validasi real-time.
3. Sistem memproses data dan mengembalikan status konfirmasi dalam < 200ms.

### 4.2 Edge Cases & Error States
- *Skenario Jaringan Terputus*: Tampilkan komponen UI offline banner dan simpan draft lokal via indexedDB.
- *Validasi Gagal*: Tampilkan pesan error spesifik di bawah input field terkait (bukan toast pop-up generik).
- *Rate Limit Exceeded*: Kembalikan status HTTP 429 dengan informasi header `Retry-After`.

## 5. Non-Functional Requirements (NFR)
- **Performance**: P95 Response Time < 150ms pada beban 500 RPS.
- **Security**: Validasi input boundaries (Zod/Pydantic), enkripsi field sensitif via AES-256, proteksi CSRF/XSS.
- **Observability**: Structured JSON logging, OpenTelemetry tracing, dan error tracking via Sentry.

## 6. Actionable Atomic Tasks (WBS & Kanban Handoff)
| Task ID | Fitur / Komponen Induk | Deskripsi Implementasi | PIC | Dependensi | Kriteria Akseptansi (DoD) |
|---|---|---|---|---|---|
| TSK-01 | Fitur 1 (Sub 1.1) | Setup skema database dan migrasi awal | Backend | - | Migrasi sukses tanpa error |
| TSK-02 | Fitur 1 (Sub 1.1) | Implementasi API endpoint dengan validasi | Backend | TSK-01 | Test coverage >= 80% |
| TSK-03 | Fitur 1 (Sub 1.2) | Slicing UI dan integrasi state client | Frontend | TSK-02 | Lolos verifikasi visual dan E2E |

## 7. Open Questions & Dependencies
- [ ] Apakah tim legal sudah menyetujui pembaruan Terms of Service untuk fitur ini?
- [ ] Ketergantungan API pihak ketiga: Menunggu rilis endpoint sandbox v2 dari partner.
```
