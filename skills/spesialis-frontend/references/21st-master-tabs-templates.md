# 21st.dev Master Tabs Templates

Analisis pola komponen Tabs (Navigasi Berjenjang) berdasarkan koleksi 239+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Tabs Modern

### Arketipe 1: The Pill Morph / Sliding Background Tab
- **Fungsi**: Segmented control atau navigasi sub-halaman modern.
- **Karakteristik**: Menggunakan kapsul (pill) yang "meluncur" secara mulus di bawah teks tab yang aktif menggunakan fitur `layoutId` dari Framer Motion. 
- **Inspirasi**: `Animated Shifting Tab Component`, `Pill Morph Tabs (Ruixen)`.

### Arketipe 2: The Animated Underline Tab
- **Fungsi**: Navigasi konten yang lebih memanjang (biasa digunakan di bagian atas halaman atau tabel data).
- **Karakteristik**: Garis bawah (underline) setebal 2px bergeser halus di bawah tab yang sedang di-klik. Menggunakan padding transparan untuk menjaga posisi statis teks.
- **Inspirasi**: `Simple Tabs with underline`, `Underline Tabs Card (Cnippet)`.

### Arketipe 3: The Vertical Settings Tab
- **Fungsi**: Sidebar pengaturan akun atau sistem kompleks (seperti layout pengaturan Mac/Windows).
- **Karakteristik**: Berada di sisi kiri (kolom menu vertikal) sementara konten merender di sisi kanan. Highlight aktif biasanya berupa fill warna solid dan icon tebal.

### Arketipe 4: The Magnetic / 3D Icon Tab
- **Fungsi**: Navigasi galeri, showcase kreatif, atau navigasi ikon.
- **Karakteristik**: Efek "menarik kursor" (*cursor tracking*) atau membesar seketika (3D spring pop) ketika di-hover atau aktif.

---

## 2. Blueprint Kode Master (React + Framer Motion)

### A. The Pill Morph Tab (Sliding Background)
Blueprint paling ikonik dari 21st.dev. Cocok untuk navigasi kecil / dashboard atas.

```tsx
import { useState } from "react";
import { motion } from "framer-motion";

const TABS = ["Account", "Security", "Notifications", "Integrations"];

export function PillMorphTabs() {
  const [activeTab, setActiveTab] = useState(TABS[0]);

  return (
    <div className="flex items-center gap-1 p-1 bg-slate-900/50 border border-slate-800 rounded-xl w-fit">
      {TABS.map((tab) => {
        const isActive = activeTab === tab;
        return (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`relative px-4 py-2 text-sm font-medium rounded-lg transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 z-10 ${
              isActive ? "text-white" : "text-slate-400 hover:text-slate-200"
            }`}
            role="tab"
            aria-selected={isActive}
          >
            {isActive && (
              <motion.div
                layoutId="pill-morph-bg"
                className="absolute inset-0 bg-slate-800 rounded-lg shadow-sm border border-slate-700/50 z-[-1]"
                transition={{
                  type: "spring",
                  stiffness: 400,
                  damping: 30,
                }}
              />
            )}
            <span className="relative z-10">{tab}</span>
          </button>
        );
      })}
    </div>
  );
}
```

### B. The Sliding Underline Tab (Classic Modern)
Cocok untuk batas atas section (seperti profil atau header tabel).

```tsx
import { useState } from "react";
import { motion } from "framer-motion";

const NAV_TABS = ["Overview", "Repositories", "Projects", "Packages"];

export function UnderlineTabs() {
  const [activeTab, setActiveTab] = useState(NAV_TABS[0]);

  return (
    <div className="border-b border-slate-800 w-full overflow-x-auto no-scrollbar">
      <div className="flex gap-6 px-2">
        {NAV_TABS.map((tab) => {
          const isActive = activeTab === tab;
          return (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`relative pb-3 pt-2 text-sm font-medium transition-colors whitespace-nowrap focus:outline-none ${
                isActive ? "text-indigo-400" : "text-slate-400 hover:text-slate-200"
              }`}
              role="tab"
              aria-selected={isActive}
            >
              <span>{tab}</span>
              {isActive && (
                <motion.div
                  layoutId="underline-tab-indicator"
                  className="absolute bottom-0 left-0 right-0 h-0.5 bg-indigo-500 rounded-t-full"
                  initial={false}
                  transition={{
                    type: "spring",
                    stiffness: 500,
                    damping: 30,
                  }}
                />
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
}
```

---

## 3. Aturan Aksesibilitas (WAI-ARIA untuk Tabs)
Berdasarkan spesifikasi Radix UI / W3C:
1. **Peran (Roles)**: 
   - Gunakan `role="tablist"` pada kontainer tombol.
   - Gunakan `role="tab"` pada setiap tombol.
   - Gunakan `role="tabpanel"` pada kontainer konten yang ditampilkan.
2. **Status Aktif**: Gunakan atribut `aria-selected="true"` pada tab yang sedang aktif.
3. **Keyboard Navigasi**: Tab yang kompleks disarankan menangani event panah (Arrow Left / Arrow Right) untuk memindahkan fokus dan mengaktifkan tab selanjutnya tanpa memencet Tab/Enter (disebut *roving tabindex*).
4. **Layout Shift Protection**: Tombol tab tidak boleh berubah ukuran fisiknya saat aktif. Gunakan ketebalan font (`font-medium`) secara konsisten pada semua state, atau gunakan padding cadangan agar panjang teks tidak mendorong elemen lain (layout shift).
