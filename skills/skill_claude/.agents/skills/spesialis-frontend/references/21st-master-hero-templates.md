# 21st.dev Master Hero Templates & Architecture

Analisis pola dan blueprint komponen Hero section berdasarkan 1,150+ komponen di 21st.dev (React 19 + TypeScript + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Hero Section Terpopuler di 21st.dev

### Arketipe 1: The Illuminated SaaS Hero (Paling Populer)
- **Komponen Khas**: `Illuminated Hero (Efferd)`, `Hero Section 06 (Ruixen)`, `SaaS Template (vvisedev)`.
- **Anatomi Visual**:
  - Background gelap pekat (`#090d16`) dengan central radial glow (mist gradient amber/indigo di bagian atas tengah).
  - Floating pill badge di atas headline (misal: "✨ Introducing v2.0 →").
  - Headline tebal dengan gradien teks atau efek shimmer.
  - Dual CTA: Tombol Glow/Shimmer primer + Tombol Glass/Border sekunder.
  - Social proof avatar stack ("Bergabung dengan 10.000+ pengguna").
  - Mockup UI / Browser preview melayang di bawah dengan border tipis dan bayangan berlapis (drop-shadow).

### Arketipe 2: The Sonar / Dither Grid Hero (Teknikal & Developer Tools)
- **Komponen Khas**: `Sonar Grid (NIMA MZ)`, `Diced Hero (Maxim Bortnikov)`, `Modern Landing Hero`.
- **Anatomi Visual**:
  - Background berupa grid titik (dot-grid) atau garis koordinat SVG dengan efek fade out radial di tepi layar.
  - Tipografi tegas monospaced (`JetBrains Mono` atau `Space Grotesk`).
  - Terminal interaktif atau kode editor melayang dengan syntax highlighting.

### Arketipe 3: The Editorial Collage / Image Fan (Brand, Kreatif & F&B)
- **Komponen Khas**: `Centered Hero with Image Fan (felipemenezes098)`, `Editorial Collage Hero`.
- **Anatomi Visual**:
  - Headline besar berkarakter (misal `Instrument Serif` atau `Playfair Display`).
  - Kartu foto bertumpuk miring (fan out) yang membuka saat di-hover.
  - Sangat cocok untuk produk visual, warung kopi, fashion, atau galeri karya.

### Arketipe 4: The 3D / Shader Kinetic Hero (Web3, AI & Eksperimental)
- **Komponen Khas**: `3D Animation (Dhileep Kumar GM)`, `flow-gradient-heroSection`.
- **Anatomi Visual**:
  - Canvas WebGL / Three.js / Spline scene di belakang atau di sebelah kanan copy.
  - Interaksi rotasi 3D mengikuti posisi kursor (mouse parallax).

---

## 2. Blueprint Kode Master (The Illuminated SaaS Hero)
Template React + Tailwind v4 + Framer Motion siap pakai:

```tsx
import { motion } from "framer-motion";
import { ArrowRight, Star, Terminal } from "lucide-react";

export function MasterHero() {
  return (
    <section className="relative min-h-[90vh] flex flex-col items-center justify-center overflow-hidden bg-[#090d16] text-white px-6 pt-24 pb-16">
      
      {/* 1. Ambient Glow & Grid Background */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[350px] bg-gradient-to-b from-indigo-500/20 via-purple-500/10 to-transparent blur-[120px] pointer-events-none" />
      <div className="absolute inset-0 bg-[linear-gradient(to_right,#1f293d0f_1px,transparent_1px),linear-gradient(to_bottom,#1f293d0f_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] pointer-events-none" />

      <div className="relative z-10 max-w-4xl mx-auto text-center flex flex-col items-center">
        
        {/* 2. Floating Announcement Pill */}
        <motion.div
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border border-indigo-500/20 bg-indigo-500/10 text-xs font-mono text-indigo-300 mb-8 backdrop-blur-md hover:border-indigo-500/40 transition-colors cursor-pointer"
        >
          <span className="w-2 h-2 rounded-full bg-indigo-400 animate-pulse" />
          <span>v2.4 Engine Live</span>
          <ArrowRight className="w-3.5 h-3.5 text-indigo-400" />
        </motion.div>

        {/* 3. Headline & Subtitle */}
        <motion.h1 
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.1 }}
          className="text-4xl sm:text-6xl md:text-7xl font-bold tracking-tight text-slate-100 leading-[1.1] max-w-3xl"
        >
          Bangun antarmuka modern <br className="hidden sm:inline" />
          <span className="bg-gradient-to-r from-indigo-400 via-purple-300 to-pink-400 bg-clip-text text-transparent">
            tanpa friksi template.
          </span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
          className="mt-6 text-base sm:text-lg text-slate-400 max-w-2xl leading-relaxed"
        >
          Sistem komponen frontend deterministik berstandar WCAG 2.2 AA. Dioptimalkan untuk kecepatan muat cepat, tipografi tegas, dan interaksi mulus.
        </motion.p>

        {/* 4. Dual Call To Action */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.3 }}
          className="mt-10 flex flex-wrap items-center justify-center gap-4 w-full sm:w-auto"
        >
          <button className="w-full sm:w-auto px-7 py-3 rounded-full bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/25 transition-all active:scale-95 flex items-center justify-center gap-2">
            <span>Mulai Sekarang</span>
            <ArrowRight className="w-4 h-4" />
          </button>
          
          <button className="w-full sm:w-auto px-7 py-3 rounded-full border border-slate-800 bg-slate-900/50 hover:bg-slate-900 text-slate-300 hover:text-white text-sm font-medium transition-all backdrop-blur-sm flex items-center justify-center gap-2">
            <Terminal className="w-4 h-4 text-slate-400" />
            <span>Dokumentasi API</span>
          </button>
        </motion.div>

        {/* 5. Social Proof / Trust Badge */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="mt-12 flex items-center gap-4 text-xs text-slate-400"
        >
          <div className="flex -space-x-2">
            <div className="w-7 h-7 rounded-full bg-slate-700 border-2 border-[#090d16]" />
            <div className="w-7 h-7 rounded-full bg-slate-600 border-2 border-[#090d16]" />
            <div className="w-7 h-7 rounded-full bg-slate-500 border-2 border-[#090d16]" />
          </div>
          <div className="flex items-center gap-1">
            <div className="flex text-amber-400">
              {[...Array(5)].map((_, i) => (
                <Star key={i} className="w-3.5 h-3.5 fill-current" />
              ))}
            </div>
            <span className="font-medium text-slate-300 ml-1">5.0</span>
            <span>(dari 1,200+ ulasan)</span>
          </div>
        </motion.div>

      </div>

      {/* 6. Floating Product Mockup / Surface Preview */}
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7, delay: 0.5 }}
        className="relative mt-16 w-full max-w-5xl rounded-2xl border border-slate-800/80 bg-slate-900/40 p-2 backdrop-blur-xl shadow-2xl shadow-indigo-500/5"
      >
        <div className="rounded-xl border border-slate-800 bg-slate-950/80 overflow-hidden aspect-[16/9] flex items-center justify-center text-slate-600 font-mono text-xs">
          [ Interactive App Workspace Preview ]
        </div>
      </motion.div>

    </section>
  );
}
```

---

## 3. Aturan Desain & Rekayasa Hero Section
1. **LCP Guard**: Hindari video background berat atau WebGL tanpa poster fallback. Pastikan teks judul utama ter-render dalam <2.5 detik.
2. **Ketinggian Kontainer**: Gunakan `min-h-[85vh]` atau `min-h-[90vh]` alih-alih `h-screen` kaku, agar di mobile browser dengan dynamic address bar konten tidak terpotong (CLS protection).
3. **Kontras Teks**: Pastikan teks di atas efek glow atau canvas tetap memiliki kontras minimal 4.5:1 terhadap background.
