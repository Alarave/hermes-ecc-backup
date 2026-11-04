# DAFTAR PERIKSA PRA-RILIS & ANTI-PATTERNS (UI UX PRO MAX)

Daftar periksa kualitas visual dan interaksi sebelum suatu halaman atau komponen disetujui (Quality Gate G4).

---

## 1. Daftar Hitam Pola Desain (Anti-Patterns Blacklist)

1. **AI Slop Purple Haze**: Menggunakan gradien latar belakang ungu neon (`from-purple-600 to-indigo-600`) pada seluruh hero section tanpa identitas merek yang jelas.
2. **Gray-on-Gray Ghost Text**: Menuliskan teks penjelasan kecil berwarna abu-abu muda (`#94A3B8`) di atas latar abu-abu terang (`#F1F5F9`), menghasilkan kontras di bawah 3:1.
3. **Emoji as Icons**: Menggunakan karakter emoji seperti 🚀, 💡, 🔥 sebagai pengganti ikon SVG resmi. Emoji merusak konsistensi rendering lintas perangkat (iOS vs Android vs Windows).
4. **Instant State Snapping**: Perubahan warna atau posisi tombol tanpa durasi transisi (0ms), membuat antarmuka terasa kaku dan murah.
5. **Horizontal Scroll Leaks**: Elemen absolut atau lebar wadah yang melebihi 100vw pada layar seluler (375px), menyebabkan halaman dapat digeser ke samping tanpa sengaja.
6. **Inaccessible Touch Targets**: Tombol navigasi mobile atau ikon tutup modal yang berukuran di bawah 36x36px sehingga sulit ditekan oleh jari pengguna.

---

## 2. Checklist Verifikasi Pra-Rilis 8 Poin

| No | Poin Pemeriksaan | Kriteria Kelulusan | Status |
|---|---|---|---|
| 1 | **Kontras Teks WCAG** | Minimum 4.5:1 untuk teks normal, 3:1 untuk teks besar/judul. | WAJIB LOLOS |
| 2 | **Fokus Keyboard** | Outline cincin fokus (*focus ring*) terlihat saat tombol Tab ditekan. | WAJIB LOLOS |
| 3 | **Ikon Vektor Resmi** | 100% menggunakan SVG (Heroicons / Lucide / Phosphor), nol emoji. | WAJIB LOLOS |
| 4 | **Ukuran Target Sentuh** | Minimal 44x44 piksel pada seluruh kontrol sentuh layar seluler. | WAJIB LOLOS |
| 5 | **Transisi Halus** | Seluruh efek hover memiliki transisi 150ms sampai 300ms kemudahan (*ease-out*). | WAJIB LOLOS |
| 6 | **Gerakan Aman** | Media query `prefers-reduced-motion` menonaktifkan animasi berat. | WAJIB LOLOS |
| 7 | **Responsif 4 Titik** | Tampilan teruji rapi di 375px (HP), 768px (Tablet), 1024px (Laptop), 1440px (Desktop). | WAJIB LOLOS |
| 8 | **Zero Layout Shift** | Wadah gambar dan banner memiliki rasio aspek atau dimensi tetap (CLS < 0.1). | WAJIB LOLOS |
