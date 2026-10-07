# 21st.dev Master Carousel & Slider Templates

Analisis pola dan blueprint komponen Carousel berdasarkan 145+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Carousel Modern

### Arketipe 1: The Stacked "Coverflow" Carousel
- **Fungsi**: Presentasi visual bergaya 3D untuk memamerkan produk premium, gambar fitur, atau portofolio desain.
- **Karakteristik Visual**:
  - Item yang tidak aktif (berada di kiri/kanan atau belakang) ukurannya diperkecil (`scale: 0.8`), opasitasnya dikurangi (`opacity: 0.5`), dan digeser ke sumbu Z.
  - Kartu aktif berada tepat di tengah dengan skala penuh (`scale: 1`) dan bayangan yang lebih tajam.
- **Inspirasi**: `Coverflow Carousel (Ruixen)`, `CardStack (Ruixen)`, `Stacked Card Carousel (ShadcnSpace)`.

### Arketipe 2: The Thumbnail Gallery Carousel
- **Fungsi**: Galeri produk e-commerce atau penampil aset foto *real estate*.
- **Karakteristik Visual**:
  - Bagian atas memuat gambar/kartu utama berukuran besar.
  - Bagian bawah memuat barisan pratinjau kecil (*Thumbnails*).
  - Mengklik thumbnail mana pun akan langsung menggeser/menganimasi gambar besar di atasnya.
- **Inspirasi**: `Thumbnail Carousel (Awanish Verma)`, `Framer Carousel Thumbnails (ui layout)`.

### Arketipe 3: The Infinite Autoplay Marquee (Testimonials)
- **Fungsi**: *Social Proof* untuk halaman pendaratan (Testimoni Pelanggan atau Klien).
- **Karakteristik Visual**:
  - Bergeser perlahan secara otomatis tanpa henti (*infinite loop*).
  - Terdapat tombol jeda (*Pause on hover*).
  - Ujung kiri dan kanan kontainer memiliki efek *gradient mask* memudar transparan agar kartu seolah-olah "muncul dari ketiadaan".
- **Inspirasi**: `Testimonial (prebuiltui)`, `Marquee (Hayden Bleasel)`.

### Arketipe 4: The Drag-to-Scroll Snap Carousel
- **Fungsi**: Tata letak standar "Geser untuk melihat lebih" yang ramah seluler (*mobile friendly*).
- **Karakteristik Visual**:
  - Mengandalkan CSS `scroll-snap-type: x mandatory` alih-alih Javascript berat.
  - Terdapat indikator titik-titik (*dot indicators*) di bagian bawah, di mana titik aktif memanjang menjadi kapsul pendek.
- **Inspirasi**: `Scroll X Carousel`, `Snap Carousel (Özer)`.

---

## 2. Blueprint Kode Master (The 3D Stacked Coverflow Carousel)

```tsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronLeft, ChevronRight } from "lucide-react";

const CAROUSEL_DATA = [
  { id: 1, title: "Desain Sistem", desc: "Arsitektur komponen modular", color: "from-indigo-500 to-purple-500" },
  { id: 2, title: "Analitik Mikro", desc: "Data akurat seketika", color: "from-rose-500 to-orange-500" },
  { id: 3, title: "Autentikasi Pintar", desc: "Login biometrik", color: "from-emerald-500 to-teal-500" },
  { id: 4, title: "Integrasi API", desc: "Menghubungkan layanan luar", color: "from-sky-500 to-indigo-500" },
];

export function StackedCoverflowCarousel() {
  const [activeIndex, setActiveIndex] = useState(0);
  const [direction, setDirection] = useState(1); // 1 = Kanan, -1 = Kiri

  const nextSlide = () => {
    setDirection(1);
    setActiveIndex((prev) => (prev + 1) % CAROUSEL_DATA.length);
  };

  const prevSlide = () => {
    setDirection(-1);
    setActiveIndex((prev) => (prev - 1 + CAROUSEL_DATA.length) % CAROUSEL_DATA.length);
  };

  return (
    <div className="relative w-full max-w-2xl mx-auto h-[400px] flex items-center justify-center overflow-hidden perspective-[1000px]">
      
      {/* Cards Container */}
      <div className="relative w-[300px] h-[400px] flex items-center justify-center">
        <AnimatePresence mode="popLayout" custom={direction}>
          {CAROUSEL_DATA.map((item, index) => {
            // Kalkulasi Jarak dari Index Aktif
            const offset = (index - activeIndex + CAROUSEL_DATA.length) % CAROUSEL_DATA.length;
            const isCenter = offset === 0;
            const isRight = offset === 1;
            const isLeft = offset === CAROUSEL_DATA.length - 1;

            if (!isCenter && !isRight && !isLeft) return null; // Sembunyikan kartu di belakang jauh

            let zIndex = isCenter ? 30 : 20;
            let scale = isCenter ? 1 : 0.85;
            let translateX = isCenter ? "0%" : isRight ? "40%" : "-40%";
            let opacity = isCenter ? 1 : 0.4;
            let rotateY = isCenter ? 0 : isRight ? -15 : 15;

            return (
              <motion.div
                key={item.id}
                custom={direction}
                initial={{ opacity: 0, scale: 0.8, x: direction === 1 ? "100%" : "-100%" }}
                animate={{
                  opacity,
                  scale,
                  x: translateX,
                  rotateY,
                  zIndex,
                }}
                exit={{ opacity: 0, scale: 0.8, x: direction === 1 ? "-100%" : "100%" }}
                transition={{ type: "spring", stiffness: 300, damping: 30 }}
                className={`absolute w-full h-[320px] rounded-3xl p-6 flex flex-col justify-end shadow-2xl bg-gradient-to-br ${item.color}`}
              >
                <div className="bg-slate-950/40 backdrop-blur-md p-4 rounded-xl border border-white/10">
                  <h3 className="text-xl font-bold text-white">{item.title}</h3>
                  <p className="text-xs text-white/80 mt-1">{item.desc}</p>
                </div>
              </motion.div>
            );
          })}
        </AnimatePresence>
      </div>

      {/* Navigation Controls */}
      <div className="absolute bottom-2 left-1/2 -translate-x-1/2 flex items-center gap-4 bg-slate-900/60 backdrop-blur-xl px-4 py-2 border border-slate-800 rounded-full z-40">
        <button onClick={prevSlide} className="p-2 rounded-full hover:bg-slate-800 text-slate-300 transition-colors">
          <ChevronLeft className="w-4 h-4" />
        </button>
        
        {/* Dot Indicators */}
        <div className="flex items-center gap-1.5">
          {CAROUSEL_DATA.map((_, idx) => (
            <div
              key={idx}
              className={`h-1.5 rounded-full transition-all duration-300 ${
                activeIndex === idx ? "w-6 bg-white" : "w-1.5 bg-slate-600"
              }`}
            />
          ))}
        </div>

        <button onClick={nextSlide} className="p-2 rounded-full hover:bg-slate-800 text-slate-300 transition-colors">
          <ChevronRight className="w-4 h-4" />
        </button>
      </div>

    </div>
  );
}
```

---

## 3. Checklist UX & Aksesibilitas Carousel
1. **WAI-ARIA Rotator**: Gunakan atribut `aria-roledescription="carousel"` pada kontainer pembungkus. Setiap slide individu harus memiliki `aria-roledescription="slide"`.
2. **Aturan "Jeda Otomatis" (Auto-pause)**: Jika *carousel* memiliki pengaturan putar otomatis (*autoplay*), itu **WAJIB** dijeda (*pause*) ketika pengguna mengarahkan kursor (*hover*) ke area carousel atau ketika mereka memfokuskan elemen di dalamnya melalui keyboard.
3. **Mekanisme Fallback Tanpa JS**: Khusus untuk *Snap Carousel* datar (bukan 3D), buat struktur DOM yang dapat digulir (*scrollable container `overflow-x-auto`*) sehingga jika animasi JS rusak, pengguna ponsel tetap dapat menggeser layar (*swipe*) menggunakan properti murni CSS `scroll-snap`.
