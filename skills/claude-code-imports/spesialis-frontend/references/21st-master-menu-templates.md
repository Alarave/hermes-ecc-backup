# 21st.dev Master Menu & Context Menu Templates

Analisis pola dan blueprint komponen Menu berdasarkan 59+ komponen modern di 21st.dev (React + Tailwind v4 + Framer Motion / Radix UI).

---

## 1. Empat Arketipe Menu Modern

### Arketipe 1: The Context Menu (Right-Click Menu)
- **Fungsi**: Menu klik kanan pada area kanvas kerja, baris tabel, atau item file explorer.
- **Karakteristik Visual**:
  - Muncul tepat di posisi koordinat pointer mouse saat pengguna mengklik kanan (`x` dan `y`).
  - Memuat aksi spesifik file: "Salin", "Duplikat", "Buka di Tab Baru", dan aksi destruktif "Hapus" berwarna merah di bagian bawah.
  - Memuat teks pintasan keyboard di sebelah kanan (`⌘C`, `⌘D`, `Del`).
- **Inspirasi**: Radix UI Context Menu.

### Arketipe 2: The Kebab / 3-Dots Action Menu (Table Rows)
- **Fungsi**: Titik masuk menu aksi sekunder pada kartu atau baris tabel data (`MoreVertical` atau `MoreHorizontal`).
- **Karakteristik Visual**:
  - Tombol bulat kecil transparan. Saat ditekan, dropdown ringkas muncul ke arah bawah atau atas.
  - Item dikelompokkan dengan garis pemisah tipis (`border-b border-slate-800`).
- **Inspirasi**: Shadcn UI Dropdown Menu.

### Arketipe 3: The Floating Radial / FAB Speed Dial Menu
- **Fungsi**: Aksi cepat pada aplikasi mobile atau aplikasi papan tulis / editor kanvas.
- **Karakteristik Visual**:
  - Tombol bulat utama di pojok kanan bawah. Saat ditekan, 3-5 sub-tombol mekar memancar keluar seperti busur lingkaran dengan animasi pegas (*spring physics*).

### Arketipe 4: The Mega Menu (Navigation Flyout)
- **Fungsi**: Menu navigasi utama di bilah header situs web produk atau SaaS besar (kategori Produk, Sumber Daya, Perusahaan).
- **Karakteristik Visual**:
  - Panel lebar (*full width* atau *bento layout*) dengan grid 2-3 kolom yang memuat ikon berwarna, judul tebal, deskripsi 1 baris, dan blok promo banner di sisi kanan.

---

## 2. Blueprint Kode Master (The 3-Dots Action Menu)

```tsx
import { useState, useRef, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { MoreVertical, Copy, ExternalLink, Archive, Trash2 } from "lucide-react";

export function TableRowActionMenu({ onAction }: { onAction?: (action: string) => void }) {
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

  // Menutup menu jika klik di luar area
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className="relative inline-block" ref={menuRef}>
      {/* 3-Dots Kebab Trigger */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Aksi baris"
        className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
      >
        <MoreVertical className="w-4 h-4" />
      </button>

      {/* Menu Panel */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: -4 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: -4 }}
            transition={{ duration: 0.12 }}
            role="menu"
            className="absolute right-0 top-full mt-1.5 w-48 p-1 rounded-xl border border-slate-800 bg-slate-900 shadow-2xl backdrop-blur-xl z-50 divide-y divide-slate-800/60"
          >
            {/* Group 1: General Actions */}
            <div className="p-1">
              <button
                onClick={() => { onAction?.("copy"); setIsOpen(false); }}
                role="menuitem"
                className="w-full flex items-center justify-between px-2.5 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition-colors"
              >
                <div className="flex items-center gap-2">
                  <Copy className="w-3.5 h-3.5 text-slate-400" />
                  <span>Salin ID</span>
                </div>
                <span className="text-[10px] font-mono text-slate-500">⌘C</span>
              </button>

              <button
                onClick={() => { onAction?.("open"); setIsOpen(false); }}
                role="menuitem"
                className="w-full flex items-center justify-between px-2.5 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition-colors"
              >
                <div className="flex items-center gap-2">
                  <ExternalLink className="w-3.5 h-3.5 text-slate-400" />
                  <span>Buka Detail</span>
                </div>
              </button>
            </div>

            {/* Group 2: Destructive / Danger Actions */}
            <div className="p-1">
              <button
                onClick={() => { onAction?.("archive"); setIsOpen(false); }}
                role="menuitem"
                className="w-full flex items-center gap-2 px-2.5 py-1.5 rounded-lg text-xs font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition-colors"
              >
                <Archive className="w-3.5 h-3.5 text-slate-400" />
                <span>Arsipkan</span>
              </button>

              <button
                onClick={() => { onAction?.("delete"); setIsOpen(false); }}
                role="menuitem"
                className="w-full flex items-center gap-2 px-2.5 py-1.5 rounded-lg text-xs font-medium text-rose-400 hover:text-rose-200 hover:bg-rose-500/10 transition-colors"
              >
                <Trash2 className="w-3.5 h-3.5" />
                <span>Hapus Permanen</span>
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

## 3. Checklist Aksesibilitas (WAI-ARIA Menu)
1. **Peran Semantik**: Kontainer luar wajib menggunakan `role="menu"` dan setiap opsi di dalamnya menggunakan `role="menuitem"`.
2. **Keyboard Roving Focus**: Pengguna harus dapat berpindah antar menu item hanya dengan menekan panah atas (`ArrowUp`) dan panah bawah (`ArrowDown`), serta memilih item dengan tombol `Enter`.
3. **Gaya Warna Destruktif**: Item yang bersifat menghapus data (*Delete / Purge*) harus selalu diletakkan di urutan paling bawah, dipisahkan oleh garis pembatas (*Divider*), dan menggunakan warna merah koral (`text-rose-400`) untuk mencegah kesalahan klik pengguna.
