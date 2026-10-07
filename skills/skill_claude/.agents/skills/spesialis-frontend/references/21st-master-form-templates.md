# 21st.dev Master Form & Multi-Step Wizard Templates

Analisis pola dan blueprint komponen Form & Multi-Step Wizard berdasarkan 1.5K+ komponen formulir di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Form Modern

### Arketipe 1: The Multi-Step Wizard Form (Progressive Disclosure)
- **Fungsi**: Formulir registrasi panjang, pembuatan organisasi/workspace baru, atau pengajuan data kompleks agar pengguna tidak merasa kewalahan (*cognitive overload*).
- **Karakteristik Visual**:
  - Bilah indikator tahapan di atas (*Step 1 → Step 2 → Step 3*).
  - Konten langkah bertransisi menggunakan animasi geser horizontal halus (*Framer Motion slide animation*).
  - Tombol navigasi "Kembali" (abu-abu/ghost) dan "Lanjut / Simpan" (warna primer).
- **Inspirasi**: `Multi-step Wizard (Dhileep Kumar GM)`, `Onboarding Wizard Form (Cnippet)`.

### Arketipe 2: The Inline Waitlist / Lead Capture Form
- **Fungsi**: Pengumpulan email prospek peluncuran produk di seksi Hero *Landing Page*.
- **Karakteristik Visual**:
  - Kolom input email yang menyatu secara elegan dengan tombol aksi di dalam satu kontainer kapsul membulat (`rounded-full p-1.5 border border-slate-800 bg-slate-900/80`).
  - Umpan balik sukses instan (*inline success message*) tanpa berpindah halaman (*AJAX/Fetch*).
- **Inspirasi**: `Waitlist 1 (Efferd)`.

### Arketipe 3: The Split-Screen Contact / Enterprise Inquiry Form
- **Fungsi**: Halaman kontak atau demo produk B2B ("Jadwalkan Konsultasi").
- **Karakteristik Visual**:
  - Sisi Kiri: Formulir lengkap (Nama, Email Perusahaan, Ukuran Tim, Pesan/Kebutuhan).
  - Sisi Kanan: Kartu testimoni pelanggan terpercaya, daftar logo mitra, dan kutipan jaminan keamanan data.
- **Inspirasi**: `Contact Page (Efferd)`, `Simple Contact Us Form (prebuiltui)`.

### Arketipe 4: The Settings Form with Sticky Action Bar
- **Fungsi**: Halaman preferensi akun, integrasi domain, atau konfigurasi profil pengguna.
- **Karakteristik Visual**:
  - Bidang isian terbagi dalam kartu-kartu grup logis yang rapi.
  - Saat ada perubahan data yang belum tersimpan, muncul bilah aksi melayang di bagian bawah layar (*Sticky Floating Save Bar*: "Perubahan belum disimpan — Simpan / Batal").

---

## 2. Blueprint Kode Master (The Modern Multi-Step Wizard)

```tsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Check, ArrowRight, ArrowLeft, Building2, User, CreditCard } from "lucide-react";

const STEPS = [
  { id: 1, name: "Profil Pribadi", icon: User },
  { id: 2, name: "Data Tim", icon: Building2 },
  { id: 3, name: "Konfirmasi", icon: CreditCard },
];

export function MultiStepWizardForm() {
  const [currentStep, setCurrentStep] = useState(1);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    teamName: "",
    plan: "developer",
  });

  const nextStep = () => setCurrentStep((prev) => Math.min(prev + 1, STEPS.length));
  const prevStep = () => setCurrentStep((prev) => Math.max(prev - 1, 1));

  return (
    <div className="w-full max-w-xl mx-auto p-6 md:p-8 rounded-3xl border border-slate-800 bg-slate-900/90 shadow-2xl backdrop-blur-xl">
      {/* Stepper Header */}
      <div className="flex items-center justify-between mb-8 pb-6 border-b border-slate-800">
        {STEPS.map((step, idx) => {
          const Icon = step.icon;
          const isCompleted = currentStep > step.id;
          const isActive = currentStep === step.id;

          return (
            <div key={step.id} className="flex items-center gap-3">
              <div
                className={`w-9 h-9 rounded-xl flex items-center justify-center text-xs font-bold transition-all duration-300 ${
                  isCompleted
                    ? "bg-emerald-500 text-white"
                    : isActive
                    ? "bg-indigo-600 text-white shadow-lg shadow-indigo-500/25 ring-2 ring-indigo-500/40"
                    : "bg-slate-800 text-slate-500"
                }`}
              >
                {isCompleted ? <Check className="w-4 h-4" /> : <Icon className="w-4 h-4" />}
              </div>

              <div className="hidden sm:block text-left">
                <p className="text-[10px] font-mono text-slate-500 uppercase">Langkah 0{step.id}</p>
                <p className={`text-xs font-semibold ${isActive ? "text-white" : "text-slate-400"}`}>
                  {step.name}
                </p>
              </div>

              {idx < STEPS.length - 1 && (
                <div className="hidden sm:block w-8 h-[1px] bg-slate-800 mx-2" />
              )}
            </div>
          );
        })}
      </div>

      {/* Dynamic Step Content */}
      <div className="min-h-[220px]">
        <AnimatePresence mode="wait">
          {currentStep === 1 && (
            <motion.div
              key="step-1"
              initial={{ opacity: 0, x: 15 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -15 }}
              transition={{ duration: 0.2 }}
              className="space-y-4"
            >
              <div>
                <label className="text-xs font-semibold text-slate-300">Nama Lengkap</label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  placeholder="Misal: Firman"
                  className="w-full mt-1.5 px-3.5 py-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
                />
              </div>

              <div>
                <label className="text-xs font-semibold text-slate-300">Email Kerja</label>
                <input
                  type="email"
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  placeholder="nama@perusahaan.com"
                  className="w-full mt-1.5 px-3.5 py-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
                />
              </div>
            </motion.div>
          )}

          {currentStep === 2 && (
            <motion.div
              key="step-2"
              initial={{ opacity: 0, x: 15 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -15 }}
              transition={{ duration: 0.2 }}
              className="space-y-4"
            >
              <div>
                <label className="text-xs font-semibold text-slate-300">Nama Organisasi / Proyek</label>
                <input
                  type="text"
                  value={formData.teamName}
                  onChange={(e) => setFormData({ ...formData, teamName: e.target.value })}
                  placeholder="Misal: Berlayar Cafe"
                  className="w-full mt-1.5 px-3.5 py-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
                />
              </div>

              <div>
                <label className="text-xs font-semibold text-slate-300">Peran Anda</label>
                <select className="w-full mt-1.5 px-3.5 py-2.5 rounded-xl border border-slate-800 bg-slate-950 text-sm text-white focus:outline-none focus:border-indigo-500">
                  <option>Software Architect / Lead</option>
                  <option>Product Manager</option>
                  <option>Founder / Exec</option>
                </select>
              </div>
            </motion.div>
          )}

          {currentStep === 3 && (
            <motion.div
              key="step-3"
              initial={{ opacity: 0, x: 15 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -15 }}
              transition={{ duration: 0.2 }}
              className="p-5 rounded-2xl bg-slate-950/60 border border-slate-800 space-y-3 font-mono text-xs"
            >
              <div className="flex justify-between text-slate-400">
                <span>Nama:</span>
                <span className="text-white font-sans">{formData.name || "-"}</span>
              </div>
              <div className="flex justify-between text-slate-400">
                <span>Email:</span>
                <span className="text-white font-sans">{formData.email || "-"}</span>
              </div>
              <div className="flex justify-between text-slate-400">
                <span>Workspace:</span>
                <span className="text-white font-sans">{formData.teamName || "-"}</span>
              </div>
              <p className="text-[11px] text-slate-500 pt-2 border-t border-slate-800 font-sans">
                Pastikan data di atas sudah akurat sebelum menyelesaikan konfigurasi akhir.
              </p>
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Navigation Buttons Footer */}
      <div className="mt-8 pt-6 border-t border-slate-800 flex items-center justify-between">
        <button
          onClick={prevStep}
          disabled={currentStep === 1}
          className="flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition-colors disabled:opacity-0 disabled:pointer-events-none"
        >
          <ArrowLeft className="w-3.5 h-3.5" />
          <span>Kembali</span>
        </button>

        {currentStep < STEPS.length ? (
          <button
            onClick={nextStep}
            className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold transition-all shadow-lg shadow-indigo-600/20"
          >
            <span>Lanjutkan</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        ) : (
          <button
            onClick={() => alert("Formulir Terkirim!")}
            className="flex items-center gap-2 px-6 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold transition-all shadow-lg shadow-emerald-600/20"
          >
            <span>Selesaikan Setup</span>
            <Check className="w-3.5 h-3.5" />
          </button>
        )}
      </div>
    </div>
  );
}
```

---

## 3. Checklist Aksesibilitas Formulir (WAI-ARIA)
1. **Penanganan Validasi Keyboard**: Form harus dapat diselesaikan dari awal hingga akhir hanya menggunakan tombol `Tab` dan `Enter`.
2. **Pengumuman Error Form**: Jika input wajib belum diisi saat menekan tombol Lanjut, pasang atribut `aria-invalid="true"` pada kolom terkait dan arahkan fokus keyboard (*auto-focus*) langsung ke kolom error pertama.
3. **Pemberitahuan Status Tahapan**: Gunakan `aria-live="polite"` pada judul langkah agar pembaca layar otomatis mengumumkan *"Langkah 2: Data Tim"* saat pengguna berpindah slide.
