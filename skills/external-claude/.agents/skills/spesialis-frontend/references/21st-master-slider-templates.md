# 21st.dev Master Slider Templates

Analisis pola dan blueprint komponen Slider (Range, Carousel, dan Comparison) berdasarkan 217+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion / Radix UI).

---

## 1. Empat Arketipe Slider Modern

### Arketipe 1: The Liquid Range Slider (Volume / Input Value)
- **Fungsi**: Memilih nilai numerik di sepanjang lintasan berkesinambungan (volume audio, ukuran brush, tingkat filter).
- **Karakteristik**:
  - Terdapat efek melar (*stretch* atau *liquid morphing*) pada *thumb* (tombol geser) ketika ditarik terlalu cepat.
  - Sering kali *thumb* menampakkan nilai angkanya (misal: "75%") melayang di atasnya saat di-*drag* (Tooltip terintegrasi).

### Arketipe 2: The Before/After Image Comparison Slider
- **Fungsi**: Membandingkan dua gambar secara langsung (misal: foto sebelum/sesudah edit, desain arsitektur vs render).
- **Karakteristik**:
  - Ada garis pemisah vertikal di tengah gambar dengan *handle* (pegangan) ikon panah kiri-kanan.
  - Gambar lapis atas di-clip (dipotong) menggunakan properti CSS `clip-path` atau `width` absolut sesuai posisi pegangan.

### Arketipe 3: The Carousel / Progressive Slide (Media)
- **Fungsi**: Menampilkan daftar gambar, kartu produk, atau testimoni berjejer horizontal.
- **Karakteristik**:
  - Interaksi *swipe* atau klik panah untuk bergeser.
  - Biasanya dilengkapi dengan navigasi titik (*dots*) atau progress bar di bawahnya.
  - Pola modern menggunakan snap-scroll CSS murni (`scroll-snap-type: x mandatory`) untuk performa maksimal.

### Arketipe 4: The 3D Coverflow Slider
- **Fungsi**: Galeri visual dramatis (portfolio, showcase cover album/film).
- **Karakteristik**: Elemen di tengah membesar dan mendapat fokus penuh, sedangkan elemen di pinggir mengecil, blur, dan merenggang ke belakang (efek z-index & rotate Y).

---

## 2. Standar Aksesibilitas Slider (WAI-ARIA)
Range slider sangat rentan bermasalah pada navigasi keyboard.
1. **Atribut ARIA**: Gunakan `role="slider"`, `aria-valuemin`, `aria-valuemax`, dan `aria-valuenow` pada elemen *thumb*.
2. **Keyboard Handling**: Tombol panah kiri/kanan (`ArrowLeft`, `ArrowRight`) wajib bisa menggeser nilai slider (umumnya dengan step = 1), sementara `PageUp`/`PageDown` melompat lebih cepat (step = 10).
3. **Visibilitas Fokus**: Outline harus jelas terlihat pada *thumb* saat tab fokus agar pengguna keyboard tahu bahwa mereka sedang mengontrol slider.

---

## 3. Blueprint Kode Master (The Minimalist Range Slider)

Blueprint ini menyimulasikan *Range Slider* yang mulus menggunakan `<input type="range">` asli HTML agar mendapat fitur aksesibilitas bawaan browser secara gratis, dengan styling kustom penuh lewat Tailwind v4.

```tsx
import { useState } from "react";
import { Volume2, VolumeX } from "lucide-react";

export function MinimalRangeSlider({ min = 0, max = 100, defaultValue = 50 }) {
  const [value, setValue] = useState(defaultValue);
  
  // Persentase untuk menghitung lebar bar aktif (fill)
  const percentage = ((value - min) / (max - min)) * 100;

  return (
    <div className="flex items-center gap-4 w-full max-w-sm p-4 rounded-2xl bg-slate-900 border border-slate-800">
      
      {/* Mute Toggle Icon */}
      <button 
        onClick={() => setValue(value === 0 ? defaultValue : 0)}
        className="text-slate-400 hover:text-slate-200 transition-colors focus:outline-none"
        aria-label={value === 0 ? "Unmute" : "Mute"}
      >
        {value === 0 ? <VolumeX className="w-5 h-5" /> : <Volume2 className="w-5 h-5" />}
      </button>

      {/* Slider Track & Thumb */}
      <div className="relative flex-1 h-2 bg-slate-800 rounded-full flex items-center">
        
        {/* Active Fill Bar */}
        <div 
          className="absolute left-0 h-full bg-indigo-500 rounded-full pointer-events-none transition-all duration-75"
          style={{ width: `${percentage}%` }}
        />

        {/* Native Input Slider (Aksesibilitas Sempurna) */}
        <input
          type="range"
          min={min}
          max={max}
          value={value}
          onChange={(e) => setValue(Number(e.target.value))}
          className="absolute inset-0 w-full h-full opacity-0 cursor-pointer focus:outline-none z-10"
          aria-label="Volume control"
        />

        {/* Custom Visual Thumb */}
        <div 
          className="absolute w-4 h-4 bg-white rounded-full shadow-md pointer-events-none transition-transform duration-75 border-2 border-indigo-500 z-0 group-focus-within:ring-2 group-focus-within:ring-indigo-500/50"
          style={{ 
            left: `calc(${percentage}% - 8px)`, // Offset sebesar radius thumb (8px)
          }}
        />
      </div>

      {/* Value Readout */}
      <span className="w-8 text-right text-xs font-mono font-medium text-slate-300 select-none">
        {value}%
      </span>
    </div>
  );
}
```

### Tips Implementasi Custom Slider:
- Menggunakan input native HTML (`<input type="range" className="opacity-0">`) yang ditumpuk di atas track khusus adalah **hacks aksesibilitas terbaik**. Ini menjamin navigasi panah keyboard, dukungan screen reader, dan interaksi sentuh *mobile* berjalan sempurna tanpa harus menulis perhitungan kalkulasi mouse (drag/touch X-coordinates) dari nol.
- Efek *Active Fill Bar* dan *Custom Visual Thumb* hanyalah lapisan dekoratif (`pointer-events-none`) yang bergerak menyesuaikan persentase nilai input tersebut.
