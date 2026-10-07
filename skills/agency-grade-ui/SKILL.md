---
name: agency-grade-ui
description: Build award-winning, agency-grade websites and landing pages matching the quality of NexStudio, TailGrids, and claude-directory. Enforces anti-AI-slop design rules, editorial typography, Framer Motion micro-interactions, and modern Tailwind patterns. Use whenever creating, redesigning, or polishing frontend websites, landing pages, or digital agency portfolios.
---

# Agency-Grade UI & Anti-Slop Design System

Panduan membuat website berstandar agensi digital papan atas (sekelas NexStudio / TailGrids / Awwwards) bebas dari tampilan generik "AI Slop".

---

## 1. Golden Tech Stack (Untuk Kualitas Visual Maksimal)

1. **Core:** React 19 / Next.js (App Router) atau Vite + React + TypeScript
2. **Styling:** Tailwind CSS v3/v4
3. **Animations:** `framer-motion` (scroll reveal, staggered entrance, hover spring) + `lenis` (smooth scroll)
4. **Icons:** `lucide-react` (stroke uniform 1.5px / 1.75px)
5. **Primitives:** Radix UI / `@radix-ui/react-*` (aksesibilitas & interaction state)
6. **FX (Optional):** Three.js / Canvas noise / subtle grid shader

---

## 2. Anti-Slop Rules (Dilarang Keras)

* ❌ **NO Generic AI Gradients:** Jangan pakai radial blur gradient ungu/cyan murahan di background.
* ❌ **NO Floating Cards Uniformity:** Jangan buat 3 card putih berjejer dengan shadow melayang besar tanpa struktur hirarki.
* ❌ **NO Marketing Cliché:** Jangan pakai copywriter klise AI ("Unleash your potential", "Revolutionize your workflow").
* ❌ **NO Rounded Everything:** Hindari `rounded-3xl` di semua elemen. Gunakan kontras radius (`rounded-md` atau `rounded-xl` dengan border presisi).
* ❌ **NO Low-Contrast Text:** Hindari `text-gray-400` pada background putih atau abu-abu pudar.

---

## 3. Visual Craft Guidelines (Ciri Khas NexStudio)

### A. Editorial Typography
* Font headline: Modern Sans tebal (`Clash Display`, `Plus Jakarta Sans`, `Inter Tight`, atau `Syne`).
* Tracking ketat untuk display title: `tracking-tight` atau `-tracking-[0.03em]`.
* Kontras hirarki ekstrem: Judul sangat besar (`text-5xl` sampai `text-7xl font-bold`), subtext padat & rapi (`text-sm` / `text-base` `text-neutral-400`).

### B. Dark & Brutal Minimalist Aesthetic
* Background gelap bertekstur: `#080808` / `#0D0D0E` (bukan pure `#000000`).
* Border hair-line elegan: `border border-white/[0.08]` atau `border-neutral-800`.
* Accent pop: 1 warna aksen elektrik (misal: neon lime `#D4FF00`, cyber orange `#FF5500`, atau cobalt blue `#0055FF`) hanya untuk CTA & badges.

### C. Bento Grids & Asymmetrical Layouts
* Gunakan layout asimetris: 1 card besar (span 2 kolom) + 2 card kecil, bukan grid seragam.
* Status badges: Pill badge kecil di atas judul (`px-3 py-1 text-xs uppercase tracking-widest border rounded-full`).

### D. Micro-Interactions (Framer Motion)
* Hover efek: Magnetik subtle atau border glow on hover (`group-hover:border-white/20 transition-all duration-300`).
* Staggered fade-up untuk teks dan komponen saat scroll.
