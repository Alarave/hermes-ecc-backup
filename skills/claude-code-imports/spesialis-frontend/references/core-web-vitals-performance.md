# Core Web Vitals Performance Engine

Panduan optimasi performa frontend untuk mencapai skor hijau pada Google Core Web Vitals (LCP < 2.5s, INP < 200ms, CLS < 0.1).

---

## 1. Optimasi LCP (Largest Contentful Paint)

Penyebab utama LCP buruk adalah pemuatan gambar hero atau font eksternal yang lambat.

### Aturan Gambar Hero Next.js:
```tsx
import Image from 'next/image';

// WAJIB: priority untuk gambar di atas fold (above the fold)
export function HeroBanner() {
  return (
    <div className="relative w-full h-[480px]">
      <Image
        src="/hero.webp"
        alt="Platform Showcase"
        fill
        priority
        sizes="(max-width: 768px) 100vw, 1200px"
        className="object-cover"
      />
    </div>
  );
}
```

---

## 2. Pencegahan CLS (Cumulative Layout Shift)

Penyebab CLS adalah rendering konten asinkron atau banner dinamis tanpa alokasi ruang tetap.

### Skeleton dengan Aspek Rasio Pasti:
```tsx
export function ProductCardSkeleton() {
  return (
    <div className="flex flex-col gap-3 p-4 border rounded-xl animate-pulse">
      {/* Aspect ratio mengunci tinggi sebelum gambar selesai dimuat */}
      <div className="aspect-[4/3] w-full bg-slate-200 rounded-lg" />
      <div className="h-5 w-3/4 bg-slate-200 rounded" />
      <div className="h-4 w-1/2 bg-slate-200 rounded" />
    </div>
  );
}
```

---

## 3. Optimasi INP (Interaction to Next Paint)

Penyebab INP buruk adalah JavaScript thread utama terblokir saat user melakukan klik atau ketik.

### Pola Pemisahan Transisi Non-Mendesak:
```tsx
import { useState, useTransition } from 'react';

export function SearchFilter({ items }: { items: string[] }) {
  const [query, setQuery] = useState('');
  const [filtered, setFiltered] = useState(items);
  const [isPending, startTransition] = useTransition();

  const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    setQuery(val); // Interaksi responsif instan untuk input field

    startTransition(() => {
      // Perhitungan berat ditandai sebagai transisi non-prioritas
      setFiltered(items.filter((item) => item.toLowerCase().includes(val.toLowerCase())));
    });
  };

  return (
    <div>
      <input value={query} onChange={handleSearch} placeholder="Cari..." />
      {isPending && <span className="text-xs text-slate-400">Memperbarui...</span>}
      <ul>
        {filtered.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );
}
```

---

## 4. Code Splitting & Dynamic Imports

Komponen besar (misal visualisasi chart, rich text editor, atau modal) tidak boleh dimasukkan ke dalam initial bundle halaman:

```tsx
import dynamic from 'next/dynamic';

const HeavyChart = dynamic(() => import('@/components/HeavyChart'), {
  loading: () => <div className="h-64 w-full bg-slate-100 animate-pulse rounded-lg" />,
  ssr: false, // Matikan SSR jika memerlukan canvas atau window object
});

export function AnalyticsDashboard() {
  return (
    <section>
      <h1>Ringkasan Metrik</h1>
      <HeavyChart />
    </section>
  );
}
```
