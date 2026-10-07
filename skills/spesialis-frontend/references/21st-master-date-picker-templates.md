# 21st.dev Master Date Picker Templates

Analisis pola dan blueprint komponen Date Picker berdasarkan 72+ komponen kalender modern di 21st.dev (React + Tailwind v4 + React Day Picker / Radix UI).

---

## 1. Lima Arketipe Date Picker Modern

### Arketipe 1: The Popover Single Date Picker
- **Fungsi**: Memilih satu tanggal tunggal (misal: Tanggal Lahir, Tanggal Tenggat Waktu).
- **Karakteristik Visual**:
  - Tampilan awal bukan kolom ketik, melainkan tombol (*Button Trigger*) berikon kalender dengan teks "Pilih tanggal...".
  - Saat diklik, muncul *Popover* berisi kalender bulan berjalan. Hari ini ditandai tebal/berwarna beda, dan tanggal terpilih diberi latar belakang pekat (misal Indigo-600).
- **Inspirasi**: `Calendar Date Picker (shadcn)`, `Input Date Range (Origin UI)`.

### Arketipe 2: The Dual-Month Date Range Picker
- **Fungsi**: Memilih rentang waktu (misal: *Check-in* & *Check-out* Hotel, Filter Laporan Transaksi).
- **Karakteristik Visual**:
  - Menampilkan dua bulan sekaligus secara berdampingan (kiri dan kanan).
  - Saat pengguna memilih dua titik tanggal, ruang di antara kedua tanggal tersebut diarsir dengan warna latar belakang lembut (misal: `bg-indigo-500/20`), menghubungkan tanggal awal dan akhir.
- **Inspirasi**: `DateRangePicker (Hero Ui)`, `Dropdown Range Date Picker (Ruixen)`.

### Arketipe 3: The Quick Preset / Chrono Select
- **Fungsi**: Mempercepat pekerjaan analitik dengan opsi waktu instan.
- **Karakteristik Visual**:
  - Menu sebelah kiri (atau tombol *chip* di atas) berisi tombol cepat: "Hari Ini", "7 Hari Terakhir", "Bulan Ini", "Tahun Ini".
  - Jika pengguna butuh waktu spesifik, kalender kustom tetap tersedia di sebelahnya.
- **Inspirasi**: `ChronoSelect (Ruixen)`.

### Arketipe 4: The Datetime Picker (Date + Time)
- **Fungsi**: Menjadwalkan pengiriman email, reservasi rapat, atau tiket penerbangan.
- **Karakteristik Visual**: Di bagian bawah atau sisi kanan kalender terdapat *input spinner* atau menu gulir (*wheel*) khusus untuk Jam (00-23) dan Menit (00-59).

### Arketipe 5: The iOS-style Date Wheel Picker
- **Fungsi**: Input tanggal ramah *mobile-first*.
- **Karakteristik Visual**: Tabung berputar 3D memanjang secara vertikal yang menampilkan Hari, Bulan, dan Tahun (menggunakan logika *Scroll Snap* CSS).

---

## 2. Blueprint Kode Master (The Popover Single Date Picker)

*Catatan: Blueprint ini mensimulasikan integrasi visual Popover Date Picker. Di dunia nyata, ini biasanya digerakkan oleh pustaka `react-day-picker` dan `date-fns`.*

