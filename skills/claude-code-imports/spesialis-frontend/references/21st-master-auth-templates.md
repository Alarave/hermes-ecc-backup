# 21st.dev Master Sign-Up & Auth Templates

Analisis pola dan blueprint komponen Registrasi / Sign-Up / Auth berdasarkan 63+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion / Zod).

---

## 1. Empat Arketipe Sign-Up Modern

### Arketipe 1: The Split-Screen Auth (Brand Hero + Form)
- **Fungsi**: Registrasi SaaS berkonversi tinggi.
- **Karakteristik Visual**:
  - Kolom Kiri (50%): Form registrasi (Social OAuth, email/password input, checkbox terms).
  - Kolom Kanan (50%): Testimonial terpercaya, visual animasi 3D, atau quote pelanggan dengan background gradien/mesh gelap.
- **Inspirasi**: `Auth Section 1 (solaceui)`, `Full Screen Signup (Preet Suthar)`.

### Arketipe 2: The Aceternity Glowing Card (Centered Modal / Card)
- **Fungsi**: Onboarding cepat dengan friksi rendah.
- **Karakteristik Visual**:
  - Kartu tunggal di tengah layar berlatar belakang *dot grid* atau *radial glow*.
  - Tombol Sosial (Google & GitHub) di bagian atas dengan efek *hover border glow*.
  - Pembatas teks horizontal ("OR CONTINUE WITH").
  - Input field dengan efek *focus beam / subtle glow*.
- **Inspirasi**: `Signup Form (Manu Arora)`, `Login Card Signup Form (Ephraim Duncan)`.

### Arketipe 3: The Multi-Step Onboarding Wizard
- **Fungsi**: Pendaftaran yang memerlukan pengumpulan profil (nama, nama tim/organisasi, tujuan penggunaan).
- **Karakteristik Visual**:
  - Memiliki *stepper progress indicator* di atas (Step 1 of 3).
  - Transisi slide horizontal antar langkah (*slide left/right*) menggunakan Framer Motion `AnimatePresence`.
- **Inspirasi**: `Onboarding Wizard Form (Cnippet)`, `Onboarding Form (Ravi Katiyar)`.

### Arketipe 4: The Fluid Auth Switch (Morphing Card)
- **Fungsi**: Menggabungkan halaman Sign In dan Sign Up dalam satu komponen tanpa refresh halaman.
- **Karakteristik Visual**: Menggunakan tab segmented control di atas kartu untuk beralih antara "Log In" dan "Sign Up", di mana kolom form beradaptasi secara mulus.

---

## 2. Standar Keamanan & Aksesibilitas Form Registrasi
1. **WCAG 2.2 SC 3.3.8 (Accessible Authentication)**:
   - Hindari tes kognitif (seperti puzzle CAPTCHA rumit).
   - Pastikan field input mendukung *copy-paste* dan *password managers* (jangan matikan fitur paste pada kolom kata sandi).
   - Gunakan atribut autocomplete yang tepat: `autocomplete="email"` dan `autocomplete="new-password"`.
2. **Password Visibility Toggle**:
   - Selalu sediakan tombol ikon mata (Show/Hide Password) agar pengguna tidak frustrasi saat salah mengetik sandi di perangkat mobile.
3. **Password Strength Indicator**:
   - Tampilkan baris indikator kekuatan sandi (lemah, sedang, kuat) secara real-time saat pengguna mengetik, bukan setelah menekan tombol submit.

---

## 3. Blueprint Kode Master (The Glowing Centered Card Sign-Up)

```tsx
import { useState } from "react";
import { Eye, EyeOff, ArrowRight } from "lucide-react";

export function ModernSignUpCard() {
  const [showPassword, setShowPassword] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Kirim data ke auth handler
    console.log({ email, password });
  };

  return (
    <div className="relative w-full max-w-md mx-auto p-8 rounded-3xl border border-slate-800 bg-slate-900/70 backdrop-blur-xl shadow-2xl">
      
      {/* Header */}
      <div className="text-center mb-8">
        <div className="inline-flex items-center justify-center w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 mb-4 font-bold text-lg font-mono">
          B
        </div>
        <h2 className="text-2xl font-bold tracking-tight text-white">Buat Akun Baru</h2>
        <p className="text-sm text-slate-400 mt-1">Mulai akses sesi deterministik Anda dalam hitungan detik.</p>
      </div>

      {/* Social Logins */}
      <div className="grid grid-cols-2 gap-3 mb-6">
        <button className="flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl border border-slate-800 bg-slate-800/40 hover:bg-slate-800 text-xs font-medium text-slate-200 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500">
          <span>Google</span>
        </button>
        <button className="flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl border border-slate-800 bg-slate-800/40 hover:bg-slate-800 text-xs font-medium text-slate-200 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500">
          <span>GitHub</span>
        </button>
      </div>

      {/* Divider */}
      <div className="relative flex items-center justify-center mb-6">
        <div className="w-full border-t border-slate-800" />
        <span className="absolute px-3 bg-slate-900 text-[11px] font-mono uppercase tracking-wider text-slate-500">
          Atau Email
        </span>
      </div>

      {/* Form */}
      <form onSubmit={handleSubmit} className="space-y-4">
        
        {/* Email Field */}
        <div className="space-y-1.5">
          <label className="text-xs font-medium text-slate-300">Alamat Email</label>
          <input
            type="email"
            required
            autoComplete="email"
            placeholder="nama@perusahaan.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full px-4 py-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all"
          />
        </div>

        {/* Password Field */}
        <div className="space-y-1.5">
          <label className="text-xs font-medium text-slate-300">Kata Sandi</label>
          <div className="relative">
            <input
              type={showPassword ? "text" : "password"}
              required
              autoComplete="new-password"
              placeholder="Minimal 8 karakter"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full pl-4 pr-10 py-2.5 rounded-xl border border-slate-800 bg-slate-950/60 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all"
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300 transition-colors focus:outline-none"
              aria-label={showPassword ? "Hide password" : "Show password"}
            >
              {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
            </button>
          </div>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="w-full mt-2 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold shadow-lg shadow-indigo-600/25 transition-all active:scale-[0.98] flex items-center justify-center gap-2 group"
        >
          <span>Daftar Akun</span>
          <ArrowRight className="w-4 h-4 text-indigo-200 group-hover:translate-x-0.5 transition-transform" />
        </button>
      </form>

      {/* Footer / Login Link */}
      <p className="text-center text-xs text-slate-400 mt-6">
        Sudah memiliki akun?{" "}
        <a href="#login" className="text-indigo-400 font-medium hover:underline">
          Masuk di sini
        </a>
      </p>

    </div>
  );
}
```
