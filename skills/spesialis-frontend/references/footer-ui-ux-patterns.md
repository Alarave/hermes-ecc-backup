# Katalog Pola & Desain Footer UI/UX Modern

Panduan referensi komprehensif tipe, fungsi, dan anatomi footer modern (berdasarkan riset Nielsen Norman Group, Awwwards, Eleken, dan standar SaaS).

---

## 1. Doormat / Multi-Column Mega Footer (Standar SaaS & E-Commerce)
- **Fungsi**: Navigasi lengkap untuk pengguna yang sudah mencapai akhir halaman dan mencari informasi spesifik.
- **Anatomi**:
  - 4-6 kolom kategori (Product, Solutions, Resources, Company, Legal).
  - Newsletter subscription box di sudut atas/samping.
  - Social media icons, copyright, status operational badge (e.g. "All systems operational").
  - Country/Language selector.
- **Kapan Digunakan**: Web aplikasi kompleks, SaaS B2B, platform edukasi, toko online besar.
- **Contoh Ref**: Stripe, Linear, GitHub, Vercel.

---

## 2. Oversized / Giant Typography & Statement Footer (Editorial & Agency)
- **Fungsi**: Memberikan kesan visual terakhir yang kuat (memorable impression) dan CTA kolaboratif yang mencolok.
- **Anatomi**:
  - Headline ukuran masif (e.g., "LET'S TALK", "WORK WITH US", nama studio raksasa).
  - Tampilan jam real-time kantor cabang (World Clock widget).
  - Interaksi kursor / hover magnetik pada link kontak.
  - Link langsung ke email (`mailto:`), phone, dan showreel.
- **Kapan Digunakan**: Studio kreatif, agency desain, portfolio personal, brand fashion.
- **Contoh Ref**: Awwwards site of the day (Rejouice, Beaucoup, Flayks).

---

## 3. Secondary-Task Hub / Action-Oriented Footer
- **Fungsi**: Membantu pengguna menyelesaikan tugas kedua tanpa harus kembali ke navigasi atas.
- **Anatomi**:
  - Input pencarian cepat (search bar).
  - Formulir dukungan tiket / customer support chat launcher.
  - Direct download links (App Store, Google Play badge).
  - Dokumentasi API / status server.
- **Kapan Digunakan**: Fintech, perbankan, platform developer tools.
- **Contoh Ref**: Wise, Linear Docs, Supabase.

---

## 4. Minimalist / Utility-Only Footer (Single-Row / Pill)
- **Fungsi**: Menjaga fokus pengguna pada konten inti tanpa distraksi tautan berlebih.
- **Anatomi**:
  - Baris tunggal horizontal (flex row wrap).
  - Hak cipta (Copyright), tautan Privacy Policy, Terms of Service.
  - 3-4 icon media sosial di sisi kanan.
- **Kapan Digunakan**: Halaman checkout, portal login/auth, form multi-step, tool fungsional satu halaman.
- **Contoh Ref**: Notion app view, Apple checkout, Stripe Checkout.

---

## 5. Sticky Floating / Bottom Dock Footer (Mobile-First / App-Like)
- **Fungsi**: Mempermudah jangkauan jempol (Thumb Zone) untuk aksi utama di perangkat mobile atau web app.
- **Anatomi**:
  - Bar melayang (floating pill dock) dengan backdrop-blur/liquid glass.
  - Tombol CTA utama (e.g., "Order Now", "Book a Demo", "Quick Menu").
  - Navigasi tab 4-5 icon utama.
- **Kapan Digunakan**: Mobile web, dashboard mobile, platform F&B / e-commerce checkout.
- **Contoh Ref**: Airbnb mobile web, Raycast web tools.

---

## 6. Contextual & Role-Aware Footer (Dynamic UX)
- **Fungsi**: Menampilkan tautan footer yang berubah dinamis tergantung status user.
- **Anatomi**:
  - **Logged-out**: Tautan Pricing, Fitur, Testimoni, CTA Sign Up.
  - **Logged-in**: Tautan Dashboard, Switch Workspace, Dokumentasi, Billing, Upgrade Plan.
- **Kapan Digunakan**: SaaS dengan retention tinggi dan dashboard terpadu.

---

## 7. Interactive / Reveal Curtain Footer (Parallax Behind Content)
- **Fungsi**: Efek modern di mana konten utama meluncur ke atas dan menyingkap footer yang berada di layer belakang (`z-index: -1` dengan `position: fixed`).
- **Anatomi**:
  - Background gelap bertekstur atau shader canvas.
  - Brand tagline besar dengan animasi reveal interaktif.
- **Kapan Digunakan**: Landing page produk premium, showcase otomotif atau hardware.

---

## Checklist Aksesibilitas & UX Footer (WCAG 2.2 AA)
1. **Target Ukuran Link**: Jarak antar link minimal 24x24px agar tidak terjadi salah klik pada mobile (Fitts's Law).
2. **Kontras Teks**: Minimal rasio kontras 4.5:1 untuk teks biasa (hindari abu-abu pudar di atas background hitam pekat).
3. **No Hidden Traps**: Hindari menaruh footer statis di halaman dengan *Infinite Scroll* tanpa tombol "Load More", karena pengguna tidak akan pernah bisa mencapai footer.
4. **Navigasi Keyboard**: Pastikan urutan Tab tetap logis saat fokus mencapai tautan footer.
