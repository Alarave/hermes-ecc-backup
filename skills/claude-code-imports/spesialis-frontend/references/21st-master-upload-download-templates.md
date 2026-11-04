# 21st.dev Master File Upload & Download Templates

Analisis pola dan blueprint komponen Upload & Download berdasarkan 154+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Upload & Download Modern

### Arketipe 1: The Interactive Drag-and-Drop Dropzone with Progress
- **Fungsi**: Pengunggahan dokumen (PDF, CSV, ZIP) atau banyak berkas (*multi-file upload*).
- **Karakteristik Visual**:
  - Kontainer bergaris putus-putus (*dashed border*).
  - Saat file diseret (*drag-over*), border berpendar biru/indigo dengan latar belakang transparan yang menyala halus.
  - Kartu daftar file yang sedang diunggah menampilkan nama file, ekstensi ikon, ukuran (misal: "2.4 MB"), bilah progres persentase, dan tombol batal/hapus silang.
- **Inspirasi**: `Animated File Upload (Edu Calvo)`, `File Upload (extend-hq)`.

### Arketipe 2: The Avatar Image Upload & Live Crop
- **Fungsi**: Penggantian foto profil pengguna di menu pengaturan akun.
- **Karakteristik Visual**:
  - Avatar bundar yang memiliki lapisan overlay gelap saat di-hover beserta ikon kamera (`Camera`).
  - Menampilkan pratinjau instan (*Instant Image Preview*) begitu pengguna memilih file foto dari komputer mereka.
- **Inspirasi**: `Avatar Upload (Abraham)`.

### Arketipe 3: The Downloadable Asset Card (Voucher / Invoice / Report)
- **Fungsi**: Menampilkan berkas siap unduh (misal: "Struk Voucher Kopi Berlayar Cafe .PDF" atau "Laporan Penjualan .CSV").
- **Karakteristik Visual**:
  - Kartu baris horizontal memuat lencana tipe file berwarna (Merah untuk PDF, Hijau untuk XLS/CSV), nama berkas, ukuran, dan tombol "Unduh" dengan animasi spinner saat berkas sedang di-*generate*.
- **Inspirasi**: `File Card Collections (Faisal Amir)`.

### Arketipe 4: The Chat Attachment Trigger
- **Fungsi**: Mengunggah berkas lampiran di dalam bilah obrolan AI / Messenger.
- **Karakteristik Visual**: Tombol klip kertas (`Paperclip`) kecil yang tersembunyi elegan di samping input teks, mendukung penempelan gambar via clipboard (*Paste to Upload*).
- **Inspirasi**: `AI Input With File (Kokonut Baffier)`, `Attachment Button (Serafim)`.

---

## 2. Blueprint Kode Master (The Drag-and-Drop Uploader with Live Progress)

```tsx
import { useState, useRef } from "react";
import { UploadCloud, FileText, CheckCircle2, X, AlertCircle } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface UploadedFile {
  name: string;
  size: string;
  progress: number;
  status: "uploading" | "complete" | "error";
}

export function FileDropzoneUploader() {
  const [isDragging, setIsDragging] = useState(false);
  const [file, setFile] = useState<UploadedFile | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const simulateUpload = (fileName: string, fileSize: number) => {
    const formattedSize = (fileSize / (1024 * 1024)).toFixed(2) + " MB";
    setFile({ name: fileName, size: formattedSize, progress: 10, status: "uploading" });

    const interval = setInterval(() => {
      setFile((prev) => {
        if (!prev) return null;
        if (prev.progress >= 100) {
          clearInterval(interval);
          return { ...prev, progress: 100, status: "complete" };
        }
        return { ...prev, progress: prev.progress + 20 };
      });
    }, 250);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const droppedFile = e.dataTransfer.files[0];
      simulateUpload(droppedFile.name, droppedFile.size);
    }
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const selected = e.target.files[0];
      simulateUpload(selected.name, selected.size);
    }
  };

  return (
    <div className="w-full max-w-md p-6 rounded-3xl border border-slate-800 bg-slate-900 shadow-2xl">
      <h3 className="text-sm font-bold text-white mb-1">Unggah Berkas</h3>
      <p className="text-xs text-slate-400 mb-4">Mendukung format PDF, PNG, atau CSV (Maks 10MB).</p>

      {/* Hidden Native Input */}
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileSelect}
        className="hidden"
        accept=".pdf,.png,.csv"
      />

      {/* Drag and Drop Box */}
      <div
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
        className={`relative flex flex-col items-center justify-center p-8 rounded-2xl border-2 border-dashed cursor-pointer transition-all duration-300 ${
          isDragging
            ? "border-indigo-500 bg-indigo-500/10 scale-[1.01]"
            : "border-slate-800 bg-slate-950/40 hover:border-slate-700 hover:bg-slate-950/70"
        }`}
      >
        <div className="w-12 h-12 rounded-2xl bg-slate-800/80 border border-slate-700/60 flex items-center justify-center text-slate-300 mb-3 shadow-inner">
          <UploadCloud className="w-6 h-6 text-indigo-400" />
        </div>
        <p className="text-xs font-semibold text-slate-200">
          <span className="text-indigo-400 hover:underline">Pilih berkas</span> atau seret ke sini
        </p>
        <p className="text-[11px] text-slate-500 mt-1 font-mono">Tarik berkas Anda ke area ini</p>
      </div>

      {/* Upload Progress Card */}
      <AnimatePresence>
        {file && (
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95 }}
            className="mt-4 p-3.5 rounded-xl border border-slate-800 bg-slate-950/60 flex items-start gap-3"
          >
            <div className="p-2 rounded-lg bg-slate-800 text-indigo-400 shrink-0 mt-0.5">
              <FileText className="w-4 h-4" />
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-center justify-between">
                <p className="text-xs font-semibold text-white truncate max-w-[200px]">
                  {file.name}
                </p>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    setFile(null);
                  }}
                  className="text-slate-500 hover:text-rose-400 transition-colors"
                >
                  <X className="w-3.5 h-3.5" />
                </button>
              </div>

              <div className="flex items-center justify-between text-[11px] font-mono text-slate-500 mt-1 mb-1.5">
                <span>{file.size}</span>
                <span className={file.status === "complete" ? "text-emerald-400" : "text-indigo-400"}>
                  {file.status === "complete" ? "Selesai" : `${file.progress}%`}
                </span>
              </div>

              {/* Progress Line */}
              <div className="w-full h-1 bg-slate-800 rounded-full overflow-hidden">
                <div
                  className={`h-full transition-all duration-300 rounded-full ${
                    file.status === "complete" ? "bg-emerald-500" : "bg-indigo-500"
                  }`}
                  style={{ width: `${file.progress}%` }}
                />
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
```

---

## 3. Checklist UX File Upload & Download
1. **Validasi MIME Type di Sisi Klien**: Selalu periksa ekstensi dan ukuran berkas (`file.size > 10 * 1024 * 1024`) seketika di peramban pengguna sebelum data mulai dikirim ke server untuk menghemat bandwidth.
2. **Indikator Keyboard Access**: Kontainer dropzone wajib memiliki atribut `tabIndex={0}` dan mendengarkan tombol `Enter` / `Space` agar pengguna yang menavigasi tanpa mouse tetap bisa membuka dialog pemilih file.
3. **Pembersihan URL Blob (Memory Leak)**: Jika Anda membuat pratinjau gambar dengan `URL.createObjectURL(file)`, pastikan untuk memanggil `URL.revokeObjectURL()` saat komponen di-unmount agar tidak menimbulkan kebocoran memori pada browser.
