# OPERATIONAL REFERENCE: SKILL VERSIONING, EVOLUTION & DEPRECATION
> Panduan operasional komprehensif Specialist Skill Architect untuk pengelolaan versi semantik (Semantic Versioning), evolusi pasca-tugas terpandu (Guided Post-Task Evolution), dan protokol penghentian skill yang aman (Graceful Deprecation).

---

## 1. Prinsip Pemeliharaan Siklus Hidup Jangka Panjang

Specialist skill yang tidak dipelihara akan cepat mengalami penurunan kinerja (*performance decay*) seiring berkembangnya teknologi model bahasa, perubahan antarmuka alat (*tools API*), dan bertambahnya kompleksitas proyek. Namun, mengubah aturan skill secara sembarangan pada setiap sesi kerja berisiko memicu regresi perilaku yang merusak kestabilan alur kerja tim.

Specialist Skill Architect menerapkan prinsip **Evolusi Berbasis Evaluasi & Bukti (*Evidence-Based Evolution*)**:
- Setiap perubahan pada instruksi atau referensi skill wajib dicatat versinya secara transparan.
- Perubahan skill tidak boleh dilakukan secara diam-diam (*no stealth mutations*).
- Penyerapan pelajaran baru wajib melalui evaluasi keberhasilan dan uji regresi.

---

## 2. Standar Penomoran Versi Semantik untuk AI Skills (SemVer for Skills)

Setiap skill menerapkan konvensi penomoran versi `MAJOR.MINOR.PATCH`:

```text
               v [MAJOR] . [MINOR] . [PATCH]
                    │         │         │
                    │         │         └─ Perbaikan bug kecil / koreksi tipografi
                    │         └─────────── Penambahan kapabilitas baru (Backward Compatible)
                    └───────────────────── Perubahan besar arsitektur / breaking changes
```

### Panduan Kenaikan Versi:
1. **MAJOR (v2.0.0)**:
   - Terjadi perubahan besar pada format pemicu atau antarmuka yang tidak kompatibel dengan versi sebelumnya (*breaking change*).
   - Penggabungan (*merging*) dua skill menjadi satu nama baru atau restrukturisasi total dari monolit ke modular.
2. **MINOR (v1.1.0)**:
   - Penambahan mode operasional baru di dalam `SKILL.md`.
   - Penambahan berkas panduan baru di direktori `references/`.
   - Penambahan integrasi alat baru dengan tetap menjaga backward compatibility.
3. **PATCH (v1.0.1)**:
   - Perbaikan kata atau koreksi tata bahasa baku KBBI/EYD V.
   - Penajaman kata pemicu pada atribut description tanpa mengubah domain kerja.
   - Pembersihan tanda pisah em dash atau en dash.

---

## 3. Protokol Evolusi Terkendali (Controlled Evolution Protocol)

Mengadopsi prinsip pembelajaran berkelanjutan (Post-Task Evolution / SkillClaw):

### Tahapan Usulan Pembaruan Skill (4 Status Mesin):
1. **PROPOSED**:
   - Terjadi saat agen atau pengembang mengidentifikasi pola kegagalan berulang atau menemukan teknik kerja baru yang lebih efisien selama eksekusi proyek.
   - Usulan dicatat ke dalam berkas usulan terstruktur memuat: observasi nyata, akar masalah, rekomendasi perubahan teks, dan estimasi risiko regresi.
2. **UNDER_REVIEW**:
   - Specialist Skill Architect dan Project Owner meninjau usulan perubahan.
   - Dijalankan pengujian regresi terhadap skenario uji representatif.
3. **APPROVED**:
   - Usulan disetujui, perubahan diimplementasikan ke berkas `SKILL.md` atau `references/`, nomor versi dinaikkan, dan dicatat di `CHANGELOG.md`.
4. **REJECTED**:
   - Usulan ditolak karena menimbulkan komplikasi berlebih, memboroskan konteks, atau melanggar prinsip desain proyek.

---

## 4. Protokol Penghentian Skill yang Aman (Graceful Deprecation)

Ketika sebuah skill diputuskan untuk dihentikan (misal: digantikan oleh skill gabungan yang lebih baik):
1. **Fase Pengumuman (Deprecation Notice)**:
   - Tambahkan awalan `[DEPRECATED]` pada nama atau deskripsi skill.
   - Berikan arahan tegas pada deskripsi: *"DEPRECATED: Gunakan skill [nama-skill-penerus] untuk seluruh kebutuhan ini."*
2. **Pengalihan Pemicu (Trigger Rerouting)**:
   - Tambahkan seluruh kata kunci pemicu lama ke dalam deskripsi skill penerus.
3. **Pencatatan Migrasi**:
   - Dokumentasikan panduan migrasi di `CHANGELOG.md` skill lama dan baru.
4. **Pengarsipan / Pembersihan Berkas**:
   - Hapus direktori skill lama dari direktori aktif atau pindahkan ke folder arsip terisolasi (`archive/skills/`).