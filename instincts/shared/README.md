# Shared Instincts Registry (Collective Intelligence)

Direktori ini menampung pengalaman, pola solusi, dan kebiasaan baru yang dipelajari oleh setiap anggota tim atau perangkat secara terdistribusi.

## Struktur Direktori
Setiap kontributor memiliki sub-folder terisolasi untuk menghindari konflik Git:
```
instincts/shared/
├── firman/
│   └── 2026-10-12_optimasi-postgres.yaml
└── kontributor-b/
    └── 2026-10-12_fix-hydration-nextjs.yaml
```

## Cara Berbagi Pengalaman Baru
Jalankan skrip pembagi pengalaman satu-klik:
```bash
python scripts/share_experience.py "Judul solusi atau pola yang berhasil"
```
Skrip akan otomatis:
1. Membuat template YAML ber-skor keyakinan (confidence).
2. Memverifikasi bebas path privat dan kredensial.
3. Melakukan git commit dan push ke repositori tim.
