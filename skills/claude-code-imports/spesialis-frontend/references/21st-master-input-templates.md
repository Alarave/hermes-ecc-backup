# 21st.dev Master Input & Form Field Templates

Analisis pola dan blueprint komponen Input berdasarkan 949+ komponen terpopuler di 21st.dev (React + Tailwind v4 + Lucide Icons).

---

## 1. Empat Arketipe Input Modern

### Arketipe 1: The Password Input with Strength Meter & Visibility Toggle
- **Fungsi**: Pendaftaran kata sandi akun dengan umpan balik keamanan instan (*real-time password strength validation*).
- **Karakteristik Visual**:
  - Kolom teks dengan ikon kunci gembok (`Lock`) di sisi kiri.
  - Ikon mata (`Eye` / `EyeOff`) di sisi kanan untuk melihat/menyembunyikan teks sandi.
  - Bilah kekuatan 4 segmen di bawah kolom (Lemah - Merah, Sedang - Kuning, Kuat - Hijau) yang bergerak secara dinamis sesuai kompleksitas karakter yang diketik.
- **Inspirasi**: `Input with Password Strength Indicator (Origin UI)`, `Password Input (Abraham)`.

### Arketipe 2: The 6-Digit OTP / PIN Verification Grid
- **Fungsi**: Verifikasi 2FA, kode login SMS, atau token otentikasi.
- **Karakteristik Visual**:
  - Terdiri dari 6 kotak persegi terpisah (`w-12 h-14`).
  - Mendukung input paste otomatis (*auto-pasting* teks 6 digit langsung mengisi semua kotak).
  - Kotak aktif memiliki cincin pendar (*focus-visible:ring-2 ring-indigo-500*).
- **Inspirasi**: `Input OTPs (ShadcnStudio)`, `ReUI Input OTP (Sean Hello)`.

### Arketipe 3: The Input Group with Prefix / Suffix Addons
- **Fungsi**: Input nominal mata uang, domain web, atau URL media sosial.
- **Karakteristik Visual**:
  - Kolom teks menyatu dengan label addon abu-abu di sisi luar atau dalam (misal: `https://` di awal atau `.com` di akhir).
  - Terdapat tombol hapus instan (*Clear Button*) '✕' saat pengguna mulai mengetik teks.
- **Inspirasi**: `Input Group (shadcn)`, `Input with End Select (Origin UI)`.

### Arketipe 4: The Tag / Chip Input
- **Fungsi**: Pengisian kata kunci tagar (*meta tags*), kategori produk, atau daftar email penerima.
- **Karakteristik Visual**:
  - Mengetik teks lalu menekan tombol `Enter` atau koma (`,`) langsung mengubah teks menjadi pil badge yang memiliki tombol hapus silang.
- **Inspirasi**: `Tags Input (ui layout)`, `Tag Input Form (shadcn)`.

---

## 2. Blueprint Kode Master

### A. The Password Input with Live Strength Bar
```tsx
import { useState } from "react";
import { Eye, EyeOff, Lock, Check } from "lucide-react";

export function PasswordInputWithStrength() {
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  // Evaluasi skor kekuatan kata sandi sederhana (0 - 4)
  const getStrength = (pass: string) => {
    let score = 0;
    if (pass.length >= 8) score++;
    if (/[A-Z]/.test(pass)) score++;
    if (/[0-9]/.test(pass)) score++;
    if (/[^A-Za-z0-9]/.test(pass)) score++;
    return score;
  };

  const strength = getStrength(password);

  const getStrengthColor = () => {
    if (strength === 0) return "bg-slate-800";
    if (strength <= 2) return "bg-rose-500";
    if (strength === 3) return "bg-amber-500";
    return "bg-emerald-500";
  };

  return (
    <div className="w-full max-w-sm space-y-2">
      <label className="text-xs font-semibold text-slate-300">Kata Sandi</label>
      
      {/* Input Container */}
      <div className="relative">
        <Lock className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-500" />
        <input
          type={showPassword ? "text" : "password"}
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Minimal 8 karakter..."
          className="w-full pl-10 pr-10 py-2.5 rounded-xl border border-slate-800 bg-slate-900/60 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all font-sans"
        />
        <button
          type="button"
          onClick={() => setShowPassword(!showPassword)}
          className="absolute right-3 top-1/2 -translate-y-1/2 p-1 text-slate-500 hover:text-slate-300 transition-colors"
          aria-label={showPassword ? "Sembunyikan sandi" : "Tampilkan sandi"}
        >
          {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
        </button>
      </div>

      {/* Strength Segments */}
      {password.length > 0 && (
        <div className="pt-1">
          <div className="grid grid-cols-4 gap-1.5 h-1 w-full">
            {[1, 2, 3, 4].map((step) => (
              <div
                key={step}
                className={`h-full rounded-full transition-colors duration-300 ${
                  strength >= step ? getStrengthColor() : "bg-slate-800"
                }`}
              />
            ))}
          </div>
          <p className="text-[10px] text-slate-400 mt-1.5 font-mono">
            Kekuatan:{" "}
            <span className="font-semibold text-slate-200">
              {strength <= 1 ? "Sangat Lemah" : strength <= 2 ? "Sedang" : strength === 3 ? "Kuat" : "Sangat Aman"}
            </span>
          </p>
        </div>
      )}
    </div>
  );
}
```

