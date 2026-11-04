# 21st.dev Master Search & Command Palette Templates

Analisis pola dan blueprint komponen Search Bar & Command Menu berdasarkan 218+ komponen terpopuler di 21st.dev (React + Tailwind v4 + Framer Motion / cmdk).

---

## 1. Empat Arketipe Search Modern

### Arketipe 1: The Apple Spotlight / Command Palette (⌘K)
- **Fungsi**: Navigasi global cepat untuk seluruh aplikasi (pencarian halaman, aksi cepat, file).
- **Karakteristik Visual**:
  - Modal melayang di tengah layar yang dipicu oleh shortcut keyboard (`⌘ + K` atau `Ctrl + K`).
  - Hasil pencarian dikelompokkan (misal: "Halaman", "Tindakan Cepat", "Dokumentasi").
  - Navigasi penuh menggunakan tombol panah atas/bawah (`ArrowUp` / `ArrowDown`) dan `Enter`.
- **Inspirasi**: `Apple Spotlight (Samit Kapoor)`, `Command (shadcn)`.

### Arketipe 2: The Inline Search Bar with Kbd Badge
- **Fungsi**: Komponen pencarian statis di dalam Navbar atas.
- **Karakteristik Visual**:
  - Ikon kaca pembesar di sisi kiri.
  - Teks placeholder redup ("Cari dokumentasi...").
  - Lencana tombol keyboard (`<kbd>⌘K</kbd>`) di sisi kanan yang berfungsi sebagai tombol pemicu.
- **Inspirasi**: `Kbd Input Group (uiable)`, `Border Beam Search`.

### Arketipe 3: The Expanding Dock Search Bar
- **Fungsi**: Menghemat ruang pada toolbar atau navbar mobile.
- **Karakteristik Visual**: Berawal hanya sebagai tombol ikon kecil. Saat diklik, tombol tersebut "melar" (expand) secara horizontal menjadi kotak input penuh dengan transisi spring.
- **Inspirasi**: `Expandable Search Bar (Arunachalam)`, `Expanding Search Dock (Moumen Soliman)`.

### Arketipe 4: Search with Integrated Category Filter
- **Fungsi**: Pencarian e-commerce atau repositori dengan filter cakupan langsung.
- **Karakteristik Visual**: Dropdown kategori (misal: "Semua", "Artikel", "Produk") disatukan di dalam border input pencarian di sisi kiri.

---

## 2. Standar Aksesibilitas & Performa Search (UX Rules)
1. **Debounce Input**: Untuk pencarian yang memanggil API eksternal, wajib gunakan *debounce* (minimal 250ms-300ms) agar tidak membanjiri server dengan request di setiap huruf yang diketik.
2. **Keyboard Roving Focus**: Pengguna harus bisa menjelajahi daftar hasil pencarian menggunakan tombol panah tanpa kehilangan fokus pada input teks.
3. **Empty / No Results State**: Tampilkan teks dan ilustrasi yang jelas ("Tidak ada hasil untuk kata kunci '...'") jika query tidak menghasilkan data, bukan sekadar membiarkan layar kosong.

---

## 3. Blueprint Kode Master (The Modern Spotlight Command Menu)

Blueprint modal pencarian global ala macOS Spotlight / Linear menggunakan React dan Framer Motion:

