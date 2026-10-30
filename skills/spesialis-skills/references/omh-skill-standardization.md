# Standar Penulisan & Optimasi Skill Oh My Hermes (OMH)

Panduan operasional dan resep baku untuk merapikan, menstandarisasi, dan mengoptimalkan seluruh modul skill agar mematuhi standar Oh My Hermes (OMH) dan RCCO.

---

## 1. Spesifikasi YAML Frontmatter OMH

Setiap berkas `SKILL.md` wajib memuat blok metadata YAML lengkap dan valid:

```yaml
---
name: <nama-skill>
description: "[omh] <Fungsi utama modul>. Use when the user says: <pemicu_1>, <pemicu_2>, <pemicu_3>."
license: MIT
author: "<Pengembang / Maintainer>"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, <tag_domain>]
    category: <kategori_domain>
    phase: <fase_siklus>
    role: <guide|tracker|reviewer|operator|planner>
    quality_tier: <evidence-gated|workflow-surface-gated>
    related_skills: [<skill_terkait_1>, <skill_terkait_2>]
---
```

### Aturan Kunci Frontmatter:
- **Kesesuaian Nama Direktori**: Kunci `name` wajib identik 1:1 dengan nama direktori kanonikal (kebab-case) dan ditulis polos tanpa tanda petik (`name: my-skill`, bukan `name: "my-skill"`). Tanda petik memicu kegagalan regex linter `^[a-z0-9_-]+$`.
- **Klausul Pemicu Wajib**: Deskripsi wajib memuat kalimat pemicu terstandarisasi: `Use when the user says: ...` untuk memastikan aktivasi berbasis intent yang deterministik.
- **Format Deskripsi Single-Line**: Hindari blok skalar multi-baris (`|` atau `>`) pada atribut `description` karena dapat memicu peringatan linter deskripsi pendek atau pemotongan pembacaan.

---

## 2. Struktur Seksi Wajib Deterministik

1. `# [Judul Modul Skill]`
2. `## Why This Exists`: Menjelaskan esensi tujuan modul dan risiko jika alur ini diabaikan (1 paragraf padat).
3. `## When to Use`: Daftar kondisi pemanggilan eksplisit dan blok `Strong routing signals: ...`.
4. `## Do Not Use When`: Batasan negatif untuk mencegah misrouting agen.
5. `## Operating Steps`: Rangkaian aksi sekuensial berbutir nomor (1, 2, 3) yang langsung dapat dieksekusi tanpa narasi kosong.
6. `## Completion Checklist`: Kriteria keberhasilan berbasis bukti verifikasi fisik (file, test, linter).
7. `## Recovery Notes`: Prosedur penanganan ketika terjadi blocker, kegagalan dependensi, atau galat eksekusi.

---

## 3. Protokol Sanitasi Tipografi & Integritas Referensi

- **Larangan Tanda Pisah Em-Dash / En-Dash**: Dilarang menggunakan karakter Unicode U+2014 (—) dan U+2013 (–) di seluruh bagian berkas, termasuk di dalam komentar atau tabel. Gunakan titik dua (:), tanda strip biasa (-), koma (,), atau tanda kurung ().
- **Verifikasi Fisik Referensi Disk**: Seluruh berkas yang didaftarkan pada `## Linked References` wajib diverifikasi keberadaan fisiknya di disk sebelum pengesahan:
  - Format `skills/<nama-skill>/SKILL.md` diverifikasi relatif terhadap root `skills/`.
  - Format `references/<berkas>.md` diverifikasi relatif terhadap folder direktori skill itu sendiri.
  - Tautan fiktif atau berkas yang hilang wajib dibersihkan.

---

## 4. Strategi Eksekusi Bergelombang & Mandat Direct Patch

- **Partisi Gelombang (Wave Execution)**: Pada repositori skala 500+ skill, pembaruan wajib dipecah menjadi gelombang klaster domain (misalnya 20-30 skill per putaran) untuk mencegah kehabisan kuota tool call dan context overflow.
- **Mandat Direct Patch**: Modifikasi naskah skill wajib dilakukan langsung via tool patch atau write_file. Dilarang membuat skrip perantara Python atau skrip shell sementara hanya untuk menyunting berkas.
- **Penanganan Berkas Raksasa (>100 KB / >1.500 baris)**: Selesaikan kasus batas (edge cases) tanda pisah terisolasi (seperti awalan baris atau akhir baris) secara spesifik terlebih dahulu sebelum menerapkan `replace_all: true` untuk pola spasi umum (` — ` menjadi `: `) agar menghindari kegagalan matcher atau timeout.
- **Verifikasi Linter**: Setiap gelombang wajib divalidasi dengan `python skills/specialist-skill-architect/scripts/validate_skill.py <path> --strict` hingga mencapai status PASS 100/100.
