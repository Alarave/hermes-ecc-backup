# 21st.dev Master Radio Group Templates

Analisis pola dan blueprint komponen Radio Group (Pilihan Eksklusif) berdasarkan 25+ komponen modern di 21st.dev (React + Tailwind v4 + Framer Motion / Radix UI).

---

## 1. Empat Arketipe Radio Group Modern

### Arketipe 1: The Selectable Card Radio Group (Pricing & Plans)
- **Fungsi**: Memilih paket langganan, jenis pengiriman, atau metode pembayaran.
- **Karakteristik Visual**:
  - Alih-alih tombol radio lingkaran kecil, seluruh kotak kartu (*Card*) berfungsi sebagai tombol yang dapat diklik.
  - Kartu yang terpilih (*selected*) mendapatkan border menyala (misal: `border-indigo-500`), background sedikit terang, dan tanda centang aktif.
  - Memuat informasi kaya: Ikon, judul tebal, deskripsi singkat, harga, dan badge rekomendasi ("Popular").
- **Inspirasi**: Stripe Checkout, GitHub Plan Selectors.

### Arketipe 2: The Minimalist Spring Radio Button
- **Fungsi**: Formulir survei atau pengaturan standar di dalam dokumen.
- **Karakteristik Visual**:
  - Lingkaran radio custom dengan border halus.
  - Titik isi (dot) di bagian dalam membesar dari `scale: 0` ke `scale: 1` menggunakan animasi fisika pegas (spring) yang lembut saat dipilih.

### Arketipe 3: The Payment / Visual Icon Radio
- **Fungsi**: Pemilihan opsi yang mengandalkan logo/gambar (Kartu Kredit, PayPal, Apple Pay, Transfer Bank).
- **Karakteristik Visual**: Grid kotak horizontal yang didominasi oleh logo penyedia layanan, meminimalkan teks agar proses checkout cepat dan visual.

### Arketipe 4: The Segmented Button Radio Group
- **Fungsi**: Memilih ukuran pakaian (S, M, L, XL), warna, atau kuota data.
- **Karakteristik Visual**: Berjajar horizontal seperti deretan tombol kecil (Button Pill) yang langsung aktif saat ditekan.

---

## 2. Standar Aksesibilitas (WAI-ARIA Radio Pattern)
Radio group memiliki aturan navigasi keyboard khusus dari W3C:
1. **Atribut ARIA**:
   - Kontainer wajib memiliki `role="radiogroup"`.
   - Setiap elemen pilihan wajib memiliki `role="radio"` dan `aria-checked="true|false"`.
2. **Navigasi Panah Keyboard (Roving Focus)**:
   - Pengguna menekan tombol `Tab` untuk masuk ke radio group (fokus jatuh ke opsi yang terpilih).
   - Pengguna menggunakan tombol panah (`ArrowUp` / `ArrowDown` atau `ArrowLeft` / `ArrowRight`) untuk berpindah opsi secara otomatis tanpa tombol Tab.

---

## 3. Blueprint Kode Master (The Selectable Card Radio Group)

Blueprint pemilihan paket/layanan berbentuk kartu interaktif yang sangat sering dipakai pada halaman *Billing* atau *Checkout*:

```tsx
import { useState } from "react";
import { CheckCircle2, Shield, Zap, Sparkles } from "lucide-react";
import { motion } from "framer-motion";

interface PlanOption {
  id: string;
  name: string;
  description: string;
  price: string;
  icon: any;
  popular?: boolean;
}

const PLANS: PlanOption[] = [
  {
    id: "starter",
    name: "Starter",
    description: "Sempurna untuk eksperimen dan proyek personal.",
    price: "$9/bln",
    icon: Shield,
  },
  {
    id: "pro",
    name: "Pro Developer",
    description: "Akses penuh ke semua model dan kuota tak terbatas.",
    price: "$29/bln",
    icon: Zap,
    popular: true,
  },
  {
    id: "enterprise",
    name: "Enterprise",
    description: "Dedicated account manager dan SLA 99.9%.",
    price: "$99/bln",
    icon: Sparkles,
  },
];

export function SelectableCardRadioGroup() {
  const [selected, setSelected] = useState<string>("pro");

  return (
    <div 
      role="radiogroup" 
      aria-label="Pilih paket langganan"
      className="w-full max-w-xl mx-auto space-y-3 select-none"
    >
      {PLANS.map((plan) => {
        const isSelected = selected === plan.id;
        const Icon = plan.icon;

        return (
          <div
            key={plan.id}
            role="radio"
            aria-checked={isSelected}
            tabIndex={isSelected ? 0 : -1}
            onClick={() => setSelected(plan.id)}
            onKeyDown={(e) => {
              if (e.key === " " || e.key === "Enter") {
                e.preventDefault();
                setSelected(plan.id);
              }
            }}
            className={`relative flex items-start gap-4 p-5 rounded-2xl border cursor-pointer transition-all duration-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 ${
              isSelected
                ? "border-indigo-500 bg-slate-900/90 shadow-lg shadow-indigo-500/10"
                : "border-slate-800 bg-slate-900/40 hover:border-slate-700/80 hover:bg-slate-900/60"
            }`}
          >
            {/* Custom Circular Radio Indicator */}
            <div className="flex-shrink-0 mt-1">
              <div className={`w-5 h-5 rounded-full border flex items-center justify-center transition-colors ${
                isSelected ? "border-indigo-500 bg-indigo-500" : "border-slate-700 bg-slate-800"
              }`}>
                {isSelected && (
                  <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    transition={{ type: "spring", stiffness: 500, damping: 30 }}
                    className="w-2 h-2 rounded-full bg-white"
                  />
                )}
              </div>
            </div>

            {/* Content Area */}
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2">
                <Icon className={`w-4 h-4 ${isSelected ? "text-indigo-400" : "text-slate-400"}`} />
                <h4 className="text-sm font-semibold text-slate-100">{plan.name}</h4>
                {plan.popular && (
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-mono font-medium bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
                    Popular
                  </span>
                )}
              </div>
              <p className="mt-1 text-xs text-slate-400 leading-relaxed">
                {plan.description}
              </p>
            </div>

            {/* Price Column */}
            <div className="text-right flex-shrink-0">
              <span className="text-sm font-bold font-mono text-slate-100">{plan.price}</span>
            </div>

          </div>
        );
      })}
    </div>
  );
}
```

---

## 3. Checklist UX Radio Group
1. **Radio vs Checkbox**: Gunakan Radio Group HANYA jika pilihan bersifat eksklusif mutlak (hanya boleh memilih tepat satu). Jika pengguna boleh memilih lebih dari satu, gunakan Checkbox.
2. **Seluruh Area Kartu Dapat Diklik**: Pastikan event `onClick` terpasang pada pembungkus kartu terluar, bukan hanya pada bulatan radio kecil di pojok.
3. **Visual Feedback Seketika**: Kartu yang aktif harus memiliki pembeda visual minimal di dua aspek (misal: warna garis tepi yang lebih cerah DAN bulatan radio yang terisi) agar mudah diidentifikasi oleh pengguna dengan gangguan penglihatan warna (Color-blind safe).
