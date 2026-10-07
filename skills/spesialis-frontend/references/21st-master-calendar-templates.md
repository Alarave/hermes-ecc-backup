# 21st.dev Master Calendar & Scheduling Templates

Analisis pola dan blueprint komponen Calendar (Kalender Penuh & Penjadwalan) berdasarkan 239+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Calendar Modern

### Arketipe 1: The Full-Month Grid Scheduler (Google Calendar Style)
- **Fungsi**: Dasbor reservasi meja cafe, penjadwalan shift barista, atau manajemen agenda event.
- **Karakteristik Visual**:
  - Kisi 7 kolom x 5-6 baris dengan sel berukuran lapang (`min-h-[100px]`).
  - Setiap sel memuat nomor tanggal di pojok kanan atas dan chip event berwarna di dalamnya.
  - Event yang melintasi beberapa hari terbentang secara horizontal (`col-span-*`).
  - Tanggal di luar bulan aktif diredupkan (`opacity-30`).

### Arketipe 2: The Inline Mini Calendar (Sidebar Widget)
- **Fungsi**: Navigasi cepat di sidebar dasbor atau pemilih tanggal instan.
- **Karakteristik Visual**:
  - Grid 7 kolom padat (`w-7 h-7` per tanggal).
  - Hari ini ditandai cincin pendar (`ring-1 ring-indigo-500`).
  - Tanggal yang memiliki event memiliki titik kecil (*dot indicator*) di bawah angka tanggal.

### Arketipe 3: The Multi-Month Range Calendar (Booking & Reservasi)
- **Fungsi**: Pemilihan tanggal check-in/check-out atau periode sewa.
- **Karakteristik Visual**:
  - Dua bulan berdampingan dengan tombol navigasi panah sinkron.
  - Area rentang terpilih diarsir (`bg-indigo-500/15`). Tanggal awal dan akhir berlatar belakang pekat (`bg-indigo-600 text-white`).

### Arketipe 4: The Weekly Timeline / Agenda View
- **Fungsi**: Tampilan jadwal per jam untuk pemesanan slot waktu (misal: reservasi meja 14:00 - 16:00).
- **Karakteristik Visual**:
  - Sumbu Y: Jam operasional (08:00 - 22:00).
  - Sumbu X: 7 hari dalam seminggu.
  - Blok waktu terisi tampak sebagai kartu melayang dengan penanda status (Terkonfirmasi, Menunggu, Selesai).

---

## 2. Blueprint Kode Master (The Interactive Monthly Scheduler Grid)

