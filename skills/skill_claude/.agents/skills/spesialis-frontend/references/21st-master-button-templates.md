# 21st.dev Master Button & CTA Action Templates

Analisis pola dan blueprint komponen Button (Tombol & Aksi Panggilan/CTA) berdasarkan 764+ variasi di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Lima Arketipe Button Modern

### Arketipe 1: The Shimmer / Glowing Border CTA (SaaS Hero Button)
- **Fungsi**: Tombol konversi primer di landing page (misal: "Mulai Uji Coba Gratis", "Beli Voucher Kopi").
- **Karakteristik Visual**:
  - Efek kilau cahaya berputar (*rotating conic gradient border*) di sekeliling tombol.
  - Latar belakang tombol semi-gelap (`bg-slate-950`) dengan pendaran neon halus di belakangnya saat di-hover.
- **Inspirasi**: `Shiny Button (Ali Imam)`, `SparkButton (Ruixen)`, `Glowing Button (prebuiltui)`.

### Arketipe 2: The Interactive Loading Spinner Button
- **Fungsi**: Pengiriman form transaksi atau request API yang membutuhkan waktu proses.
- **Karakteristik Visual**:
  - Teks tombol tidak hilang secara kasar, melainkan bertransisi mulus ke ikon pemintal (*spinner*) dengan teks status ("Menyimpan...").
  - Tombol otomatis dinonaktifkan (`disabled`) dan kursor berubah menjadi `cursor-not-allowed` untuk mencegah *double-click submit*.
- **Inspirasi**: `Loading Button (Origin UI)`, `Button Loading (Cnippet)`.

### Arketipe 3: The Split Action Button
- **Fungsi**: Aksi utama dengan opsi sekunder tersemat (misal: "Publish Post" + tombol panah bawah untuk "Schedule Post" atau "Save Draft").
- **Karakteristik Visual**:
  - Terdiri dari dua bagian bersebelahan: tombol teks lebar di kiri dan tombol ikon panah bawah (`ChevronDown`) di kanan yang dipisahkan garis vertikal tipis.
- **Inspirasi**: `Split Button (tigran tumasov)`, `Split Button (shadcn)`.

### Arketipe 4: The Tactile 3D / Retro Button
- **Fungsi**: Aplikasi berorientasi gaming, Web3, atau UI bergaya retro neobrutalism.
- **Karakteristik Visual**:
  - Memiliki bayangan bawah tebal (*bottom border/shadow* 3D: `border-b-4 border-indigo-700`).
  - Saat ditekan (`active:translate-y-1 active:border-b-0`), tombol terasa tertekan ke dalam secara mekanis.
- **Inspirasi**: `Retro Button (Serafim)`, `3D Button (Utkarsh Pandey)`.

### Arketipe 5: The Tactile Icon Button (Ghost / Outline Variant)
- **Fungsi**: Toolbar, pemutar audio, atau aksi mikro baris tabel (Edit, Delete, Bookmark).
- **Karakteristik Visual**:
  - Bentuk persegi bundar (`w-9 h-9 rounded-xl`) dengan latar belakang transparan yang hanya menampakkan warna saat disorot kursor mouse (`hover:bg-slate-800`).

---

## 2. Blueprint Kode Master (The Complete Button Architecture)

