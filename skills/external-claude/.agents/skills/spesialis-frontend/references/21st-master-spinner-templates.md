# 21st.dev Master Spinner & Loader Templates

Katalog dan blueprint komponen Loading (Spinner, Skeleton, AI Wait States) berdasarkan tren 480+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Loading State Modern

### Arketipe 1: The AI Generation Loader
- **Fungsi**: Digunakan saat pengguna menunggu respon dari AI (biasanya memakan waktu 5-30 detik).
- **Karakteristik**: Spinner tradisional terasa terlalu lama jika digunakan lebih dari 3 detik. Arketipe ini menggunakan animasi *Morphing Square*, *Siri Wave*, atau teks gradien animasi berurutan (contoh: "Menganalisis data..." → "Menyusun ringkasan...").
- **Inspirasi**: `AI Loading State (Kokonut Baffier)`, `Siri Wave`, `Morphing Loader`.

### Arketipe 2: The Inline Button Spinner
- **Fungsi**: Umpan balik mikro ketika pengguna menekan tombol Submit/Save.
- **Karakteristik**: Sangat kecil (`w-4 h-4`), biasanya berbentuk *Concentric Ring* atau *Bobbing Dots*, menggantikan ikon asli tombol tanpa mengubah lebar tombol secara drastis (mencegah *layout shift*).

### Arketipe 3: The Content Skeleton
- **Fungsi**: Memuat tata letak halaman sebelum data sebenarnya tiba (*Perceived Performance*).
- **Karakteristik**: Bentuk bayangan abu-abu dengan animasi `animate-pulse` atau `shimmer` (sapuan cahaya bergerak) yang secara akurat meniru bentuk paragraf, kartu, atau avatar asli.
- **Inspirasi**: `Skeleton Loader (animbits)`.

### Arketipe 4: The Determinate Progress Bar
- **Fungsi**: Digunakan untuk upload file atau memuat dataset berukuran spesifik.
- **Karakteristik**: Berupa garis horizontal lurus di sisi atas layar (seperti navigasi Next.js/Vercel) atau di dalam *Toast Notification*.

---

## 2. Blueprint Kode Master (React + Tailwind v4)

### A. The AI Generative Loader (Morphing Dots & Text)
Desain tanpa *layout shift* untuk mensimulasikan "AI Thinking State" dengan pergerakan organik (menggunakan Framer Motion).

```tsx
import { useState, useEffect } from "react";
import { motion } from "framer-motion";

const LOADING_MESSAGES = [
  "Menganalisis kueri...",
  "Mengumpulkan data kontekstual...",
  "Menyusun respon...",
  "Menyelaraskan sintaks..."
];

export function AILoadingState() {
  const [msgIndex, setMsgIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setMsgIndex((prev) => (prev + 1) % LOADING_MESSAGES.length);
    }, 2500); // Ganti pesan tiap 2.5 detik untuk mengurangi bosan
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex flex-col items-center justify-center gap-4 py-8">
      {/* Morphing Dots / Siri Wave Simulation */}
      <div className="flex items-center gap-2 h-8">
        {[0, 1, 2].map((i) => (
          <motion.div
            key={i}
            animate={{
              scale: [1, 1.5, 1],
              opacity: [0.3, 1, 0.3],
            }}
            transition={{
              duration: 1,
              repeat: Infinity,
              delay: i * 0.2, // Efek bergelombang
              ease: "easeInOut"
            }}
            className="w-2.5 h-2.5 rounded-full bg-indigo-500"
          />
        ))}
      </div>
      
      {/* Dynamic Text Update */}
      <motion.p 
        key={msgIndex}
        initial={{ opacity: 0, y: 5 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -5 }}
        transition={{ duration: 0.3 }}
        className="text-sm font-medium bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent"
      >
        {LOADING_MESSAGES[msgIndex]}
      </motion.p>
    </div>
  );
}
```

### B. The Inline Button Spinner (SVG Murni, Tanpa Dependensi)
Spinner ikonik untuk disematkan di dalam tombol saat proses penyimpanan.

```tsx
export function ButtonSpinner({ className = "w-4 h-4" }: { className?: string }) {
  return (
    <svg 
      className={`animate-spin text-current ${className}`} 
      xmlns="http://www.w3.org/2000/svg" 
      fill="none" 
      viewBox="0 0 24 24"
    >
      <circle 
        className="opacity-25" 
        cx="12" 
        cy="12" 
        r="10" 
        stroke="currentColor" 
        strokeWidth="4" 
      />
      <path 
        className="opacity-75" 
        fill="currentColor" 
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" 
      />
    </svg>
  );
}

/* Contoh Penggunaan dalam Tombol */
// <button disabled className="...">
//   <ButtonSpinner className="w-4 h-4 mr-2" />
//   Menyimpan...
// </button>
```

### C. The Shimmer Skeleton Loader
Menggunakan CSS murni (Tailwind v4) untuk menghasilkan *shimmer effect* yang mulus. Sangat baik sebagai pengganti area gambar dan paragraf.

Tambahkan di `tailwind.config.ts`:
```js
// Tambahan theme.extend
animation: {
  shimmer: "shimmer 2s infinite linear",
},
keyframes: {
  shimmer: {
    "0%": { backgroundPosition: "200% 0" },
    "100%": { backgroundPosition: "-200% 0" },
  }
}
```

Implementasi Komponen:
```tsx
export function CardSkeleton() {
  return (
    <div className="w-full rounded-2xl border border-slate-800 bg-slate-900/50 p-6 flex flex-col gap-4">
      {/* Title Skeleton */}
      <div className="w-1/3 h-6 rounded-md bg-gradient-to-r from-slate-800 via-slate-700 to-slate-800 bg-[length:200%_100%] animate-shimmer" />
      
      {/* Paragraph Lines */}
      <div className="space-y-2 mt-2">
        <div className="w-full h-3 rounded-sm bg-gradient-to-r from-slate-800 via-slate-700 to-slate-800 bg-[length:200%_100%] animate-shimmer" />
        <div className="w-5/6 h-3 rounded-sm bg-gradient-to-r from-slate-800 via-slate-700 to-slate-800 bg-[length:200%_100%] animate-shimmer" />
        <div className="w-4/6 h-3 rounded-sm bg-gradient-to-r from-slate-800 via-slate-700 to-slate-800 bg-[length:200%_100%] animate-shimmer" />
      </div>

      {/* Button Skeleton */}
      <div className="w-24 h-8 mt-4 rounded-lg bg-gradient-to-r from-slate-800 via-slate-700 to-slate-800 bg-[length:200%_100%] animate-shimmer" />
    </div>
  );
}
```

---

## 3. Checklist UX untuk Status Pemuatan (Loading States)
1. **Jangan Beri Spinner Jika Di Bawah 300ms**: Untuk tindakan instan (navigasi lokal yang di-*cache*), menampilkan spinner yang hanya berkedip 100ms justru membebani mata (disebut *loading flash*).
2. **AI Wajib Progresif**: Karena AI memakan waktu lama, ubah teks indikator tiap beberapa detik agar pengguna tahu proses tidak *hang/freeze*.
3. **Nonaktifkan Tombol (Disable)**: Saat *Button Spinner* aktif, selalu set `disabled={true}` pada tombol untuk mencegah *double-submit* dari klik beruntun pengguna.