```tsx
import { useState, useRef, useEffect } from "react";
import { Calendar as CalendarIcon, ChevronLeft, ChevronRight } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export function ModernDatePicker() {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedDate, setSelectedDate] = useState<number | null>(15); // Simulasi tgl 15 terpilih
  const pickerRef = useRef<HTMLDivElement>(null);

  // Auto-close ketika klik di luar komponen
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (pickerRef.current && !pickerRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // Simulasi array bulan (Kosong untuk padding + 31 Hari)
  const daysInMonth = Array.from({ length: 31 }, (_, i) => i + 1);
  const emptyDays = [0, 0, 0]; // Mulai hari Kamis (simulasi)

  return (
    <div className="relative inline-block w-full max-w-xs" ref={pickerRef}>
      
      {/* Date Input Trigger */}
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className={`w-full flex items-center gap-2 px-3 py-2.5 rounded-xl border transition-colors text-sm font-medium ${
          selectedDate 
            ? "border-slate-700 bg-slate-900 text-white" 
            : "border-slate-800 bg-slate-900/60 text-slate-400 hover:bg-slate-800"
        }`}
      >
        <CalendarIcon className={`w-4 h-4 ${selectedDate ? "text-indigo-400" : "text-slate-500"}`} />
        <span>{selectedDate ? `${selectedDate} Oktober 2026` : "Pilih tanggal..."}</span>
      </button>

      {/* Calendar Popover */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 5 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 5 }}
            transition={{ duration: 0.15, ease: "easeOut" }}
            className="absolute left-0 top-full mt-2 p-4 w-[280px] rounded-2xl border border-slate-800 bg-slate-900 shadow-2xl backdrop-blur-xl z-50"
          >
            {/* Calendar Header */}
            <div className="flex items-center justify-between mb-4">
              <button className="p-1 rounded-lg hover:bg-slate-800 text-slate-400 transition-colors">
                <ChevronLeft className="w-4 h-4" />
              </button>
              <h4 className="text-sm font-bold text-white">Oktober 2026</h4>
              <button className="p-1 rounded-lg hover:bg-slate-800 text-slate-400 transition-colors">
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>

            {/* Weekdays Row */}
            <div className="grid grid-cols-7 gap-1 mb-2 text-center">
              {["Sn", "Sl", "Rb", "Km", "Jm", "Sb", "Mg"].map((day) => (
                <div key={day} className="text-[10px] font-mono font-medium text-slate-500">
                  {day}
                </div>
              ))}
            </div>

            {/* Days Grid */}
            <div className="grid grid-cols-7 gap-1">
              {emptyDays.map((_, i) => (
                <div key={`empty-${i}`} className="w-8 h-8" />
              ))}
              
              {daysInMonth.map((day) => {
                const isSelected = selectedDate === day;
                const isToday = day === 8; // Simulasi hari ini

                return (
                  <button
                    key={day}
                    onClick={() => {
                      setSelectedDate(day);
                      setIsOpen(false); // Tutup otomatis saat dipilih
                    }}
                    className={`flex items-center justify-center w-8 h-8 rounded-lg text-xs font-medium transition-all ${
                      isSelected
                        ? "bg-indigo-600 text-white shadow-md shadow-indigo-500/20"
                        : isToday
                        ? "bg-slate-800 text-indigo-300 ring-1 ring-indigo-500/50"
                        : "text-slate-300 hover:bg-slate-800 hover:text-white"
                    }`}
                  >
                    {day}
                  </button>
                );
              })}
            </div>
          </motion.div>
        )}
      </AnimatePresence>

    </div>
  );
}
```

---

## 3. Aturan Desain Komponen Tanggal (Best Practices)
1. **Jangan Gunakan Input String Manual (`type="text"`)**: Input manual mewajibkan pengguna menebak format Anda (DD/MM/YYYY atau MM/DD/YYYY). Selalu gunakan tombol kalender visual untuk mencegah kesalahan validasi API.
2. **Kesesuaian Lokalisasi (i18n)**: Berikan perhatian ekstra pada label hari (Senin mulai duluan di Eropa/Asia, Minggu mulai duluan di US) melalui konfigurasi bahasa kalender (seperti locale `id-ID` dari `date-fns`).
3. **Peringatan Aksesibilitas Popover**: Popover kalender harus dapat dinavigasi sepenuhnya menggunakan tombol `Panah Keyboard` tanpa harus mengklik sel kalender secara manual menggunakan mouse.
