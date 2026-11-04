# 21st.dev Master Portfolio & Creative Agency Shell (AURA Architecture)

Pola arsitektur portfolio studio kreatif modern berbasis GSAP, Framer Motion, dan Tailwind CSS (Inspirasi: AURA Creative Agency Template by larsen66).

---

## 1. Anatomi Portofolio Kreatif Modern (Editorial Luxury)

1. **Tipografi Editorial Raksasa**:
   - Judul berukuran masif (80px+) dengan pelacakan huruf rapat (`tracking-tighter`).
   - Kombinasi font serif anggun / display editorial dengan sans-serif minimalis.
2. **Kinetic Hover Reveal (Cursor Following Thumbnail)**:
   - Saat pengunjung mengarahkan kursor ke daftar proyek teks, gambar preview proyek melayang mengikuti posisi pointer mouse.
3. **Smooth Magnetic Navigation & Marquee Reel**:
   - Strip teks berjalan tanpa henti (*infinite horizontal reel*) yang memperlihatkan keahlian atau kutipan studio.
4. **Grid Asimetris Karya Pilihan (Selected Works)**:
   - Kartu proyek dengan rasio aspek editorial (4:5 atau 16:9), dilengkapi transisi zoom gambar saat hover.

---

## 2. Blueprint Kode Master (The AURA Creative Agency Shell)

