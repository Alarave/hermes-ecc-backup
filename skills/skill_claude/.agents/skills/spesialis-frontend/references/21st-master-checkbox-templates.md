# 21st.dev Master Checkbox & Selection Templates

Analisis pola dan blueprint komponen Checkbox berdasarkan 238+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Checkbox Modern

### Arketipe 1: The Form Checkbox with Description
- **Fungsi**: Persetujuan *Terms & Conditions* atau pengaturan preferensi profil (misal: "Izinkan notifikasi email").
- **Karakteristik Visual**:
  - Kotak centang kustom (`w-5 h-5`) berada di sisi kiri.
  - Sisi kanan memuat struktur teks bertingkat: Judul tebal dan deskripsi abu-abu halus di bawahnya.
- **Inspirasi**: `Checkbox w/ description (Abraham)`, `Checkbox (Origin UI)`.

### Arketipe 2: The Selectable Card (Checkbox Group)
- **Fungsi**: Pemilihan opsi kompleks seperti Metode Pembayaran (Kartu Kredit, PayPal) atau paket layanan.
- **Karakteristik Visual**:
  - Seluruh kartu dapat diklik (*Clickable Surface*).
  - Saat aktif, border kartu menyala (`border-indigo-500`) dan background berubah samar (`bg-indigo-500/10`).
  - Kotak centang berada di sudut kanan atas atau kiri tengah.
- **Inspirasi**: `Payment Method Card Checkbox (Cnippet)`, `Checkbox Parent (ShadcnStudio)`.

### Arketipe 3: The Animated SVG Checkmark
- **Fungsi**: Checkbox estetis untuk aplikasi produktivitas atau *To-Do List*.
- **Karakteristik Visual**:
  - Menyembunyikan input asli HTML.
  - Ikon SVG centang "digambar" masuk (*path length animation*) menggunakan Framer Motion saat status berubah menjadi *checked*.
- **Inspirasi**: `Animated Check Box (ring labs)`.

### Arketipe 4: The Indeterminate Master Checkbox
- **Fungsi**: Kotak centang *Select All* di baris paling atas (*header*) tabel data.
- **Karakteristik Visual**:
  - Memiliki 3 status: Kosong, Tercentang (✓), dan Indeterminate (garis minus horizontal `-`).
  - Status *indeterminate* muncul jika hanya sebagian baris tabel yang dipilih pengguna.

---

## 2. Blueprint Kode Master (The Selectable Card Checkbox)

```tsx
import { useState } from "react";
import { Check, CreditCard, Wallet, Landmark } from "lucide-react";
import { motion } from "framer-motion";

const PAYMENT_METHODS = [
  { id: "card", title: "Kartu Kredit / Debit", description: "Visa, Mastercard, JCB", icon: CreditCard },
  { id: "wallet", title: "E-Wallet", description: "OVO, GoPay, Dana", icon: Wallet },
  { id: "bank", title: "Transfer Bank", description: "Virtual Account", icon: Landmark },
];

export function SelectableCardCheckboxGroup() {
  const [selectedMethods, setSelectedMethods] = useState<string[]>(["card"]);

  const toggleSelection = (id: string) => {
    setSelectedMethods((prev) =>
      prev.includes(id) ? prev.filter((item) => item !== id) : [...prev, id]
    );
  };

  return (
    <div className="w-full max-w-md space-y-3">
      <h3 className="text-sm font-bold text-white mb-4">Pilih Metode Pembayaran</h3>
      
      {PAYMENT_METHODS.map((method) => {
        const isChecked = selectedMethods.includes(method.id);
        const Icon = method.icon;

        return (
          <label
            key={method.id}
            className={`relative flex items-center justify-between p-4 cursor-pointer rounded-2xl border transition-all duration-300 ${
              isChecked
                ? "border-indigo-500 bg-indigo-500/10 shadow-lg shadow-indigo-500/10"
                : "border-slate-800 bg-slate-900/60 hover:bg-slate-800 hover:border-slate-700"
            }`}
          >
            {/* Hidden Native Checkbox for Accessibility & Form Submission */}
            <input
              type="checkbox"
              className="sr-only"
              checked={isChecked}
              onChange={() => toggleSelection(method.id)}
            />

            <div className="flex items-center gap-4">
              <div className={`p-2.5 rounded-xl border transition-colors ${
                isChecked ? "bg-indigo-500/20 border-indigo-500/30 text-indigo-400" : "bg-slate-800 border-slate-700 text-slate-400"
              }`}>
                <Icon className="w-5 h-5" />
              </div>
              
              <div>
                <h4 className={`text-sm font-semibold transition-colors ${isChecked ? "text-white" : "text-slate-200"}`}>
                  {method.title}
                </h4>
                <p className="text-xs text-slate-500 mt-0.5">{method.description}</p>
              </div>
            </div>

            {/* Custom Checkbox Indicator */}
            <div className={`flex items-center justify-center w-6 h-6 rounded-md border transition-all duration-300 ${
              isChecked 
                ? "bg-indigo-600 border-indigo-600 text-white" 
                : "bg-slate-950 border-slate-700"
            }`}>
              {isChecked && (
                <motion.div
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ type: "spring", stiffness: 400, damping: 25 }}
                >
                  <Check className="w-3.5 h-3.5 stroke-[3]" />
                </motion.div>
              )}
            </div>
          </label>
        );
      })}
    </div>
  );
}
```

---

## 3. Checklist UX Checkbox (WCAG)
1. **Aturan "Area Sentuh Lebar" (Hitbox)**: Pastikan tag `<label>` membungkus keseluruhan kartu atau teks deskripsi. Pengguna tidak boleh dipaksa untuk mengarahkan mouse tepat ke kotak kecil `w-5 h-5` saja untuk mencentangnya.
2. **Fokus Keyboard Ring**: Sembunyikan input native dengan kelas `sr-only` (Screen Reader Only), tapi pastikan Anda menangkap *focus state* dari input tersebut untuk menggambar cincin (ring) putih/indigo di sekeliling kartu saat pengguna melakukan navigasi `Tab` keyboard.
3. **Checkbox vs Radio Button**: 
   - Gunakan **Checkbox** jika pengguna boleh memilih LEBIH DARI SATU opsi, atau opsi bersifat mematikan/menyalakan tunggal (Ya/Tidak).
   - Gunakan **Radio Button** jika pengguna HANYA BOLEH memilih SATU opsi dari banyak pilihan (contoh: "Laki-laki" atau "Perempuan").
