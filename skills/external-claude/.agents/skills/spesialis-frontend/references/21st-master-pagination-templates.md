# 21st.dev Master Pagination Templates

Analisis pola dan blueprint komponen Pagination berdasarkan 22+ komponen modern di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Pagination Modern

### Arketipe 1: The Classic Numbered Rail (B2B & Tables)
- **Fungsi**: Standar industri untuk tabel data besar, *dashboard* admin, atau direktori pencarian.
- **Karakteristik Visual**:
  - Tombol "Previous" dan "Next" di kedua ujung dengan ikon Chevron (`<` dan `>`).
  - Deretan angka halaman yang aktif ditekankan dengan *background* warna primer (misal: Indigo-500) dan teks putih tebal.
  - Terdapat Elipsis (`...`) jika jumlah halaman terlalu banyak (contoh: `1, 2, 3, ..., 99, 100`).
- **Inspirasi**: Shadcn UI Default Pagination.

### Arketipe 2: The Animated Sliding Pill Pagination
- **Fungsi**: Digunakan di *landing page* atau galeri produk yang menitikberatkan interaksi visual (SaaS/B2C).
- **Karakteristik Visual**:
  - Mirip dengan *Tabs*, kotak *background* aktif (pill) bergerak meluncur dari angka 1 ke angka 2 menggunakan animasi elastis murni (Framer Motion `layoutId`).
- **Inspirasi**: Animated Navigation Tabs.

### Arketipe 3: The Minimalist Pager (Next/Prev Only)
- **Fungsi**: Blog post (*infinite scroll fallback*) atau formulir wizard multi-step.
- **Karakteristik Visual**:
  - Hanya terdiri dari dua tombol ("← Halaman Sebelumnya" dan "Halaman Berikutnya →") tanpa deretan angka rumit di tengah. Sering disandingkan dengan indikator teks kecil ("Halaman 4 dari 12").

### Arketipe 4: The Mobile-First Dot Pagination
- **Fungsi**: Carousel geser (Swipeable Card) atau proses *onboarding mobile*.
- **Karakteristik Visual**: Titik-titik bundar kecil di bagian bawah. Titik yang aktif memanjang seperti pil (*capsule width morphing*).

---

## 2. Standar Aksesibilitas Pagination (WAI-ARIA)
1. **Pembungkus Navigasi**: Gunakan tag HTML semantik `<nav aria-label="Pagination">`.
2. **Penunjuk Status Aktif**: Pada angka yang sedang aktif, wajib sisipkan `aria-current="page"`.
3. **Label Tombol Bebas Teks**: Jika tombol Previous/Next hanya berupa ikon `<` dan `>`, wajib tambahkan atribut `aria-label="Previous page"` dan `aria-label="Next page"` agar dimengerti pembaca layar (Screen Reader).
4. **State Nonaktif (Disabled)**: Jika pengguna berada di halaman 1, tombol "Previous" harus benar-benar dinonaktifkan dengan atribut `disabled` dan CSS `opacity-50 cursor-not-allowed`.

---

## 3. Blueprint Kode Master (The Modern Sliding Pagination)

```tsx
import { useState } from "react";
import { motion } from "framer-motion";
import { ChevronLeft, ChevronRight, MoreHorizontal } from "lucide-react";

export function ModernPagination({ totalPages = 10, initialPage = 1 }) {
  const [activePage, setActivePage] = useState(initialPage);

  // Simulasi logika Elipsis Sederhana (Contoh: Tampil 1, 2, 3, ..., 10)
  const renderPages = () => {
    const pages = [];
    for (let i = 1; i <= totalPages; i++) {
      if (i <= 3 || i === totalPages || (i >= activePage - 1 && i <= activePage + 1)) {
        pages.push(
          <button
            key={i}
            onClick={() => setActivePage(i)}
            aria-current={activePage === i ? "page" : undefined}
            className={`relative flex items-center justify-center w-8 h-8 rounded-lg text-sm font-medium transition-colors ${
              activePage === i ? "text-white" : "text-slate-400 hover:text-slate-100"
            }`}
          >
            {activePage === i && (
              <motion.div
                layoutId="activePaginationIndicator"
                className="absolute inset-0 bg-indigo-500 rounded-lg -z-10"
                transition={{ type: "spring", stiffness: 400, damping: 30 }}
              />
            )}
            {i}
          </button>
        );
      } else if (pages[pages.length - 1]?.key !== `ellipsis-${i}`) {
        // Mencegah cetak ellipsis berulang
        if (i === 4 && activePage > 4) {
          pages.push(
            <div key={`ellipsis-start`} className="flex items-center justify-center w-8 h-8">
              <MoreHorizontal className="w-4 h-4 text-slate-600" />
            </div>
          );
        } else if (i === totalPages - 1 && activePage < totalPages - 3) {
          pages.push(
            <div key={`ellipsis-end`} className="flex items-center justify-center w-8 h-8">
              <MoreHorizontal className="w-4 h-4 text-slate-600" />
            </div>
          );
        }
      }
    }
    return pages;
  };

  return (
    <nav aria-label="Pagination" className="flex items-center gap-1 p-2 rounded-xl border border-slate-800 bg-slate-900/60 w-fit">
      {/* Previous Button */}
      <button
        onClick={() => setActivePage((p) => Math.max(1, p - 1))}
        disabled={activePage === 1}
        aria-label="Halaman Sebelumnya"
        className="flex items-center justify-center w-8 h-8 rounded-lg text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition-colors disabled:opacity-30 disabled:cursor-not-allowed"
      >
        <ChevronLeft className="w-4 h-4" />
      </button>

      {/* Number Rails */}
      <div className="flex items-center gap-1 mx-2">
        {renderPages()}
      </div>

      {/* Next Button */}
      <button
        onClick={() => setActivePage((p) => Math.min(totalPages, p + 1))}
        disabled={activePage === totalPages}
        aria-label="Halaman Berikutnya"
        className="flex items-center justify-center w-8 h-8 rounded-lg text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition-colors disabled:opacity-30 disabled:cursor-not-allowed"
      >
        <ChevronRight className="w-4 h-4" />
      </button>
    </nav>
  );
}
```

---

## 4. Checklist UX Pagination Ekstra
1. **Area Sentuh (Touch Target)**: Karena Pagination sering diakses via *mobile*, pastikan setiap angka dan ikon `<`/`>` dibungkus kontainer minimal `w-8 h-8` (32x32 piksel), walau teks di dalamnya kecil.
2. **Keyboard Shortcut**: Untuk aplikasi B2B tingkat lanjut, ikat tombol arah keyboard (Panah Kiri / Kanan) untuk berpindah halaman bila pengguna sedang memegang fokus di area tabel/pagination.
