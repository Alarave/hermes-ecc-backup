---
name: contract-freezer
description: "Pola adaptasi dari Lean Autoformalization: Membekukan dan memvalidasi file kontrak (API/Interface/Schema) agar tidak dapat diubah diam-diam oleh sub-agen pekerja."
---

# Role
API Contract & Architecture Freezer. Bertugas sebagai penjaga gerbang (Gatekeeper) untuk memastikan dokumen spesifikasi teknis dan antarmuka (interface) yang sudah disetujui tidak dimanipulasi selama tahap implementasi.

# Context
Dalam orkestrasi multi-agen (RCCO), sub-agen sering kali mencoba jalan pintas dengan mengubah kontrak API, skema DB, atau tipe interface ketika mereka gagal mengimplementasikan kode yang rumit. Skill ini digunakan tepat setelah arsitektur disetujui (Gate G3) untuk membekukan spesifikasi tersebut, dan dipanggil lagi di Gate G4/Integrasi untuk memvalidasinya.

# Mechanism (The Frozen Anchor)
Skill ini menyediakan skrip `freeze_contract.py` dan `verify_frozen_contract.py`.
1. **Freeze**: Hash isi file kontrak target (contoh: `api.yaml`, `schema.prisma`, `types.ts`) dan simpan hash tersebut di file `.frozen_contracts.json`.
2. **Verify**: Sebelum status tugas dinyatakan `DONE`, verifikasi ulang apakah hash file kontrak saat ini masih identik dengan hash yang dibekukan. Jika berbeda = **REJECT IMPLEMENTATION**.

# Cara Penggunaan
Gunakan skrip helper di dalam direktori `scripts/`:

```bash
# Membekukan kontrak (Dijalankan oleh Pram/Architect)
python scripts/freeze_contract.py path/to/contract.yaml

# Memverifikasi kontrak (Dijalankan di Quality Gate / CI)
python scripts/verify_frozen_contract.py path/to/contract.yaml
```
