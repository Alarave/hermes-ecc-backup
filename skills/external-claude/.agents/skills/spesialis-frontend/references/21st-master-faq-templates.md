# 21st.dev Master FAQ Templates

Kumpulan blueprint komponen FAQ bergaya 21st.dev (React + Tailwind v4 + Framer Motion). Template ini dirancang modular agar bisa disesuaikan dengan berbagai kebutuhan (dari halaman pendaftaran sederhana hingga platform SaaS kompleks).

---

## Tipe 1: The Floating Card / Separate Card Accordion
**Inspirasi**: *Separate Card-Based Accordion (shadcn / Origin UI)*
**Kapan Digunakan**: Halaman landing utama, pricing page, atau layout dengan latar belakang (background) gelap/bertekstur.
**Karakteristik UX**: Setiap pertanyaan memiliki batas kotak (card) sendiri. Menggunakan indikator Plus/Minus.

```tsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Plus, Minus } from "lucide-react";

export function FloatingCardFAQ({ faqs }) {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  return (
    <div className="w-full max-w-3xl mx-auto space-y-3">
      {faqs.map((faq, i) => {
        const isOpen = openIndex === i;
        return (
          <div 
            key={i} 
            className={`rounded-2xl border transition-all duration-300 ${
              isOpen ? "border-indigo-500/40 bg-slate-900/60 shadow-lg" : "border-slate-800/80 bg-slate-900/20 hover:border-slate-700/80 hover:bg-slate-900/40"
            }`}
          >
            <button
              onClick={() => setOpenIndex(isOpen ? null : i)}
              className="flex w-full items-center justify-between p-5 text-left focus:outline-none"
            >
              <span className="text-sm font-semibold text-slate-200">{faq.question}</span>
              <div className={`p-1.5 rounded-full transition-colors ${isOpen ? "bg-indigo-500/10 text-indigo-400" : "bg-slate-800 text-slate-400"}`}>
                {isOpen ? <Minus className="w-4 h-4" /> : <Plus className="w-4 h-4" />}
              </div>
            </button>
            <AnimatePresence initial={false}>
              {isOpen && (
                <motion.div
                  initial={{ height: 0, opacity: 0 }}
                  animate={{ height: "auto", opacity: 1 }}
                  exit={{ height: 0, opacity: 0 }}
                  transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }} // Spring-like ease
                >
                  <div className="px-5 pb-5 pt-1 text-sm text-slate-400 leading-relaxed border-t border-slate-800/40 mt-2">
                    {faq.answer}
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        );
      })}
    </div>
  );
}
```

---

## Tipe 2: The Categorized / Tabbed FAQ
**Inspirasi**: *Categorized FAQ (Edu Calvo) / Tabbed FAQ Accordion (Diar Muradi)*
**Kapan Digunakan**: Pusat Bantuan (Help Center) atau halaman FAQ dedikasi di mana pertanyaan berjumlah banyak (>10).
**Karakteristik UX**: Memisahkan FAQ dengan navigasi kapsul (Pill Navigation). Menghindari scrolling berlebih.

```tsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronDown } from "lucide-react";

const CATEGORIES = ["General", "Billing", "Security"];

export function CategorizedFAQ({ faqData }) {
  const [activeCategory, setActiveCategory] = useState(CATEGORIES[0]);
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  const activeFaqs = faqData[activeCategory] || [];

  return (
    <div className="w-full max-w-4xl mx-auto flex flex-col md:flex-row gap-8 lg:gap-16">
      
      {/* Kolom Kiri: Navigasi Kategori */}
      <div className="w-full md:w-1/3 flex flex-row md:flex-col gap-2 overflow-x-auto no-scrollbar pb-4 md:pb-0">
        {CATEGORIES.map((cat) => (
          <button
            key={cat}
            onClick={() => {
              setActiveCategory(cat);
              setOpenIndex(null); // Tutup accordion saat pindah kategori
            }}
            className={`relative px-4 py-2.5 text-sm font-medium rounded-lg text-left transition-colors whitespace-nowrap ${
              activeCategory === cat ? "text-indigo-400" : "text-slate-400 hover:text-slate-200"
            }`}
          >
            {activeCategory === cat && (
              <motion.div 
                layoutId="activeCategory" 
                className="absolute inset-0 bg-indigo-500/10 rounded-lg border border-indigo-500/20" 
              />
            )}
            <span className="relative z-10">{cat}</span>
          </button>
        ))}
      </div>

      {/* Kolom Kanan: Daftar Pertanyaan */}
      <div className="w-full md:w-2/3 divide-y divide-slate-800">
        <AnimatePresence mode="wait">
          <motion.div
            key={activeCategory}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.2 }}
          >
            {activeFaqs.map((faq, i) => {
              const isOpen = openIndex === i;
              return (
                <div key={i} className="py-4">
                  <button
                    onClick={() => setOpenIndex(isOpen ? null : i)}
                    className="flex w-full items-center justify-between text-left group"
                  >
                    <span className="text-sm font-medium text-slate-200 group-hover:text-indigo-300 transition-colors">{faq.question}</span>
                    <ChevronDown className={`w-4 h-4 text-slate-500 transition-transform duration-300 ${isOpen ? "rotate-180" : ""}`} />
                  </button>
                  <AnimatePresence initial={false}>
                    {isOpen && (
                      <motion.div
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: "auto", opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.3 }}
                      >
                        <div className="pt-3 pr-8 text-sm text-slate-400 leading-relaxed">
                          {faq.answer}
                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              );
            })}
          </motion.div>
        </AnimatePresence>
      </div>
    </div>
  );
}
```

---

## Tipe 3: The 2-Column Reveal / Multi-Level FAQ
**Inspirasi**: *FAQ Accordion Reveal (hirael) / FAQ Accordion Columns (Diar Muradi)*
**Kapan Digunakan**: Area yang lebih condong melebar (wide screen) di mana menumpuk satu baris terlalu menyisakan ruang kosong.
**Karakteristik UX**: Grid 2 kolom di layar desktop, menyusut jadi 1 kolom di mobile. Konten lebih padat.

```tsx
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

export function TwoColumnFAQ({ faqs }) {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  return (
    <div className="w-full max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-x-12 md:gap-y-6">
      {faqs.map((faq, i) => {
        const isOpen = openIndex === i;
        return (
          <div key={i} className="border-b border-slate-800 pb-4 h-fit">
            <button
              onClick={() => setOpenIndex(isOpen ? null : i)}
              className="flex w-full items-start text-left gap-4"
            >
              <div className="mt-0.5 text-indigo-400 font-mono text-xs opacity-70">
                0{i + 1}
              </div>
              <div className="flex-1">
                <span className={`text-sm font-medium transition-colors ${isOpen ? "text-indigo-300" : "text-slate-200"}`}>
                  {faq.question}
                </span>
                <AnimatePresence initial={false}>
                  {isOpen && (
                    <motion.div
                      initial={{ height: 0, opacity: 0, y: -5 }}
                      animate={{ height: "auto", opacity: 1, y: 0 }}
                      exit={{ height: 0, opacity: 0, y: -5 }}
                      transition={{ duration: 0.2 }}
                    >
                      <p className="pt-2 text-sm text-slate-400 leading-relaxed">
                        {faq.answer}
                      </p>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            </button>
          </div>
        );
      })}
    </div>
  );
}
```

## Checklist Adaptasi Template
1. **Warna Dasar**: Ganti `bg-slate-900` dengan palet proyek (misal `bg-[#0b0c10]` untuk tema Midnight Neon).
2. **Timing Animasi**: Gunakan `duration: 0.3` dipadukan dengan kurva *spring* kustom `ease: [0.16, 1, 0.3, 1]` untuk gerak UI Apple-like.
3. **Target Sentuh**: Pastikan padding pada tombol minimal `p-4` atau `p-5` agar tombol cukup lebar diklik di layar sentuh.
4. **Indikator**: Gunakan **ChevronDown** untuk desain yang bersih (clean), dan **Plus/Minus** untuk desain berbasis kartu (card-based).
