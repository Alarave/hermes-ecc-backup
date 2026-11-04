# React 19 & Next.js 15 Patterns

Pola modern React 19 dan Next.js 15 untuk arsitektur antarmuka enterprise yang efisien.

---

## 1. Prinsip Server/Client Component Boundary

Aturan fondasi: letakkan batas `'use client'` sedalam mungkin di pohon komponen.

```
app/
  page.tsx             <-- Server Component (zero JS ke client)
    └── ProductList    <-- Server Component (ambil data langsung)
          └── ProductCard.tsx    <-- Server Component
                └── FavoriteButton.tsx  <-- 'use client' (hanya komponen interaktif ini)
```

### Pola Implementasi:
```tsx
// app/page.tsx - Server Component
import { ProductList } from '@/components/ProductList';

async function fetchProducts() {
  const res = await fetch('https://api.example.com/products', { next: { revalidate: 60 } });
  return res.json();
}

export default async function ProductPage() {
  const products = await fetchProducts();
  return <ProductList products={products} />;
}
```

```tsx
// components/FavoriteButton.tsx - Client Component minimal
'use client';

import { useState } from 'react';

export function FavoriteButton({ productId }: { productId: string }) {
  const [isFav, setIsFav] = useState(false);
  return (
    <button onClick={() => setIsFav(!isFav)} aria-label={isFav ? 'Hapus dari favorit' : 'Tambah ke favorit'}>
      {isFav ? 'Hapus Favorit' : 'Favorit'}
    </button>
  );
}
```

---

## 2. Mutasi Formulir dengan `useActionState`

Gantikan pola submit manual dengan Server Actions + `useActionState` untuk feedback kesalahan dan status terintegrasi:

```tsx
'use client';

import { useActionState } from 'react';
import { submitContactForm } from '@/app/actions/contact';

export function ContactForm() {
  const [state, formAction, isPending] = useActionState(submitContactForm, null);

  return (
    <form action={formAction} className="flex flex-col gap-4">
      <input
        name="email"
        type="email"
        aria-invalid={state?.errors?.email ? 'true' : 'false'}
        aria-describedby={state?.errors?.email ? 'email-error' : undefined}
      />
      {state?.errors?.email && (
        <span id="email-error" role="alert" className="text-red-600 text-sm">
          {state.errors.email}
        </span>
      )}

      <button type="submit" disabled={isPending} className="btn-primary">
        {isPending ? 'Mengirim...' : 'Kirim Pesan'}
      </button>
    </form>
  );
}
```

```tsx
// app/actions/contact.ts
'use server';

export async function submitContactForm(prevState: unknown, formData: FormData) {
  const email = formData.get('email') as string;

  if (!email.includes('@')) {
    return { errors: { email: 'Format email tidak valid.' } };
  }

  // Proses pengiriman data...
  return { success: true };
}
```

---

## 3. Optimistic UI dengan `useOptimistic`

Untuk interaksi yang membutuhkan umpan balik instan (like, bookmark, status toggle):

```tsx
'use client';

import { useOptimistic, useTransition } from 'react';
import { toggleBookmark } from '@/app/actions/bookmarks';

export function BookmarkButton({ articleId, initialBookmarked }: { articleId: string; initialBookmarked: boolean }) {
  const [optimisticBookmarked, setOptimisticBookmarked] = useOptimistic(initialBookmarked);
  const [, startTransition] = useTransition();

  const handleToggle = () => {
    startTransition(async () => {
      setOptimisticBookmarked(!optimisticBookmarked); // Update UI instan
      await toggleBookmark(articleId);               // Request ke server setelahnya
    });
  };

  return (
    <button onClick={handleToggle} aria-pressed={optimisticBookmarked}>
      {optimisticBookmarked ? 'Tersimpan' : 'Simpan Artikel'}
    </button>
  );
}
```

---

## 4. Error Boundary untuk Komponen Berbasis Data

```tsx
'use client';

import { Component, type ReactNode } from 'react';

interface ErrorBoundaryProps {
  fallback: ReactNode;
  children: ReactNode;
}

interface ErrorBoundaryState {
  hasError: boolean;
  error?: Error;
}

export class DataErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  state: ErrorBoundaryState = { hasError: false };

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error };
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback;
    }
    return this.props.children;
  }
}
```

### Cara Pakai:
```tsx
<DataErrorBoundary fallback={<div className="p-4 text-red-600">Gagal memuat data. Coba muat ulang.</div>}>
  <ProductChart />
</DataErrorBoundary>
```
