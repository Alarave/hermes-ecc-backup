# 21st.dev Master Bento Grid & Layout Templates

Analisis pola dan blueprint komponen Grid & Bento Box berdasarkan 620+ komponen modern di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe Grid & Bento Modern

### Arketipe 1: The Asymmetric SaaS Bento Grid (Feature Showcase)
- **Fungsi**: Memamerkan fitur-fitur andalan platform dengan variasi ukuran kartu (besar, sedang, tinggi). Menggantikan deretan kartu 3-kolom yang membosankan.
- **Karakteristik Visual**:
  - Grid responsif berbasis Tailwind CSS (`grid grid-cols-1 md:grid-cols-3 gap-4`).
  - Kartu utama memakan 2 kolom (`md:col-span-2`), sedangkan kartu penunjang memakan 1 kolom (`md:col-span-1`).
  - Setiap kartu memiliki efek batas halus, latar belakang kaca (*Glassmorphism*), dan grafis mini interaktif di dalamnya (grafik mini, sakelar toggle, atau simulasi kode).
- **Inspirasi**: `Ruixen Bento Cards`, `Feature Section with Bento Grid (Tommy Jepsen)`.

### Arketipe 2: The Vignette Grid Pattern Background
- **Fungsi**: Pola latar belakang geometris yang elegan untuk bagian Hero atau seluruh halaman web.
- **Karakteristik Visual**:
  - Pola kotak-kotak halus (Grid Lines) atau titik-titik (Dot Matrix) berbasis SVG murni.
  - Dilengkapi *Radial Gradient Mask* (`mask-image: radial-gradient(ellipse at center, black, transparent 75%)`) sehingga garis-garis kotak hanya terlihat jelas di tengah dan memudar secara dramatis di tepian layar.
- **Inspirasi**: `Grid Background (meghtrix)`, `Vignette Grid Background (Rushil Dhinoja)`.

### Arketipe 3: The Monochrome Logo Cloud Grid
- **Fungsi**: Menampilkan daftar mitra kerja sama, klien, atau investor (*Social Proof*).
- **Karakteristik Visual**:
  - Grid 4 atau 6 kolom berisi logo monokrom abu-abu (`opacity-50 grayscale`).
  - Saat kursor mouse menyorot (*hover*), logo kembali ke warna aslinya dan bersinar lembut (`group-hover:opacity-100 group-hover:grayscale-0 transition-all`).
- **Inspirasi**: `Logo Cloud 2 (Efferd)`.

### Arketipe 4: The Masonry / Staggered Testimonials Grid
- **Fungsi**: Menampilkan ulasan testimoni atau tangkapan layar kartu portofolio dengan tinggi bervariasi tanpa menyisakan ruang kosong bolong.
- **Karakteristik Visual**: Menggunakan CSS Columns (`columns-1 md:columns-2 lg:columns-3 gap-4 space-y-4`).

---

## 2. Blueprint Kode Master (The Modern SaaS Bento Grid)

