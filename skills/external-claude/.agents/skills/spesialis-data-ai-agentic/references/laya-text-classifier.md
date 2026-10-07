# Laya Text Classifier

Gunakan Laya untuk klasifikasi data teks lokal, routing, atau keputusan yes/no secara instan. Menghemat waktu dan kuota token LLM utama.

## Penggunaan

Jalankan via `execute_code`:

```python
from laya import Router
router = Router()

# Pilihan ganda
hasil = router.choice("Teks data", ["kategori_A", "kategori_B"])
print(hasil)

# Yes/No
is_valid = router.yes_no(text="Teks data", question="Pertanyaan?")
print(is_valid)
```

Gunakan untuk pra-filter dataset besar sebelum dianalisis lebih dalam.