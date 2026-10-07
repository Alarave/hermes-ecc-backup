# 21st.dev Master Toast & Notification Templates

Analisis pola dan blueprint komponen Toast (Alerts & Notifications) berdasarkan 61+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion / Sonner).

---

## 1. Empat Arketipe Toast UI/UX Modern

### Arketipe 1: The Stacked Toast (Sonner-style)
- **Fungsi**: Notifikasi beruntun yang tidak memenuhi layar.
- **Karakteristik**: Menggantikan list vertikal biasa dengan efek tumpukan kartu (stacking). Toast baru muncul di depan, menekan toast lama ke belakang dengan efek *scale down* dan *translate-y*.
- **Inspirasi**: `Sonner Custom Toast (Bundui.io)`, `Sonner Promise Toast`.

### Arketipe 2: The Action / Promise Toast
- **Fungsi**: Memberikan umpan balik (feedback) pada aksi pengguna dan status asinkron (loading, success, error).
- **Karakteristik**: 
  - **Promise State**: Menampilkan *spinner* saat proses berjalan, lalu berubah halus menjadi ikon centang (success) atau silang (error).
  - **Action Button**: Memiliki tombol kecil sekunder seperti `Undo`, `View`, atau `Retry`.
- **Inspirasi**: `Save Changes Toast`, `Google Drive Uploader Toast`, `Unsaved Changes Reminder Toast`.

### Arketipe 3: The Gamified / Rich Context Toast
- **Fungsi**: Notifikasi yang merayakan pencapaian atau menampilkan data kompleks.
- **Karakteristik**: Memuat Avatar, progres bar, atau lencana (badge) khusus.
- **Inspirasi**: `Achievement Unlocked (trophyso)`, `8-bit Toast (OrcDev)`, `Reshaped Toast / Avatar`.

### Arketipe 4: The Banner / Persistent Toast
- **Fungsi**: Konfirmasi penting yang membutuhkan aksi eksplisit dari pengguna.
- **Karakteristik**: Tidak hilang secara otomatis (no auto-dismiss). Sering digunakan untuk Cookie Banner atau peringatan form yang belum disimpan.

---

## 2. Standar Aksesibilitas Toast (WAI-ARIA)
Agar notifikasi layar ramah terhadap pengguna *Screen Reader*:
1. **Atribut `role="status"` atau `role="alert"`**: 
   - Gunakan `status` untuk notifikasi sukses (tidak mengganggu apa yang sedang dibaca).
   - Gunakan `alert` untuk error kritis (langsung membajak perhatian *screen reader*).
2. **`aria-live="polite"` vs `"assertive"`**: Toast biasa menggunakan `polite`, sementara pesan kritis menggunakan `assertive`.
3. **Fokus pada Action**: Jika toast memiliki tombol (misal: "Undo"), pastikan dapat dijangkau menggunakan tombol `Tab`. Waktu tampil (*duration*) sebaiknya lebih lama jika ada tombol aksi (minimal 5000ms - 8000ms).

---

## 3. Blueprint Kode Master (The Modern Action & Promise Toast)

Alih-alih membuat sistem *context* Toast kompleks dari nol (yang disarankan menggunakan library `sonner`), berikut adalah blueprint komponen UI fisik untuk satu Toast Item bergaya 21st.dev menggunakan **Framer Motion**:

```tsx
import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { CheckCircle2, AlertCircle, Loader2, X } from "lucide-react";

export type ToastStatus = "success" | "error" | "loading" | "info";

interface ModernToastProps {
  id: string;
  title: string;
  description?: string;
  status: ToastStatus;
  action?: {
    label: string;
    onClick: () => void;
  };
  onClose: (id: string) => void;
}

export function ModernToast({ id, title, description, status, action, onClose }: ModernToastProps) {
  // Auto dismiss setelah 5 detik jika bukan loading
  useEffect(() => {
    if (status !== "loading") {
      const timer = setTimeout(() => onClose(id), 5000);
      return () => clearTimeout(timer);
    }
  }, [id, status, onClose]);

  const getIcon = () => {
    switch (status) {
      case "success": return <CheckCircle2 className="w-5 h-5 text-emerald-500" />;
      case "error": return <AlertCircle className="w-5 h-5 text-rose-500" />;
      case "loading": return <Loader2 className="w-5 h-5 text-indigo-400 animate-spin" />;
      case "info": return <AlertCircle className="w-5 h-5 text-sky-400" />;
    }
  };

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 50, scale: 0.9 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, y: 20, scale: 0.9 }}
      transition={{ type: "spring", stiffness: 400, damping: 25 }}
      role={status === "error" ? "alert" : "status"}
      aria-live={status === "error" ? "assertive" : "polite"}
      className="relative flex items-start gap-4 p-4 w-full sm:w-[380px] rounded-2xl border border-slate-800 bg-slate-900/90 backdrop-blur-xl shadow-[0_8px_30px_rgb(0,0,0,0.12)] pointer-events-auto"
    >
      {/* Icon Area */}
      <div className="flex-shrink-0 mt-0.5">
        {getIcon()}
      </div>

      {/* Content Area */}
      <div className="flex-1 min-w-0">
        <h4 className="text-sm font-semibold text-slate-200">{title}</h4>
        {description && (
          <p className="mt-1 text-sm text-slate-400 line-clamp-2 leading-relaxed">
            {description}
          </p>
        )}
        
        {/* Action Button (e.g. Undo, Retry) */}
        {action && status !== "loading" && (
          <button
            onClick={action.onClick}
            className="mt-3 text-sm font-semibold text-indigo-400 hover:text-indigo-300 transition-colors focus:outline-none focus:underline"
          >
            {action.label}
          </button>
        )}
      </div>

      {/* Close Button */}
      <button
        onClick={() => onClose(id)}
        className="flex-shrink-0 p-1 rounded-md text-slate-500 hover:text-slate-300 hover:bg-slate-800 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500"
        aria-label="Close notification"
      >
        <X className="w-4 h-4" />
      </button>
    </motion.div>
  );
}
```

### Konfigurasi Global Wrapper (The Toast Container)
Untuk membuat efek notifikasi bertumpuk di sudut bawah layar:

```tsx
<div className="fixed bottom-0 right-0 z-50 p-4 sm:p-6 flex flex-col gap-3 pointer-events-none">
  <AnimatePresence mode="popLayout">
    {/* Looping dari Toast Context / State Manager */}
    {toasts.map((toast) => (
      <ModernToast key={toast.id} {...toast} />
    ))}
  </AnimatePresence>
</div>
```