```tsx
import React, { useState, useEffect } from "react";
import { motion, useMotionValue, useSpring } from "framer-motion";
import { ArrowUpRight, Plus } from "lucide-react";

interface ProjectItem {
  id: string;
  title: string;
  category: string;
  year: string;
  image: string;
}

const PROJECTS: ProjectItem[] = [
  {
    id: "1",
    title: "Berlayar Coffee Roastery",
    category: "Brand Identity & POS Web",
    year: "2026",
    image: "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?q=80&w=1200&auto=format&fit=crop",
  },
  {
    id: "2",
    title: "Verve Kinetic Audio",
    category: "Sound Design & Digital Platform",
    year: "2025",
    image: "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=1200&auto=format&fit=crop",
  },
  {
    id: "3",
    title: "Onyx Architectural Studio",
    category: "Spatial Experience & WebGL",
    year: "2025",
    image: "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=1200&auto=format&fit=crop",
  },
];

export function AuraCreativeAgencyPortfolio() {
  const [activeImage, setActiveImage] = useState<string | null>(null);

  // Kursor magnetis untuk thumbnail preview melayang
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  const springConfig = { damping: 25, stiffness: 200 };
  const cursorX = useSpring(mouseX, springConfig);
  const cursorY = useSpring(mouseY, springConfig);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      mouseX.set(e.clientX);
      mouseY.set(e.clientY);
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, [mouseX, mouseY]);

  return (
    <div className="min-h-screen bg-[#0d0d0f] text-[#f2f2f5] font-sans selection:bg-white selection:text-black">
      
      {/* Floating Cursor Thumbnail Preview */}
      {activeImage && (
        <motion.div
          style={{ x: cursorX, y: cursorY }}
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 0.8 }}
          transition={{ duration: 0.2 }}
          className="fixed top-0 left-0 w-80 h-52 pointer-events-none z-50 -translate-x-1/2 -translate-y-1/2 overflow-hidden rounded-xl shadow-2xl border border-white/20 hidden md:block"
        >
          <img
            src={activeImage}
            alt="Preview Project"
            className="w-full h-full object-cover"
          />
        </motion.div>
      )}

      {/* Header Nav */}
      <header className="fixed top-0 inset-x-0 z-40 px-8 py-6 flex items-center justify-between mix-blend-difference">
        <span className="font-mono text-sm tracking-widest uppercase font-bold">AURA STUDIO</span>
        <div className="flex items-center gap-8 text-xs font-mono tracking-widest uppercase">
          <a href="#work" className="hover:opacity-70 transition-opacity">Work</a>
          <a href="#about" className="hover:opacity-70 transition-opacity">Studio</a>
          <a href="#contact" className="hover:opacity-70 transition-opacity">Contact</a>
        </div>
      </header>

      {/* Hero Section */}
      <section className="min-h-[80vh] flex flex-col justify-end px-8 pb-20 pt-36 border-b border-white/10">
        <div className="font-mono text-xs text-neutral-400 mb-6 tracking-widest uppercase">
          [ 01 / CREATIVE DIRECTION & FRONTEND ARCHITECTURE ]
        </div>
        <h1 className="text-6xl sm:text-8xl lg:text-9xl font-bold tracking-tighter leading-none mb-8">
          DIGITAL <br />
          <span className="italic font-serif font-light text-neutral-400">ARTIFACTS.</span>
        </h1>
        <p className="max-w-md text-sm text-neutral-400 font-light leading-relaxed">
          Crafting bespoke digital interfaces and elevated interactive systems for brands that demand enduring aesthetic relevance.
        </p>
      </section>

      {/* Selected Works - Interactive List Pattern */}
      <section id="work" className="px-8 py-24">
        <div className="flex items-center justify-between pb-8 border-b border-white/10 font-mono text-xs text-neutral-500 uppercase">
          <span>Selected Index</span>
          <span>(03)</span>
        </div>

        <div className="divide-y divide-white/10">
          {PROJECTS.map((item) => (
            <div
              key={item.id}
              onMouseEnter={() => setActiveImage(item.image)}
              onMouseLeave={() => setActiveImage(null)}
              className="group py-12 flex flex-col sm:flex-row sm:items-center justify-between gap-4 cursor-pointer transition-colors hover:px-4 duration-300"
            >
              <div className="flex items-baseline gap-6">
                <span className="font-mono text-xs text-neutral-500">{item.id}</span>
                <h2 className="text-3xl sm:text-5xl font-bold tracking-tight group-hover:italic transition-all">
                  {item.title}
                </h2>
              </div>

              <div className="flex items-center gap-12 font-mono text-xs text-neutral-400">
                <span>{item.category}</span>
                <span>{item.year}</span>
                <ArrowUpRight className="w-5 h-5 text-white transform group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Infinite Text Marquee */}
      <div className="py-12 border-y border-white/10 overflow-hidden select-none bg-[#09090b]">
        <div className="flex whitespace-nowrap gap-12 animate-marquee font-mono text-xs uppercase tracking-widest text-neutral-400">
          <span>AURA STUDIO • BERLIN / JAKARTA</span>
          <span>INTERACTION ENGINEERING • REACT 19 • GSAP</span>
          <span>HIGH-FIDELITY DESIGN SYSTEMS</span>
          <span>AURA STUDIO • BERLIN / JAKARTA</span>
          <span>INTERACTION ENGINEERING • REACT 19 • GSAP</span>
        </div>
      </div>

      {/* Minimal Footer */}
      <footer id="contact" className="px-8 py-20 flex flex-col sm:flex-row items-baseline justify-between gap-8 font-mono text-xs text-neutral-500">
        <div>
          <p className="text-white text-base font-bold mb-2">HAVE AN AMBITIOUS VISION?</p>
          <p>hello@aurastudio.agency</p>
        </div>
        <div>
          <p>© 2026 AURA STUDIO. ALL RIGHTS RESERVED.</p>
        </div>
      </footer>

    </div>
  );
}
```

---

## 3. Catatan Teknis & Kepatuhan Performa
1. **Kinetic Hover Preview**: Kursor mouse menggunakan `useMotionValue` dan `useSpring` dari Framer Motion untuk interpolasi koordinat mouse tanpa memicu re-render react berulang, menjaga performa tetap 60fps.
2. **Fallback Mobile**: Pada layar sentuh (`hidden md:block`), preview melayang dinonaktifkan agar tidak mengganggu navigasi sentuh.
