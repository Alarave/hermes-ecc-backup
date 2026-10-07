# 21st.dev Master Landing Page Shell Templates

Analisis pola dan blueprint arsitektur Landing Page SaaS/Agency berdasarkan 134+ template premium di 21st.dev (khususnya "Northstar - AI Agency & Agent Studio Site").

---

## 1. Lima Seksi Kritis Landing Page Modern (Cinematic Dark Mode)

Sebuah *Landing Page* SaaS atau AI modern (berbayar/premium) tidak lagi menggunakan desain flat putih. Mereka mengandalkan estetika *Cinematic Dark* dengan struktur 5 pilar berikut:

### Pilar 1: The Luminous Hero Section (Puncak)
- **Karakteristik**:
  - Teks *Headline* raksasa di tengah layar menggunakan `bg-clip-text text-transparent bg-gradient-to-br from-white to-slate-500`.
  - Tombol CTA ganda: Primary (Glowing) dan Secondary (Ghost/Outline).
  - Elemen Latar Belakang: Cincin cahaya, *Grid Vignette*, atau *Radial Blur* yang memudar.
  - Video Demo / Mockup Aplikasi di bawah tombol CTA dengan pinggiran bergaya *glassmorphism* atau *3D tilt*.

### Pilar 2: The Monochromatic Logo Cloud (Kepercayaan)
- **Karakteristik**:
  - Deretan logo klien atau teknologi pendukung yang ditampilkan meredup (`opacity-50 grayscale`) dan bersinar ketika dilewati mouse.

### Pilar 3: The Bento Grid Features (Fitur Utama)
- **Karakteristik**:
  - Menggantikan daftar fitur kuno dengan kotak-kotak *Bento* asimetris.
  - Setiap kartu *Bento* memuat simulasi UI mikro (grafik palsu, avatar palsu, cuplikan baris kode).
  - Lihat blueprint master grid di `21st-master-grid-bento-templates.md`.

### Pilar 4: The Marquee Testimonials (Bukti Sosial)
- **Karakteristik**:
  - Barisan kartu ulasan (Avatar, Nama, Jabatan, dan Teks ulasan) yang bergerak terus menerus secara horizontal di layar (*infinite scroll*).
  - Ujung kiri-kanan layar ditutupi dengan gradien pekat agar seolah-olah kartu "masuk dari balik layar gelap".

### Pilar 5: The Magnetic Footer (Aksi Akhir)
- **Karakteristik**:
  - Terletak tepat di atas Footer utama, menyajikan satu CTA raksasa ("Mulai Bersama Kami") yang memikat perhatian sebelum pengunjung meninggalkan situs.

---

## 2. Blueprint Kode Master (The Northstar AI Agency Shell)

