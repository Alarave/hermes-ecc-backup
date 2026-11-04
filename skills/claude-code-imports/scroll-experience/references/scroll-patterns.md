# POLA IMPLEMENTASI TEKNIS ANIMASI GULIR (SCROLL EXPERIENCE PATTERNS)

Panduan implementasi teknis untuk pustaka motion modern: GSAP ScrollTrigger, Framer Motion, Lenis, dan CSS scroll-timeline native.

---

## 1. Implementasi GSAP ScrollTrigger

Pilihan terbaik untuk animasi kompleks, multi-lapisan paralaks, dan penguncian seksi (*pinning*).

```javascript
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// 1. Pinned Section dengan Scrubbing
gsap.to('.hero-visual', {
  scrollTrigger: {
    trigger: '.hero-container',
    start: 'top top',
    end: '+=1200',
    pin: true,
    scrub: 1, // Smoothing 1 detik terhadap scroll roda
    anticipatePin: 1
  },
  scale: 1.25,
  opacity: 0.85
});

// 2. Paralaks Berlapis Multi-Layer
gsap.to('.layer-bg', {
  scrollTrigger: {
    trigger: '.story-section',
    start: 'top bottom',
    end: 'bottom top',
    scrub: true
  },
  y: '-15%'
});

gsap.to('.layer-fg', {
  scrollTrigger: {
    trigger: '.story-section',
    start: 'top bottom',
    end: 'bottom top',
    scrub: true
  },
  y: '-40%'
});
```

---

## 2. Implementasi React & Framer Motion

Pilihan terbaik untuk proyek React / Next.js dengan declarative syntax.

```tsx
'use client';

import { motion, useScroll, useTransform, useReducedMotion } from 'framer-motion';
import { useRef } from 'react';

export function CinematicSection() {
  const containerRef = useRef<HTMLDivElement>(null);
  const shouldReduceMotion = useReducedMotion();

  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start end', 'end start']
  });

  // Terapkan gerak hanya jika pengguna tidak meminta reduced motion
  const yBg = useTransform(scrollYProgress, [0, 1], shouldReduceMotion ? ['0%', '0%'] : ['0%', '-25%']);
  const opacityText = useTransform(scrollYProgress, [0.1, 0.4, 0.8, 1], [0, 1, 1, 0]);

  return (
    <div ref={containerRef} className="relative h-[200vh] bg-slate-950">
      <div className="sticky top-0 h-screen flex items-center justify-center overflow-hidden">
        <motion.div style={{ y: yBg }} className="absolute inset-0 bg-cover bg-center" />
        <motion.h2 style={{ opacity: opacityText }} className="relative z-10 text-5xl font-bold text-white">
          Pengalaman Sinematik Nyata
        </motion.h2>
      </div>
    </div>
  );
}
```

---

## 3. Implementasi CSS Native (Scroll-Timeline 2026+)

Pilihan paling ringan (0 KB JavaScript) untuk animasi penyingkapan elemen sederhana pada browser modern.

```css
@keyframes revealOnScroll {
  from {
    opacity: 0;
    transform: translateY(40px) scale(0.96);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.scroll-reveal-card {
  animation: revealOnScroll linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 35%;
}

@media (prefers-reduced-motion: reduce) {
  .scroll-reveal-card {
    animation: none;
    opacity: 1;
    transform: none;
  }
}
```
