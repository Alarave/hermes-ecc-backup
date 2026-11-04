# STANDAR OPERASIONAL & TEMPLATE: BLAMELESS INCIDENT POSTMORTEM
> Standar retrospektif kegagalan sistem berpedoman pada Google SRE Handbook.

---

## 🏛️ PRINSIP UTAMA POSTMORTEM
1. **Blameless (Bebas Tuduhan)**: Asumsikan semua engineer bekerja dengan niat baik dan informasi terbaik saat itu. Kegagalan terjadi akibat celah desain, arsitektur, atau kurangnya otomatisasi pengujian.
2. **Timeline Presisi**: Kronologi kejadian wajib dicatat detik-per-detik (WIB / UTC).
3. **5-Whys Analysis**: Terus tanyakan "Mengapa" hingga menyentuh akar kelemahan sistemik/proses, bukan sekadar bug sintaks koding.
4. **Action Items Terukur**: Setiap tindakan pencegahan wajib memiliki nomor tiket, prioritas (P0-P2), PIC, dan tenggat waktu.

---

## 📝 TEMPLATE STRUKTUR INCIDENT POSTMORTEM

```markdown
# Incident Postmortem: [Judul Insiden Singkat & Jelas]
**Tanggal Insiden**: YYYY-MM-DD  
**Status**: DRAFT / UNDER REVIEW / CLOSED  
**Author / Incident Lead**: [Nama TPM / Lead Engineer]  
**Severity**: P0 (Kritis Nasional/Total Down) / P1 (Fitur Utama Lumpuh) / P2 (Degradasi Parsial)

## 1. Executive Summary & Metrik Durasi
- **Ringkasan Dampak**: [Jelaskan dampak bisnis secara ringkas, misal: "35% transaksi checkout gagal selama 42 menit."]
- **Time-to-Detect (TTD)**: [Waktu sejak error terjadi hingga alarm monitor/tim merespons (misal: 4 menit)]
- **Time-to-Mitigate (TTM)**: [Waktu sejak investigasi dimulai hingga sistem pulih kembali (misal: 38 menit)]
- **Total Downtime**: [Total durasi gangguan aktif]

## 2. Kronologi Kejadian (Timeline)
*Semua waktu dalam zona WIB*
- **14:02** - Deploy rilis v2.4.1 selesai dijalankan via CI/CD pipeline.
- **14:06** - Alarm Datadog memicu peringatan lonjakan error 500 pada endpoint `/api/v1/orders`.
- **14:10** - Tim SRE dan Backend berkumpul di War Room untuk triage insiden.
- **14:22** - Akar masalah ditemukan: Migrasi database mengunci tabel `orders` akibat operasi ALTER COLUMN tanpa timeout.
- **14:35** - Rollback rilis dijalankan ke versi v2.4.0 dan connection pool database di-restart.
- **14:44** - Seluruh metrik kembali normal, verifikasi integritas data selesai, insiden dinyatakan mereda.

## 3. Investigasi Akar Masalah (5-Whys Analysis)
1. *Mengapa endpoint /api/v1/orders gagal merespons?*  
   Karena koneksi database ke tabel orders mengalami exhaustion (timeout).
2. *Mengapa koneksi database mengalami timeout?*  
   Karena tabel orders terkunci oleh proses DDL migration.
3. *Mengapa proses DDL mengunci tabel secara eksklusif?*  
   Karena penambahan kolom baru dilakukan tanpa parameter non-blocking (CONCURRENTLY).
4. *Mengapa migrasi berisiko tinggi tersebut lolos ke produksi?*  
   Karena pengujian staging menggunakan dataset kecil sehingga penguncian tabel tidak terasa.
5. *Mengapa tidak ada linter migrasi otomatis di CI/CD?*  
   Karena pipeline build belum memasang tool static analysis untuk schema migration safety.

## 4. Tindakan Pencegahan & Remediasi (Action Items)
| ID | Tindakan Pencegahan | Tipe | Prioritas | PIC | Due Date | Status |
|---|---|:---:|:---:|:---:|:---:|:---:|
| ACT-01 | Pasang linter migrasi otomatis (strong_migrations) di CI pipeline | Prevent | P0 | @backend-lead | YYYY-MM-DD | TODO |
| ACT-02 | Tambahkan alert Datadog untuk lock timeout database > 5 detik | Detect | P1 | @devops | YYYY-MM-DD | IN PROGRESS |
| ACT-03 | Simulasikan beban dataset produksi pada lingkungan staging | Mitigate | P2 | @qa-lead | YYYY-MM-DD | TODO |

## 5. Lessons Learned & Hal Positif
- **Apa yang berjalan baik**: Rollback otomatis berjalan mulus dalam 9 menit setelah keputusan diambil.
- **Apa yang berjalan buruk**: Alarm error membutuhkan waktu 4 menit sebelum memicu notifikasi pager duty.
- **Di mana kita beruntung**: Insiden terjadi di luar jam sibuk (peak traffic) sehingga kerugian finansial minimal.
```