```tsx
import { useState, forwardRef } from "react";
import { Loader2, ArrowRight, Sparkles, ChevronDown } from "lucide-react";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "shiny" | "secondary" | "outline" | "ghost" | "destructive";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}

export const MasterButton = forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      children,
      variant = "primary",
      size = "md",
      isLoading = false,
      leftIcon,
      rightIcon,
      disabled,
      className = "",
      ...props
    },
    ref
  ) => {
    // 1. Pemetaan Ukuran
    const sizeClasses = {
      sm: "h-8 px-3 text-xs rounded-lg gap-1.5",
      md: "h-10 px-4 text-sm rounded-xl gap-2",
      lg: "h-12 px-6 text-base rounded-2xl gap-2.5",
    };

    // 2. Pemetaan Varian
    const variantClasses = {
      primary: "bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-600/20 active:scale-[0.98]",
      secondary: "bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700/80 active:scale-[0.98]",
      outline: "border border-slate-800 bg-transparent hover:bg-slate-800 text-slate-300 hover:text-white active:scale-[0.98]",
      ghost: "bg-transparent hover:bg-slate-800/80 text-slate-400 hover:text-white",
      destructive: "bg-rose-600 hover:bg-rose-500 text-white shadow-lg shadow-rose-600/20 active:scale-[0.98]",
      shiny: "relative overflow-hidden bg-slate-950 text-white border border-indigo-500/30 shadow-[0_0_20px_rgba(99,102,241,0.25)] hover:border-indigo-500/60 active:scale-[0.98]",
    };

    const isDisabled = disabled || isLoading;

    return (
      <button
        ref={ref}
        disabled={isDisabled}
        className={`inline-flex items-center justify-center font-semibold transition-all duration-200 select-none focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 disabled:opacity-50 disabled:pointer-events-none ${
          sizeClasses[size]
        } ${variantClasses[variant]} ${className}`}
        {...props}
      >
        {/* Efek Garis Kilau Berputar Khusus Varian "shiny" */}
        {variant === "shiny" && (
          <span className="absolute inset-0 -translate-x-full bg-gradient-to-r from-transparent via-white/10 to-transparent transition-transform duration-1000 group-hover:translate-x-full" />
        )}

        {/* State Loading Spinner */}
        {isLoading ? (
          <>
            <Loader2 className="w-4 h-4 animate-spin text-current shrink-0" />
            <span>Memproses...</span>
          </>
        ) : (
          <>
            {leftIcon && <span className="shrink-0">{leftIcon}</span>}
            <span>{children}</span>
            {rightIcon && <span className="shrink-0">{rightIcon}</span>}
          </>
        )}
      </button>
    );
  }
);

MasterButton.displayName = "MasterButton";

// --- CONTOH KOMPONEN: THE SPLIT ACTION BUTTON ---
export function SplitActionButton({
  label = "Terbitkan Perubahan",
  onMainClick,
  onOptionClick,
}: {
  label?: string;
  onMainClick?: () => void;
  onOptionClick?: () => void;
}) {
  return (
    <div className="inline-flex rounded-xl shadow-lg shadow-indigo-600/20">
      <button
        onClick={onMainClick}
        className="h-10 px-4 rounded-l-xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold transition-colors flex items-center gap-2"
      >
        <Sparkles className="w-4 h-4" />
        <span>{label}</span>
      </button>
      <div className="w-[1px] bg-indigo-700" />
      <button
        onClick={onOptionClick}
        className="h-10 px-2.5 rounded-r-xl bg-indigo-600 hover:bg-indigo-500 text-white transition-colors flex items-center justify-center"
        aria-label="Opsi publikasi tambahan"
      >
        <ChevronDown className="w-4 h-4" />
      </button>
    </div>
  );
}
```

---

## 3. Checklist Aksesibilitas Button (WCAG 2.2 Level AA)
1. **Target Sentuh Minimum (Touch Target)**:
   - Tombol pada perangkat layar sentuh wajib memiliki ukuran fisik minimal `44px x 44px` atau minimal diberi margin/padding ekstra agar tidak terjadi salah pencet jempol (*fat-finger error*).
2. **Cincin Fokus (*Focus-Visible Ring*)**:
   - Jangan pernah mematikan outline keyboard dengan `outline-none` tanpa menyertakan pengganti! Gunakan selalu `focus-visible:ring-2 focus-visible:ring-indigo-500` agar pengguna keyboard mengetahui dengan jelas tombol mana yang sedang aktif.
3. **Pemberitahuan Screen Reader untuk Icon-Only**:
   - Jika tombol tidak memiliki label teks (hanya ikon roda gigi `Settings` atau pensil `Edit`), tombol **WAJIB** memiliki atribut `aria-label="Pengaturan profil"`.
4. **Keamanan State Disabled**:
   - Ketika tombol berada dalam status memproses (`isLoading`), sematkan `aria-busy="true"` dan nonaktifkan klik ganda dengan `disabled={true}`.
