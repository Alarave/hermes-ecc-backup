# OPERATIONAL REFERENCE: TROUBLESHOOTING & FAILURE RECOVERY FOR AI SKILLS
> Panduan diagnosis dan pemulihan cepat Specialist Skill Architect saat menghadapi masalah operasional skill, tabrakan pemicu, kegagalan linter, kehabisan context window, dan kegagalan tools.

---

## 1. Matriks Diagnostik Cepat Galat Skill (Fast Diagnostic Matrix)

| Gejala Masalah (Symptom) | Kemungkinan Akar Masalah (Root Cause) | Langkah Investigasi (Investigation) | Tindakan Pemulihan Cepat (Fast Fix) |
|:---|:---|:---|:---|
| **Skill Tidak Pernah Aktif Saat Dipanggil (Trigger Miss)** | Kata kunci di atribut description terlalu sempit, terlalu umum, atau format YAML rusak. | Periksa frontmatter YAML; bandingkan kata perintah pengguna dengan kata kunci pemicu. | Tambahkan variasi sinonim kata perintah pengguna ke dalam atribut description di `SKILL.md`. |
| **Dua Skill Aktif Bersamaan (Trigger Collision)** | Ada kata kunci pemicu yang identik pada dua berkas `SKILL.md` yang berbeda. | Jalankan skrip audit tabrakan pemicu lintas repositori. | Bedakan domain pemicu secara spesifik atau gabungkan kedua skill via strategi COMBINE. |
| **Skor Linter Audit Gagal (< 100/100)** | Ada path komputer lokal absolut (`C:\...`), teks em dash, atau ketiadaan section RCCO. | Jalankan `python scripts/audit_incoming_skills.py` dan baca nomor baris yang dilaporkan. | Perbaiki baris yang melanggar: ganti path lokal dengan path relatif, hapus em dash, lengkapi blok RCCO. |
| **Galat Berkas Referensi Tidak Ditemukan** | Penamaan berkas di section Linked References salah ketik atau berkas belum dibuat di disk. | Periksa direktori `references/` menggunakan perintah `ls`. | Sesuaikan penamaan path berkas atau buat berkas referensi yang hilang di disk. |
| **Context Window Cepat Habis & Terkompaksi** | Berkas `SKILL.md` terlalu panjang (> 5.000 token) atau agen memuat seluruh referensi sekaligus. | Hitung jumlah kata berkas utama; periksa kebiasaan pemanggilan agen. | Lakukan refactoring: pindahkan teks panjang ke `references/` dan terapkan progressive disclosure. |
| **Sub-Agen Mengklaim Selesai Tanpa Bukti** | Terjadi halusinasi penyelesaian (*Fabricated Success Claim*) akibat ketiadaan proof gate. | Periksa direktori artefak dan log eksekusi terminal. | Hard reject: turunkan status ke FAILED, paksa eksekusi test runner nyata, dan minta bukti log exit code 0. |

---

## 2. Prosedur Investigasi Akar Masalah 5-Whys (Root Cause Analysis SOP)

Ketika terjadi kegagalan operasional skill yang berulang, arsitek wajib menerapkan metode interogasi 5-Whys:

```text
[MASALAH]: Sub-agen salah memodifikasi berkas konfigurasi sistem saat mengerjakan fitur baru.
  ├── Mengapa 1? Agen mengira berkas konfigurasi masuk dalam ruang lingkup tugasnya.
  ├── Mengapa 2? Context Pack yang dikirimkan tidak mencantumkan daftar Hard Out-of-Scope yang eksplisit.
  ├── Mengapa 3? Orchestrator membuat instruksi tugas secara terburu-buru tanpa menyalin template Context Pack baku.
  ├── Mengapa 4? Prosedur pembekuan kontrak (Frozen Contracts) tidak dijalankan sebelum koding dimulai.
  └── Mengapa 5 (AKAR MASALAH)? Gate G3 dilompati karena agen menganggap tugas tersebut berisiko rendah.
```

**Tindakan Korektif Permanen**:
Perketat aturan pada gerbang Gate G3: Wajib mencantumkan daftar Hard Out-of-Scope eksplisit pada setiap paket tugas sebelum status diubah menjadi IN_PROGRESS.

---

## 3. Protokol Penanganan Kegagalan Lingkungan Windows Host

Ketika agen dijalankan pada lingkungan host Windows 11:
1. **Penanganan Kunci Berkas (`EBUSY / Permission Denied`)**:
   - Jika perintah penghapusan berkas atau pembersihan Git worktree gagal karena kunci berkas Windows NTFS, tambahkan jeda waktu singkat (*sleep 2*) atau gunakan penanganan pengecualian pada skrip Python pembantu.
2. **Inkonsistensi Separator Baris Baru (`CRLF vs LF`)**:
   - Pastikan seluruh berkas Markdown dan skrip Python disimpan dengan separator baris standar LF atau biarkan Git menanganinya melalui konfigurasi `.gitattributes`.
3. **Pemisahan Perintah Shell**:
   - Pastikan perintah terminal ditulis menggunakan sintaks POSIX bash standar (MSYS/Git Bash) yang didukung oleh environment runtime lokal.