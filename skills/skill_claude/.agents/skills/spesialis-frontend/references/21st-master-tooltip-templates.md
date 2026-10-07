# 21st.dev Master Tooltip Templates & Architecture

Analisis pola dan blueprint komponen Tooltip berdasarkan tren UI modern di 21st.dev (React + Tailwind v4 + Framer Motion / Floating UI / Radix UI).

---

## 1. Empat Arketipe Tooltip Modern

### Arketipe 1: The Micro-Shortcut Tooltip (SaaS / Developer Tools)
- **Fungsi**: Memberikan panduan cepat untuk aksi atau keyboard shortcut.
- **Anatomi**: Teks label sederhana dipadukan dengan chip tombol shortcut (misal: `<kbd>⌘</kbd> <kbd>K</kbd>`).
- **Desain**: Kotak kecil gelap (`bg-slate-900`), teks putih kontras, border tipis, dan *arrow* kecil mengarah ke elemen trigger.

### Arketipe 2: The Rich Content / Profile Tooltip (Social / E-Commerce)
- **Fungsi**: Menampilkan ringkasan informasi kompleks (Mini-Card) saat kursor diarahkan ke nama pengguna atau produk.
- **Anatomi**: Memuat Avatar, nama tebal, bio singkat, status online, atau gambar mini produk.
- **Desain**: Lebih besar dari tooltip biasa. Sering menggunakan efek glassmorphism (`backdrop-blur-md`, `bg-slate-900/80`).

### Arketipe 3: The Cursor-Following / Magnetic Tooltip (Creative / Portfolio)
- **Fungsi**: Memberi keterangan dinamis pada gallery gambar atau area kanvas.
- **Anatomi**: Kotak keterangan kecil yang terus menempel dan bergerak mengikuti koordinat kursor mouse `(x, y)` selama berada di area target.
- **Desain**: Animasi *spring physics* (Framer Motion) agar pergerakannya organik dan mulus tanpa jitter.

### Arketipe 4: The Glow / Neon Tooltip (Web3 / Gaming / AI)
- **Fungsi**: Menonjolkan fitur premium atau elemen baru (feature discovery).
- **Anatomi**: Kotak tooltip standar dengan tambahan *drop-shadow* neon atau border bercahaya.

---

## 2. Standar Aksesibilitas (WCAG & ARIA)
Tooltip sering kali menjadi fitur yang paling sulit diakses jika tidak dibangun dengan benar.
1. **Trigger Berbasis Keyboard**: Tooltip wajib muncul saat elemen trigger di-hover (`onMouseEnter`) ATAU saat mendapatkan fokus keyboard (`onFocus`).
2. **Atribut ARIA**: Elemen trigger harus memiliki `aria-describedby="tooltip-id"` jika tooltip hanya berisi info tambahan.
3. **Escape to Close**: Pengguna harus bisa menutup tooltip dengan menekan tombol `Escape` tanpa kehilangan fokus kursor.
4. **Smart Positioning**: Gunakan *Radix UI Tooltip* atau *Floating UI* agar tooltip tidak terpotong (clipping) keluar layar saat dibuka di sudut layar mobile.

---

## 3. Blueprint Kode Master (The Micro-Shortcut Tooltip)
Berikut template Tooltip interaktif berbasis *Framer Motion* murni tanpa dependensi eksternal berat, cocok untuk UI/UX berstandar tinggi.

```tsx
import React, { useState, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";

interface TooltipProps {
  children: React.ReactNode;
  content: string;
  shortcut?: string[]; // e.g., ["⌘", "K"]
  position?: "top" | "bottom" | "left" | "right";
}

export function ModernTooltip({ children, content, shortcut, position = "top" }: TooltipProps) {
  const [isVisible, setIsVisible] = useState(false);
  const timeoutRef = useRef<NodeJS.Timeout | null>(null);

  const showTooltip = () => {
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
    setIsVisible(true);
  };

  const hideTooltip = () => {
    timeoutRef.current = setTimeout(() => {
      setIsVisible(false);
    }, 150); // Delay kecil agar tooltip tidak berkedip jika kursor lewat cepat
  };

  // Konfigurasi posisi animasi
  const getInitialPosition = () => {
    switch (position) {
      case "top": return { y: 8, x: "-50%", opacity: 0, scale: 0.95 };
      case "bottom": return { y: -8, x: "-50%", opacity: 0, scale: 0.95 };
      case "left": return { x: 8, y: "-50%", opacity: 0, scale: 0.95 };
      case "right": return { x: -8, y: "-50%", opacity: 0, scale: 0.95 };
    }
  };

  const getAnimatePosition = () => {
    switch (position) {
      case "top": return { y: 0, x: "-50%", opacity: 1, scale: 1 };
      case "bottom": return { y: 0, x: "-50%", opacity: 1, scale: 1 };
      case "left": return { x: 0, y: "-50%", opacity: 1, scale: 1 };
      case "right": return { x: 0, y: "-50%", opacity: 1, scale: 1 };
    }
  };

  const getAbsoluteClasses = () => {
    switch (position) {
      case "top": return "bottom-full left-1/2 mb-2";
      case "bottom": return "top-full left-1/2 mt-2";
      case "left": return "right-full top-1/2 mr-2";
      case "right": return "left-full top-1/2 ml-2";
    }
  };

  return (
    <div 
      className="relative inline-flex"
      onMouseEnter={showTooltip}
      onMouseLeave={hideTooltip}
      onFocus={showTooltip}
      onBlur={hideTooltip}
    >
      {/* Target Element */}
      {children}

      {/* Tooltip Content */}
      <AnimatePresence>
        {isVisible && (
          <motion.div
            initial={getInitialPosition()}
            animate={getAnimatePosition()}
            exit={getInitialPosition()}
            transition={{ type: "spring", stiffness: 300, damping: 20 }}
            className={`absolute z-50 pointer-events-none whitespace-nowrap ${getAbsoluteClasses()}`}
            role="tooltip"
          >
            <div className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-slate-700/80 bg-slate-900 shadow-xl">
              <span className="text-xs font-medium text-slate-200">{content}</span>
              
              {shortcut && (
                <div className="flex items-center gap-1 ml-2">
                  {shortcut.map((key, i) => (
                    <kbd 
                      key={i} 
                      className="inline-flex items-center justify-center min-w-[20px] h-5 px-1 rounded-sm bg-slate-800 border border-slate-700 text-[10px] font-mono text-slate-400 font-semibold"
                    >
                      {key}
                    </kbd>
                  ))}
                </div>
              )}
              
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
```

### Cara Penggunaan di Komponen:
```tsx
<ModernTooltip content="Cari Dokumen" shortcut={["⌘", "K"]} position="top">
  <button className="p-2 rounded-md bg-slate-800 text-slate-300 hover:text-white focus:ring-2 ring-indigo-500">
    <SearchIcon className="w-5 h-5" />
  </button>
</ModernTooltip>
```
