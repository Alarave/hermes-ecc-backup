# 21st.dev Master Notification & Inbox Templates

Analisis pola dan blueprint komponen Notification & Notification Center berdasarkan 247+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Notifikasi Modern

### Arketipe 1: The Notification Center / Inbox Popover
- **Fungsi**: Pusat notifikasi pengguna di bilah navigasi utama (Navbar).
- **Karakteristik Visual**:
  - Tombol pemicu ikon Lonceng (`Bell`) dengan lencana angka merah/indigo (`Badge`) penunjuk pesan belum dibaca.
  - Saat diklik, membuka popover/panel bertingkat berisi:
    - *Header*: Judul "Notifikasi", jumlah pesan belum dibaca, dan tombol "Tandai semua telah dibaca".
    - *Filter Tab*: Pilihan filter seperti "Semua" dan "Belum Dibaca".
    - *List*: Baris notifikasi dengan avatar, waktu relatif (misal: "5m yang lalu"), teks ringkas, dan titik penunjuk status aktif (*unread dot*).
- **Inspirasi**: `Notification Center (Origin UI / Ruixen)`.

### Arketipe 2: The Actionable Invite Notification Card
- **Fungsi**: Notifikasi yang membutuhkan persetujuan langsung (misalnya undangan ke tim, permintaan akses file, transfer dana).
- **Karakteristik Visual**:
  - Di bawah pesan notifikasi terdapat dua tombol aksi kontras: tombol utama (misal: "Terima" - Indigo) dan tombol sekunder ("Tolak" - Ghost/Slate).
- **Inspirasi**: `The Item one (felipemenezes098)`, `Dismissible Alert Stack (7ovr)`.

### Arketipe 3: The Persistent Maintenance / System Banner
- **Fungsi**: Pengumuman global di seluruh aplikasi (misal: "Sistem akan maintenance malam ini pukul 23:00").
- **Karakteristik Visual**:
  - Bilah tipis horizontal berlatar belakang amber atau indigo di puncak halaman dengan tombol tutup silang (*Dismiss*).
- **Inspirasi**: `Astryx Banner (Astryx)`, `HeroUI Alert`.

### Arketipe 4: The Status Dot Ping (Micro Indicator)
- **Fungsi**: Menandakan koneksi live / data baru yang masuk secara real-time.
- **Karakteristik Visual**:
  - Titik bundar kecil hijau/biru dengan cincin luar yang membesar dan memudar berulang (*radar ping effect*: `animate-ping`).
- **Inspirasi**: `Status Dot (Edwin Vakayil)`.

---

## 2. Perbedaan Krusial: Notification vs Toast
- **Toast**: Sementara (*ephemeral*), muncul di sudut layar selama beberapa detik lalu hilang otomatis tanpa jejak (biasanya untuk respon aksi: "Berhasil disimpan").
- **Notification**: Abadi (*persistent*), disimpan di database dan masuk ke dalam kotak masuk (*inbox*) pengguna sampai mereka membacanya atau menghapusnya sendiri.

---

## 3. Blueprint Kode Master (The Notification Center Popover)

