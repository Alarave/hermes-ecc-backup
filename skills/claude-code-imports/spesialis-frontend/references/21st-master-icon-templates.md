# 21st.dev Master Icon Interaction Templates

Analisis pola dan blueprint komponen Icon (Ikon Interaktif & Morphing) berdasarkan 851+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion / Lucide Icons).

---

## 1. Empat Arketipe Ikon Modern

### Arketipe 1: The Morphing State Icon (Copy → Checkmark)
- **Fungsi**: Umpan balik visual langsung saat pengguna menekan tombol salin (Copy ID, Salin API Key, Share Link).
- **Karakteristik Visual**:
  - Ikon dua lembar kertas (`Copy`) memudar dan mengecil (*scale-down*), lalu digantikan oleh ikon centang hijau (`Check`) yang memantul masuk (*spring pop*) selama 2 detik sebelum kembali ke wujud semula.
- **Inspirasi**: GitHub Code Blocks, Raycast Copy Action.

### Arketipe 2: The Glassmorphic Illuminated Icon Badge
- **Fungsi**: Ikon fitur pada kartu Bento Grid di *Landing Page* atau seksi *Features*.
- **Karakteristik Visual**:
  - Ikon diletakkan di dalam kontainer kotak membulat (*squircle* `rounded-2xl`).
  - Latar belakang semi-transparan dengan pendaran cahaya neon halus di belakangnya (`shadow-lg shadow-indigo-500/20 border border-indigo-500/30 bg-gradient-to-br from-indigo-500/10 to-transparent`).
- **Inspirasi**: Linear & Apple Features Grid.

### Arketipe 3: The Animated Hamburger to Close (Mobile Nav Toggle)
- **Fungsi**: Tombol pemicu menu navigasi di tampilan ponsel (*Mobile Drawer*).
- **Karakteristik Visual**:
  - Tiga garis horizontal SVG yang berputar dan melipat silang menjadi huruf 'X' saat diklik secara mulus tanpa pergantian aset gambar (*pure SVG line morphing*).

### Arketipe 4: The Micro-Interaction Burst (Heart / Like Button)
- **Fungsi**: Aksi simpan favorit (*Bookmark*) atau *Like*.
- **Karakteristik Visual**:
  - Saat ditekan, ikon membesar sejenak (scale: 1.3) disertai letupan partikel kecil di sekelilingnya (*confetti spark burst*), lalu warna garis outline berubah menjadi warna merah muda padat (*solid fill*).

---

## 2. Blueprint Kode Master

### A. The Copy-to-Check Animated Icon Button
```tsx
import { useState } from "react";
import { Copy, Check } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export function CopyActionButton({ textToCopy = "API_KEY_12345678" }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(textToCopy);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error("Gagal menyalin", err);
    }
  };

  return (
    <button
      onClick={handleCopy}
      aria-label={copied ? "Tersalin ke papan klip" : "Salin ke papan klip"}
      className="relative flex items-center gap-2 px-3 py-1.5 rounded-xl border border-slate-800 bg-slate-900/80 hover:bg-slate-800 text-slate-300 hover:text-white transition-colors"
    >
      <div className="relative w-4 h-4 flex items-center justify-center">
        <AnimatePresence mode="wait" initial={false}>
          {copied ? (
            <motion.div
              key="check"
              initial={{ scale: 0, rotate: -45 }}
              animate={{ scale: 1, rotate: 0 }}
              exit={{ scale: 0, opacity: 0 }}
              transition={{ type: "spring", stiffness: 500, damping: 25 }}
            >
              <Check className="w-4 h-4 text-emerald-400" />
            </motion.div>
          ) : (
            <motion.div
              key="copy"
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.8, opacity: 0 }}
              transition={{ duration: 0.15 }}
            >
              <Copy className="w-4 h-4 text-slate-400" />
            </motion.div>
          )}
        </AnimatePresence>
      </div>
      
      <span className="text-xs font-mono font-medium">
        {copied ? "Tersalin!" : "Salin"}
      </span>
    </button>
  );
}
```

### B. The Illuminated Feature Icon Tile (Bento Style)
```tsx
import { LucideIcon } from "lucide-react";

export function IlluminatedIconTile({ 
  icon: Icon, 
  color = "indigo" 
}: { 
  icon: LucideIcon; 
  color?: "indigo" | "emerald" | "amber" | "rose" 
}) {
  const colorMap = {
    indigo: "border-indigo-500/20 bg-indigo-500/10 text-indigo-400 shadow-indigo-500/10 group-hover:border-indigo-500/40",
    emerald: "border-emerald-500/20 bg-emerald-500/10 text-emerald-400 shadow-emerald-500/10 group-hover:border-emerald-500/40",
    amber: "border-amber-500/20 bg-amber-500/10 text-amber-400 shadow-amber-500/10 group-hover:border-amber-500/40",
    rose: "border-rose-500/20 bg-rose-500/10 text-rose-400 shadow-rose-500/10 group-hover:border-rose-500/40",
  };

  return (
    <div className="group relative inline-block">
      {/* Soft Glow Ambient Layer */}
      <div className="absolute -inset-1 rounded-2xl bg-gradient-to-r from-indigo-500 to-purple-500 opacity-0 group-hover:opacity-25 blur-lg transition-opacity duration-500" />
      
      {/* Icon Squircle Box */}
      <div className={`relative flex items-center justify-center w-12 h-12 rounded-2xl border backdrop-blur-xl shadow-lg transition-all duration-300 group-hover:scale-105 ${colorMap[color]}`}>
        <Icon className="w-6 h-6 transition-transform duration-300 group-hover:rotate-3" />
      </div>
    </div>
  );
}
```

---

## 3. Standar Aksesibilitas Ikon (WAI-ARIA)
1. **Ikon Murni Dekoratif**: Jika ikon diletakkan mendampingi teks (contoh tombol yang memiliki teks `"Salin"`), sematkan atribut `aria-hidden="true"` pada tag ikon agar pembaca layar tidak mengucapkannya dua kali.
2. **Ikon Tanpa Teks (Icon-Only Button)**: Jika tombol hanya berupa gambar ikon (seperti tombol silang 'X' atau tombol pencarian kaca pembesar), tombol pembungkusnya **wajib** memiliki atribut `aria-label="Tutup jendela"` atau `aria-label="Cari"`.
