# 21st.dev Master Popover Templates

Analisis pola dan blueprint komponen Popover berdasarkan 179+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion / Radix UI).

---

## 1. Empat Arketipe Popover Modern

### Arketipe 1: The Tour / Onboarding Beacon Popover (Feature Discovery)
- **Fungsi**: Memandu pengguna baru saat pertama kali menggunakan dashboard (Guided Product Tour).
- **Karakteristik Visual**:
  - Memiliki panah penunjuk (*caret/arrow*) yang menempel tepat ke elemen yang sedang dijelaskan.
  - Memuat hitungan tahapan ("Langkah 2 dari 4") dan tombol aksi navigasi ("Kembali", "Lanjut", "Lewati").
- **Inspirasi**: `Tour Popover (Ruixen)`, `Tooltip-like Popover with steps (Origin UI)`.

### Arketipe 2: The Morphing Popover (Form / Quick Note)
- **Fungsi**: Menyediakan form kecil tanpa perlu membuka dialog modal penuh (misal: feedback instan, share link, catatan cepat).
- **Karakteristik Visual**:
  - Tombol pemicu "berubah wujud" (*morph*) secara elastis menjadi kartu popover lengkap dengan textarea dan tombol kirim menggunakan animasi *layoutId* (Framer Motion).
- **Inspirasi**: `Morphing Popover (Julien Thibeaut)`.

### Arketipe 3: The Calendar / Date Range Picker Popover
- **Fungsi**: Filter rentang tanggal pada tabel atau laporan analitik.
- **Karakteristik Visual**: Pemicu berupa tombol bertuliskan "Pilih Tanggal ▾", yang saat diklik memunculkan kalender 2 bulan berdampingan.

### Arketipe 4: The Contextual Action Popover (Share / Invite)
- **Fungsi**: Tindakan spesifik seperti membagikan tautan dokumen atau mengundang anggota tim.
- **Karakteristik Visual**: Memuat input tautan readonly dengan tombol "Salin Tautan" satu klik, dan daftar avatar pengguna yang sudah memiliki akses.

---

## 2. Standar Aksesibilitas Popover (WAI-ARIA Dialog Pattern)
Popover berbeda dengan Tooltip karena **Popover bersifat interaktif** (bisa berisi form, tombol, dan link).
1. **Fokus Trap (Focus Management)**: Saat popover terbuka, fokus keyboard pertama kali harus jatuh ke elemen interaktif pertama di dalam popover (misal tombol tutup atau input pertama).
2. **Escape to Dismiss**: Menekan tombol `Escape` wajib menutup popover dan mengembalikan fokus kursor ke tombol pemicu semula.
3. **Klik Luar (Outside Click / Dismissal)**: Klik di luar area popover harus menutup popover secara otomatis.

---

## 3. Blueprint Kode Master (The Tour / Feature Discovery Popover)

```tsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Sparkles, ArrowRight, X } from "lucide-react";

export function TourPopover({ children }: { children: React.ReactNode }) {
  const [isOpen, setIsOpen] = useState(true);
  const [step, setStep] = useState(1);
  const totalSteps = 3;

  return (
    <div className="relative inline-block">
      {/* Target Element yang Diberi Sorotan */}
      <div className={isOpen ? "ring-2 ring-indigo-500 rounded-xl p-0.5" : ""}>
        {children}
      </div>

      {/* Popover Bubble */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, scale: 0.9, y: 8 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.9, y: 8 }}
            transition={{ type: "spring", stiffness: 400, damping: 25 }}
            className="absolute left-0 top-full mt-3 z-50 w-72 p-4 rounded-2xl border border-slate-800 bg-slate-900 shadow-2xl backdrop-blur-xl"
            role="dialog"
            aria-modal="true"
          >
            {/* Header: Badge & Close */}
            <div className="flex items-center justify-between mb-2">
              <span className="inline-flex items-center gap-1 text-[10px] font-mono font-medium px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
                <Sparkles className="w-3 h-3" />
                Fitur Baru
              </span>
              <button 
                onClick={() => setIsOpen(false)}
                className="p-1 rounded-md text-slate-500 hover:text-slate-300 hover:bg-slate-800 transition-colors"
                aria-label="Tutup tur"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            </div>

            {/* Content */}
            <h4 className="text-xs font-bold text-white">Filter Multi-Dimensi</h4>
            <p className="text-[11px] text-slate-400 mt-1 leading-relaxed">
              Sekarang Anda dapat menggabungkan filter tanggal, status, dan kategori secara bersamaan di sini.
            </p>

            {/* Footer Navigation */}
            <div className="mt-4 pt-3 border-t border-slate-800 flex items-center justify-between">
              <span className="text-[10px] font-mono text-slate-500">
                {step} dari {totalSteps}
              </span>

              <div className="flex items-center gap-2">
                {step < totalSteps ? (
                  <button
                    onClick={() => setStep(step + 1)}
                    className="flex items-center gap-1 px-3 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold transition-colors"
                  >
                    <span>Lanjut</span>
                    <ArrowRight className="w-3 h-3" />
                  </button>
                ) : (
                  <button
                    onClick={() => setIsOpen(false)}
                    className="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold transition-colors"
                  >
                    Selesai
                  </button>
                )}
              </div>
            </div>

            {/* Caret / Arrow Menunjuk ke Atas */}
            <div className="absolute -top-1.5 left-6 w-3 h-3 rotate-45 border-t border-l border-slate-800 bg-slate-900" />

          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
```

---

## 3. Checklist UX Popover
1. **Popover vs Tooltip**: Jangan gunakan Popover untuk teks penjelasan 1 baris (gunakan Tooltip). Popover dikhususkan bila ada interaksi klik, form, atau konten multi-baris dengan navigasi.
2. **Posisi Pintar (Collision Detection)**: Jika diletakkan di pojok kanan layar, popover harus otomatis menyejajarkan diri ke kanan (`right-0`) agar tidak meluber keluar dari batas browser (*viewport clipping*).
3. **Penyimpanan State**: Untuk *Product Tour Popover*, selalu simpan status penyelesaian di `localStorage` agar pengguna tidak terganggu oleh tour yang muncul berulang kali setiap me-refresh halaman.
