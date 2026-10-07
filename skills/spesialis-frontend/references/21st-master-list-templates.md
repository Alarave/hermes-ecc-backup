# 21st.dev Master List & Activity Feed Templates

Analisis pola dan blueprint komponen List (Daftar Interaktif) berdasarkan 349+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe List Modern

### Arketipe 1: The Reorderable / Draggable Priority List
- **Fungsi**: Daftar tugas (*To-Do List*), prioritas antrean pengerjaan, atau penyusunan navigasi yang dapat digeser posisinya secara drag-and-drop.
- **Karakteristik Visual**:
  - Terdapat ikon pegangan geser (*GripVertical*) di sisi paling kiri.
  - Saat item diseret (*drag*), item tersebut terangkat sedikit dengan bayangan melayang (*elevation shadow* dan *spring physics*).
- **Inspirasi**: `Draggable Priority List`, `AI Task List (Edu Calvo)`.

### Arketipe 2: The Animated Activity Feed (Staggered Insertion)
- **Fungsi**: Riwayat aktivitas langsung (Audit log, transaksi masuk terbaru, feed integrasi API).
- **Karakteristik Visual**:
  - Garis linimasa vertikal halus yang menghubungkan antar item.
  - Setiap item baru yang masuk muncul dengan efek animasi meluncur ke bawah (*staggered slide down*) secara elegan tanpa menghentak layout.
- **Inspirasi**: `Animated List`, `Changelog 1 (Shadcnblocks)`.

### Arketipe 3: The Member / Collaborator Permission List
- **Fungsi**: Halaman manajemen tim di aplikasi SaaS (Pengaturan Akun / Workspace).
- **Karakteristik Visual**:
  - Kolom kiri: Avatar pengguna, nama lengkap, dan email.
  - Kolom kanan: Dropdown hak akses (Admin, Editor, Viewer) dan tombol titik tiga (`MoreVertical`).
- **Inspirasi**: `Member List`, `The Item one (felipemenezes098)`.

### Arketipe 4: The Integration / Connected Services List
- **Fungsi**: Menampilkan daftar integrasi alat pihak ketiga (Slack, GitHub, Figma, Stripe).
- **Karakteristik Visual**:
  - Kartu baris horizontal memuat logo resmi aplikasi, status koneksi ("Terhubung" - badge hijau, atau "Belum Terhubung"), dan tombol sakelar (*Toggle*).
- **Inspirasi**: `Integrations 02`.

---

## 2. Blueprint Kode Master (The Reorderable Task List)

```tsx
import { useState } from "react";
import { Reorder, motion } from "framer-motion";
import { GripVertical, CheckCircle2, Circle, Clock } from "lucide-react";

interface ListItem {
  id: string;
  title: string;
  category: string;
  due: string;
  completed: boolean;
}

const INITIAL_ITEMS: ListItem[] = [
  { id: "task-1", title: "Audit Kepatuhan Aksesibilitas WCAG 2.2", category: "Frontend", due: "Hari ini", completed: true },
  { id: "task-2", title: "Optimasi Web Vitals (INP < 200ms)", category: "Performance", due: "Besok", completed: false },
  { id: "task-3", title: "Integrasi API Pembayaran Berlayar Cafe", category: "Backend", due: "3 hari lagi", completed: false },
];

export function InteractiveReorderList() {
  const [items, setItems] = useState(itemsWithKey(INITIAL_ITEMS));

  function itemsWithKey(list: ListItem[]) {
    return list;
  }

  const toggleStatus = (id: string) => {
    setItems(items.map((it) => (it.id === id ? { ...it, completed: !it.completed } : it)));
  };

  return (
    <div className="w-full max-w-lg p-5 rounded-2xl border border-slate-800 bg-slate-900 shadow-xl">
      {/* Header */}
      <div className="flex items-center justify-between mb-4 pb-3 border-b border-slate-800">
        <div>
          <h3 className="text-sm font-bold text-white">Daftar Prioritas Pengerjaan</h3>
          <p className="text-xs text-slate-400 mt-0.5">Tarik dan geser posisi untuk mengatur prioritas.</p>
        </div>
        <span className="text-xs font-mono font-semibold px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
          {items.length} Tugas
        </span>
      </div>

      {/* Reorderable Container */}
      <Reorder.Group axis="y" values={items} onReorder={setItems} className="space-y-2.5">
        {items.map((item) => (
          <Reorder.Item
            key={item.id}
            value={item}
            className="flex items-center gap-3 p-3 rounded-xl border border-slate-800 bg-slate-800/40 hover:border-slate-700 select-none cursor-grab active:cursor-grabbing backdrop-blur-md transition-colors"
            whileDrag={{
              scale: 1.02,
              boxShadow: "0 20px 25px -5px rgb(0 0 0 / 0.5), 0 8px 10px -6px rgb(0 0 0 / 0.5)",
              backgroundColor: "rgba(30, 41, 59, 0.9)",
            }}
          >
            {/* Drag Handle */}
            <div className="text-slate-500 hover:text-slate-300 transition-colors">
              <GripVertical className="w-4 h-4" />
            </div>

            {/* Completion Toggle */}
            <button
              onClick={() => toggleStatus(item.id)}
              className="text-slate-500 hover:text-emerald-400 transition-colors"
            >
              {item.completed ? (
                <CheckCircle2 className="w-4 h-4 text-emerald-500" />
              ) : (
                <Circle className="w-4 h-4 text-slate-500" />
              )}
            </button>

            {/* Task Info */}
            <div className="flex-1 min-w-0">
              <h4
                className={`text-xs font-semibold truncate transition-colors ${
                  item.completed ? "text-slate-500 line-through" : "text-slate-200"
                }`}
              >
                {item.title}
              </h4>
              <div className="flex items-center gap-2 mt-1">
                <span className="text-[10px] font-medium px-1.5 py-0.5 rounded bg-slate-700/60 text-slate-400">
                  {item.category}
                </span>
                <span className="flex items-center gap-1 text-[10px] font-mono text-slate-500">
                  <Clock className="w-3 h-3" />
                  {item.due}
                </span>
              </div>
            </div>
          </Reorder.Item>
        ))}
      </Reorder.Group>
    </div>
  );
}
```

---

## 3. Checklist Aksesibilitas List (WAI-ARIA)
1. **Grip Accessibility**: Untuk pengguna yang hanya menggunakan keyboard (tanpa mouse), fitur *drag-and-drop* harus menyediakan tombol alternatif pintasan keyboard (misal: `Alt + Panah Atas` untuk memindahkan baris 1 langkah ke atas).
2. **List Semantics**: Struktur daftar harus dibungkus tag semantik `<ul>` dan `<li>` (atau menggunakan `role="list"` dan `role="listitem"` pada kontainer kustom).
3. **Empty State**: Selalu sediakan ilustrasi/tampilan saat daftar kosong (`items.length === 0`) agar layar tidak terlihat seperti halaman yang gagal memuat API.
