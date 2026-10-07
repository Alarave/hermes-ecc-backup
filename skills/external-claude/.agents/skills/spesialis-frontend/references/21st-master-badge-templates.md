# 21st.dev Master Badge & Status Pill Templates

Analisis pola dan blueprint komponen Badge (Lencana / Pil Indikator) berdasarkan 605+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Lima Arketipe Badge Modern

### Arketipe 1: The Status Indicator Badge
- **Fungsi**: Menunjukkan status aktif/berhasil/gagal pada tabel analitik atau profil pengguna.
- **Karakteristik Visual**:
  - Warna semantik halus: Sukses (Background Emerald-500/10, Teks Emerald-400), Pending (Amber), Error (Rose).
  - Terdapat titik bulat kecil di sisi kiri teks (`w-1.5 h-1.5 rounded-full`) yang sewarna dengan teks badge.
- **Inspirasi**: `Status Badge (Arihant jain)`.

### Arketipe 2: The Outline Tag / Filter Chip
- **Fungsi**: Label kategori produk, tag artikel blog, atau filter pencarian.
- **Karakteristik Visual**:
  - Background transparan, hanya mengandalkan garis pembatas tipis (`border border-slate-700`).
  - Sering kali *clickable* dan memuat ikon silang 'X' kecil di ujung kanan untuk membatalkan filter.
- **Inspirasi**: `Badge Tag`, `Filter Badge (Serafim)`.

### Arketipe 3: The Delta / Trend Badge
- **Fungsi**: Angka tren naik/turun pada *Metric Card* di Dashboard Analitik (misal: "+12.5%").
- **Karakteristik Visual**:
  - Teks menggunakan font-mono yang presisi (`tabular-nums`).
  - Memuat ikon panah (`ArrowUpRight` atau `ArrowDownRight`) di sebelah kiri.
- **Inspirasi**: `Badge Delta`.

### Arketipe 4: The Hero Tagline (Pill Badge)
- **Fungsi**: Pengumuman rilis fitur baru yang diletakkan tepat di atas teks judul raksasa (Hero Section).
- **Karakteristik Visual**:
  - Sudut membulat penuh seperti pil (`rounded-full`).
  - Dilengkapi efek pendaran lembut (*glow/shadow*) atau border berpendar ringan (`border-indigo-500/30`).
  - Menyatukan lencana "NEW" yang menonjol dan teks "Baca rilis terbaru" beserta tanda panah `→`.
- **Inspirasi**: `Tagline (shadcncraft)`, `BeUI Animated Badge`.

### Arketipe 5: The Notification Counter (Micro Badge)
- **Fungsi**: Angka merah di atas ikon lonceng atau keranjang belanja.
- **Karakteristik Visual**: Bulatan sangat kecil (`w-5 h-5`) dengan font berukuran `10px` super tebal (`font-black`) dan diletakkan secara melayang (*absolute position*).

---

## 2. Blueprint Kode Master

### A. The Master Polymorphic Badge
```tsx
import { ArrowUpRight, ArrowDownRight, X, Sparkles } from "lucide-react";

interface BadgeProps {
  children: React.ReactNode;
  variant?: "default" | "status-success" | "status-pending" | "status-error" | "outline" | "hero-glow";
  size?: "sm" | "md" | "lg";
  onDismiss?: () => void;
  className?: string;
}

export function MasterBadge({
  children,
  variant = "default",
  size = "md",
  onDismiss,
  className = "",
}: BadgeProps) {
  
  // 1. Pemetaan Ukuran
  const sizeClasses = {
    sm: "px-2 py-0.5 text-[10px]",
    md: "px-2.5 py-1 text-xs",
    lg: "px-3 py-1.5 text-sm",
  };

  // 2. Pemetaan Varian Gaya & Warna
  const variantClasses = {
    "default": "bg-slate-800 text-slate-200 border border-slate-700",
    "status-success": "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20",
    "status-pending": "bg-amber-500/10 text-amber-400 border border-amber-500/20",
    "status-error": "bg-rose-500/10 text-rose-400 border border-rose-500/20",
    "outline": "bg-transparent text-slate-300 border border-slate-700 hover:bg-slate-800 transition-colors",
    "hero-glow": "bg-indigo-500/10 text-indigo-300 border border-indigo-500/30 shadow-[0_0_10px_rgba(99,102,241,0.2)]",
  };

  const isStatus = variant.startsWith("status");

  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-md font-medium font-mono whitespace-nowrap select-none ${sizeClasses[size]} ${variantClasses[variant]} ${className}`}
    >
      {/* 3. Auto-Inject Status Dot jika Varian adalah Status */}
      {isStatus && (
        <span
          className={`w-1.5 h-1.5 rounded-full shrink-0 ${
            variant === "status-success" ? "bg-emerald-500" :
            variant === "status-pending" ? "bg-amber-500" :
            "bg-rose-500"
          }`}
        />
      )}

      {children}

      {/* 4. Auto-Inject Close Icon jika onDismiss disediakan (sebagai Filter Chip) */}
      {onDismiss && (
        <button
          type="button"
          onClick={onDismiss}
          className="ml-1 p-0.5 rounded-sm hover:bg-black/20 focus:outline-none focus:ring-1 focus:ring-current transition-colors"
          aria-label="Hapus filter"
        >
          <X className="w-3 h-3 opacity-70 hover:opacity-100" />
        </button>
      )}
    </span>
  );
}

// --- CONTOH KOMPONEN KHUSUS: THE HERO TAGLINE PILL ---
export function HeroTaglineBadge({ label = "Versi 2.0 Telah Rilis", link = "#" }) {
  return (
    <a 
      href={link}
      className="group inline-flex items-center gap-2 p-1 pr-3 rounded-full border border-indigo-500/20 bg-indigo-500/5 hover:bg-indigo-500/10 transition-colors cursor-pointer w-fit"
    >
      <span className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-indigo-500 text-white text-[10px] font-bold tracking-wide uppercase shadow-md shadow-indigo-500/30">
        <Sparkles className="w-3 h-3" />
        Baru
      </span>
      <span className="text-xs font-semibold text-indigo-200">{label}</span>
      <ArrowUpRight className="w-3.5 h-3.5 text-indigo-400 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
    </a>
  );
}
```

---

## 3. Aturan Desain Badge & Tag
1. **Aturan Radius (Rounded)**:
   - Jika badge diletakkan di dalam tabel data (Status Transaksi), gunakan `rounded-md` atau `rounded-lg` agar terlihat profesional dan selaras dengan tepian sel tabel.
   - Jika badge digunakan sebagai pengumuman (*Tagline*) di pilar *Hero Section*, gunakan `rounded-full` (bentuk oval murni) agar terlihat dinamis dan modern.
2. **Keterbacaan Huruf (Legibility)**: Teks di dalam badge biasanya berukuran super mungil (`text-[10px]` atau `text-xs`). Karenanya, gunakan huruf tebal (`font-semibold` atau `font-medium`) serta seringkali mengadopsi keluarga font monospace (`font-mono`) agar angka tren analitik terlihat stabil.
3. **Peringatan Warna Status**: Jangan mendesain Badge Success dengan latar belakang *solid* (misal: balok hijau pekat dengan tulisan putih). Di *Dark Mode*, blok warna yang solid dan cerah akan menyilaukan mata dan mendominasi layar. Selalu gunakan *Tinted Background* (Latar Belakang Temaram: `bg-emerald-500/10` dengan teks warna terang `text-emerald-400`).
