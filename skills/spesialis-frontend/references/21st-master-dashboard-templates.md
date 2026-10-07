# 21st.dev Master Dashboard Layout & Shell Templates

Analisis pola dan blueprint komponen Dashboard (Antarmuka Admin & Analitik) berdasarkan 400+ tata letak dashboard di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Tiga Pilar Arsitektur Dashboard Modern

### Pilar 1: The Dashboard Shell (Cangkang Utama)
- **Fungsi**: Kerangka tata letak yang menampung seluruh konten aplikasi.
- **Karakteristik Visual**:
  - Memiliki *Sidebar* yang bisa dilipat (Collapsible Sidebar) di sisi kiri untuk navigasi modul.
  - Memiliki *Top Header* yang memuat *Breadcrumbs*, *Global Search / Command Palette*, dan Menu Profil/Notifikasi di kanan atas.
  - Area konten utama memiliki latar belakang sedikit lebih gelap (atau terang) dari sidebar untuk memberikan hierarki visual (contoh: Sidebar `bg-slate-950`, Konten `bg-slate-900`).
- **Inspirasi**: `Dashboard with Collapsible Sidebar (Sonu kumar)`.

### Pilar 2: The KPI Metric Cards (Stat Tiles)
- **Fungsi**: Baris paling atas dari area konten, memberikan ringkasan data sekilas (SaaS metrics).
- **Karakteristik Visual**:
  - Biasanya grid 3 atau 4 kolom (`grid-cols-1 md:grid-cols-4`).
  - Setiap kartu memuat Judul (misal: "Pendapatan"), Nilai Raksasa ("Rp 45.000.000"), dan Tren Persentase warna hijau/merah ("+12.5% bulan ini").
- **Inspirasi**: `Statistics Card 13`, `Stats cards with links`.

### Pilar 3: The Data Visualization Cards
- **Fungsi**: Penjabaran data mendalam melalui grafik dan tabel.
- **Karakteristik Visual**:
  - Memanfaatkan *Bento Grid* asimetris. Misal: Kolom kiri memakan 2 ruang (`col-span-2`) untuk *Area Chart*, sedangkan kolom kanan memakan 1 ruang (`col-span-1`) untuk daftar *Recent Activity*.
- **Inspirasi**: `Area Chart Analytics Card`, `Data Grid Table`.

---

## 2. Blueprint Kode Master (The Modern Dashboard Shell & Layout)

