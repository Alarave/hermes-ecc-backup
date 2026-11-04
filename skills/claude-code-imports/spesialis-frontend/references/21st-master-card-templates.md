# 21st.dev Master Card & Container Templates

Analisis pola dan blueprint komponen Card (Kartu Kontainer) berdasarkan 1.780+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Card Modern

### Arketipe 1: The Liquid Glass / Glassmorphism Card
- **Fungsi**: Wadah elemen bergaya futuristik yang banyak digunakan pada aplikasi AI, *Dashboard* analitik, dan latar belakang kompleks.
- **Karakteristik Visual**:
  - Efek buram latar belakang (*Backdrop Blur* `backdrop-blur-xl`).
  - Latar belakang semi-transparan (`bg-slate-900/40` atau putih transparan 10%).
  - Garis batas gradien tipis (biasanya menggunakan inset shadow atau border semi transparan `border border-white/10`).
- **Inspirasi**: `Liquid Glass Card`, `Glass Card`.

### Arketipe 2: The 3D Hover Tilt Card
- **Fungsi**: Memamerkan aset premium, kartu harga (*Pricing Card*), atau produk toko online.
- **Karakteristik Visual**:
  - Saat kursor mouse bergerak melintasi kartu, sudut kartu akan sedikit miring (*tilt*) mengikuti posisi mouse (memanfaatkan matematika rotasi X dan Y).
  - Terdapat kilatan cahaya (*glare*) melayang di atas permukaan kartu.
- **Inspirasi**: `BeUI Tilt Card (Saurabh)`, `3D tilt card (Awanish Verma)`.

### Arketipe 3: The Pattern / Noise Textured Card
- **Fungsi**: Kartu fitur atau blog yang ingin menghindari ruang kosong yang membosankan (*flat UI*).
- **Karakteristik Visual**:
  - Dilapisi dengan latar belakang SVG statis berupa bintik-bintik derau (*Noise Pattern*) atau grid titik putus-putus samar (`Card with Noise Pattern`, `Grid Ellipsis Pattern`).
- **Inspirasi**: `Card with Grid Ellipsis Pattern`, `Gradient Bold Card (Ruixen)`.

### Arketipe 4: The Interactive Data/Metric Card
- **Fungsi**: Kotak KPI pada baris paling atas dashboard.
- **Karakteristik Visual**:
  - Struktur kaku: Ikon di sudut kanan atas, angka besar tebal di tengah, dan grafik *sparkline* kecil atau teks tren (*+14%*) di bawah.
- **Inspirasi**: `Progress Metric Card`, `Stats cards with links`.

---

## 2. Blueprint Kode Master

### A. The Liquid Glass Card (SaaS/AI Style)
```tsx
import { Sparkles, ArrowRight } from "lucide-react";

export function LiquidGlassCard() {
  return (
    <div className="relative group w-full max-w-sm overflow-hidden rounded-3xl p-[1px]">
      
      {/* Animated Gradient Border (Glow effect behind the card) */}
      <span className="absolute inset-0 bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 opacity-50 group-hover:opacity-100 transition-opacity duration-500 blur-sm" />
      
      {/* Main Glass Surface */}
      <div className="relative h-full w-full rounded-[23px] bg-slate-950/60 backdrop-blur-2xl px-6 py-8 flex flex-col justify-between">
        
        {/* Subtle noise overlay (Optional, but adds texture) */}
        <div className="absolute inset-0 opacity-[0.03] bg-[url('https://grainy-gradients.vercel.app/noise.svg')]" />
        
        <div className="relative z-10">
          <div className="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 mb-6 shadow-[0_0_15px_rgba(99,102,241,0.2)]">
            <Sparkles className="w-6 h-6" />
          </div>
          
          <h3 className="text-xl font-bold text-white mb-2 tracking-tight">Kecerdasan Agen</h3>
          <p className="text-sm text-slate-400 leading-relaxed mb-8">
            Diberdayakan oleh pemodelan bahasa deterministik yang dioptimalkan untuk keputusan berpresisi tinggi.
          </p>
        </div>

        {/* Action Link */}
        <div className="relative z-10 flex items-center gap-2 text-sm font-semibold text-indigo-400 group-hover:text-indigo-300 transition-colors cursor-pointer w-fit">
          <span>Pelajari arsitekturnya</span>
          <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
        </div>
      </div>
    </div>
  );
}
```

### B. The 3D Kinetic Tilt Card
```tsx
import { useRef, useState } from "react";
import { motion } from "framer-motion";

export function ThreeDTiltCard() {
  const cardRef = useRef<HTMLDivElement>(null);
  
  // State rotasi X dan Y
  const [rotateX, setRotateX] = useState(0);
  const [rotateY, setRotateY] = useState(0);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!cardRef.current) return;

    const rect = cardRef.current.getBoundingClientRect();
    const width = rect.width;
    const height = rect.height;
    
    // Posisi mouse relatif terhadap kartu
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    // Kalkulasi rotasi (Max tilt: 10 derajat)
    const rotateYValue = ((mouseX - width / 2) / (width / 2)) * 10;
    const rotateXValue = ((mouseY - height / 2) / (height / 2)) * -10;

    setRotateX(rotateXValue);
    setRotateY(rotateYValue);
  };

  const handleMouseLeave = () => {
    // Reset posisi kartu ke datar saat mouse pergi
    setRotateX(0);
    setRotateY(0);
  };

  return (
    <div className="perspective-[1000px] w-full max-w-xs cursor-pointer">
      <motion.div
        ref={cardRef}
        onMouseMove={handleMouseMove}
        onMouseLeave={handleMouseLeave}
        animate={{
          rotateX,
          rotateY,
          transformPerspective: 1000,
        }}
        transition={{ type: "spring", stiffness: 400, damping: 30, mass: 0.5 }}
        className="w-full rounded-3xl border border-slate-800 bg-slate-900 p-8 shadow-2xl overflow-hidden"
      >
        <h3 className="text-2xl font-black text-white mb-2">Paket Pro</h3>
        <p className="text-3xl font-bold text-indigo-400 mb-6">Rp 150.000<span className="text-sm text-slate-500 font-medium">/bln</span></p>
        
        <ul className="space-y-3 text-sm text-slate-400">
          <li className="flex items-center gap-2">✔ Tanpa batas transaksi</li>
          <li className="flex items-center gap-2">✔ Dukungan prioritas 24/7</li>
          <li className="flex items-center gap-2">✔ Analitik tingkat lanjut</li>
        </ul>

        <button className="mt-8 w-full py-3 rounded-xl bg-indigo-600 text-white font-bold hover:bg-indigo-500 transition-colors pointer-events-none">
          Mulai Uji Coba
        </button>
      </motion.div>
    </div>
  );
}
```

---

## 3. Checklist Desain Kontainer Kartu
1. **Aturan Sudut Melengkung (Nested Border Radius)**: Jika *padding* kartu adalah `1rem` (16px) dan Anda memasukkan kotak/gambar bundar di dalamnya, radius bingkai luar kartu harus **lebih besar** daripada radius elemen di dalamnya (`Border Radius Luar = Border Radius Dalam + Padding`). Jika kartu memiliki `rounded-3xl` (24px) dengan padding 16px, maka gambar di dalamnya harus `rounded-lg` (8px). Ini agar lengkungan seirama secara geometris.
2. **Hitbox (Aksesibilitas Sentuhan)**: Seperti dibahas di tautan, pastikan Anda menggunakan *pseudo-element stretch link* (`after:absolute after:inset-0`) jika ingin menyulap kartu informasional utuh menjadi tautan web interaktif.
