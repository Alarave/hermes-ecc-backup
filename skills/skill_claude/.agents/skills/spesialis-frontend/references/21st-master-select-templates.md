# 21st.dev Master Select & Multi-Select Templates

Analisis pola dan blueprint komponen Select / Combobox / Multi-Select berdasarkan tren unduhan tertinggi di 21st.dev (React + Tailwind v4 + Framer Motion / Radix UI / cmdk).

---

## 1. Empat Arketipe Select & Multi-Select Modern

### Arketipe 1: The Tagged Multi-Select (Paling Populer)
- **Fungsi**: Memilih beberapa item sekaligus (misal: memilih teknologi, tag artikel, atau anggota tim).
- **Karakteristik Visual**:
  - Item yang terpilih muncul sebagai *Removable Chip* (Badge kapsul kecil dengan tombol silang) di dalam kotak input.
  - Sisa pilihan yang meluap dapat disingkat menjadi badge hitungan (misal: "+3 lainnya").
  - Memiliki tombol "Clear all" (Hapus semua) di ujung kanan.
- **Inspirasi**: `Multi-Select with Badges`, `Fancy Multi-Select (cmdk)`.

### Arketipe 2: The Searchable Combobox (Command Palette Style)
- **Fungsi**: Menyeleksi satu item dari daftar yang sangat panjang (>20 opsi).
- **Karakteristik Visual**:
  - Saat dropdown terbuka, terdapat input pencarian (*search bar*) kecil di baris teratas.
  - Menggunakan animasi *check icon* di samping opsi yang sedang terpilih.

### Arketipe 3: The Rich Item Select (Avatar & Description)
- **Fungsi**: Pemilihan profil pengguna (*Assignee selector*), mata uang, atau status.
- **Karakteristik Visual**: Setiap baris opsi di dalam dropdown memuat gambar kecil/avatar, teks judul tebal, dan deskripsi sekunder (subtext).

### Arketipe 4: Grouped & Categorized Select
- **Fungsi**: Mengelompokkan opsi berdasarkan konteks (misal: Framework Frontend vs Backend).
- **Karakteristik Visual**: Terdapat header kategori kecil berwarna abu-abu yang tidak bisa diklik (*disabled header*) dan garis pembatas halus.

---

## 2. Blueprint Kode Master (The Searchable Multi-Select)

Blueprint ini menggabungkan input pencarian real-time dengan pemilihan multi-item menggunakan Chip Badge:

```tsx
import { useState, useRef, useEffect } from "react";
import { Check, ChevronDown, X } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface Option {
  id: string;
  label: string;
}

const OPTIONS: Option[] = [
  { id: "react", label: "React 19" },
  { id: "next", label: "Next.js 15" },
  { id: "tailwind", label: "Tailwind CSS v4" },
  { id: "framer", label: "Framer Motion" },
  { id: "typescript", label: "TypeScript" },
];

export function SearchableMultiSelect() {
  const [selected, setSelected] = useState<Option[]>([]);
  const [isOpen, setIsOpen] = useState(false);
  const [search, setSearch] = useState("");
  const containerRef = useRef<HTMLDivElement>(null);

  // Close dropdown on outside click
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const toggleOption = (option: Option) => {
    if (selected.some((item) => item.id === option.id)) {
      setSelected(selected.filter((item) => item.id !== option.id));
    } else {
      setSelected([...selected, option]);
    }
  };

  const removeOption = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setSelected(selected.filter((item) => item.id !== id));
  };

  const filteredOptions = OPTIONS.filter((opt) =>
    opt.label.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div ref={containerRef} className="relative w-full max-w-md mx-auto select-none">
      
      {/* 1. Trigger Box / Input Area */}
      <div
        onClick={() => setIsOpen(!isOpen)}
        className={`min-h-[46px] p-2 flex flex-wrap items-center gap-1.5 rounded-xl border bg-slate-900 cursor-pointer transition-all ${
          isOpen 
            ? "border-indigo-500 ring-1 ring-indigo-500" 
            : "border-slate-800 hover:border-slate-700"
        }`}
      >
        {selected.length === 0 && (
          <span className="text-sm text-slate-500 px-2">Pilih teknologi...</span>
        )}

        {/* Selected Chips */}
        {selected.map((item) => (
          <span
            key={item.id}
            className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg text-xs font-medium bg-slate-800 border border-slate-700 text-slate-200"
          >
            <span>{item.label}</span>
            <button
              onClick={(e) => removeOption(item.id, e)}
              className="p-0.5 rounded hover:bg-slate-700 text-slate-400 hover:text-slate-200 focus:outline-none"
            >
              <X className="w-3 h-3" />
            </button>
          </span>
        ))}

        <div className="flex-1 flex justify-end items-center pr-1 text-slate-400">
          <ChevronDown className={`w-4 h-4 transition-transform duration-200 ${isOpen ? "rotate-180" : ""}`} />
        </div>
      </div>

      {/* 2. Dropdown Panel */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: -6, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -6, scale: 0.98 }}
            transition={{ duration: 0.15, ease: "easeOut" }}
            className="absolute z-50 w-full mt-2 rounded-xl border border-slate-800 bg-slate-900/95 backdrop-blur-xl shadow-2xl p-1 overflow-hidden"
          >
            {/* Search Input */}
            <div className="p-1 border-b border-slate-800 mb-1">
              <input
                type="text"
                placeholder="Cari opsi..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                onClick={(e) => e.stopPropagation()}
                className="w-full px-3 py-1.5 text-xs bg-slate-950/60 rounded-lg text-slate-200 placeholder-slate-500 border border-slate-800 focus:outline-none focus:border-indigo-500"
              />
            </div>

            {/* Options List */}
            <div className="max-h-52 overflow-y-auto no-scrollbar space-y-0.5">
              {filteredOptions.length === 0 ? (
                <div className="p-4 text-center text-xs text-slate-500">
                  Tidak ada hasil ditemukan.
                </div>
              ) : (
                filteredOptions.map((option) => {
                  const isSelected = selected.some((item) => item.id === option.id);
                  return (
                    <div
                      key={option.id}
                      onClick={() => toggleOption(option)}
                      className={`flex items-center justify-between px-3 py-2 rounded-lg text-xs font-medium cursor-pointer transition-colors ${
                        isSelected
                          ? "bg-indigo-500/10 text-indigo-400"
                          : "text-slate-300 hover:bg-slate-800/60"
                      }`}
                    >
                      <span>{option.label}</span>
                      {isSelected && <Check className="w-3.5 h-3.5 text-indigo-400" />}
                    </div>
                  );
                })
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>

    </div>
  );
}
```

---

## 3. Checklist UX Select & Multi-Select
1. **Pencegahan Event Bubbling**: Klik pada tombol hapus chip (`X`) harus menggunakan `e.stopPropagation()` agar tidak memicu buka-tutup dropdown secara tidak sengaja.
2. **Keyboard Roving & Escape**: Menekan tombol `Escape` harus menutup panel dropdown seketika dan mengembalikan fokus ke kontainer utama.
3. **Tinggi Dinamis vs Overflow**: Saat banyak chip dipilih, kotak input harus tumbuh vertikal (`min-h-[46px] flex-wrap`) tanpa menggeser elemen di bawahnya secara mendadak.
