# 21st.dev Master Link & Hyperlink Interaction Templates

Analisis pola dan blueprint komponen Link (Tautan Interaktif) berdasarkan 354+ komponen modern di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Link Modern

### Arketipe 1: The Directional Underline Slide (Magnetic Line)
- **Fungsi**: Tautan teks di dalam badan artikel, paragraf dokumentasi, atau menu navigasi minimalis.
- **Karakteristik Visual**:
  - Tautan tidak memiliki garis bawah (*underline*) bawaan browser yang kaku.
  - Saat kursor mouse menyorot (*hover*), sebuah garis horizontal tipis beranimasi memanjang dari kiri ke kanan (atau dari tengah ke kedua ujung) secara elastis menggunakan transisi CSS `scale-x-0 group-hover:scale-x-100 origin-left`.
- **Inspirasi**: Stripe & Vercel Documentation Links.

### Arketipe 2: The Arrow Reveal / 45° Kinetic Launch (External Links)
- **Fungsi**: Tautan CTA sekunder ("Pelajari Selengkapnya →") atau tautan ke situs luar/tab baru.
- **Karakteristik Visual**:
  - Ikon panah (`ArrowUpRight` atau `ArrowRight`) bergerak beberapa piksel ke arah serong kanan-atas saat di-hover (`group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform`).
- **Inspirasi**: `Feature Modern (brijr)`.

### Arketipe 3: The Stretched Card Link (Pseudo-Element Clickable Area)
- **Fungsi**: Membuat seluruh bidang kartu (misal: kartu artikel blog, kartu lowongan kerja) dapat diklik tanpa merusak semantik HTML.
- **Karakteristik Visual**:
  - Tautan utama di dalam judul kartu diperluas ke seluruh kartu menggunakan kelas Tailwind `after:absolute after:inset-0`. Ini mencegah penulisan kode buruk seperti membungkus seluruh tag `<div>` besar atau `<article>` di dalam tag `<a>`.

### Arketipe 4: The Gradient Glow Text Shimmer
- **Fungsi**: Tautan eksklusif atau penawaran khusus (misal: "Upgrade ke Enterprise ✨").
- **Karakteristik Visual**:
  - Teks tautan menggunakan gradien warna berpendar yang memiliki efek kilau cahaya mengalir saat di-hover.

---

## 2. Blueprint Kode Master (The 3 Essential Link Variants)

```tsx
import { ArrowUpRight, ArrowRight, Sparkles } from "lucide-react";

// Variant 1: Magnetic Underline Link (Untuk Teks Panjang)
export function UnderlineLink({ href, children }: { href: string; children: React.ReactNode }) {
  return (
    <a
      href={href}
      className="group relative inline-block font-medium text-slate-200 hover:text-white transition-colors"
    >
      <span>{children}</span>
      {/* Animated Underline */}
      <span className="absolute bottom-0 left-0 w-full h-[1.5px] bg-indigo-500 origin-left scale-x-0 transition-transform duration-300 ease-out group-hover:scale-x-100" />
    </a>
  );
}

// Variant 2: Kinetic Arrow Link (Untuk Aksi CTA & Tab Baru)
export function KineticArrowLink({ href, label = "Lihat Dokumentasi API" }: { href: string; label?: string }) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className="group inline-flex items-center gap-1.5 text-xs font-semibold text-indigo-400 hover:text-indigo-300 transition-colors"
    >
      <span>{label}</span>
      <ArrowUpRight className="w-3.5 h-3.5 transition-transform duration-200 ease-out group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
    </a>
  );
}

// Variant 3: Accessible Stretched Card Link Pattern
export function StretchedCardLink({
  title,
  description,
  href,
}: {
  title: string;
  description: string;
  href: string;
}) {
  return (
    <div className="relative p-5 rounded-2xl border border-slate-800 bg-slate-900/50 hover:bg-slate-900 hover:border-slate-700 transition-all duration-300 group shadow-lg">
      <div className="flex items-start justify-between">
        <h3 className="text-sm font-bold text-white group-hover:text-indigo-400 transition-colors">
          {/* Stretched Anchor: Memperluas area klik ke seluruh kontainer div */}
          <a href={href} className="after:absolute after:inset-0 after:rounded-2xl focus:outline-none">
            {title}
          </a>
        </h3>
        <ArrowRight className="w-4 h-4 text-slate-500 group-hover:text-indigo-400 group-hover:translate-x-1 transition-all duration-300" />
      </div>
      
      <p className="text-xs text-slate-400 mt-2 leading-relaxed">
        {description}
      </p>
    </div>
  );
}
```

---

## 3. Checklist Aksesibilitas Link (WCAG 2.2)
1. **Pembeda Visual Non-Warna**: Tautan yang berada di tengah paragraf teks tidak boleh hanya mengandalkan perbedaan warna biru saja. Beri sedikit garis bawah permanen atau tebalkan fontnya (`font-semibold`) agar pengguna dengan buta warna dapat membedakan kata tersebut sebagai tautan.
2. **Atribut Keamanan Tab Baru**: Tautan eksternal yang menggunakan `target="_blank"` **wajib** menyertakan `rel="noopener noreferrer"` untuk mencegah serangan celah keamanan *Tabnabbing*.
3. **Pemberitahuan Eksternal untuk Screen Reader**: Untuk tautan yang melompat ke situs lain atau tab baru, sematkan teks tersembunyi seperti `<span className="sr-only">(buka di tab baru)</span>`.
