# 21st.dev Master Charts & Data Viz Templates

Analisis pola dan blueprint komponen Visualisasi Data (Charts) berdasarkan 246+ komponen di 21st.dev (React + Tailwind v4 + Recharts / Visx).

---

## 1. Empat Arketipe Visualisasi Data Modern

### Arketipe 1: The Area Chart Analytics (SaaS Standard)
- **Fungsi**: Visualisasi pendapatan bulanan (MRR) atau lalu lintas pengunjung (*traffic*) di halaman utama dashboard.
- **Karakteristik Visual**:
  - Garis kurva menggunakan tipe "Monotone" agar mulus (tidak kaku bergerigi).
  - Latar di bawah kurva diberi warna gradien yang memudar ke transparan di dasar sumbu X (`fillOpacity="1" fill="url(#colorUv)"`).
  - Sumbu Y sering disembunyikan (*grid horizontal saja*) untuk kesan lebih bersih.
  - Memiliki *Custom Tooltip* gelap (*dark card*) yang muncul saat kursor melintasi titik data.
- **Inspirasi**: `Area Chart Analytics Card`, `Line Charts (shadcn)`.

### Arketipe 2: The Micro-Sparkline
- **Fungsi**: Disematkan di dalam *Metric Card* kecil atau tabel untuk sekadar memberikan gambaran tren naik/turun sekilas.
- **Karakteristik Visual**:
  - Grafik garis atau batang sangat mungil (`h-12 w-24`).
  - Tidak memiliki label sumbu X/Y, tidak memiliki grid, dan tidak memiliki tooltip. Murni elemen dekoratif penunjuk arah (*Trendline*).
- **Inspirasi**: `Sparkline Chart`.

### Arketipe 3: The Activity Heatmap (GitHub Contribution Style)
- **Fungsi**: Melacak konsistensi aktivitas harian pengguna selama satu tahun.
- **Karakteristik Visual**:
  - Grid kotak-kotak kecil di mana opasitas warna kotak (misal: Indigo) semakin pekat seiring tingginya jumlah aktivitas pada hari tersebut.
- **Inspirasi**: `GitHub calendar (Ali Imam)`, `Monthly Heatmap Calendar`.

### Arketipe 4: The Radial / Gauge Progress Chart
- **Fungsi**: Menunjukkan skor spesifik (misal: Skor Kesehatan Sistem, Skor SEO, atau Kuota Sisa).
- **Karakteristik Visual**:
  - Grafik berbentuk busur setengah lingkaran (*Speedometer*) atau cincin penuh bergaya donat. Teks angka diletakkan tepat di tengah lubang donat.
- **Inspirasi**: `Gauge Component`, `Radial Progress`.

---

## 2. Blueprint Kode Master (The Modern Area Chart dengan Recharts)

*Catatan: Contoh ini menggunakan logika dasar komponen Recharts (`recharts` npm package) yang merupakan standar industri de-facto untuk visualisasi React ringan.*

