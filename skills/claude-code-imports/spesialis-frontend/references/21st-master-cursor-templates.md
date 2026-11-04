# 21st.dev Master Cursor & Mouse Interaction Templates

Analisis pola dan blueprint komponen Kursor Kustom & Interaksi Mouse berdasarkan 115+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Interaksi Kursor Modern

### Arketipe 1: The Spring Trailing Cursor (Follower Dot)
- **Fungsi**: Memberikan kesan halus dan estetis pada situs web portofolio atau pameran desain agensi kreatif.
- **Karakteristik Visual**:
  - Menyembunyikan kursor bawaan sistem (`cursor-none` pada body).
  - Merender lingkaran SVG kecil (atau titik) yang mengikuti posisi koordinat kursor asli `(x, y)` namun dengan penundaan elastis (*spring physics delay*).
- **Inspirasi**: `Fluid Magnetic Cursor (Hossain Jahed)`, `Cursor with spring (Julien Thibeaut)`.

### Arketipe 2: The Spotlight / Flashlight Effect
- **Fungsi**: Menerangi kartu fitur gelap (Bento Grid) saat di-hover, memancarkan batas bercahaya yang mengikuti posisi mouse.
- **Karakteristik Visual**:
  - Menggunakan CSS *Radial Gradient* dinamis yang pusatnya (`background-position`) terus diperbarui berdasarkan koordinat kursor mouse relatif terhadap tepi kartu.
- **Inspirasi**: `Spotlight Border Only (Julien Thibeaut)`.

### Arketipe 3: The Cursor Proximity Sensor (Distance Reaction)
- **Fungsi**: Menu navigasi yang sangat hidup atau tipografi tebal yang merespons jarak kursor pengguna.
- **Karakteristik Visual**:
  - Huruf atau ikon akan membesar (*scale up*) atau menebal secara bobot font (*variable font weight interpolating*) semakin dekat jarak kursor ke elemen tersebut. Menggunakan fungsi pitagoras untuk menghitung jarak.
- **Inspirasi**: `Text Cursor Proximity Scale (Cnippet)`, `Variable Font Proximity Nav`.

### Arketipe 4: The Liquid / Noise Trail
- **Fungsi**: Efek artistik murni eksperimental (Webgl/Canvas).
- **Karakteristik Visual**: Meninggalkan jejak seperti cairan tinta, distorsi, atau noise cyberpunk saat mouse digerakkan cepat.
- **Inspirasi**: `Liquid Cursor`, `NeuralNoiseCursor`.

---

## 2. Blueprint Kode Master

