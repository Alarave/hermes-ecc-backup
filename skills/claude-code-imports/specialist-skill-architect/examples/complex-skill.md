# EXAMPLE 3: COMPLEX SPECIALIST SKILL WITH SCRIPTS & TEST HARNESS
> Contoh implementasi specialist skill kelas industri tingkat lanjut yang memadukan instruksi RCCO, skrip otomatisasi Python, skema validasi JSON, dan pengujian regresi komprehensif.

---

## 1. Konteks Desain & Kapan Dipilih
- **Jenis Skenario**: Pipeline MLOps otomatis, compiler diagram vektor, atau engine audit kepatuhan repositori.
- **Strategi Rekayasa**: CREATE (Enterprise Scale).
- **Ciri Khas**: Mengombinasikan instruksi LLM tingkat tinggi dengan eksekusi script deterministik lokal untuk menjamin akurasi 100% pada tugas-tugas kritis.

---

## 2. Struktur Direktori Lengkap

```text
skills/enterprise-mlops-engineer/
├── SKILL.md
├── scripts/
│   ├── validate_anti_leakage.py
│   └── evaluate_diebold_mariano.py
├── schemas/
│   └── pipeline_config_schema.json
├── references/
│   ├── time-series-protocols.md
│   ├── drift-monitoring-sop.md
│   └── hardware-allocation.md
├── examples/
│   └── sample-lstm-experiment.md
├── tests/
│   ├── regression-cases.md
│   └── validation-checklist.md
└── CHANGELOG.md
```

---

## 3. Cuplikan Berkas Skrip Deterministik (`scripts/validate_anti_leakage.py`)

```python
# Skrip deterministik untuk menguji ketiadaan kebocoran data (Data Leakage)
import sys
import pandas as pd
import numpy as np

def verify_temporal_split(train_csv, test_csv, timestamp_col):
    df_train = pd.read_csv(train_csv)
    df_test = pd.read_csv(test_csv)
    
    max_train_time = pd.to_datetime(df_train[timestamp_col]).max()
    min_test_time = pd.to_datetime(df_test[timestamp_col]).min()
    
    if max_train_time >= min_test_time:
        print(f"CRITICAL ERROR: Data leakage terdeteksi!")
        print(f"Max train time: {max_train_time} >= Min test time: {min_test_time}")
        sys.exit(1)
        
    print("VERIFIKASI SUKSES: Anti-leakage temporal split terbukti valid.")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Penggunaan: python validate_anti_leakage.py <train.csv> <test.csv> <timestamp_col>")
        sys.exit(2)
    verify_temporal_split(sys.argv[1], sys.argv[2], sys.argv[3])
```

---

## 4. Keunggulan Arsitektur Kompleks
Dengan memisahkan tugas inferensi probabilistik model bahasa besar (seperti pemahaman konteks bisnis dan perumusan hipotesis) dari tugas deterministik (seperti validasi stasioneritas data dan perhitungan nilai p-value uji Diebold-Mariano), skill ini mencapai tingkat keandalan yang tidak dapat dicapai oleh prompt generik biasa.