# 21st.dev Master Dropdown Mechanics & Templates

Analisis pola dan blueprint komponen Dropdown berdasarkan 27+ komponen di 21st.dev (React + Tailwind v4). Komponen Dropdown sering bertumpang tindih secara visual dengan **Menu**, **Select**, dan **Popover**. Dokumen ini difokuskan pada *mekanika dasar* (Headless Logic).

---

## 1. Hubungan Dropdown dengan Arketipe UI Lain
Dropdown bukanlah satu komponen tunggal, melainkan *mekanisme interaksi* yang memunculkan panel terapung.
- **Jika berisi aksi klik (Salin, Hapus)** → Gunakan blueprint **Menu** (`21st-master-menu-templates.md`).
- **Jika berisi form / tanggal / konten baca** → Gunakan blueprint **Popover** (`21st-master-popover-templates.md`).
- **Jika digunakan untuk memilih satu nilai (seperti `<select>`)** → Gunakan blueprint **Select & Combobox** (`21st-master-select-templates.md`).

---

## 2. Tiga Arketipe Fundamental Dropdown

### Arketipe 1: The Account / Profile Dropdown
- **Fungsi**: Menu profil di kanan atas (*Navbar*).
- **Karakteristik Visual**:
  - Pemicu (*trigger*) berupa Avatar kecil.
  - Dropdown panel memuat header (Nama & Email), diikuti item menu (Pengaturan, Bantuan), dan diakhiri dengan tombol *Log Out* (berwarna kontras).

### Arketipe 2: The Multi-level / Nested Dropdown
- **Fungsi**: Navigasi hirarki kompleks di mana hover/klik pada satu opsi membuka panel sub-opsi di sebelahnya.
- **Karakteristik Visual**:
  - Item pemicu sub-menu memiliki ikon chevron kanan (`>`).
  - Animasi pembukaan sub-menu biasanya muncul dari samping (offset sumbu X).

### Arketipe 3: The Filter / Sorting Dropdown
- **Fungsi**: Mengurutkan tabel (Terbaru, Terlama, Alfabetis).
- **Karakteristik Visual**: Opsi yang sedang aktif memiliki ikon centang (`Check`) di sampingnya.

---

## 3. Blueprint Kode Master (The Nested Filter Dropdown dengan Checkbox)

```tsx
import { useState, useRef, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Filter, Check, ChevronRight } from "lucide-react";

export function FilterDropdownMenu() {
  const [isOpen, setIsOpen] = useState(false);
  const [activeSort, setActiveSort] = useState("terbaru");
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Hook penanganan klik di luar untuk menutup dropdown
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const SORT_OPTIONS = [
    { id: "terbaru", label: "Terbaru Diubah" },
    { id: "terlama", label: "Terlama Diubah" },
    { id: "abjad-a", label: "Abjad (A - Z)" },
  ];

  return (
    <div className="relative inline-block" ref={dropdownRef}>
      {/* Trigger Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-slate-800 bg-slate-900 text-sm font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition-colors"
      >
        <Filter className="w-4 h-4 text-slate-400" />
        <span>Filter & Urutkan</span>
      </button>

      {/* Dropdown Panel */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: -5 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: -5 }}
            transition={{ duration: 0.15, ease: "easeOut" }}
            className="absolute right-0 mt-2 w-56 p-1.5 rounded-xl border border-slate-800 bg-slate-900 shadow-2xl backdrop-blur-xl z-[100]"
          >
            <div className="px-2 py-1.5 mb-1 border-b border-slate-800/80">
              <span className="text-[10px] font-bold font-mono text-slate-500 uppercase tracking-widest">
                Urutkan Berdasarkan
              </span>
            </div>

            <div className="space-y-0.5">
              {SORT_OPTIONS.map((opt) => (
                <button
                  key={opt.id}
                  onClick={() => { setActiveSort(opt.id); setIsOpen(false); }}
                  className="w-full flex items-center justify-between px-2.5 py-1.5 rounded-md text-xs font-medium text-slate-300 hover:text-white hover:bg-slate-800/80 transition-colors"
                >
                  <span>{opt.label}</span>
                  {activeSort === opt.id && <Check className="w-3.5 h-3.5 text-indigo-400" />}
                </button>
              ))}
            </div>

            {/* Nested Sub-Menu Trigger (Visual Simulation) */}
            <div className="mt-1 pt-1 border-t border-slate-800/80">
              <button className="w-full flex items-center justify-between px-2.5 py-1.5 rounded-md text-xs font-medium text-slate-400 hover:text-white hover:bg-slate-800/80 transition-colors">
                <span>Opsi Lanjutan</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
```

---

## 4. Checklist Z-Index & Portal (Masalah Umum Dropdown)
1. **Penjara Z-Index (*Z-Index Clipping*)**: Kesalahan paling umum adalah membiarkan Dropdown terpotong (*clipped*) oleh div bungkusnya yang memiliki `overflow-hidden`. 
2. **Solusi Portal React**: Untuk aplikasi skala besar, dropdown panel mutlak dirender menggunakan *React Portals* (atau komponen bawaan `@radix-ui/react-dropdown-menu`) agar elemen dropdown di-inject langsung ke dalam tag `<body>`, bebas dari aturan tata letak parent-nya, sehingga selalu tampil di lapisan teratas (z-index absolut).
