# 21st.dev Master Chip, Badge & Tag Templates

Analisis pola komponen Chip / Badge / Tag berdasarkan koleksi 74+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Chip / Badge Modern

### Arketipe 1: The Status Badge (Solid / Subtle)
- **Fungsi**: Menandakan status data (Active, Pending, Error, Success).
- **Karakteristik**: Menggunakan palet "Subtle" (latar belakang dengan opacity 10% dan teks warna solid).
- **Desain**: Sering disertai dot (titik) berwarna di sebelah kiri teks. `bg-emerald-500/10 text-emerald-500` dengan `w-1.5 h-1.5 rounded-full bg-emerald-500`.

### Arketipe 2: The Interactive Filter Chip (Pill)
- **Fungsi**: Memilih kategori atau filter pada pencarian / galeri.
- **Karakteristik**: Berbentuk kapsul (rounded-full). Berubah warna secara signifikan ketika aktif (selected).
- **Desain**: `border border-slate-700 bg-slate-800/50 hover:bg-slate-700` saat tidak aktif, menjadi `bg-white text-slate-900` saat aktif.

### Arketipe 3: The Glowing / Announcement Pill
- **Fungsi**: Menarik perhatian ke fitur baru atau pengumuman kecil (di atas Hero Section).
- **Karakteristik**: Dilengkapi dengan animasi *border beam* (cahaya berjalan di pinggir) atau *pulse* kecil.
- **Desain**: Backrop blur `backdrop-blur-md` dengan gradient border atau *box-shadow glow*.

### Arketipe 4: The Removable Token (Tag Input)
- **Fungsi**: Label data pada input form (misalnya memasukkan banyak alamat email atau tag artikel).
- **Karakteristik**: Memiliki ikon "Silang (X)" di sisi kanan untuk menghapus tag tersebut dari list.

---

## 2. Blueprint Kode Master (The Modern Status & Filter Chips)

### A. The Glowing Announcement Pill (Animated)
Cocok digunakan di bagian atas Hero section.

```tsx
import { ArrowRight } from "lucide-react";

export function AnnouncementChip({ text, link = "#" }) {
  return (
    <a 
      href={link}
      className="group relative inline-flex items-center justify-center gap-2 px-3 py-1 text-xs font-medium rounded-full overflow-hidden border border-indigo-500/20 bg-indigo-500/10 text-indigo-300 hover:border-indigo-500/40 transition-colors"
    >
      <span className="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-pulse" />
      <span className="relative z-10">{text}</span>
      <ArrowRight className="w-3.5 h-3.5 text-indigo-400 group-hover:translate-x-0.5 transition-transform" />
      
      {/* Subtle background glow on hover */}
      <div className="absolute inset-0 bg-gradient-to-r from-indigo-500/0 via-indigo-500/10 to-indigo-500/0 opacity-0 group-hover:opacity-100 transition-opacity" />
    </a>
  );
}
```

### B. The Status Badge (Dot Indicator)
Komponen ringan untuk tabel data, dashboard, atau list transaksi.

```tsx
type StatusType = "success" | "warning" | "error" | "neutral";

export function StatusBadge({ status, label }: { status: StatusType; label: string }) {
  const styles = {
    success: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20",
    warning: "bg-amber-500/10 text-amber-400 border-amber-500/20",
    error: "bg-rose-500/10 text-rose-400 border-rose-500/20",
    neutral: "bg-slate-500/10 text-slate-400 border-slate-500/20",
  };

  const dotColors = {
    success: "bg-emerald-400",
    warning: "bg-amber-400",
    error: "bg-rose-400",
    neutral: "bg-slate-400",
  };

  return (
    <span className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-md text-xs font-medium border ${styles[status]}`}>
      <span className={`w-1.5 h-1.5 rounded-full ${dotColors[status]}`} />
      {label}
    </span>
  );
}
```

### C. The Removable Token / Tag
Digunakan dalam input multiple-tags.

```tsx
import { X } from "lucide-react";

export function RemovableChip({ label, onRemove }) {
  return (
    <span className="inline-flex items-center gap-1.5 pl-2.5 pr-1 py-1 rounded-md text-xs font-medium bg-slate-800 text-slate-200 border border-slate-700">
      <span>{label}</span>
      <button 
        onClick={onRemove}
        className="p-0.5 rounded-sm hover:bg-slate-700 hover:text-white transition-colors focus:outline-none focus:ring-1 focus:ring-slate-400"
        aria-label={`Remove ${label}`}
      >
        <X className="w-3 h-3" />
      </button>
    </span>
  );
}
```

---

## 3. Checklist UX / Aksesibilitas Chips
1. **Interactive vs Static**: Bedakan secara visual antara Badge statis (sebagai info/status) dengan Chip interaktif (filter/tombol). Chip interaktif wajib memiliki `hover state` dan outline fokus keyboard.
2. **Hit Area pada Tombol Hapus**: Pada *Removable Token*, pastikan tombol silang (X) memiliki padding cukup agar mudah ditekan di layar sentuh, tanpa tidak sengaja menekan chip utama.
3. **Warna & Kontras (WCAG)**: Hindari badge dengan teks putih di atas background kuning/hijau muda. Gunakan background ber-opacity 10% (Subtle) dengan teks warna solid (Tingkat 400 atau 500) pada mode gelap.
