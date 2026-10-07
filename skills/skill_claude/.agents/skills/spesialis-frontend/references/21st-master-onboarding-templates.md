# 21st.dev Master Onboarding Templates

Analisis pola dan blueprint komponen Onboarding berdasarkan 53+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Onboarding Modern

### Arketipe 1: The Setup Checklist (Task Tracker)
- **Fungsi**: Mendorong pengguna baru untuk menyelesaikan profil atau pengaturan awal dengan prinsip psikologis *Endowed Progress Effect* (misal: "Anda sudah selesai 1 dari 4 langkah").
- **Karakteristik Visual**:
  - Kartu melayang (Widget) berisi bilah progres (Progress Bar).
  - Daftar periksa vertikal dengan ikon centang (`CheckCircle`) atau kotak kosong (`Circle`).
  - Baris tugas yang sudah selesai (*completed*) sering kali meredup (*opacity-50*) atau memiliki teks coret (*line-through*).
- **Inspirasi**: `Onboarding Checklist (Caio Bonato / Ravi Katiyar)`.

### Arketipe 2: The Multi-Step Welcome Modal (Carousel)
- **Fungsi**: Layar sapaan pertama setelah pendaftaran sukses. Menjelaskan nilai jual utama produk dalam 3-4 slide ringkas.
- **Karakteristik Visual**:
  - Dialog Modal yang muncul di tengah layar.
  - Ilustrasi besar atau *Lottie animation* di bagian atas, diikuti judul, deskripsi, dan tombol navigasi ("Lanjut").
  - Terdapat indikator titik (Dot Pagination) di bagian bawah.
- **Inspirasi**: `Welcome Modal (Ravi Katiyar)`, `Onboarding Dialog (Patrick Xin)`.

### Arketipe 3: The Permission Request Pre-prompt
- **Fungsi**: Meminta izin sensitif (Kamera, Mikrofon, Lokasi, atau Notifikasi) dengan bahasa manusia sebelum memicu jendela popup bawaan browser yang terkesan mengintimidasi.
- **Karakteristik Visual**: Kartu simpel dengan ikon hardware (Kamera/Lonceng) yang bergoyang pelan, teks penjelasan rasional mengapa izin tersebut dibutuhkan, dan tombol "Izinkan" / "Nanti".
- **Inspirasi**: `Camera Permission Request Card (Ahmed Mayara)`.

### Arketipe 4: The Interactive Tech Stack / Config Builder
- **Fungsi**: Personalisasi pengalaman (*Personalization Engine*). Bertanya kepada pengguna "Apa peran Anda?" atau "Alat apa yang Anda gunakan?" untuk menyesuaikan dashboard.
- **Karakteristik Visual**: Kisi-kisi kotak (Grid Bento) logo teknologi atau label peran yang bisa dipilih multi-klik (*multi-select chips*).

---

## 2. Blueprint Kode Master (The Setup Checklist Widget)

```tsx
import { useState } from "react";
import { CheckCircle2, Circle, Trophy, ArrowRight } from "lucide-react";

interface Task {
  id: string;
  title: string;
  description: string;
  completed: boolean;
}

const INITIAL_TASKS: Task[] = [
  { id: "1", title: "Lengkapi Profil", description: "Tambahkan foto dan peran Anda.", completed: true },
  { id: "2", title: "Undang Tim", description: "Kolaborasi lebih baik bersama rekan.", completed: false },
  { id: "3", title: "Buat Proyek Pertama", description: "Mulai pelacakan dan analitik Anda.", completed: false },
];

export function OnboardingChecklist() {
  const [tasks, setTasks] = useState<Task[]>(INITIAL_TASKS);

  const completedCount = tasks.filter((t) => t.completed).length;
  const progressPercent = Math.round((completedCount / tasks.length) * 100);
  const isAllDone = completedCount === tasks.length;

  const toggleTask = (id: string) => {
    setTasks(tasks.map((t) => (t.id === id ? { ...t, completed: !t.completed } : t)));
  };

  return (
    <div className="w-full max-w-sm p-5 rounded-2xl border border-slate-800 bg-slate-900 shadow-xl">
      {/* Header & Progress */}
      <div className="flex items-start justify-between mb-4">
        <div>
          <h3 className="text-sm font-bold text-white flex items-center gap-2">
            Panduan Memulai
            {isAllDone && <Trophy className="w-4 h-4 text-amber-400" />}
          </h3>
          <p className="text-xs text-slate-400 mt-1">
            {completedCount} dari {tasks.length} langkah diselesaikan
          </p>
        </div>
        <span className="text-xs font-mono font-semibold text-indigo-400">{progressPercent}%</span>
      </div>

      {/* Progress Bar Track */}
      <div className="w-full h-1.5 bg-slate-800 rounded-full overflow-hidden mb-5">
        <div 
          className="h-full bg-gradient-to-r from-indigo-500 to-purple-500 transition-all duration-700 ease-out rounded-full"
          style={{ width: `${progressPercent}%` }}
        />
      </div>

      {/* Tasks List */}
      <div className="space-y-3">
        {tasks.map((task) => (
          <button
            key={task.id}
            onClick={() => toggleTask(task.id)}
            className={`w-full flex items-start gap-3 p-3 rounded-xl border text-left transition-all ${
              task.completed 
                ? "border-emerald-500/20 bg-emerald-500/5 hover:bg-emerald-500/10" 
                : "border-slate-800 bg-slate-800/40 hover:bg-slate-800/80 hover:border-slate-700"
            }`}
          >
            {task.completed ? (
              <CheckCircle2 className="w-5 h-5 text-emerald-500 shrink-0 mt-0.5" />
            ) : (
              <Circle className="w-5 h-5 text-slate-500 shrink-0 mt-0.5" />
            )}
            
            <div>
              <h4 className={`text-sm font-semibold transition-colors ${task.completed ? "text-emerald-400 line-through opacity-70" : "text-slate-200"}`}>
                {task.title}
              </h4>
              <p className="text-xs text-slate-500 mt-0.5 leading-relaxed">
                {task.description}
              </p>
            </div>
          </button>
        ))}
      </div>

      {/* Action Footer */}
      {isAllDone && (
        <div className="mt-5 pt-4 border-t border-slate-800 animate-in fade-in slide-in-from-bottom-2">
          <button className="w-full flex items-center justify-center gap-2 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold transition-colors">
            Masuk ke Dashboard
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      )}
    </div>
  );
}
```

---

## 3. Checklist UX Onboarding Ekstra
1. **Penyembunyian Otomatis (Auto-Dismissal)**: Jika Onboarding Checklist ini berada di layar beranda dashboard, ia harus menyediakan tombol "Tutup" atau menyembunyikan diri secara permanen (simpan di database/lokal) ketika progres mencapai 100%.
2. **Konteks Izin Hardware**: Untuk arketipe *Permission Request*, hindari memaksa izin (misal notifikasi) segera setelah *Sign Up*. Minta izin **hanya saat pengguna benar-benar menekan tombol fitur** yang membutuhkannya (misal menekan ikon 🔔).