```tsx
import { useState, useEffect } from "react";
import { Search, Command, FileText, Settings, ArrowRight, X } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface SearchItem {
  id: string;
  title: string;
  category: "Pages" | "Actions";
  icon: any;
}

const ITEMS: SearchItem[] = [
  { id: "1", title: "Overview Dashboard", category: "Pages", icon: FileText },
  { id: "2", title: "Analytics & Reports", category: "Pages", icon: FileText },
  { id: "3", title: "User Account Settings", category: "Pages", icon: Settings },
  { id: "4", title: "Create New Project", category: "Actions", icon: ArrowRight },
  { id: "5", title: "Switch Dark / Light Mode", category: "Actions", icon: ArrowRight },
];

export function SpotlightSearchModal() {
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [selectedIndex, setSelectedIndex] = useState(0);

  // Toggle dengan tombol keyboard (⌘K atau Ctrl+K)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault();
        setIsOpen((prev) => !prev);
      }
      if (e.key === "Escape") {
        setIsOpen(false);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  const filteredItems = ITEMS.filter((item) =>
    item.title.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <>
      {/* Trigger Button di Navbar */}
      <button
        onClick={() => setIsOpen(true)}
        className="flex items-center gap-3 px-3.5 py-2 rounded-xl border border-slate-800 bg-slate-900/50 hover:bg-slate-800/80 text-slate-400 hover:text-slate-200 text-xs transition-colors focus:outline-none"
      >
        <Search className="w-3.5 h-3.5" />
        <span>Cari apa saja...</span>
        <kbd className="ml-4 px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 font-mono text-[10px] text-slate-400">
          ⌘K
        </kbd>
      </button>

      {/* Modal Dialog */}
      <AnimatePresence>
        {isOpen && (
          <div className="fixed inset-0 z-50 flex items-start justify-center pt-24 px-4">
            
            {/* Backdrop Blur */}
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setIsOpen(false)}
              className="fixed inset-0 bg-black/60 backdrop-blur-sm"
            />

            {/* Search Card */}
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: -20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: -20 }}
              transition={{ duration: 0.2, ease: "easeOut" }}
              className="relative w-full max-w-xl rounded-2xl border border-slate-800 bg-slate-900 shadow-2xl overflow-hidden z-10"
            >
              {/* Input Header */}
              <div className="flex items-center gap-3 px-4 py-3.5 border-b border-slate-800">
                <Search className="w-5 h-5 text-slate-400" />
                <input
                  type="text"
                  autoFocus
                  placeholder="Ketik perintah atau cari dokumen..."
                  value={query}
                  onChange={(e) => {
                    setQuery(e.target.value);
                    setSelectedIndex(0);
                  }}
                  className="flex-1 bg-transparent text-sm text-slate-200 placeholder-slate-500 outline-none"
                />
                <button
                  onClick={() => setIsOpen(false)}
                  className="p-1 rounded-md text-slate-500 hover:text-slate-300 hover:bg-slate-800 transition-colors"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>

              {/* Search Results List */}
              <div className="max-h-80 overflow-y-auto p-2 space-y-1 no-scrollbar">
                {filteredItems.length === 0 ? (
                  <div className="py-12 text-center text-xs text-slate-500">
                    Tidak ada hasil yang cocok dengan "{query}".
                  </div>
                ) : (
                  filteredItems.map((item, idx) => {
                    const Icon = item.icon;
                    const isSelected = selectedIndex === idx;
                    return (
                      <div
                        key={item.id}
                        onClick={() => {
                          console.log("Selected:", item.title);
                          setIsOpen(false);
                        }}
                        onMouseEnter={() => setSelectedIndex(idx)}
                        className={`flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-medium cursor-pointer transition-colors ${
                          isSelected
                            ? "bg-indigo-600 text-white"
                            : "text-slate-300 hover:bg-slate-800/60"
                        }`}
                      >
                        <div className="flex items-center gap-3">
                          <Icon className={`w-4 h-4 ${isSelected ? "text-white" : "text-slate-400"}`} />
                          <span>{item.title}</span>
                        </div>
                        <span className={`text-[10px] uppercase font-mono px-2 py-0.5 rounded ${
                          isSelected ? "bg-indigo-700 text-white" : "bg-slate-800 text-slate-400"
                        }`}>
                          {item.category}
                        </span>
                      </div>
                    );
                  })
                )}
              </div>

              {/* Footer Helper */}
              <div className="px-4 py-2 bg-slate-950/60 border-t border-slate-800 flex items-center justify-between text-[11px] text-slate-500 font-mono">
                <div className="flex items-center gap-3">
                  <span>↑↓ Navigasi</span>
                  <span>↵ Pilih</span>
                </div>
                <span>ESC Tutup</span>
              </div>

            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </>
  );
}
```