```tsx
import { useState } from "react";
import { 
  Home, BarChart3, Users, Settings, Search, 
  Bell, Menu, ArrowUpRight, ArrowDownRight,
  TrendingUp, CreditCard, Activity
} from "lucide-react";

// --- KOMPONEN: METRIC CARD ---
function MetricCard({ title, value, trend, isPositive, icon: Icon }: any) {
  return (
    <div className="p-5 rounded-2xl border border-slate-800 bg-slate-900/50 flex flex-col justify-between">
      <div className="flex justify-between items-start mb-4">
        <span className="text-xs font-semibold text-slate-400">{title}</span>
        <div className="p-2 rounded-lg bg-slate-800/80 text-indigo-400">
          <Icon className="w-4 h-4" />
        </div>
      </div>
      <div>
        <h3 className="text-2xl font-black text-white">{value}</h3>
        <div className="flex items-center gap-1 mt-2">
          {isPositive ? (
            <ArrowUpRight className="w-3.5 h-3.5 text-emerald-400" />
          ) : (
            <ArrowDownRight className="w-3.5 h-3.5 text-rose-400" />
          )}
          <span className={`text-[11px] font-mono font-medium ${isPositive ? "text-emerald-400" : "text-rose-400"}`}>
            {trend}
          </span>
          <span className="text-[11px] text-slate-500 ml-1">vs bulan lalu</span>
        </div>
      </div>
    </div>
  );
}

// --- KOMPONEN UTAMA: DASHBOARD SHELL ---
export function DashboardLayout() {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  return (
    <div className="min-h-screen bg-slate-950 flex text-slate-200 font-sans">
      
      {/* 1. SIDEBAR KIRI */}
      <aside 
        className={`${
          sidebarOpen ? "w-64" : "w-20"
        } transition-all duration-300 border-r border-slate-800 bg-slate-950 flex flex-col`}
      >
        <div className="h-16 flex items-center justify-between px-4 border-b border-slate-800">
          {sidebarOpen && <span className="font-bold text-white tracking-tight">Berlayar Cafe</span>}
          <button 
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <Menu className="w-5 h-5" />
          </button>
        </div>

        <nav className="flex-1 p-3 space-y-1">
          {[
            { name: "Overview", icon: Home, active: true },
            { name: "Analytics", icon: BarChart3 },
            { name: "Customers", icon: Users },
            { name: "Settings", icon: Settings },
          ].map((item) => (
            <button 
              key={item.name}
              className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-colors ${
                item.active 
                  ? "bg-indigo-500/10 text-indigo-400" 
                  : "text-slate-400 hover:text-white hover:bg-slate-800/50"
              }`}
            >
              <item.icon className="w-4 h-4 shrink-0" />
              {sidebarOpen && <span>{item.name}</span>}
            </button>
          ))}
        </nav>
      </aside>

      {/* 2. AREA KONTEN UTAMA */}
      <main className="flex-1 flex flex-col min-w-0 bg-[#0b0f19]">
        
        {/* HEADER ATAS */}
        <header className="h-16 flex items-center justify-between px-6 border-b border-slate-800 bg-slate-950/50 backdrop-blur-md sticky top-0 z-10">
          <div className="flex-1 max-w-md relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-500" />
            <input 
              type="text" 
              placeholder="Cari transaksi, laporan, atau menu..." 
              className="w-full pl-9 pr-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-sm text-white focus:outline-none focus:border-indigo-500 transition-colors"
            />
          </div>

          <div className="flex items-center gap-4">
            <button className="relative p-2 rounded-full text-slate-400 hover:text-white transition-colors">
              <Bell className="w-5 h-5" />
              <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-rose-500" />
            </button>
            <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-indigo-500 to-purple-500 border-2 border-slate-800" />
          </div>
        </header>

        {/* KONTEN HALAMAN */}
        <div className="p-6 md:p-8 overflow-y-auto">
          <div className="flex items-center justify-between mb-6">
            <h1 className="text-2xl font-bold text-white">Dashboard Analitik</h1>
            <button className="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold transition-colors">
              Unduh Laporan
            </button>
          </div>

          {/* Grid Metric Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <MetricCard title="Pendapatan Harian" value="Rp 4.520.000" trend="+12.5%" isPositive={true} icon={TrendingUp} />
            <MetricCard title="Total Transaksi" value="342" trend="+5.2%" isPositive={true} icon={CreditCard} />
            <MetricCard title="Waktu Rata-rata Pelayanan" value="4.2 mnt" trend="-1.5%" isPositive={false} icon={Activity} />
          </div>

          {/* Grid Konten Besar (Bento) */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            {/* Main Chart Card (col-span-2) */}
            <div className="lg:col-span-2 p-6 rounded-2xl border border-slate-800 bg-slate-900/50 h-[350px] flex flex-col justify-center items-center text-slate-500">
              <BarChart3 className="w-10 h-10 mb-2 opacity-50" />
              <p className="text-sm font-medium">Area Chart Komponen Ditempatkan Di Sini</p>
            </div>

            {/* Side List Card (col-span-1) */}
            <div className="lg:col-span-1 p-6 rounded-2xl border border-slate-800 bg-slate-900/50 h-[350px]">
              <h3 className="text-sm font-bold text-white mb-4">Transaksi Terakhir</h3>
              <div className="space-y-3">
                {[1, 2, 3, 4].map((i) => (
                  <div key={i} className="flex items-center justify-between p-3 rounded-xl bg-slate-800/40 border border-slate-700/50">
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400">
                        <CreditCard className="w-3.5 h-3.5" />
                      </div>
                      <div>
                        <p className="text-xs font-semibold text-slate-200">Meja 0{i}</p>
                        <p className="text-[10px] text-slate-500">2 mnt lalu</p>
                      </div>
                    </div>
                    <span className="text-xs font-mono font-medium text-slate-300">Rp 120k</span>
                  </div>
                ))}
              </div>
            </div>

          </div>
        </div>

      </main>
    </div>
  );
}
```

---

## 3. Checklist UX Tata Letak Dashboard
1. **Viewport & Penguncian Scroll**: Tag terluar dashboard WAJIB menggunakan `h-screen` atau `min-h-screen` dengan tata letak `flex`. Sidebar harus tetap menempel di tempatnya (tidak ikut terguling ke bawah), dan hanya area kotak konten (`main`) yang memiliki `overflow-y-auto`.
2. **Kepadatan Data (Data Density)**: Hindari font berukuran raksasa untuk data analitik. Metrik utama boleh besar, namun teks keterangan harus tetap mungil (`text-xs` hingga `text-[10px]`) dan ketat agar puluhan baris data tabel dapat muat di layar laptop standar (13 inch).
3. **Pemuatan Bertahap (Skeleton Loading)**: Kartu grafik *(Charts)* atau daftar transaksi lambat memuat data. Gunakan animasi *Skeleton* abu-abu berkedip sebelum grafik selesai dirender (menggunakan blueprint `Skeleton`).
