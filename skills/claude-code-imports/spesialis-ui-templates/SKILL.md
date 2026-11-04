---
name: spesialis-ui-templates
description: "[DEPRECATED] Gunakan spesialis-frontend v2.0.0 sebagai gantinya. Seluruh kapabilitas design system, komponen UI, dan brand references telah diserap penuh ke spesialis-frontend."
---

# [DEPRECATED] Spesialis UI Templates (spesialis-ui-templates)

## R (Role & Deprecation Notice)
- **Status Modul**: DEPRECATED (Usang). Seluruh kapabilitas telah digabung (COMBINE) ke dalam `spesialis-frontend` v2.0.0.
- **Tanggung Jawab**: Mengarahkan pemanggilan legacy secara otomatis ke modul kanonikal `spesialis-frontend`.
- **Standar Bahasa**: Bahasa Indonesia teknik baku EYD V. Bebas dari karakter em dash atau en dash.

---

## C (Context & Redirect)
- Dipicu ketika pengguna atau alur kerja memanggil template antarmuka lawas (`/spesialis-ui-templates`).
- Agen WAJIB mengalihkan pemanggilan ini langsung ke `spesialis-frontend`.

---

## C (Constraints & Boundaries)
- Dilarang menambahkan template atau aset baru pada modul ini. Seluruh penambahan wajib dilakukan di dalam direktori `skills/spesialis-frontend/`.
- Mematuhi standar Pilar 2 Antarmuka Pengguna (`ui-ux-pro-max`, `scroll-experience`, `anti-ui-slop`, `impeccable`).

---

## O (Output Format & Delegation)
- Delegasikan eksekusi langsung ke `/spesialis-frontend`.
- Jangan hasilkan kode antarmuka terpisah dari modul ini.

---

## Linked References
- `skills/spesialis-frontend/SKILL.md` (Modul Kanonikal Utama)
