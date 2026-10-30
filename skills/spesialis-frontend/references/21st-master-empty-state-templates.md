# 21st.dev Master Empty State & 404 Templates

Analisis pola dan blueprint komponen Empty State berdasarkan 77+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Empty State Modern

### Arketipe 1: The Dashboard "No Data" State
- **Fungsi**: Muncul di dalam ruang kosong sebuah tabel, folder proyek, atau daftar tugas saat belum ada data yang dibuat oleh pengguna.
- **Karakteristik Visual**:
  - Border bergaris putus-putus (*dashed border*) yang menyiratkan "ruang ini siap diisi".
  - Ikon besar berwarna pucat (abu-abu/slate) dengan judul yang jelas dan deskripsi persuasif.
  - Wajib menyertakan tombol aksi utama (CTA: "Buat Proyek Pertama").
- **Inspirasi**: `EmptyState - Beautiful, Accessible (Sonu kumar)`, `Invoice Empty State`.

### Arketipe 2: The "No Search Results" State
- **Fungsi**: Umpan balik ketika *query* pencarian pengguna tidak membuahkan hasil (di Command Palette atau bilah pencarian).
- **Karakteristik Visual**:
  - Ilustrasi kaca pembesar patah atau ikon wajah sedih.
  - Menampilkan kembali kata kunci yang diketik pengguna: *"Kami tidak dapat menemukan hasil untuk 'xyz' "*.
  - Memberikan opsi tombol "Hapus Pencarian".
- **Inspirasi**: `Empty Search (shadcn)`.

### Arketipe 3: The Interactive 404 Page Not Found
- **Fungsi**: Halaman penuh (*full-page*) saat rute URL tidak ditemukan.
- **Karakteristik Visual**:
  - Angka "404" besar bergaya distorsi (glitch) atau ditemani ilustrasi animasi melayang (misal: *ghost 404 page* dengan animasi naik turun).
  - Terdapat tombol utama "Kembali ke Beranda". Kadang menyisipkan tautan ringkas menuju pusat bantuan.
- **Inspirasi**: `ghost 404 page (Kain Xu)`, `Not Found Page (Efferd)`.

### Arketipe 4: The Offline / Error State
- **Fungsi**: Muncul ketika koneksi internet terputus atau server gagal merespons data API (bukan karena data tidak ada, tapi karena gagal dimuat).
- **Karakteristik Visual**:
  - Ikon colokan listrik tercabut, atau peringatan segitiga.
  - Menyertakan tombol "Coba Lagi" (*Retry*) dengan ikon putar (`RefreshCw`).
- **Inspirasi**: `Offline Empty State (Bundui.io)`, `Error Empty State (7ovr)`.

---

## 2. Blueprint Kode Master (The Interactive "No Data" Dashboard State)

```tsx
import { FolderX, Plus, ArrowRight } from "lucide-react";
import { motion } from "framer-motion";

export function DashboardEmptyState({ 
  onCreateNew 
}: { 
  onCreateNew?: () => void 
}) {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.3, ease: "easeOut" }}
      className="w-full max-w-2xl mx-auto p-12 flex flex-col items-center justify-center text-center rounded-3xl border-2 border-dashed border-slate-800 bg-slate-900/40"
    >
      {/* Icon Wrapper dengan Efek Pendar Latar (Glow) */}
      <div className="relative mb-6">
        <div className="absolute inset-0 bg-indigo-500/20 rounded-full blur-xl animate-pulse" />
        <div className="relative w-20 h-20 rounded-2xl bg-slate-800 border border-slate-700/60 shadow-inner flex items-center justify-center">
          <FolderX className="w-10 h-10 text-slate-400" />
        </div>
      </div>

      {/* Typography */}
      <h3 className="text-xl font-bold text-white mb-2">Belum ada proyek aktif</h3>
      <p className="text-sm text-slate-400 max-w-sm mb-8 leading-relaxed">
        Ruang kerja ini masih kosong. Mulai buat proyek pertama Anda atau integrasikan data dari repositori eksternal.
      </p>

      {/* Action Buttons */}
      <div className="flex flex-col sm:flex-row items-center gap-3">
        <button
          onClick={onCreateNew}
          className="flex items-center gap-2 px-6 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold transition-all shadow-lg shadow-indigo-600/20"
        >
          <Plus className="w-4 h-4" />
          <span>Buat Proyek Baru</span>
        </button>
        
        <button className="flex items-center gap-2 px-6 py-2.5 rounded-xl border border-slate-800 bg-transparent hover:bg-slate-800 text-slate-300 text-sm font-medium transition-colors">
          <span>Baca Panduan</span>
          <ArrowRight className="w-4 h-4" />
        </button>
      </div>

      {/* Subtle Hint */}
      <p className="mt-8 text-[11px] font-mono text-slate-500 uppercase tracking-widest">
        Atau tekan <kbd className="px-1.5 py-0.5 rounded bg-slate-800 text-slate-300 border border-slate-700 mx-1">C</kbd> untuk memulai cepat
      </p>
    </motion.div>
  );
}
```

---

## 3. Checklist UX Empty State (WAI-ARIA & Copywriting)
1. **Aturan "Berikan Solusi, Bukan Sekadar Masalah"**: Empty State yang baik tidak hanya berhenti di kata *"Tidak Ditemukan"*. Desain ini **wajib** menyertakan tombol pintas CTA yang menjadi solusi atas kekosongan tersebut (misal tombol *Upload* pada Empty State direktori file).
2. **Pola Gambar yang Terukur**: Jangan gunakan gambar raster (PNG/JPG) yang sangat besar. Gunakan Ikon SVG yang elegan (`lucide-react`) atau Lottie Animation agar cepat dimuat.
3. **Peran Semantik Region**: Pastikan wilayah kosong dalam tabel atau dashboard memiliki struktur *fallback* yang terbaca layar. Jika itu tabel, pastikan ada baris khusus `<td colSpan={10}>...</td>` yang memuat teks Empty State tersebut, agar *Screen Reader* mengidentifikasi tabel kosong dengan semantik yang valid.
