# OPERATIONAL REFERENCE: SKILL DISCOVERY & LOCAL ENVIRONMENT AUDIT
> Panduan operasional komprehensif Specialist Skill Architect untuk inventarisasi lingkungan kerja lokal, pemetaan pohon kapabilitas, deteksi tumpang tindih, dan analisis kesenjangan fungsional (Gap Analysis).

---

## 1. Tujuan & Filosofi Penemuan Kemampuan Lokal

Prinsip fundamental dalam rekayasa sistem AI adalah **Mencegah Duplikasi dan Pemborosan (*Avoid Redundant Creation*)**. Sering kali pengembang AI secara tergesa-gesa menulis prompt atau membuat skill baru dari nol, padahal kemampuan tersebut sudah tersedia di repositori lokal atau dapat diselesaikan dengan sedikit perluasan pada skill yang sudah ada.

Specialist Skill Architect menerapkan protokol **Pemeriksaan Lingkungan Mendahului Pembuatan (*Inspect Environment Before Building*)**. Sebelum membuat berkas baru, arsitek wajib memindai repositori kerja lokal untuk:
1. Memetakan seluruh kapabilitas yang sudah terpasang.
2. Mengidentifikasi kata kunci pemicu yang sudah terdaftar guna mencegah tabrakan pemicu (*trigger collision*).
3. Menganalisis tingkat kesehatan dan kepatuhan arsitektur skill terhadap standar RCCO.
4. Menemukan kesenjangan kapabilitas (*capability gaps*) yang benar-benar membutuhkan pembuatan skill baru.

---

## 2. Struktur Peta Direktori Skill di Lingkungan Hermes

Di lingkungan kerja lokal Hermes dan Claude Code, specialist skill terdistribusi di beberapa tingkatan direktori:
- `skills/`: Direktori utama skill lokal aktif tingkat pengguna dan proyek.
- `.agent/skills/`: Direktori skill bawaan sistem atau dependensi eksternal proyek.
- `.agents/skills/`: Direktori skill agen otonom terdistribusi.
- `.claude/skills/` dan `.cursor/skills/`: Direktori konvensi IDE pendukung.

### Perintah Pemindaian Inventarisasi Cepat:
Arsitek menggunakan utilitas pencarian berkas untuk menyusun daftar seluruh berkas `SKILL.md` yang tersedia:
```bash
# Mencari seluruh direktori skill lokal aktif
find skills/ -maxdepth 2 -name "SKILL.md" | sort
```

---

## 3. Matriks Audit 12 Parameter Kesehatan Skill Lokal

Setiap skill yang ditemukan di lingkungan kerja lokal dievaluasi menggunakan matriks audit 12 parameter:

| No | Parameter Pemeriksaan | Kriteria Kelulusan Standar | Risiko Jika Gagal |
|:---|:---|:---|:---|
| 1 | **Format Identitas YAML** | Memiliki metadata frontmatter YAML valid dengan field `name` dan `description`. | Skill gagal diindeks oleh sistem parser runtime. |
| 2 | **Kesesuaian Nama File & Direktori** | Nama skill di frontmatter identik dengan nama folder pembungkus (kebab-case). | Tabrakan referensi path dan kegagalan autoload. |
| 3 | **Struktur Arsitektur RCCO** | Memuat section R (Role), C (Context), C (Constraints), dan O (Output Format). | Pola kerja agen menjadi liar dan tidak terprediksi. |
| 4 | **Ketajaman Deskripsi Pemicu** | Deskripsi memuat frasa pemicu eksplisit (*"Use when user says..."*) <= 1024 karakter. | Trigger misses (agen tidak aktif saat dibutuhkan) atau trigger hallucination. |
| 5 | **Efisiensi Konteks Entrypoint** | Berkas `SKILL.md` utama berukuran ringkas (< 5.000 token) dan mendelegasikan rincian ke `references/`. | Context window cepat habis, memicu auto-compaction dini. |
| 6 | **Integritas Referensi Berkas** | Seluruh tautan di bawah section `Linked References` benar-benar ada di sistem berkas fisik. | Galat berkas tidak ditemukan saat pemanggilan `skill_view`. |
| 7 | **Realisme Pemilihan Tools** | Tools yang disebutkan di instruksi benar-benar tersedia di runtime lokal. | Agen macet saat mencoba memanggil fungsi fiktif. |
| 8 | **Sanitasi Kredensial & PII** | Nol kebocoran data pada 8 kategori data pribadi dan kredensial rahasia (`[REDACTED]`). | Kebocoran rahasia ke log publik atau commit repositori. |
| 9 | **Kebersihan Tipografi Baku** | Nol karakter tanda pisah panjang em dash atau en dash. | Pelanggaran standar gaya penulisan proyek. |
| 10 | **Kesesuaian Bahasa EYD V / KBBI** | Teks instruksi bahasa Indonesia mematuhi kaidah baku tanpa kata klise AI-slop. | Penurunan wibawa instruksi dan instruksi bertele-tele. |
| 11 | **Ketersediaan Pengujian Regresi** | Memiliki minimal 1 berkas skenario pengujian di direktori `tests/`. | Ketidakmampuan memvalidasi stabilitas pasca-perubahan. |
| 12 | **Kesiapan Isolasi Worktree** | Prosedur eksekusi kode mendukung pengoperasian di direktori terisolasi. | Tabrakan kode dan modifikasi tidak sengaja pada branch utama. |

---

## 4. Alur Kerja Deteksi Tumpang Tindih & Analisis Kesenjangan (Gap Analysis)

Ketika ada permintaan kemampuan baru dari pengguna, Specialist Skill Architect menjalankan alur kerja 5 tahap:

```text
[Permintaan Kapabilitas Baru] 
             │
             ▼
[Tahap 1: Ekstraksi Kata Kunci Kebutuhan]
             │
             ▼
[Tahap 2: Pemindaian Index Skill Lokal] ──(Ditemukan Kecocokan >= 90%)──► [Strategi: REUSE]
             │ (Kecocokan 50% - 89%)
             ▼
[Tahap 3: Evaluasi Perluasan vs Pemisahan] ──(Domain Selaras)───────────► [Strategi: EXTEND]
             │ (Domain Terfragmentasi)
             ▼
[Tahap 4: Deteksi Duplikasi Parsial] ─────(Ada 2 Skill Beririsan)───────► [Strategi: COMBINE]
             │ (Kecocokan < 50%)
             ▼
[Tahap 5: Riset Eksternal & Pembuatan] ───(Riset GitHub Selesai)────────► [Strategi: CREATE / ADAPT]
```

### Prosedur Deteksi Tumpang Tindih Pemicu (Trigger Collision Detection):
Dua skill dilarang menggunakan sekumpulan kata pemicu yang identik jika domain keahliannya berbeda. Arsitek memeriksa daftar kata pemicu di seluruh berkas `SKILL.md` lokal:
```python
# Prosedur logis deteksi tabrakan kata pemicu
import re
from pathlib import Path

def audit_trigger_collisions(skills_dir):
    triggers = {}
    for skill_path in Path(skills_dir).rglob("SKILL.md"):
        content = skill_path.read_text(encoding="utf-8")
        match = re.search(r'description:\s*"([^"]+)"', content)
        if match:
            desc = match.group(1).lower()
            keywords = re.findall(r"'([^']+)'", desc)
            for kw in keywords:
                if kw in triggers:
                    triggers[kw].append(skill_path.parent.name)
                else:
                    triggers[kw] = [skill_path.parent.name]
    
    collisions = {k: v for k, v in triggers.items() if len(v) > 1}
    return collisions
```

Jika ditemukan tabrakan kata kunci antara dua skill berbeda, arsitek wajib melakukan spesialisasi pemicu (*trigger disambiguation*) atau menggabungkan kedua skill menjadi satu modul yang utuh (*skill consolidation*).