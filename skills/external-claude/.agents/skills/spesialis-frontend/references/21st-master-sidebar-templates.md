# 21st.dev Master Sidebar Templates

Analisis pola dan blueprint komponen Sidebar (Navigasi Dashboard) berdasarkan tren UI modern di 21st.dev (React + Tailwind v4 + Framer Motion / Lucide).

---

## 1. Empat Arketipe Sidebar Modern

### Arketipe 1: The Collapsible Icon Rail (Linear & Shadcn Style)
- **Fungsi**: Memaksimalkan ruang kerja dashboard saat user butuh fokus.
- **Karakteristik Visual**:
  - Saat dibuka (*expanded*): Menampilkan icon, teks nama menu, dan badge notifikasi kecil. Lebar sekitar `w-64`.
  - Saat diciutkan (*collapsed*): Lebar menyusut menjadi `w-16`, hanya menyisakan deretan icon. Teks nama menu otomatis beralih menjadi *Tooltip* saat di-hover.
- **Inspirasi**: `Animated Sidebar (unlumen)`, `Shadcn Sidebar Primitives`.

### Arketipe 2: The Floating / Detached Glass Sidebar
- **Fungsi**: Antarmuka SaaS modern (AI tools, Canva/Figma-like editors).
- **Karakteristik Visual**:
  - Tidak menempel di tepi kiri layar, melainkan melayang (*floating*) dengan margin `m-4`.
  - Menggunakan sudut melengkung besar (`rounded-3xl`), border halus, dan efek `backdrop-blur-xl`.

### Arketipe 3: The Dual-Rail Workspace Sidebar (Slack / Discord Style)
- **Fungsi**: Aplikasi dengan multi-tenant atau banyak workspace/organisasi.
- **Karakteristik Visual**:
  - Kolom pertama (kiri sempit `w-14`): Logo avatar untuk berganti workspace/organisasi.
  - Kolom kedua (kanan `w-60`): Menu internal, channels, atau navigasi proyek dari workspace yang sedang aktif.

### Arketipe 4: The Mobile Responsive Drawer / Sheet
- **Fungsi**: Navigasi sidebar pada layar smartphone/tablet.
- **Karakteristik Visual**:
  - Tersembunyi di luar layar (kiri).
  - Meluncur masuk (*slide-in*) saat tombol burger ditekan dengan background gelap transparan (*backdrop overlay*).

---

## 2. Blueprint Kode Master (The Collapsible Icon Rail)

Menggunakan Framer Motion untuk transisi lebar (*width*) yang mulus tanpa patah-patah:

```tsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { 
  LayoutDashboard, 
  Layers, 
  BarChart3, 
  Settings, 
  PanelLeftClose, 
  PanelLeftOpen, 
  UserCircle 
} from "lucide-react";

const MENU_ITEMS = [
  { icon: LayoutDashboard, label: "Overview", active: true },
  { icon: Layers, label: "Projects", count: 4 },
  { icon: BarChart3, label: "Analytics" },
  { icon: Settings, label: "Settings" },
];

export function CollapsibleSidebar() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <motion.aside
      animate={{ width: collapsed ? "68px" : "260px" }}
      transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
      className="h-screen bg-slate-900 border-r border-slate-800 flex flex-col justify-between p-3 select-none relative"
    >
      {/* 1. Header & Brand Logo */}
      <div>
        <div className="flex items-center justify-between px-2 py-3 mb-4">
          <div className="flex items-center gap-3 overflow-hidden">
            <div className="w-8 h-8 rounded-xl bg-indigo-600 flex items-center justify-center text-white font-bold font-mono text-sm flex-shrink-0">
              B
            </div>
            {!collapsed && (
              <motion.span 
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                className="font-bold text-slate-100 text-sm tracking-tight whitespace-nowrap"
              >
                Berlayar Portal
              </motion.span>
            )}
          </div>
          
          {/* Toggle Button */}
          <button 
            onClick={() => setCollapsed(!collapsed)}
            className="p-1.5 rounded-lg text-slate-500 hover:text-slate-300 hover:bg-slate-800 transition-colors focus:outline-none"
            aria-label={collapsed ? "Expand sidebar" : "Collapse sidebar"}
          >
            {collapsed ? <PanelLeftOpen className="w-4 h-4" /> : <PanelLeftClose className="w-4 h-4" />}
          </button>
        </div>

        {/* 2. Menu Navigation */}
        <nav className="space-y-1">
          {MENU_ITEMS.map((item, i) => {
            const Icon = item.icon;
            return (
              <button
                key={i}
                className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-colors relative group focus:outline-none ${
                  item.active 
                    ? "bg-indigo-500/10 text-indigo-400 border border-indigo-500/20" 
                    : "text-slate-400 hover:text-slate-200 hover:bg-slate-800/60"
                }`}
              >
                <Icon className="w-5 h-5 flex-shrink-0" />
                
                {/* Text Label */}
                {!collapsed && (
                  <motion.div 
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    className="flex-1 flex items-center justify-between overflow-hidden"
                  >
                    <span className="whitespace-nowrap">{item.label}</span>
                    {item.count && (
                      <span className="px-2 py-0.5 text-[10px] font-mono bg-slate-800 text-slate-400 rounded-md">
                        {item.count}
                      </span>
                    )}
                  </motion.div>
                )}

                {/* Floating Tooltip if collapsed (Hover only) */}
                {collapsed && (
                  <div className="absolute left-full ml-3 px-2.5 py-1 rounded-md bg-slate-800 text-slate-200 text-xs font-medium whitespace-nowrap shadow-xl border border-slate-700/80 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity z-50">
                    {item.label}
                  </div>
                )}
              </button>
            );
          })}
        </nav>
      </div>

      {/* 3. Footer / User Profile Card */}
      <div className="border-t border-slate-800/80 pt-3">
        <div className="flex items-center gap-3 p-2 rounded-xl hover:bg-slate-800/40 transition-colors cursor-pointer">
          <UserCircle className="w-8 h-8 text-slate-400 flex-shrink-0" />
          {!collapsed && (
            <motion.div 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="flex-1 overflow-hidden"
            >
              <p className="text-xs font-semibold text-slate-200 truncate">Firman</p>
              <p className="text-[11px] text-slate-500 truncate">Pro Account</p>
            </motion.div>
          )}
        </div>
      </div>

    </motion.aside>
  );
}
```

---

## 3. Checklist UX Sidebar
1. **Lebar Dinamis**: Hindari perubahan teks yang terpotong secara instan. Selalu gunakan `overflow-hidden` dan `whitespace-nowrap` pada label teks saat sidebar menyusut.
2. **Peralihan Tooltip Otomatis**: Saat sidebar berubah ke mode ciut (*collapsed/icon-only*), pengguna kehilangan label teks. Pastikan komponen Tooltip otomatis aktif pada kondisi tersebut.
3. **Backdrop pada Mobile**: Di smartphone, sidebar wajib berperilaku sebagai modal/drawer mengambang lengkap dengan tombol tutup dan *backdrop blur* agar konten di belakangnya terkunci dari scroll.
