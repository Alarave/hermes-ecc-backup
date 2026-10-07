# 21st.dev Master Developer Portfolio Blueprint (Victor Eke Architecture)

Analisis pola arsitektur portfolio pribadi Software Engineer / Developer berdasarkan referensi populer open-source Victor Eke di 21st.dev (Next.js, Sanity/MDX, Tailwind CSS, Lucide Icons).

---

## 1. Karakteristik Developer Personal Portfolio

Berbeda dengan studio kreatif agensi (yang menonjolkan visual mewah dan video), portofolio personal seorang insinyur perangkat lunak memiliki karakteristik fungsional yang berakar pada kredibilitas teknis:

1. **Biografi Langsung & Status Ketersediaan (Availability Beacon)**:
   - Menampilkan status ketersediaan kerja aktif dengan titik hijau berdenyut (*pulsing green dot*): "Available for freelance / full-time".
2. **Koleksi Proyek Berbasis Stack Nyata**:
   - Kartu proyek menampilkan gambar mockup, deskripsi singkat, tag teknologi yang dipakai (misal: React, TypeScript, PostgreSQL), serta tombol langsung ke repositori GitHub dan live demo.
3. **Pilar Artikel Teknis / Tulisan Blog**:
   - Menunjukkan kapasitas pemikiran insinyur melalui tulisan atau dokumentasi pembelajaran.
4. **Setup / Stack Peralatan Kerja (Gear & Tools)**:
   - Sesi opsional namun populer yang merinci perangkat keras dan piranti lunak yang digunakan sehari-hari.

---

## 2. Blueprint Kode Master (The Developer Portfolio Shell)

