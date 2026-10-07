# 21st.dev Master Sign-In & Authentication Templates

Analisis pola dan blueprint komponen Sign-In / Login berdasarkan 103+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Sign-In Modern

### Arketipe 1: The Modern Compact Login Card (Standard SaaS)
- **Fungsi**: Alur masuk standar yang cepat dan fokus.
- **Karakteristik Visual**:
  - Kolom Email & Password dengan tautan "Lupa Kata Sandi?" yang diletakkan sejajar dengan label password di sisi kanan atas.
  - Opsi checkbox "Ingat Saya" (Remember me).
  - Tombol aksi primer dengan state loading terintegrasi.
- **Inspirasi**: `Login Card`, `Minimal Auth Page`, `Login Form Card`.

### Arketipe 2: The Passkey / Biometric Sign-In
- **Fungsi**: Login tanpa kata sandi (Passwordless) generasi baru (WebAuthn / FIDO2).
- **Karakteristik Visual**:
  - Terdapat tombol besar atau animasi sensor sidik jari (Fingerprint / Face ID) di tengah kartu.
  - Teks panduan: "Sentuh sensor sidik jari atau gunakan kunci keamanan fisik Anda".
- **Inspirasi**: `Passkey Sign-In`, `Neural Access Login`.

### Arketipe 3: The One-Time Password (OTP) / PIN Card
- **Fungsi**: Verifikasi 2FA atau login instan via kode SMS/WhatsApp/Email.
- **Karakteristik Visual**:
  - 4 sampai 6 kotak input angka terpisah berukuran besar.
  - Auto-focus berurutan (saat mengetik angka pertama, kursor otomatis melompat ke kotak berikutnya).
  - Fitur paste otomatis: jika pengguna menyalin kode 6 digit, semua kotak terisi seketika.
- **Inspirasi**: `One Time Password Sign In Card`, `Push Approval Card`.

### Arketipe 4: The Enterprise SSO Login (Single Sign-On)
- **Fungsi**: Autentikasi untuk karyawan perusahaan besar (B2B).
- **Karakteristik Visual**:
  - Hanya meminta alamat email kerja pengguna.
  - Sistem mendeteksi domain perusahaan (misal `@google.com` atau `@acme.corp`) lalu mengalihkan pengguna ke portal SSO Okta/Microsoft Azure/Google Workspace.
- **Inspirasi**: `Login with SSO`.

---

## 2. Blueprint Kode Master (The 6-Digit OTP / PIN Input)

Pola interaksi OTP adalah komponen yang paling sering dicari dan membutuhkan penanganan UX keyboard yang sangat presisi:

```tsx
import React, { useState, useRef } from "react";
import { ArrowRight, ShieldCheck } from "lucide-react";

export function OTPVerificationCard({ length = 6, onComplete }: { length?: number; onComplete?: (code: string) => void }) {
  const [otp, setOtp] = useState<string[]>(new Array(length).fill(""));
  const inputRefs = useRef<(HTMLInputElement | null)[]>([]);

  const handleChange = (element: HTMLInputElement, index: number) => {
    const val = element.value;
    if (isNaN(Number(val))) return; // Hanya izinkan angka

    const newOtp = [...otp];
    newOtp[index] = val.substring(val.length - 1); // Ambil digit terakhir
    setOtp(newOtp);

    // Auto-focus ke input berikutnya
    if (val && index < length - 1 && inputRefs.current[index + 1]) {
      inputRefs.current[index + 1]?.focus();
    }

    // Panggil callback jika semua terisi
    if (newOtp.every((digit) => digit !== "")) {
      onComplete?.(newOtp.join(""));
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>, index: number) => {
    // Backspace handling: kembali ke input sebelumnya jika kosong
    if (e.key === "Backspace" && !otp[index] && index > 0) {
      inputRefs.current[index - 1]?.focus();
    }
  };

  const handlePaste = (e: React.ClipboardEvent<HTMLInputElement>) => {
    e.preventDefault();
    const pasteData = e.clipboardData.getData("text").trim().slice(0, length);
    if (!/^\d+$/.test(pasteData)) return; // Validasi angka saja

    const newOtp = pasteData.split("");
    while (newOtp.length < length) newOtp.push("");
    setOtp(newOtp);

    // Fokus ke kotak terakhir yang belum diisi atau kotak paling akhir
    const nextIndex = Math.min(pasteData.length, length - 1);
    inputRefs.current[nextIndex]?.focus();

    if (pasteData.length === length) {
      onComplete?.(pasteData);
    }
  };

  return (
    <div className="w-full max-w-md mx-auto p-8 rounded-3xl border border-slate-800 bg-slate-900/80 backdrop-blur-xl text-center">
      
      {/* Icon */}
      <div className="inline-flex items-center justify-center w-12 h-12 rounded-2xl bg-indigo-500/10 text-indigo-400 mb-4 border border-indigo-500/20">
        <ShieldCheck className="w-6 h-6" />
      </div>

      <h3 className="text-xl font-bold text-white tracking-tight">Verifikasi Akses</h3>
      <p className="text-xs text-slate-400 mt-1.5 mb-8">
        Masukkan 6 digit kode keamanan yang kami kirimkan ke perangkat Anda.
      </p>

      {/* Input PIN Digits */}
      <div className="flex items-center justify-center gap-2 sm:gap-3 mb-8">
        {otp.map((digit, i) => (
          <input
            key={i}
            ref={(el) => (inputRefs.current[i] = el)}
            type="text"
            inputMode="numeric"
            maxLength={1}
            value={digit}
            onChange={(e) => handleChange(e.target, i)}
            onKeyDown={(e) => handleKeyDown(e, i)}
            onPaste={handlePaste}
            className="w-11 h-13 sm:w-12 sm:h-14 text-center text-lg sm:text-xl font-mono font-bold text-slate-100 rounded-xl border border-slate-700/80 bg-slate-950/60 focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 outline-none transition-all"
          />
        ))}
      </div>

      {/* Submit Button */}
      <button
        disabled={otp.some((d) => d === "")}
        onClick={() => onComplete?.(otp.join(""))}
        className="w-full py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 disabled:bg-slate-800 disabled:text-slate-600 text-white text-sm font-semibold shadow-lg shadow-indigo-600/25 transition-all flex items-center justify-center gap-2"
      >
        <span>Verifikasi & Masuk</span>
        <ArrowRight className="w-4 h-4" />
      </button>

      {/* Resend Link */}
      <p className="text-xs text-slate-500 mt-6">
        Tidak menerima kode?{" "}
        <button className="text-indigo-400 font-medium hover:underline focus:outline-none">
          Kirim Ulang
        </button>
      </p>

    </div>
  );
}
```

---

## 3. Checklist UX Sign-In Modern
1. **Atribut Autocomplete**: Gunakan `autoComplete="current-password"` pada field kata sandi untuk memberi sinyal ke browser/1Password/Bitwarden agar otomatis mengisi credentials.
2. **InputMode Numeric untuk PIN**: Pada OTP, selalu gunakan `inputMode="numeric"` agar keyboard smartphone otomatis memunculkan keypad angka bukan huruf.
3. **Inline Error Feedback**: Tampilkan pesan error di bawah field secara langsung (merah) tanpa menghilangkan email yang sudah diketik pengguna saat password salah.
