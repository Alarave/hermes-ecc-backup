# WCAG Accessibility Handbook (a11y) untuk Frontend Modern

Panduan praktis kepatuhan aksesibilitas WCAG 2.1 Level AA untuk komponen React, Next.js, dan Tailwind CSS.

---

## 1. Aturan Emas Semantik HTML

| Elemen Semantik | Jangan Pernah Gunakan | Alasan |
|---|---|---|
| `<button type="button">` | `<div onClick={...}>` | Hilang penanganan keyboard (`Enter`, `Space`) dan fokus default. |
| `<a href="...">` | `<button onClick={() => router.push(...)}>` | Mengabaikan fungsi navigasi native (open in new tab, bookmark). |
| `<nav>`, `<header>`, `<main>` | Generic `<div>` berlebihan | Merusak navigasi landmark untuk pembaca layar (screen reader). |

---

## 2. Formulir Masukan Aksesibel

Setiap input wajib memiliki label eksplisit dan pesan error terhubung via ID:

```tsx
interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label: string;
  error?: string;
  hint?: string;
}

export function AccessibleInput({ label, error, hint, id, ...props }: InputProps) {
  const hintId = `${id}-hint`;
  const errorId = `${id}-error`;

  return (
    <div className="flex flex-col gap-1.5">
      <label htmlFor={id} className="text-sm font-medium text-slate-800">
        {label}
      </label>
      {hint && (
        <span id={hintId} className="text-xs text-slate-500">
          {hint}
        </span>
      )}
      <input
        id={id}
        aria-invalid={error ? 'true' : 'false'}
        aria-describedby={[hint ? hintId : '', error ? errorId : ''].filter(Boolean).join(' ') || undefined}
        className={`px-3 py-2 border rounded-md focus:outline-none focus:ring-2 ${
          error ? 'border-red-500 focus:ring-red-200' : 'border-slate-300 focus:ring-blue-200'
        }`}
        {...props}
      />
      {error && (
        <span id={errorId} role="alert" className="text-xs text-red-600 font-medium">
          {error}
        </span>
      )}
    </div>
  );
}
```

---

## 3. Focus Trapping & Modal Dialog

Dialog wajib mengunci fokus di dalam modal dan dapat ditutup menggunakan tombol Escape:

```tsx
import { useEffect, useRef } from 'react';

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
}

export function AccessibleModal({ isOpen, onClose, title, children }: ModalProps) {
  const modalRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!isOpen) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
        return;
      }
      if (e.key === 'Tab' && modalRef.current) {
        const focusables = modalRef.current.querySelectorAll<HTMLElement>(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        if (focusables.length === 0) return;
        const first = focusables[0];
        const last = focusables[focusables.length - 1];

        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4"
    >
      <div
        ref={modalRef}
        className="bg-white rounded-lg p-6 max-w-md w-full shadow-xl"
      >
        <h2 id="modal-title" className="text-lg font-semibold mb-4">
          {title}
        </h2>
        {children}
      </div>
    </div>
  );
}
```

---

## 4. Perlindungan Preferensi Gerak Berkurang (Reduced Motion)

Pastikan setiap animasi Framer Motion memeriksa `useReducedMotion`:

```tsx
import { motion, useReducedMotion } from 'framer-motion';

export function AnimatedCard({ children }: { children: React.ReactNode }) {
  const shouldReduceMotion = useReducedMotion();

  return (
    <motion.div
      initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: shouldReduceMotion ? 0.1 : 0.4 }}
    >
      {children}
    </motion.div>
  );
}
```