### A. The Spring Trailing Custom Cursor (Framer Motion)
```tsx
import { useEffect, useState } from "react";
import { motion, useMotionValue, useSpring } from "framer-motion";

export function CustomSpringCursor() {
  // Posisi asli kursor (tidak di-render)
  const cursorX = useMotionValue(-100);
  const cursorY = useMotionValue(-100);

  // Animasi pegas untuk kursor pengikut (Trailer)
  const springConfig = { damping: 25, stiffness: 400, mass: 0.5 };
  const cursorXSpring = useSpring(cursorX, springConfig);
  const cursorYSpring = useSpring(cursorY, springConfig);

  const [isClicking, setIsClicking] = useState(false);
  const [isHoveringLink, setIsHoveringLink] = useState(false);

  useEffect(() => {
    // 1. Memperbarui posisi
    const moveCursor = (e: MouseEvent) => {
      // Offset -16px agar kursor tetap di tengah lingkaran (ukuran w-8 = 32px)
      cursorX.set(e.clientX - 16);
      cursorY.set(e.clientY - 16);
    };

    // 2. Deteksi klik
    const handleMouseDown = () => setIsClicking(true);
    const handleMouseUp = () => setIsClicking(false);

    // 3. Deteksi hover elemen yang bisa diklik (<a> atau <button>)
    const handleMouseOver = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      if (target.closest("a") || target.closest("button") || target.closest("[role='button']")) {
        setIsHoveringLink(true);
      } else {
        setIsHoveringLink(false);
      }
    };

    window.addEventListener("mousemove", moveCursor);
    window.addEventListener("mousedown", handleMouseDown);
    window.addEventListener("mouseup", handleMouseUp);
    window.addEventListener("mouseover", handleMouseOver);

    return () => {
      window.removeEventListener("mousemove", moveCursor);
      window.removeEventListener("mousedown", handleMouseDown);
      window.removeEventListener("mouseup", handleMouseUp);
      window.removeEventListener("mouseover", handleMouseOver);
    };
  }, [cursorX, cursorY]);

  return (
    <>
      {/* 
        Sembunyikan kursor asli (Opsional):
        Tambahkan <style>{`body { cursor: none; }`}</style> jika ingin mematikan panah mouse murni.
      */}
      
      {/* Render Spring Trailer Circle */}
      <motion.div
        className="fixed top-0 left-0 w-8 h-8 rounded-full border border-indigo-500/50 pointer-events-none z-[9999] mix-blend-screen flex items-center justify-center"
        style={{
          x: cursorXSpring,
          y: cursorYSpring,
        }}
        animate={{
          scale: isClicking ? 0.8 : isHoveringLink ? 1.5 : 1,
          backgroundColor: isHoveringLink ? "rgba(99, 102, 241, 0.1)" : "transparent",
        }}
        transition={{ type: "spring", stiffness: 300, damping: 20 }}
      >
        {/* Core Dot (Kursor aslinya) */}
        <motion.div 
          className="w-1.5 h-1.5 bg-indigo-400 rounded-full"
          animate={{ scale: isHoveringLink ? 0 : 1 }}
        />
      </motion.div>
    </>
  );
}
```

### B. The Hover Spotlight Card Effect
```tsx
import { useRef, useState } from "react";

export function SpotlightCard({ children }: { children: React.ReactNode }) {
  const divRef = useRef<HTMLDivElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [opacity, setOpacity] = useState(0);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!divRef.current) return;
    const rect = divRef.current.getBoundingClientRect();
    setPosition({ x: e.clientX - rect.left, y: e.clientY - rect.top });
  };

  return (
    <div
      ref={divRef}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setOpacity(1)}
      onMouseLeave={() => setOpacity(0)}
      className="relative overflow-hidden rounded-2xl border border-slate-800 bg-slate-900/60 p-6 shadow-2xl group"
    >
      {/* Spotlight Gradient yang Mengikuti Mouse */}
      <div
        className="pointer-events-none absolute -inset-px transition-opacity duration-300"
        style={{
          opacity,
          background: `radial-gradient(400px circle at ${position.x}px ${position.y}px, rgba(99, 102, 241, 0.15), transparent 40%)`,
        }}
      />
      {/* Konten Asli Kartu */}
      <div className="relative z-10">{children}</div>
    </div>
  );
}
```

---

## 3. Aturan Emas Desain Kursor Kustom
1. **Aturan "Pointer-Events-None"**: Setiap elemen kursor kustom WAJIB menggunakan kelas CSS `pointer-events-none`. Jika terlupa, elemen lingkaran kursor tersebut akan menghalangi panah mouse asli untuk menekan tombol atau mengisi input di bawahnya (menyebabkan *dead clicks*).
2. **Kapan Boleh Mematikan Kursor Bawaan?**: Mematikan kursor sistem (`cursor: none`) hanya diperbolehkan untuk situs pameran seni, agensi visual, atau portofolio interaktif. Untuk produk SaaS perangkat lunak harian, **pertahankan panah bawaan** dan cukup gunakan kursor kustom sebagai "pengikut bayangan" (trailer) saja agar produktivitas tidak terganggu.
3. **Efisiensi Performa**: Terus merender posisi mouse puluhan kali per detik (60fps) bisa membebani browser lambat. Gunakan `useMotionValue` (Framer Motion) atau `transform: translate3d` alih-alih merender ulang *React state* yang memicu *re-render* DOM massal.