```tsx
import React from "react";
import { 
  Github, 
  Twitter, 
  Linkedin, 
  Mail, 
  ArrowUpRight, 
  Code2, 
  Briefcase, 
  BookOpen, 
  Layers 
} from "lucide-react";

interface Project {
  title: string;
  description: string;
  tags: string[];
  githubUrl?: string;
  liveUrl?: string;
  image: string;
}

const FEATURED_PROJECTS: Project[] = [
  {
    title: "Berlayar Cafe POS & Voucher Engine",
    description: "Sistem kasir cerdas berbasis kupon termal dengan integrasi akses satu kali ke model AI lokal.",
    tags: ["React 19", "Tailwind v4", "TypeScript", "Hermes Agent"],
    githubUrl: "https://github.com",
    liveUrl: "https://berlayar.cafe",
    image: "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?q=80&w=800&auto=format&fit=crop",
  },
  {
    title: "Aspect-Based Sentiment Mining EV",
    description: "Pipeline penambangan sentimen ulasan kendaraan listrik berbahasa Mandarin dan Indonesia berbasis LLM.",
    tags: ["Python", "PyTorch", "FastAPI", "React"],
    githubUrl: "https://github.com",
    image: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=800&auto=format&fit=crop",
  },
];

export function DeveloperPortfolio() {
  return (
    <div className="min-h-screen bg-[#0a0a0c] text-neutral-200 font-sans selection:bg-indigo-500/30">
      
      {/* Container Lebar Tengah Bersih */}
      <div className="max-w-3xl mx-auto px-6 py-20">
        
        {/* PROFILE HEADER */}
        <header className="flex flex-col-reverse sm:flex-row sm:items-center justify-between gap-6 pb-12 border-b border-neutral-800">
          <div>
            <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white mb-2">
              Firman
            </h1>
            <p className="text-neutral-400 text-base leading-relaxed mb-4">
              Software Engineer & Frontend Specialist. Membangun antarmuka modular, performan, dan sistem cerdas berbasis AI.
            </p>

            {/* Status Ketersediaan */}
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-mono">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
              <span>Tersedia untuk proyek baru</span>
            </div>
          </div>

          {/* Avatar / Foto Profil */}
          <div className="w-24 h-24 rounded-2xl overflow-hidden border border-neutral-700 bg-neutral-900 shrink-0">
            <img 
              src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=400&auto=format&fit=crop" 
              alt="Foto Profil" 
              className="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-300"
            />
          </div>
        </header>

        {/* TAUTAN SOSIAL / GITHUB */}
        <div className="flex items-center gap-4 py-6 border-b border-neutral-800 text-neutral-400 text-sm">
          <a href="https://github.com" target="_blank" rel="noreferrer" className="flex items-center gap-1.5 hover:text-white transition-colors">
            <Github className="w-4 h-4" />
            <span>GitHub</span>
          </a>
          <a href="https://linkedin.com" target="_blank" rel="noreferrer" className="flex items-center gap-1.5 hover:text-white transition-colors">
            <Linkedin className="w-4 h-4" />
            <span>LinkedIn</span>
          </a>
          <a href="mailto:hello@example.com" className="flex items-center gap-1.5 hover:text-white transition-colors">
            <Mail className="w-4 h-4" />
            <span>Email</span>
          </a>
        </div>

        {/* PROYEK PILIHAN */}
        <section className="py-12 border-b border-neutral-800">
          <div className="flex items-center justify-between mb-8">
            <h2 className="text-xl font-bold text-white flex items-center gap-2">
              <Code2 className="w-5 h-5 text-indigo-400" />
              Proyek Pilihan
            </h2>
          </div>

          <div className="flex flex-col gap-8">
            {FEATURED_PROJECTS.map((proj) => (
              <div 
                key={proj.title}
                className="group p-5 rounded-2xl border border-neutral-800/80 bg-neutral-900/40 hover:bg-neutral-900/80 hover:border-neutral-700 transition-all flex flex-col sm:flex-row gap-6"
              >
                <div className="w-full sm:w-44 h-32 rounded-xl overflow-hidden bg-neutral-950 shrink-0 border border-neutral-800">
                  <img src={proj.image} alt={proj.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                </div>

                <div className="flex flex-col justify-between flex-1">
                  <div>
                    <div className="flex items-center justify-between gap-2 mb-2">
                      <h3 className="font-bold text-white text-lg group-hover:text-indigo-400 transition-colors">
                        {proj.title}
                      </h3>
                      {proj.liveUrl && (
                        <a href={proj.liveUrl} target="_blank" rel="noreferrer" className="text-neutral-400 hover:text-white">
                          <ArrowUpRight className="w-4 h-4" />
                        </a>
                      )}
                    </div>
                    <p className="text-neutral-400 text-sm leading-relaxed mb-4">
                      {proj.description}
                    </p>
                  </div>

                  <div className="flex flex-wrap gap-2">
                    {proj.tags.map((tag) => (
                      <span key={tag} className="px-2 py-0.5 rounded-md bg-neutral-800 text-[11px] font-mono text-neutral-300">
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* RIWAYAT PENGALAMAN / KARIER RINGKAS */}
        <section className="py-12 border-b border-neutral-800">
          <h2 className="text-xl font-bold text-white flex items-center gap-2 mb-6">
            <Briefcase className="w-5 h-5 text-indigo-400" />
            Pengalaman
          </h2>

          <div className="space-y-6">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1">
              <div>
                <h4 className="font-semibold text-white">Lead Frontend Engineer</h4>
                <p className="text-sm text-neutral-400">Berlayar Studio Labs</p>
              </div>
              <span className="text-xs font-mono text-neutral-500">2024 — Sekarang</span>
            </div>

            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1">
              <div>
                <h4 className="font-semibold text-white">Data Mining Specialist (USB Team)</h4>
                <p className="text-sm text-neutral-400">Universitas Gunadarma</p>
              </div>
              <span className="text-xs font-mono text-neutral-500">2025 — 2026</span>
            </div>
          </div>
        </section>

        {/* FOOTER */}
        <footer className="pt-12 text-center text-xs font-mono text-neutral-600">
          <p>© 2026 Firman. Dibuat dengan React 19 & Tailwind v4.</p>
        </footer>

      </div>
    </div>
  );
}
```

---

## 3. Perbedaan Pola Desain (Creative Studio vs Personal Developer)
- **Creative Studio (AURA)**: Mengutamakan tipografi raksasa, kursor custom, dan transisi visual eksperimental untuk menarik agensi dan desainer.
- **Developer Portfolio (Victor Eke)**: Mengutamakan format linear vertikal terfokus (`max-w-3xl`), keterbacaan tinggi, stack badges (`React`, `TypeScript`), dan tautan langsung ke kode sumber (GitHub / Live Demo).