```tsx
import { Sparkles, Zap, ShieldCheck, BarChart3, ArrowRight } from "lucide-react";

export function ModernBentoGrid() {
  return (
    <section className="py-16 px-4 max-w-6xl mx-auto">
      {/* Section Header */}
      <div className="text-center max-w-2xl mx-auto mb-12">
        <span className="text-xs font-mono font-semibold px-3 py-1 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
          FITUR UNGGULAN
        </span>
        <h2 className="text-3xl font-black text-white mt-3 tracking-tight">
          Dirancang untuk Kecepatan & Presisi
        </h2>
        <p className="text-sm text-slate-400 mt-2">
          Eksplorasi infrastruktur dan kemampuan antarmuka modern kami dalam satu ekosistem terpadu.
        </p>
      </div>

      {/* Bento Grid Canvas */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 auto-rows-[280px]">
        
        {/* Card 1: Large Featured Card (Span 2 Columns) */}
        <div className="md:col-span-2 relative p-6 rounded-3xl border border-slate-800 bg-slate-900/60 overflow-hidden group hover:border-slate-700 transition-all flex flex-col justify-between">
          {/* Subtle Ambient Glow */}
          <div className="absolute top-0 right-0 w-80 h-80 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none group-hover:bg-indigo-500/15 transition-all" />
          
          <div>
            <div className="w-10 h-10 rounded-xl bg-indigo-500/20 border border-indigo-500/30 flex items-center justify-center text-indigo-400 mb-4">
              <Zap className="w-5 h-5" />
            </div>
            <h3 className="text-xl font-bold text-white">Performa Instan Sub-detik</h3>
            <p className="text-xs text-slate-400 mt-1 max-w-md leading-relaxed">
              Arsitektur kode dioptimalkan untuk menjaga Web Vitals (INP di bawah 200ms) tanpa frame drop.
            </p>
          </div>

          {/* Interactive Simulation / Visual Mockup */}
          <div className="mt-4 p-4 rounded-2xl bg-slate-950/80 border border-slate-800/80 flex items-center justify-between font-mono text-xs text-slate-400">
            <span className="flex items-center gap-2 text-emerald-400">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
              99.98% System Uptime
            </span>
            <span className="text-slate-500">Latency: 14ms</span>
          </div>
        </div>

        {/* Card 2: Tall/Single Column Card */}
        <div className="md:col-span-1 relative p-6 rounded-3xl border border-slate-800 bg-slate-900/60 overflow-hidden group hover:border-slate-700 transition-all flex flex-col justify-between">
          <div>
            <div className="w-10 h-10 rounded-xl bg-purple-500/20 border border-purple-500/30 flex items-center justify-center text-purple-400 mb-4">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-white">Standar Keamanan Ketat</h3>
            <p className="text-xs text-slate-400 mt-1 leading-relaxed">
              Enkripsi end-to-end dengan validasi berbasis zero-trust architecture.
            </p>
          </div>

          <div className="flex items-center gap-2 pt-4 border-t border-slate-800/60 text-xs font-semibold text-purple-400">
            <span>Pelajari Protokol</span>
            <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
          </div>
        </div>

        {/* Card 3: Single Column Card */}
        <div className="md:col-span-1 relative p-6 rounded-3xl border border-slate-800 bg-slate-900/60 overflow-hidden group hover:border-slate-700 transition-all flex flex-col justify-between">
          <div>
            <div className="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/30 flex items-center justify-center text-amber-400 mb-4">
              <BarChart3 className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-white">Analitik Waktu Nyata</h3>
            <p className="text-xs text-slate-400 mt-1 leading-relaxed">
              Pemantauan transaksi dan aliran pengunjung yang diperbarui seketika.
            </p>
          </div>

          <div className="h-12 flex items-end gap-1.5 pt-2">
            {[35, 60, 45, 80, 65, 95, 75].map((val, i) => (
              <div 
                key={i} 
                className="flex-1 bg-amber-500/30 hover:bg-amber-400 transition-all rounded-t"
                style={{ height: `${val}%` }}
              />
            ))}
          </div>
        </div>

        {/* Card 4: Double Column Card */}
        <div className="md:col-span-2 relative p-6 rounded-3xl border border-slate-800 bg-slate-900/60 overflow-hidden group hover:border-slate-700 transition-all flex flex-col justify-between">
          <div className="flex items-start justify-between">
            <div>
              <div className="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-emerald-400 mb-4">
                <Sparkles className="w-5 h-5" />
              </div>
              <h3 className="text-xl font-bold text-white">Kecerdasan Agen Terintegrasi</h3>
              <p className="text-xs text-slate-400 mt-1 max-w-md leading-relaxed">
                Menghubungkan alur kerja otomatisasi dengan kemampuan LLM dan retrieval data berkecepatan tinggi.
              </p>
            </div>
          </div>

          <div className="mt-4 flex items-center justify-between text-xs text-slate-400 font-mono pt-4 border-t border-slate-800/60">
            <span>Model: Deterministic Hybrid</span>
            <span className="text-emerald-400">Active Node</span>
          </div>
        </div>

      </div>
    </section>
  );
}
```

---

## 3. Background Pattern Snippet (The Vignette Grid)
```tsx
export function VignetteGridBackground({ children }: { children: React.ReactNode }) {
  return (
    <div className="relative min-h-screen w-full bg-[#090d16] text-white">
      {/* Background Grid Pattern with Radial Mask */}
      <div 
        className="absolute inset-0 bg-[linear-gradient(to_right,#1f293d_1px,transparent_1px),linear-gradient(to_bottom,#1f293d_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] pointer-events-none" 
      />
      {/* Foreground Content */}
      <div className="relative z-10">
        {children}
      </div>
    </div>
  );
}
```

---

## 4. Checklist UX Bento & Grid Layouts
1. **Aturan Responsif Mutlak**: Jangan pernah mempertahankan `grid-cols-3` pada tampilan ponsel. Selalu mulai dari mobile-first: `grid-cols-1`, lalu buka ke `md:grid-cols-3` di layar tablet/desktop.
2. **Ketinggian Baris yang Konsisten**: Terapkan utilitas seperti `auto-rows-[280px]` pada kontainer grid agar kartu-kartu yang berjejer memiliki ritme vertikal yang simetris dan rapi.
3. **Peredam Beban GPU**: Gunakan `pointer-events-none` pada semua elemen *Ambient Glow Blur* atau *Grid Lines Background* agar scroll mouse tetap mulus tanpa terbebani rendering berlebih.
