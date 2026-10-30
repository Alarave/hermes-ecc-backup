# 21st.dev Master Progress & Stepper Templates

Analisis pola dan blueprint komponen Progress Bar, Radial Progress, dan Stepper berdasarkan 375+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion / SVG).

---

## 1. Empat Arketipe Progress Modern

### Arketipe 1: The Smooth Linear Bar with Shimmer (Uploads & Quotas)
- **Fungsi**: Pelacak unggahan file (*File Upload*), batas pemakaian kuota storage/API, atau skor kelengkapan profil.
- **Karakteristik Visual**:
  - Garis horizontal dengan radius membulat penuh (`rounded-full`).
  - Bar bagian dalam terisi (*fill*) memanjang secara mulus dengan transisi CSS `transition-all duration-500`.
  - Dilengkapi efek *shimmer / gradient streak* yang berjalan di atas bar aktif.
- **Inspirasi**: `Storage Usage Progress`, `UploadThing Progress (Cameron Kelliher)`.

### Arketipe 2: The Circular / Radial Gauge Progress
- **Fungsi**: Visualisasi statistik ringkas (skor kesehatan sistem, performa Lighthouse, persentase baterai).
- **Karakteristik Visual**:
  - Lingkaran cincin berbasis SVG (`stroke-dasharray` dan `stroke-dashoffset`).
  - Angka persentase besar di titik pusat lingkaran (`text-xl font-bold font-mono`).
- **Inspirasi**: `Animated Circular Progress Bar`, `Circle Progress (Ali Imam)`.

### Arketipe 3: The Scroll Reading Indicator
- **Fungsi**: Indikator artikel/dokumentasi panjang yang diletakkan di puncak paling atas layar (`fixed top-0 left-0 right-0 z-50`).
- **Karakteristik Visual**:
  - Garis tipis setinggi 2px-3px berwarna terang yang memanjang dari kiri ke kanan mengikuti posisi scroll halaman pengguna (`scrollYProgress` dari Framer Motion).
- **Inspirasi**: `Scroll Progress (Ali Imam)`, `Reading Progress`.

### Arketipe 4: The Onboarding Stepper / Timeline Rail
- **Fungsi**: Menampilkan tahapan form multi-step (Step 1 → Step 2 → Step 3).
- **Karakteristik Visual**:
  - Deretan lingkaran bernomor urut yang dihubungkan oleh garis penghubung.
  - Lingkaran yang sudah selesai (*completed*) berubah menjadi ikon centang hijau, langkah aktif (*active*) berpendar, dan langkah mendatang (*upcoming*) abu-abu redup.
- **Inspirasi**: `Onboarding Stepper Progress`, `Multi-step Wizard`.

---

## 2. Blueprint Kode Master

### A. Linear Storage Quota Progress Bar
```tsx
interface ProgressBarProps {
  value: number; // 0 sampai 100
  label?: string;
  subtext?: string;
}

export function LinearProgressBar({ value, label = "Penggunaan Kuota", subtext = "7.5 GB dari 10 GB" }: ProgressBarProps) {
  const clampedValue = Math.min(Math.max(value, 0), 100);

  return (
    <div className="w-full max-w-md p-4 rounded-2xl border border-slate-800 bg-slate-900/60">
      <div className="flex items-center justify-between text-xs font-medium mb-2">
        <span className="text-slate-200">{label}</span>
        <span className="font-mono text-indigo-400 font-semibold">{clampedValue}%</span>
      </div>

      {/* Progress Track */}
      <div 
        role="progressbar" 
        aria-valuenow={clampedValue} 
        aria-valuemin={0} 
        aria-valuemax={100}
        className="relative h-2 w-full bg-slate-800 rounded-full overflow-hidden"
      >
        <div 
          className="h-full bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full transition-all duration-500 ease-out"
          style={{ width: `${clampedValue}%` }}
        />
      </div>

      <p className="text-[11px] text-slate-500 mt-2 font-mono">{subtext}</p>
    </div>
  );
}
```

### B. Animated Circular Progress (SVG Native)
```tsx
export function CircularProgress({ percentage = 75, size = 120, strokeWidth = 10 }) {
  const radius = (size - strokeWidth) / 2;
  const circumference = radius * 2 * Math.PI;
  const offset = circumference - (percentage / 100) * circumference;

  return (
    <div className="relative inline-flex items-center justify-center">
      <svg width={size} height={size} className="transform -rotate-90">
        {/* Background Circle */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke="currentColor"
          strokeWidth={strokeWidth}
          className="text-slate-800"
          fill="transparent"
        />
        {/* Animated Progress Circle */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke="currentColor"
          strokeWidth={strokeWidth}
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          strokeLinecap="round"
          className="text-indigo-500 transition-all duration-700 ease-out"
          fill="transparent"
        />
      </svg>
      {/* Centered Readout */}
      <div className="absolute flex flex-col items-center">
        <span className="text-xl font-bold font-mono text-slate-100">{percentage}%</span>
        <span className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">Skor</span>
      </div>
    </div>
  );
}
```

### C. Top-Screen Reading Progress Bar (Framer Motion)
```tsx
import { motion, useScroll } from "framer-motion";

export function ReadingProgressBar() {
  const { scrollYProgress } = useScroll();

  return (
    <motion.div
      style={{ scaleX: scrollYProgress }}
      className="fixed top-0 left-0 right-0 h-1 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 origin-left z-50"
    />
  );
}
```

---

## 3. Checklist Aksesibilitas (WAI-ARIA)
1. **Atribut Wajib**: Elemen bar wajib menyertakan `role="progressbar"`, `aria-valuenow`, `aria-valuemin="0"`, dan `aria-valuemax="100"`.
2. **Indeterminate State**: Jika persentase tidak diketahui (misal proses persiapan file yang tidak pasti), hilangkan atribut `aria-valuenow` dan pasang animasi berputar/berdenyut berulang (*indeterminate animation*).
3. **Pemberitahuan Screen Reader**: Jika bar mengalami perubahan dinamis signifikan, letakkan teks keterbacaan (*sr-only*) agar pembaca layar mengumumkan progres secara berkala.