```tsx
import { Area, AreaChart, ResponsiveContainer, Tooltip, XAxis, YAxis, CartesianGrid } from "recharts";

const DATA = [
  { month: "Jan", revenue: 4000, expenses: 2400 },
  { month: "Feb", revenue: 3000, expenses: 1398 },
  { month: "Mar", revenue: 2000, expenses: 9800 },
  { month: "Apr", revenue: 2780, expenses: 3908 },
  { month: "Mei", revenue: 1890, expenses: 4800 },
  { month: "Jun", revenue: 2390, expenses: 3800 },
  { month: "Jul", revenue: 3490, expenses: 4300 },
];

// Kustom Tooltip untuk menggantikan tooltip standar putih yang jelek
const CustomTooltip = ({ active, payload, label }: any) => {
  if (active && payload && payload.length) {
    return (
      <div className="p-3 rounded-xl border border-slate-800 bg-slate-900/90 shadow-2xl backdrop-blur-md">
        <p className="text-xs font-semibold text-slate-400 mb-2">{label} 2026</p>
        <div className="space-y-1.5">
          <div className="flex items-center gap-4 justify-between text-sm">
            <span className="flex items-center gap-1.5 text-slate-300">
              <div className="w-2 h-2 rounded-full bg-indigo-500" />
              Pendapatan
            </span>
            <span className="font-mono font-bold text-white">
              Rp {payload[0].value.toLocaleString()}
            </span>
          </div>
          {payload[1] && (
            <div className="flex items-center gap-4 justify-between text-sm">
              <span className="flex items-center gap-1.5 text-slate-300">
                <div className="w-2 h-2 rounded-full bg-rose-500" />
                Pengeluaran
              </span>
              <span className="font-mono font-bold text-white">
                Rp {payload[1].value.toLocaleString()}
              </span>
            </div>
          )}
        </div>
      </div>
    );
  }
  return null;
};

export function AnalyticsAreaChart() {
  return (
    <div className="w-full h-full min-h-[300px] p-6 rounded-2xl border border-slate-800 bg-slate-900/40">
      <div className="mb-6">
        <h3 className="text-sm font-bold text-white">Laporan Keuangan Kuartal 2</h3>
        <p className="text-xs text-slate-400 mt-1">Perbandingan tren pendapatan dan pengeluaran operasional bulanan.</p>
      </div>

      <div className="h-[250px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={DATA} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
            {/* SVG Defs untuk Gradien Latar */}
            <defs>
              <linearGradient id="colorRevenue" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#6366f1" stopOpacity={0.3} />
                <stop offset="95%" stopColor="#6366f1" stopOpacity={0} />
              </linearGradient>
              <linearGradient id="colorExpense" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#f43f5e" stopOpacity={0.3} />
                <stop offset="95%" stopColor="#f43f5e" stopOpacity={0} />
              </linearGradient>
            </defs>

            {/* Sumbu X & Y */}
            <XAxis 
              dataKey="month" 
              axisLine={false} 
              tickLine={false} 
              tick={{ fontSize: 11, fill: "#64748b" }} 
              dy={10} 
            />
            <YAxis 
              axisLine={false} 
              tickLine={false} 
              tick={{ fontSize: 11, fill: "#64748b" }} 
              tickFormatter={(value) => `${value / 1000}k`}
            />

            {/* Grid Latar Belakang (Hanya Garis Horizontal) */}
            <CartesianGrid vertical={false} stroke="#1e293b" strokeDasharray="4 4" />

            {/* Kustom Interaksi Hover */}
            <Tooltip content={<CustomTooltip />} cursor={{ stroke: '#334155', strokeWidth: 1, strokeDasharray: '4 4' }} />

            {/* Data Garis & Area (Expenses / Pengeluaran) */}
            <Area
              type="monotone"
              dataKey="expenses"
              stroke="#f43f5e"
              strokeWidth={2}
              fillOpacity={1}
              fill="url(#colorExpense)"
            />

            {/* Data Garis & Area (Revenue / Pendapatan) */}
            <Area
              type="monotone"
              dataKey="revenue"
              stroke="#6366f1"
              strokeWidth={2}
              fillOpacity={1}
              fill="url(#colorRevenue)"
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
```

---

## 3. Aturan Desain Visualisasi Data
1. **Bersihkan Chart Junk**: Hindari garis pembatas yang tebal pada sumbu (*Axis line*) dan matikan garis grid vertikal (`vertical={false}`). Biarkan data bernapas. Gunakan garis putus-putus samar untuk grid horizontal saja.
2. **Kustom Tooltip Wajib**: Tooltip bawaan sebagian besar library *chart* merusak tema *Dark Mode* karena memaksa kotak berlatar belakang putih terang. Selalu buat fungsi `CustomTooltip` (seperti di atas) yang di-styling dengan Tailwind agar menyatu dengan antarmuka Anda.
3. **Format Angka Presisi**: Jangan tampilkan angka `4000` di sumbu Y jika bisa diformat menjadi `4k` atau `4.0M`. Manfaatkan properti `tickFormatter` untuk menghemat ruang margin di sisi kiri grafik.
