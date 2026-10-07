# 21st.dev Master Modal & Dialog Templates

Analisis pola dan blueprint komponen Modal / Dialog berdasarkan 328+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Modal Modern

### Arketipe 1: The Progressive Blur Backdrop Modal
- **Fungsi**: Dialog sentral standar untuk pembuatan item baru (New Workspace, Create Project) atau modal otentikasi.
- **Karakteristik Visual**:
  - Latar belakang (*Backdrop*) tidak sekadar hitam gelap (`bg-black/50`), tetapi juga memiliki efek buram (*backdrop-blur*) yang menyembunyikan elemen halaman di belakangnya dengan elegan.
  - Kartu modal menggunakan efek *Glassmorphism* (`bg-slate-900/90 border-slate-800`).
- **Inspirasi**: `Progressive Blur Modal (pate1kiran)`, `Modal Card (Berat Berkay)`.

### Arketipe 2: The Destructive Alert Dialog (Type-to-Confirm)
- **Fungsi**: Konfirmasi penghapusan data kritis atau keluar dari akun (*Logout / Delete Account*).
- **Karakteristik Visual**:
  - Ikon peringatan berwarna merah/koral.
  - Sering kali dilengkapi tantangan ketik: *"Ketik 'HAPUS BERLAYAR CAFE' untuk melanjutkan"*.
  - Tombol aksi destruktif berada di sisi kanan (warna merah), berdampingan dengan tombol batal.
- **Inspirasi**: `Logout Confirmation Dialog (Cnippet)`, `Type to confirm (felipemenezes098)`.

### Arketipe 3: The Scrollable Drawer (Slide-Over)
- **Fungsi**: Formulir panjang, panel pengaturan fitur, atau filter tabel yang memakan ruang tinggi.
- **Karakteristik Visual**:
  - Bukan melayang di tengah, melainkan meluncur (*slide-in*) dari sisi kanan atau kiri layar yang memenuhi tinggi penuh (`h-screen`).
  - Memiliki header yang menempel (*sticky*) dan area konten yang dapat digulir (*scrollable*).
- **Inspirasi**: `HeroUI Drawer (Hero Ui)`.

### Arketipe 4: The Dotted / Spotlight Dialog
- **Fungsi**: Dialog pengumuman fitur baru atau pembaruan persyaratan layanan (*Terms & Conditions*).
- **Karakteristik Visual**: Latar belakang kartu modal memiliki dekorasi pola titik-titik (*dot matrix*) atau pendar cahaya (*spotlight*) untuk menegaskan fokus desain.

---

## 2. Blueprint Kode Master (The Progressive Blur Alert Dialog)

```tsx
import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { AlertTriangle, X } from "lucide-react";

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: () => void;
  title?: string;
  description?: string;
  confirmText?: string;
  isDestructive?: boolean;
}

export function BlurAlertDialog({
  isOpen,
  onClose,
  onConfirm,
  title = "Hapus Proyek Ini?",
  description = "Aksi ini tidak dapat dibatalkan. Semua data, pengaturan, dan riwayat tugas yang terkait dengan proyek ini akan dihapus secara permanen dari peladen kami.",
  confirmText = "Ya, Hapus Permanen",
  isDestructive = true,
}: ModalProps) {
  
  // Mengunci scroll background ketika modal terbuka
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "unset";
    }
    return () => {
      document.body.style.overflow = "unset";
    };
  }, [isOpen]);

  // Menutup dengan tombol Escape
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape" && isOpen) onClose();
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
          
          {/* Progressive Blur Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
            onClick={onClose}
            className="absolute inset-0 bg-slate-950/60 backdrop-blur-sm"
            aria-hidden="true"
          />

          {/* Dialog Card */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 10 }}
            transition={{ type: "spring", damping: 25, stiffness: 300 }}
            role="alertdialog"
            aria-modal="true"
            className="relative w-full max-w-md overflow-hidden rounded-3xl border border-slate-800 bg-slate-900 shadow-2xl"
          >
            {/* Spotlight Accent */}
            <div className={`absolute top-0 left-1/2 -translate-x-1/2 w-64 h-32 rounded-full blur-3xl opacity-20 pointer-events-none ${isDestructive ? 'bg-rose-500' : 'bg-indigo-500'}`} />

            {/* Header */}
            <div className="flex items-start justify-between px-6 pt-6 pb-4">
              <div className={`w-12 h-12 rounded-2xl flex items-center justify-center border shadow-inner ${
                isDestructive 
                  ? "bg-rose-500/10 border-rose-500/20 text-rose-400" 
                  : "bg-indigo-500/10 border-indigo-500/20 text-indigo-400"
              }`}>
                <AlertTriangle className="w-6 h-6" />
              </div>
              <button 
                onClick={onClose}
                className="p-1.5 rounded-xl text-slate-500 hover:bg-slate-800 hover:text-slate-300 transition-colors"
                aria-label="Tutup dialog"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {/* Content */}
            <div className="px-6 pb-6 relative z-10">
              <h2 className="text-lg font-bold text-white mb-2">{title}</h2>
              <p className="text-sm text-slate-400 leading-relaxed">
                {description}
              </p>
            </div>

            {/* Footer Actions */}
            <div className="flex items-center justify-end gap-3 px-6 py-4 bg-slate-950/50 border-t border-slate-800/80">
              <button
                onClick={onClose}
                className="px-4 py-2 rounded-xl text-sm font-medium text-slate-300 hover:bg-slate-800 transition-colors"
              >
                Batal
              </button>
              <button
                onClick={onConfirm}
                className={`px-5 py-2 rounded-xl text-sm font-semibold text-white shadow-lg transition-all ${
                  isDestructive 
                    ? "bg-rose-600 hover:bg-rose-500 shadow-rose-600/20" 
                    : "bg-indigo-600 hover:bg-indigo-500 shadow-indigo-600/20"
                }`}
              >
                {confirmText}
              </button>
            </div>
          </motion.div>

        </div>
      )}
    </AnimatePresence>
  );
}
```

---

## 3. Checklist Aksesibilitas Modal (WAI-ARIA & UX)
1. **Fokus Trap (Focus Lock)**: 
   - Modal WAJIB mengunci *tab focus* di dalam kartunya. Jika pengguna terus menekan `Tab`, fokus harus berputar dari tombol Batal → tombol Hapus → Batal, tidak boleh melompat ke elemen di belakang layar (Background).
2. **Kunci Scroll Layar (`overflow: hidden`)**: 
   - Seperti yang diterapkan dalam blueprint (`document.body.style.overflow = "hidden"`), cegah latar belakang halaman bergulir ke atas/bawah ketika pengguna sedang berusaha menscroll teks panjang di dalam modal.
3. **Penyelarasan Warna Berbasis Tindakan**: 
   - Aksi destruktif (Menghapus Data) harus menggunakan palet merah (`rose` / `red`).
   - Aksi progresif (Menyimpan / Menyetujui) harus menggunakan palet merek utama (`indigo` / `emerald`).