```tsx
import { useState } from "react";
import { ChevronLeft, ChevronRight, Plus } from "lucide-react";

interface CalendarEvent {
  id: string;
  date: number; // hari dalam bulan
  title: string;
  time: string;
  category: "booking" | "shift" | "event";
}

const EVENTS: CalendarEvent[] = [
  { id: "e1", date: 5, title: "Reservasi VIP Meja 3", time: "14:00", category: "booking" },
  { id: "e2", date: 12, title: "Restock Biji Kopi", time: "09:00", category: "shift" },
  { id: "e3", date: 18, title: "Live Music Berlayar", time: "19:30", category: "event" },
  { id: "e4", date: 18, title: "Reservasi Meja 7", time: "20:00", category: "booking" },
  { id: "e5", date: 25, title: "Maintenance Mesin Espresso", time: "07:00", category: "shift" },
];

const categoryStyles = {
  booking: "bg-emerald-500/15 text-emerald-300 border-emerald-500/30",
  shift: "bg-amber-500/15 text-amber-300 border-amber-500/30",
  event: "bg-indigo-500/15 text-indigo-300 border-indigo-500/30",
};

export function FullMonthScheduler() {
  const [currentMonth, setCurrentMonth] = useState("Oktober 2026");
  const [selectedDay, setSelectedDay] = useState<number | null>(18);

  const daysInMonth = 31;
  const startDayOffset = 3; // Mulai hari Kamis (0=Senin, 6=Minggu)
  const totalSlots = Math.ceil((daysInMonth + startDayOffset) / 7) * 7;

  const weekdays = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"];

  return (
    <div className="w-full max-w-5xl mx-auto rounded-3xl border border-slate-800 bg-slate-900/80 backdrop-blur-xl shadow-2xl overflow-hidden">
      {/* Header Navigasi */}
      <div className="flex items-center justify-between p-6 border-b border-slate-800">
        <div>
          <h2 className="text-xl font-bold text-white tracking-tight">{currentMonth}</h2>
          <p className="text-xs text-slate-400 mt-0.5">Jadwal Operasional & Reservasi Berlayar Cafe</p>
        </div>

        <div className="flex items-center gap-3">
          <div className="flex items-center gap-1 rounded-xl border border-slate-800 bg-slate-950/60 p-1">
            <button
              aria-label="Bulan sebelumnya"
              className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <button
              onClick={() => setSelectedDay(8)}
              className="px-3 py-1 text-xs font-semibold text-slate-300 hover:text-white transition-colors"
            >
              Hari Ini
            </button>
            <button
              aria-label="Bulan berikutnya"
              className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>

          <button className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-lg shadow-indigo-600/20 transition-colors">
            <Plus className="w-3.5 h-3.5" />
            <span>Tambah Jadwal</span>
          </button>
        </div>
      </div>

      {/* Baris Nama Hari */}
      <div className="grid grid-cols-7 border-b border-slate-800 bg-slate-950/40 text-center">
        {weekdays.map((day) => (
          <div key={day} className="py-2.5 text-xs font-mono font-medium text-slate-400">
            {day}
          </div>
        ))}
      </div>

      {/* Grid Sel Kalender */}
      <div className="grid grid-cols-7 divide-x divide-y divide-slate-800/80 bg-slate-950/20">
        {Array.from({ length: totalSlots }).map((_, idx) => {
          const dayNumber = idx - startDayOffset + 1;
          const isCurrentMonth = dayNumber > 0 && dayNumber <= daysInMonth;
          const isToday = dayNumber === 8;
          const isSelected = selectedDay === dayNumber && isCurrentMonth;
          const dayEvents = isCurrentMonth ? EVENTS.filter((e) => e.date === dayNumber) : [];

          return (
            <div
              key={idx}
              onClick={() => isCurrentMonth && setSelectedDay(dayNumber)}
              className={`min-h-[105px] p-2 flex flex-col justify-between transition-colors select-none ${
                !isCurrentMonth
                  ? "bg-slate-950/40 text-slate-700 pointer-events-none"
                  : isSelected
                  ? "bg-indigo-500/5 cursor-pointer"
                  : "hover:bg-slate-800/30 cursor-pointer"
              }`}
            >
              {/* Tanggal Header Sel */}
              <div className="flex items-center justify-between">
                <span
                  className={`inline-flex items-center justify-center text-xs font-mono font-bold rounded-lg ${
                    isToday
                      ? "w-6 h-6 bg-indigo-600 text-white shadow-md shadow-indigo-500/30"
                      : isSelected
                      ? "text-indigo-400"
                      : isCurrentMonth
                      ? "text-slate-300"
                      : "text-slate-600"
                  }`}
                >
                  {isCurrentMonth ? dayNumber : ""}
                </span>

                {dayEvents.length > 2 && (
                  <span className="text-[10px] font-mono text-slate-500">
                    +{dayEvents.length - 2}
                  </span>
                )}
              </div>

              {/* Event Chips */}
              <div className="space-y-1 mt-1 flex-1 overflow-hidden">
                {dayEvents.slice(0, 2).map((ev) => (
                  <div
                    key={ev.id}
                    className={`truncate text-[10px] font-medium px-1.5 py-0.5 rounded-md border ${
                      categoryStyles[ev.category]
                    }`}
                    title={`${ev.time} - ${ev.title}`}
                  >
                    <span className="font-mono mr-1 opacity-75">{ev.time}</span>
                    {ev.title}
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
```

---

## 3. Checklist UX & Aksesibilitas Calendar
1. **Pemisahan Semantik Grid**: Kontainer hari wajib memakai `role="grid"`, baris minggu `role="row"`, dan tiap sel tanggal `role="gridcell"`.
2. **Keyboard Roving Focus**: Pengguna keyboard harus bisa berpindah hari dengan panah `ArrowLeft`/`ArrowRight`, lompat 1 minggu dengan `ArrowUp`/`ArrowDown`, dan memilih tanggal via `Enter`.
3. **Truncation & Overflow Safeguard**: Sel tanggal yang memuat lebih dari 2 event wajib membatasi tampilan (`slice(0, 2)`) dan menyertakan indikator `+N lainnya` untuk mencegah sel melar dan merusak ritme tinggi grid.
4. **i18n Locale Ready**: Urutan hari pertama (Senin vs Minggu) dan nama bulan harus dapat diinjeksi via konfigurasi locale peramban (`Intl.DateTimeFormat`), bukan teks hardcoded.
