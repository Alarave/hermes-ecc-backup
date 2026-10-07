# 21st.dev Master Toggle & Switch Templates

Katalog dan blueprint komponen Toggle (Switch, Theme Switcher, Segmented Controls) berdasarkan tren 532+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Toggle UI/UX

### Arketipe 1: The Cinematic / Animated Theme Switcher
- **Fungsi**: Beralih antara Dark Mode dan Light Mode.
- **Karakteristik**: Menggunakan ikon Sun & Moon dengan transisi spasial. Varian modern meliputi:
  - *Light Pull Switcher*: Menarik tali animasi untuk mengganti tema.
  - *Curtain / Vertical Wipe*: Transisi warna menyapu seluruh layar dari titik toggle.
  - *Cinematic Glow*: Menggunakan efek *inner-shadow* pada toggle dan rotasi spring saat switch ditekan.

### Arketipe 2: The Liquid / Bouncy Toggle
- **Fungsi**: Switch (On/Off) untuk pengaturan aplikasi (Settings / Privacy).
- **Karakteristik**:
  - Efek fisika (spring bounce) yang hiper-realistis pada lingkaran indikator (knob/thumb).
  - *Liquid effect*: Indikator merentang/memanjang (stretch) sesaat saat bergeser, mirip tetesan air.

### Arketipe 3: Segmented Control / Toggle Group
- **Fungsi**: Pilihan *mutually exclusive* berjejer secara horizontal (misalnya: Harga "Monthly" vs "Yearly", tab "Preview" vs "Code").
- **Karakteristik**:
  - Pill shape atau rounded rectangle.
  - Menggunakan *layoutId* (Framer Motion) agar background/penanda aktif meluncur mulus di bawah teks, persis seperti antarmuka iOS/macOS.

### Arketipe 4: Switch with Icon & Description
- **Fungsi**: Pengaturan lanjutan atau perizinan notifikasi (Privacy Settings).
- **Karakteristik**: Toggle digabungkan dalam satu *card list* bersama Icon penanda di kiri, judul pengaturan di atas, dan deskripsi detail di bawah.

---

## 2. Blueprint Kode Master (The Liquid Bouncy Switch & Segmented Control)

### A. The Liquid Bouncy Switch (Pengaturan On/Off)
```tsx
import { useState } from "react";
import { motion } from "framer-motion";

export function LiquidToggle({ label, defaultState = false }) {
  const [isOn, setIsOn] = useState(defaultState);

  return (
    <div className="flex items-center justify-between p-3 rounded-xl hover:bg-slate-800/40 transition-colors">
      <span className="text-sm font-medium text-slate-200">{label}</span>
      <button
        onClick={() => setIsOn(!isOn)}
        className={`relative inline-flex h-6 w-11 flex-shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-slate-900 ${
          isOn ? "bg-indigo-500" : "bg-slate-700"
        }`}
        role="switch"
        aria-checked={isOn}
      >
        <span className="sr-only">Toggle {label}</span>
        <motion.span
          layout
          initial={false}
          animate={{
            x: isOn ? 20 : 0,
            scaleX: [1, 1.3, 1], // Efek merentang (liquid/stretching)
          }}
          transition={{
            type: "spring",
            stiffness: 500,
            damping: 30,
            mass: 0.8,
          }}
          className="pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow-sm ring-0"
        />
      </button>
    </div>
  );
}
```

### B. Segmented Control (Pill Toggle Group)
*Contoh sempurna untuk opsi penagihan "Monthly" vs "Annually"*

```tsx
import { useState } from "react";
import { motion } from "framer-motion";

const OPTIONS = ["Monthly", "Annually"];

export function SegmentedToggle() {
  const [selected, setSelected] = useState(OPTIONS[0]);

  return (
    <div className="relative inline-flex items-center p-1 rounded-full bg-slate-900 border border-slate-800 shadow-inner">
      {OPTIONS.map((option) => (
        <button
          key={option}
          onClick={() => setSelected(option)}
          className={`relative px-6 py-2 text-sm font-semibold rounded-full transition-colors z-10 focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 ${
            selected === option ? "text-slate-900" : "text-slate-400 hover:text-slate-200"
          }`}
        >
          {selected === option && (
            <motion.div
              layoutId="segmented-indicator"
              className="absolute inset-0 bg-white rounded-full shadow-sm"
              initial={false}
              transition={{
                type: "spring",
                stiffness: 400,
                damping: 30,
              }}
            />
          )}
          <span className="relative z-20">{option}</span>
        </button>
      ))}
    </div>
  );
}
```

### C. The Cinematic Theme Switcher (Dark/Light)
```tsx
import { useState } from "react";
import { motion } from "framer-motion";
import { Sun, Moon } from "lucide-react";

export function ThemeSwitcher() {
  const [isDark, setIsDark] = useState(true);

  return (
    <button
      onClick={() => setIsDark(!isDark)}
      className="relative flex items-center justify-center w-10 h-10 rounded-full border border-slate-800 bg-slate-900 text-slate-400 hover:text-indigo-300 hover:border-slate-700 transition-colors focus:outline-none"
      aria-label="Toggle Dark Mode"
    >
      <motion.div
        initial={false}
        animate={{
          scale: isDark ? 1 : 0,
          rotate: isDark ? 0 : 90,
          opacity: isDark ? 1 : 0
        }}
        transition={{ type: "spring", stiffness: 300, damping: 20 }}
        className="absolute"
      >
        <Moon className="w-5 h-5 fill-current" />
      </motion.div>
      
      <motion.div
        initial={false}
        animate={{
          scale: isDark ? 0 : 1,
          rotate: isDark ? -90 : 0,
          opacity: isDark ? 0 : 1
        }}
        transition={{ type: "spring", stiffness: 300, damping: 20 }}
        className="absolute"
      >
        <Sun className="w-5 h-5" />
      </motion.div>
    </button>
  );
}
```

---

## 3. Checklist Aksesibilitas Switch (WAI-ARIA)
1. **Atribut `role`**: Gunakan `role="switch"` untuk tombol On/Off tunggal.
2. **Atribut `aria-checked`**: Sinkronkan nilai `true/false` pada atribut ini sesuai state toggle.
3. **Screen Reader**: Tambahkan `<span>` dengan kelas `sr-only` (misalnya: "Toggle Notifications") agar tombol dimengerti oleh pembaca layar.
4. **Fokus Keyboard**: Pastikan batas outline (focus ring) terlihat saat melakukan navigasi dengan tombol `Tab` (`focus:ring-2 focus:ring-indigo-500`).