### B. The Segmented 6-Digit OTP Field (Auto-Advance)
```tsx
import { useState, useRef } from "react";

export function SixDigitOtpInput({ onComplete }: { onComplete?: (code: string) => void }) {
  const [otp, setOtp] = useState(["", "", "", "", "", ""]);
  const inputsRef = useRef<(HTMLInputElement | null)[]>([]);

  const handleChange = (val: string, index: number) => {
    // Hanya izinkan angka/karakter tunggal
    const char = val.slice(-1);
    const newOtp = [...otp];
    newOtp[index] = char;
    setOtp(newOtp);

    // Otomatis lompat ke kotak berikutnya jika diisi
    if (char && index < 5) {
      inputsRef.current[index + 1]?.focus();
    }

    if (newOtp.every((d) => d !== "")) {
      onComplete?.(newOtp.join(""));
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>, index: number) => {
    // Otomatis kembali ke kotak sebelumnya jika menekan Backspace pada kotak kosong
    if (e.key === "Backspace" && !otp[index] && index > 0) {
      inputsRef.current[index - 1]?.focus();
    }
  };

  const handlePaste = (e: React.ClipboardEvent) => {
    e.preventDefault();
    const pastedData = e.clipboardData.getData("text").slice(0, 6).split("");
    const newOtp = [...otp];
    pastedData.forEach((char, i) => {
      newOtp[i] = char;
    });
    setOtp(newOtp);
    inputsRef.current[Math.min(pastedData.length, 5)]?.focus();
    if (newOtp.every((d) => d !== "")) onComplete?.(newOtp.join(""));
  };

  return (
    <div className="flex items-center gap-2" onPaste={handlePaste}>
      {otp.map((digit, i) => (
        <input
          key={i}
          ref={(el) => { inputsRef.current[i] = el; }}
          type="text"
          inputMode="numeric"
          maxLength={1}
          value={digit}
          onChange={(e) => handleChange(e.target.value, i)}
          onKeyDown={(e) => handleKeyDown(e, i)}
          className="w-11 h-14 text-center text-lg font-mono font-bold text-white bg-slate-900 border border-slate-800 rounded-xl focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-all"
        />
      ))}
    </div>
  );
}
```

---

## 3. Checklist UX Input & Form
1. **Atribut Mobile `inputMode`**: Untuk input nomor HP atau kode PIN/OTP, pasang selalu `inputMode="numeric"` agar ponsel otomatis memunculkan papan angka (NumPad), bukan keyboard alfabet lengkap.
2. **Keterkaitan Label Form (`htmlFor` dan `id`)**: Pastikan teks `<label>` terhubung langsung ke `<input>` dengan atribut `htmlFor="input-id"` untuk memenuhi kepatuhan WCAG tingkat AA.
3. **Pesan Validasi Error yang Manusiawi**: Tampilkan teks pesan error merah di bawah kolom input dengan penjelasan solusi nyata (misal: bukan sekadar *"Format salah"*, tetapi *"Format email harus menyertakan tanda '@'"*).
