# STANDAR OPERASIONAL ANTI-AI SLOP TERPADU (3-PILAR: KODE, UI, TEKS)

Dokumen standar kualitas tertinggi untuk seluruh ekosistem agen di bawah koordinasi Pram Orchestrator dan Asep. Diadaptasi dari tolok ukur standar terbuka (mdskills.ai, ZeroSlop, Deslop, dan Anti-UI-Slop).

---

## 1. Definisi & Ancaman AI Slop

AI Slop adalah keluaran generik, berlebihan, template, atau hampa substansi yang dihasilkan oleh model bahasa AI akibat kecenderungan memilih kata yang paling lazim (*mode collapse/post-training bias*). AI Slop merusak integritas perangkat lunak, membingungkan pengguna, dan menghabiskan anggaran token.

Pram Orchestrator mewajibkan penegakan standar mutu anti-slop pada 3 pilar utama:
1. **Pilar Kode & Arsitektur (Code & Architecture Slop)**
2. **Pilar Antarmuka Pengguna & Frontend (UI & Design Slop)**
3. **Pilar Naskah, Dokumentasi & Prosa (Text & Documentation Slop)**

---

## 2. Pilar 1: Anti-Slop Kode & Arsitektur (Code Slop)

Mengadopsi pola Deslop dan AI-Slop-Cleaner. AI cenderung menulis kode dengan scaffolding berlebihan, komentar naratif yang berisik, dan penanganan error defensif palsu.

### Aturan Penegakan Mutu Kode:
1. **Dilarang Komentar Naratif AI (No AI Commentary Noise)**:
   - Dilarang menulis komentar yang hanya mengulang fungsi baris kode (contoh: `// increment counter by 1`, `i++`).
   - Dilarang menulis header komentar berbunga-bunga (contoh: `// ==================== HELPER FUNCTION ====================`).
   - Kode bersih harus dapat menjelaskan dirinya sendiri melalui penamaan variabel dan fungsi yang presisi (*Self-Documenting Code*).
2. **Dilarang Wrapper Defensif Palsu pada Jalur Terpercaya (No Redundant Defensive Checks)**:
   - Dilarang membungkus setiap fungsi internal dengan blok `try-catch` kosong atau `try-except pass` yang menelan error diam-diam.
   - Validasi data hanya wajib di batas sistem (*trust boundaries*: input pengguna, API publik, pembacaan file eksternal).
3. **Dilarang Jalan Pintas Pengetikan (No Type-Cast Escapes)**:
   - Dilarang memotong validasi tipe dengan `any` pada TypeScript atau `typing.Any` pada Python tanpa justifikasi tertulis.
4. **Prinsip Deletion-First (YAGNI Mutlak)**:
   - Utamakan menghapus kode daripada menambah fungsi baru.
   - Dilarang membuat abstraksi dini (interface dengan 1 implementasi, factory untuk 1 objek tunggal).

---

## 3. Pilar 2: Anti-Slop Antarmuka Pengguna & Frontend (UI Slop)

Mengadopsi pola Anti-UI-Slop dan UI UX Pro Max. Agen koding cenderung menghasilkan tampilan web generik template yang seragam dan membosankan (*AI Aesthetic*).

### Aturan Penegakan Desain Frontend:
1. **Dilarang Kartu Generik & Gradien Norak (No Template Aesthetic)**:
   - Dilarang membuat tampilan yang hanya terdiri dari deretan kartu putih berbayang abu-abu tipis tanpa hirarki kontras.
   - Dilarang menggunakan gradien ungu-biru neon generik khas AI generator pada latar belakang teks tanpa tujuan fungsional.
2. **Wajib Kelengkapan Status Komponen (State Completeness)**:
   - Setiap elemen interaktif (tombol, form, kartu) wajib memiliki status visual lengkap: Default, Hover, Focus, Active, Disabled, Loading, dan Error.
   - Dilarang membiarkan komponen dalam keadaan kaku (*inert components*).
3. **Wajib Tipografi & Kontras Berstandar (Editorial Typography & Contrast)**:
   - Hirarki tipografi wajib proporsional (Hero, H1, H2, Body, Caption) dengan bobot font yang berkarakter.
   - Rasio kontras teks terhadap latar belakang wajib mematuhi standar aksesibilitas WCAG AAA/AA.
4. **Verifikasi Tampilan Nyata (Evidence Before Shipped)**:
   - Wajib memeriksa visual sebelum klaim selesai untuk mendeteksi teks terpotong (*clipping*), tabrakan margin (*layout shift*), atau scroll horizontal yang tidak diinginkan.

---

## 4. Pilar 3: Anti-Slop Naskah, Dokumentasi & Prosa (Text Slop)

Mengadopsi pola Zero Slop dengan taksonomi 294 pola dan leksikon 96 istilah klise.

### Aturan Penegakan Naskah & Teks:
1. **Larangan Kalimat Pembuka Template (No Canned Openers)**:
   - Dilarang membuka dokumen/pesan dengan: "Di era digital yang berkembang pesat ini", "We are thrilled to announce", "In today's fast-paced world", "Here is the thing".
2. **Larangan Kontras Biner Buatan (No Synthetic Binary Contrast)**:
   - Dilarang menggunakan retorika: "Ini bukan sekadar X, melainkan Y", "It is not just about X, it is about Y".
3. **Larangan Pemasaran Hampa & Dramatisasi (No Significance Inflation)**:
   - Dilarang menggunakan kata sifat berlebihan: "solusi mutakhir", "revolusioner", "seamless", "robust", "leverage", "cutting-edge", "game-changer", "pivotal moment".
4. **Fidelitas Data 100% (Zero Data Drift)**:
   - Seluruh angka metrik, nama orang, versi pustaka, path file, dan perintah terminal wajib dipertahankan secara akurat saat penyuntingan berlangsung. Dilarang mengarang fakta baru.

---

## 5. Integrasi ke Gerbang Mutu Pram (Quality Gates G0 s.d. G4)

| Gerbang Mutu | Verifikasi Anti-Slop yang Wajib Lolos | Seal Terkait |
|---|---|---|
| **Gate G0 (Brief)** | Bebas dari basa-basi pembuka dan dramatisasi masalah. | Semantic Seal |
| **Gate G1 (PRD)** | Bebas dari fitur hampa (gold plating); fokus pada pain point riil. | Semantic Seal |
| **Gate G2 (Domain)** | Bebas dari modul palsu yang tidak memiliki domain bisnis terikat. | Semantic Seal |
| **Gate G3 (Architecture)** | Bebas dari over-engineering (YAGNI); skema type-safe terkunci. | Machine Seal |
| **Gate G4 (Code/TDD)** | 1) Zero code slop (bebas komentar AI/any cast). 2) Zero UI slop (komponen dinamis & responsif). 3) Zero text slop (README/laporan lugas). | Dual Audit Seal |

---

## 6. Sanksi & Prosedur Penolakan (Reject & Recover)

Jika agen pengembang menyerahkan deliverable yang terindikasi AI Slop:
1. Pram Orchestrator langsung menolak status `SUCCESS` dan mengembalikan ke `IN_PROGRESS`.
2. Terbitkan laporan audit ringkas mengutip baris kode, elemen visual, atau frasa yang melanggar.
3. Jalankan pembersihan terfokus via sub-agen spesialis (`deslop` untuk kode, `anti-ui-slop` untuk antarmuka, `zero-slop` untuk tulisan).
4. Penggabungan cabang hanya sah setelah Dual Audit Seal diterbitkan dengan status `VERIFIED`.