```tsx
import React from "react";
import { ArrowRight, Sparkles, Code2, Zap, BrainCircuit, PlayCircle } from "lucide-react";

// Shell Gabungan Landing Page
export function NorthstarLandingPage() {
  return (
    <div className="min-h-screen bg-[#090d16] text-white selection:bg-indigo-500/30 font-sans">
      
      {/* --- BACKGROUND PATTERN --- */}
      <div className="fixed inset-0 z-0 pointer-events-none">
        <div className="absolute top-[-20%] left-[-10%] w-[500px] h-[500px] rounded-full bg-indigo-600/20 blur-[120px]" />
        <div className="absolute top-[20%] right-[-10%] w-[400px] h-[400px] rounded-full bg-purple-600/10 blur-[120px]" />
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#1e293b_1px,transparent_1px),linear-gradient(to_bottom,#1e293b_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] opacity-30" />
      </div>

      {/* --- HEADER NAV --- */}
      <header className="fixed top-0 inset-x-0 z-50 flex items-center justify-between px-6 lg:px-12 py-4 bg-[#090d16]/80 backdrop-blur-md border-b border-white/5">
        <div className="flex items-center gap-2 font-bold text-xl tracking-tighter">
          <BrainCircuit className="text-indigo-500 w-6 h-6" />
          <span>Northstar<span className="text-indigo-500">.</span></span>
        </div>
        <nav className="hidden md:flex items-center gap-8 text-sm font-medium text-slate-400">
          <a href="#solusi" className="hover:text-white transition-colors">Solusi</a>
          <a href="#fitur" className="hover:text-white transition-colors">Fitur Agen</a>
          <a href="#harga" className="hover:text-white transition-colors">Harga</a>
        </nav>
        <button className="px-5 py-2 rounded-full bg-white text-black text-sm font-bold hover:bg-slate-200 transition-colors">
          Mulai Uji Coba
        </button>
      </header>

      {/* --- MAIN CONTENT --- */}
      <main className="relative z-10 pt-32 pb-20 px-6 lg:px-12 flex flex-col items-center text-center">
        
        {/* HERO SECTION */}
        <section className="max-w-4xl mx-auto flex flex-col items-center">
          {/* Pill Badge */}
          <a href="#" className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border border-indigo-500/20 bg-indigo-500/10 text-indigo-300 text-xs font-semibold mb-8 hover:bg-indigo-500/20 transition-colors">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Memperkenalkan Northstar Agent Studio v2.0</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </a>

          {/* Headline */}
          <h1 className="text-5xl md:text-7xl font-black tracking-tighter mb-6 leading-tight">
            Bangun Agen AI Otonom <br className="hidden md:block" />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400">
              Dalam Hitungan Menit.
            </span>
          </h1>

          {/* Sub-headline */}
          <p className="text-lg md:text-xl text-slate-400 max-w-2xl mb-10 leading-relaxed">
            Platform orkestrasi agensi AI pertama yang menyatukan alur kerja bisnis dengan kecerdasan bahasa terpusat tanpa penulisan kode rumit.
          </p>

          {/* CTA Group */}
          <div className="flex flex-col sm:flex-row items-center gap-4 w-full justify-center">
            <button className="w-full sm:w-auto flex items-center justify-center gap-2 px-8 py-4 rounded-full bg-indigo-600 hover:bg-indigo-500 text-white font-bold transition-all shadow-[0_0_30px_rgba(99,102,241,0.3)] hover:shadow-[0_0_40px_rgba(99,102,241,0.5)]">
              Rancang Agen Pertama
              <ArrowRight className="w-4 h-4" />
            </button>
            <button className="w-full sm:w-auto flex items-center justify-center gap-2 px-8 py-4 rounded-full border border-slate-700 bg-slate-900/50 hover:bg-slate-800 text-white font-bold transition-colors">
              <PlayCircle className="w-4 h-4 text-slate-400" />
              Lihat Demo Interaktif
            </button>
          </div>
        </section>

        {/* HERO MOCKUP / VIDEO PREVIEW */}
        <section className="mt-20 w-full max-w-5xl mx-auto perspective-[2000px]">
          <div className="relative rounded-3xl border border-white/10 bg-slate-950 p-2 shadow-2xl overflow-hidden transform rotate-x-[15deg] scale-95 origin-top hover:rotate-x-[5deg] hover:scale-100 transition-all duration-700 ease-out">
            <div className="absolute inset-0 bg-gradient-to-t from-[#090d16] via-transparent to-transparent z-10" />
            <img 
              src="https://images.unsplash.com/photo-1618477247222-ac60ceb0a416?q=80&w=2560&auto=format&fit=crop" 
              alt="Dashboard App" 
              className="rounded-2xl w-full object-cover aspect-video opacity-80"
            />
          </div>
        </section>

        {/* LOGO CLOUD */}
        <section className="mt-32 w-full max-w-4xl border-t border-white/5 pt-12">
          <p className="text-sm font-semibold text-slate-500 uppercase tracking-widest mb-8">
            Dipercaya Oleh Tim Teknologi Perintis
          </p>
          <div className="flex flex-wrap justify-center gap-8 md:gap-16 opacity-50 grayscale">
            {/* Simulasi Logo */}
            {["Acme Corp", "Quantum", "Echo Valley", "Nexus", "Stellar"].map((logo) => (
              <div key={logo} className="text-xl font-black tracking-tighter text-white hover:opacity-100 hover:grayscale-0 transition-all cursor-pointer">
                {logo}
              </div>
            ))}
          </div>
        </section>

      </main>
    </div>
  );
}
```

---

## 3. Strategi Psikologi Landing Page Berlayar Cafe
Jika kita mengadaptasi arsitektur "Northstar" (Template senilai $39 ini) untuk **Berlayar Cafe**, berikut adalah terjemahan konseptualnya:
1. **Hero Gradient**: Ubah warna *glow* dari Indigo/Purple menjadi perpaduan Cokelat Kopi Emas (Amber) dan Senja Laut (Teal).
2. **Pill Badge**: Alih-alih "Memperkenalkan AI", ganti menjadi lencana "Voucher Eksklusif — Terbatas Bulan Ini".
3. **Hero Mockup**: Jangan tampilkan foto dasbor, tapi tampilkan *mockup* layar ponsel (Telegram Bot) berdampingan dengan ilustrasi mesin kasir pintar yang memancarkan struk digital.
4. **Logo Cloud**: Gantikan dengan logo *partner* kopi lokal atau merek *roastery* yang mensuplai biji kopi.
