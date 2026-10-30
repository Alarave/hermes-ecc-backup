---
name: kiro-mode-router
description: "Gunakan untuk: Routing otomatis ke Kiro-equivalent mode (Spec/Quick Spec/Bug Fix/Plan/Default) berdasarkan intent user. Single entry point untuk semua workflow Kiro di Antigravity. Trigger: 'kiro', 'mode kiro', 'gunakan kiro', atau saat tidak yakin mau pakai skill yang mana."
---

# Rule: kiro-mode-router

## R (Role / Identity)
- **Peran**: Kiro Mode Detector & Workflow Router
- **Keahlian**: Menganalisis konteks / intent user dan merutekan ke skill Antigravity yang paling tepat — meniru UX pemilihan mode Kiro (Default / Spec / Quick Spec / Bug Fix / Plan).

---

## C (Context & Input)
- Digunakan saat user menyebut "kiro", "mode kiro", atau saat permintaan ambigu antara spec, plan, bugfix, dan coding umum.
- Input bisa berupa: deskripsi fitur, laporan bug, permintaan plan, atau pertanyaan umum.
- Router ini adalah **thin wrapper** — tidak menduplikasi logika, hanya mendeteksi mode lalu mendelegasikan.

---

## C (Constraints & Guardrails)
- **DILARANG** memulai implementasi sebelum mode ditentukan.
- Jika konteks masih ambigu setelah baca pesan user, tanyakan **1 pertanyaan klarifikasi** saja (lihat format di bawah).
- Setelah mode ditentukan, **langsung load dan ikuti skill yang sesuai** — jangan duplikasi instruksinya di sini.
- Jika user sudah eksplisit menyebut kata kunci mode, **skip pertanyaan klarifikasi** dan langsung route.

---

## O (Output Format)

### Mode Detection Rules

Baca pesan user dan cocokkan dengan tabel berikut (prioritas dari atas ke bawah):

| Trigger Keywords | Mode Terdeteksi | Delegasikan ke Skill |
|-----------------|-----------------|----------------------|
| "spec penuh", "kiro spec", "fitur besar", "requirements", "desain fitur", "rancang sistem" | **SPEC (Full)** | `kiro-workflow` → jalur standar (requirements.md + design.md + tasks.md) |
| "quick spec", "spec cepat", "fitur kecil", "1-3 hari", "kiro quick" | **QUICK SPEC** | `kiro-workflow` → jalur cepat (quick-spec.md) |
| "micro spec", "bug spec", "kiro micro", "tweak", "< 1 hari", "perubahan kecil" | **MICRO SPEC** | `kiro-workflow` → jalur mikro (micro-spec.md) |
| "bug", "error", "crash", "broken", "tidak berfungsi", "debug", "investigate", "diagnose", "kiro bug" | **BUG FIX** | `systematic-debugging` |
| "plan saja", "jangan coding dulu", "plan only", "breakdown rencana", "kiro plan", "no code" | **PLAN** | `create-plan` (ringan/verbal) atau `writing-plans` (simpan ke file) |
| Semua lainnya / ambigu | **DEFAULT** | Deteksi skill otomatis via `using-superantigravity` |

---

### Routing Announcement

Selalu umumkan mode yang terdeteksi sebelum delegate, dengan format:

```
🎯 **Mode terdeteksi**: [MODE_NAME]
📋 **Mendelegasikan ke**: `[skill-name]` — [jalur jika ada]
```

Contoh:
```
🎯 **Mode terdeteksi**: QUICK SPEC
📋 **Mendelegasikan ke**: `kiro-workflow` — jalur cepat (quick-spec.md)
```

---

### Clarification Question (jika ambigu)

Jika tidak bisa menentukan mode dari konteks, ajukan pertanyaan ini **sekali saja**:

```
Saya perlu tahu mode yang tepat untuk request ini. Pilih salah satu:

**A) Spec Penuh** — Fitur baru besar, butuh requirements.md + design.md + tasks.md
**B) Quick Spec** — Fitur kecil (1-3 hari), satu file ringkas
**C) Micro Spec / Bug Spec** — Tweak kecil atau bug fix < 1 hari
**D) Bug Fix** — Ada sesuatu yang rusak/error, perlu investigation mendalam
**E) Plan Only** — Mau breakdown rencana, TANPA langsung coding
**F) Coding Langsung** — Langsung bantu implementasi tanpa spec dulu

Reply dengan huruf pilihanmu (atau ketik sendiri kalau beda).
```

---

## Mapping Lengkap: Kiro Built-in → Antigravity Equivalent

| Kiro Mode | Deskripsi Kiro | Antigravity Equivalent | Skill |
|-----------|---------------|------------------------|-------|
| **Default** | General coding assistance | Meta-skill detection otomatis | `using-superantigravity` |
| **Spec** | Structured feature development | Jalur standar 3-file | `kiro-workflow` |
| **Quick Spec** | Clarify → requirements → design → tasks (fast) | Jalur cepat 1-file | `kiro-workflow` (quick) |
| **Bug Fix** | Investigate → Diagnose → Resolve | Root-cause first debugging | `systematic-debugging` |
| **Plan** | Plan-only, no code changes | Plan ringan atau plan ke file | `create-plan` / `writing-plans` |

---

## Referensi Skill yang Didelegasikan

- [`kiro-workflow`](C:\Users\HP\.gemini\antigravity\skills\kiro-workflow\SKILL.md) — Spec workflow utama (3 jalur)
- [`systematic-debugging`](C:\Users\HP\.gemini\antigravity\skills\systematic-debugging\SKILL.md) — Bug fix dengan root cause investigation
- [`diagnosing-bugs`](C:\Users\HP\.gemini\antigravity\skills\diagnosing-bugs\SKILL.md) — Hard bugs dengan feedback loop
- [`create-plan`](C:\Users\HP\.gemini\antigravity\skills\create-plan\SKILL.md) — Plan ringan, read-only
- [`writing-plans`](C:\Users\HP\.gemini\antigravity\skills\writing-plans\SKILL.md) — Plan detail yang disimpan ke file
- [`using-superantigravity`](C:\Users\HP\.gemini\antigravity\skills\using-superantigravity\SKILL.md) — Meta-skill detection