```tsx
import { useState } from "react";
import { Bell, Check, Trash2, Clock, UserPlus } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface NotificationItem {
  id: string;
  title: string;
  description: string;
  time: string;
  isRead: boolean;
  type: "invite" | "system";
}

const INITIAL_DATA: NotificationItem[] = [
  {
    id: "1",
    title: "Sarah mengundang Anda ke Proyek",
    description: "Desain Sistem UI Mobile Berlayar Cafe",
    time: "10 menit lalu",
    isRead: false,
    type: "invite",
  },
  {
    id: "2",
    title: "Penyimpanan Hampir Penuh",
    description: "Kapasitas storage Anda sudah mencapai 85%.",
    time: "2 jam lalu",
    isRead: false,
    type: "system",
  },
  {
    id: "3",
    title: "Deployment Berhasil",
    description: "Versi 2.4.0 live di production.",
    time: "1 hari lalu",
    isRead: true,
    type: "system",
  },
];

export function NotificationCenter() {
  const [notifications, setNotifications] = useState<NotificationItem[]>(INITIAL_DATA);
  const [isOpen, setIsOpen] = useState(false);

  const unreadCount = notifications.filter((n) => !n.isRead).length;

  const markAllAsRead = () => {
    setNotifications(notifications.map((n) => ({ ...n, isRead: true })));
  };

  const removeNotification = (id: string) => {
    setNotifications(notifications.filter((n) => n.id !== id));
  };

  return (
    <div className="relative inline-block">
      {/* Bell Trigger Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Notifikasi"
        className="relative p-2.5 rounded-xl border border-slate-800 bg-slate-900/80 hover:bg-slate-800 text-slate-300 hover:text-white transition-colors"
      >
        <Bell className="w-5 h-5" />
        
        {/* Unread Counter Badge */}
        {unreadCount > 0 && (
          <span className="absolute -top-1 -right-1 flex items-center justify-center w-5 h-5 rounded-full bg-indigo-600 text-[10px] font-mono font-bold text-white ring-2 ring-slate-950">
            {unreadCount}
          </span>
        )}
      </button>

      {/* Popover Dropdown Panel */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 10 }}
            transition={{ duration: 0.15 }}
            className="absolute right-0 top-full mt-2 w-80 md:w-96 rounded-2xl border border-slate-800 bg-slate-900 shadow-2xl backdrop-blur-xl z-50 overflow-hidden"
          >
            {/* Header */}
            <div className="flex items-center justify-between p-4 border-b border-slate-800">
              <div className="flex items-center gap-2">
                <h3 className="text-sm font-bold text-white">Notifikasi</h3>
                {unreadCount > 0 && (
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-mono font-semibold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
                    {unreadCount} baru
                  </span>
                )}
              </div>

              {unreadCount > 0 && (
                <button
                  onClick={markAllAsRead}
                  className="text-xs text-indigo-400 hover:text-indigo-300 font-medium transition-colors"
                >
                  Tandai dibaca
                </button>
              )}
            </div>

            {/* List Body */}
            <div className="max-h-80 overflow-y-auto divide-y divide-slate-800/60">
              {notifications.length === 0 ? (
                <div className="p-8 text-center text-xs text-slate-500 font-mono">
                  Kotak masuk bersih. Tidak ada notifikasi.
                </div>
              ) : (
                notifications.map((item) => (
                  <div
                    key={item.id}
                    className={`p-4 flex items-start gap-3 transition-colors ${
                      item.isRead ? "bg-transparent opacity-75" : "bg-slate-800/20"
                    }`}
                  >
                    {/* Icon / Type */}
                    <div className="p-2 rounded-lg bg-slate-800 text-indigo-400 shrink-0 mt-0.5">
                      {item.type === "invite" ? <UserPlus className="w-4 h-4" /> : <Clock className="w-4 h-4" />}
                    </div>

                    {/* Content */}
                    <div className="flex-1 min-w-0">
                      <div className="flex items-start justify-between gap-1">
                        <h4 className="text-xs font-semibold text-slate-200 truncate">
                          {item.title}
                        </h4>
                        {!item.isRead && (
                          <span className="w-2 h-2 rounded-full bg-indigo-500 shrink-0 mt-1" />
                        )}
                      </div>
                      
                      <p className="text-xs text-slate-400 mt-0.5 leading-relaxed">
                        {item.description}
                      </p>

                      <div className="flex items-center justify-between mt-2 pt-1 text-[11px] text-slate-500 font-mono">
                        <span>{item.time}</span>
                        <button
                          onClick={() => removeNotification(item.id)}
                          className="text-slate-500 hover:text-rose-400 p-1 transition-colors"
                          aria-label="Hapus"
                        >
                          <Trash2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </div>
                  </div>
                ))
              )}
            </div>

            {/* Footer */}
            <div className="p-3 bg-slate-950/40 border-t border-slate-800 text-center">
              <a href="#all" className="text-xs text-slate-400 hover:text-white font-medium transition-colors">
                Lihat semua di Pengaturan Akun →
              </a>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
```

---

## 4. Checklist UX Notifikasi
1. **Live Region (Screen Reader)**: Panel notifikasi wajib disematkan `aria-live="polite"` agar saat pesan penting masuk, suara layar membacakan pesan tersebut tanpa memotong kalimat pengguna yang sedang aktif.
2. **Scrolling Containment**: Beri `max-h-80` atau `max-h-96` dengan `overflow-y-auto` pada kontainer daftar agar dropdown tidak memanjang melebihi tinggi layar ponsel atau laptop resolusi kecil.
