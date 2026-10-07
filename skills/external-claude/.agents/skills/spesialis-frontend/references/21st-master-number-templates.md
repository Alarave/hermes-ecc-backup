# 21st.dev Master Number Animation Templates

Analisis pola dan blueprint komponen Number (Animasi Angka) berdasarkan 37+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Animasi Angka Modern

### Arketipe 1: The Odometer / Sliding Digits (Number Flow)
- **Fungsi**: Digunakan saat nilai angka diperbarui secara dinamis tanpa me-refresh halaman (misalnya perpindahan harga Bulanan ↔ Tahunan, dasbor kripto, atau skor metrik langsung).
- **Karakteristik Visual**:
  - Angka bergerak secara vertikal ke atas atau bawah seperti spidometer/odometer mekanik.
  - Sering kali hanya kolom digit spesifik yang berubah yang ikut meluncur, menciptakan efek transisi yang presisi (*Framer Motion layout transition*).
- **Inspirasi**: `Sliding Number (Julien Thibeaut)`, `Number Flow (Maxwell Barvian)`.

### Arketipe 2: The Count-Up / Number Ticker
- **Fungsi**: Tampilan statistik pencapaian di *landing page* (misal: "1.500+ Pengguna", "99.9% Uptime") yang mulai beranimasi saat digulir masuk ke layar (*scroll-triggered*).
- **Karakteristik Visual**:
  - Angka berjalan mulus dari 0 hingga ke batas target akhir dengan kurva percepatan yang melambat di akhir (*ease-out*).
- **Inspirasi**: `Number Ticker (Dillion Verma)`, `Count Up (unlumen)`.

### Arketipe 3: The Split Flap / Flip Countdown
- **Fungsi**: Tenggat waktu promo diskon (*flash sale*) atau hitung mundur peluncuran produk.
- **Karakteristik Visual**:
  - Angka dipotong secara horizontal di bagian tengah, dan lempeng atas menjatuhkan diri ke bawah seperti jam stasiun kereta klasik (*CSS 3D transform rotateX*).
- **Inspirasi**: `FlipCountdown (Hossain Jahed)`.

### Arketipe 4: The Shuffle / Blur Decrypt
- **Fungsi**: Tampilan bernuansa *cyberpunk*, enkripsi, atau AI di mana data sedang "dianalisis".
- **Karakteristik Visual**:
  - Angka mengacak secara acak melalui karakter-karakter aneh (`#`, `@`, `%`, angka acak) yang berkedip dengan efek *blur* singkat sebelum akhirnya membeku di angka asli.
- **Inspirasi**: `Animated Blur Number (Serafim)`, `Shuffle Number (reuno-ui)`.

---

## 2. Blueprint Kode Master (The Landing Page Count-Up Ticker)

```tsx
import { useEffect, useState } from "react";
import { motion, useAnimation, useInView } from "framer-motion";
import { useRef } from "react";

export function CountUpTicker({
  value = 1000,
  duration = 2, // Durasi detik
  label = "Total Pengguna Aktif",
  suffix = "+",
}: {
  value?: number;
  duration?: number;
  label?: string;
  suffix?: string;
}) {
  const [count, setCount] = useState(0);
  const ref = useRef(null);
  
  // Deteksi ketika komponen masuk ke layar (viewport)
  const isInView = useInView(ref, { once: true, margin: "-50px" });

  useEffect(() => {
    if (isInView) {
      let start = 0;
      // Framerate stabil (asumsi 60fps)
      const totalSteps = duration * 60; 
      const increment = value / totalSteps;
      let currentStep = 0;

      const timer = setInterval(() => {
        currentStep++;
        start += increment;
        
        // Logika Ease-Out kustom sederhana (opsional: bisa pakai framer-motion useSpring)
        if (currentStep >= totalSteps) {
          setCount(value);
          clearInterval(timer);
        } else {
          setCount(Math.ceil(start));
        }
      }, 1000 / 60);

      return () => clearInterval(timer);
    }
  }, [isInView, value, duration]);

  return (
    <div ref={ref} className="flex flex-col items-center justify-center p-6 bg-slate-900 rounded-2xl border border-slate-800 w-fit">
      <div className="flex items-baseline gap-1">
        <motion.span 
          className="text-4xl md:text-5xl font-black font-mono text-transparent bg-clip-text bg-gradient-to-br from-indigo-400 to-purple-500 tracking-tighter"
        >
          {Intl.NumberFormat("id-ID").format(count)}
        </motion.span>
        {suffix && (
          <span className="text-3xl font-bold text-indigo-500">{suffix}</span>
        )}
      </div>
      
      <p className="text-sm font-semibold text-slate-400 mt-2 tracking-wide uppercase">
        {label}
      </p>
    </div>
  );
}
```

---

## 3. Checklist UX Animasi Angka
1. **Lebar Tetap (Tabular Nums)**: Wajib terapkan utilitas Tailwind `tabular-nums` atau CSS `font-variant-numeric: tabular-nums;` pada kontainer font angka (biasanya `font-mono`). Ini mencegah ukuran lebar komponen melompat-lompat (*layout jitter*) ketika angka '1' (yang sempit) berubah menjadi angka '8' (yang lebar) saat efek *ticker* berjalan.
2. **Aksesibilitas (Screen Reader Bypass)**:
   - Efek *count-up* yang berkedip ribuan kali setiap detiknya sangat berbahaya dan membingungkan jika diucapkan oleh pembaca layar.
   - Sembunyikan elemen beranimasi tersebut dengan `aria-hidden="true"`, lalu buat tag tersembunyi `sr-only` yang langsung menuliskan hasil finalnya. 
   - Contoh: `<span className="sr-only">1000 Total Pengguna Aktif</span>`.
3. **Pemicu Jendela (Intersection Observer)**: Jangan pernah menjalankan animasi *Count-Up* saat halaman dimuat jika posisi angkanya ada di dasar (*footer*). Selalu tunggu hingga pengguna menggulir sampai elemen tersebut terlihat (seperti contoh `useInView` di atas).
