# Panduan Arsitektur & Template UI/UX FAQ Modern

Dokumen referensi pola desain (UI patterns), layout, interaksi, dan aksesibilitas untuk komponen FAQ (Frequently Asked Questions) di website profesional.

---

## 1. Empat Pola Layout FAQ Standar Industri

### Pola A: Split-Column Category + Accordion (SaaS / Platform Kompleks)
- **Struktur**:
  - Kolom Kiri (1/3): Header ("Pusat Bantuan & FAQ"), subjudul, dan navigasi Tab Kategori vertikal (Akun, Billing, Keamanan, Integrasi).
  - Kolom Kanan (2/3): Accordion yang berganti dinamis berdasarkan tab yang dipilih.
- **Keunggulan UX**: Mencegah pengguna harus scroll terlalu jauh jika ada lebih dari 10 pertanyaan (Hick's Law).
- **Contoh Ref**: Stripe, Supabase, Vercel, Shopify.

### Pola B: Centered Minimalist with Instant Search (Apple & Linear Style)
- **Struktur**:
  - Header terpusat dengan search bar real-time ("Cari pertanyaan...") di bagian atas.
  - Daftar accordion rapi vertikal (lebar maksimal `max-w-3xl`) dengan pembatas garis tipis (`border-slate-800`).
  - Animasi rotasi icon chevron (+/- atau panah turun) yang halus.
- **Keunggulan UX**: Fokus, tenang, tidak membebani kognitif, mudah dicari langsung lewat keyboard.

### Pola C: 2-Column Bento Card FAQ (Web3 & Agency Showcase)
- **Struktur**:
  - Grid 2 kolom berisi kartu permanen terbuka atau semi-terbuka.
  - Setiap kartu memiliki icon penanda tema di sudut atas, judul tebal, dan jawaban ringkas.
- **Keunggulan UX**: Cocok jika pertanyaan sedikit (4–6 pertanyaan kunci) dan ingin audiens langsung membaca tanpa harus klik membuka accordion.

### Pola D: Accordion + Embedded "Still Have Questions?" Support Card
- **Struktur**:
  - Bagian atas: Accordion pertanyaan populer.
  - Bagian bawah: Card CTA "Belum menemukan jawaban?" dengan avatar tim support, link Chat WhatsApp / Telegram.
- **Keunggulan UX**: Menutup celah konversi agar calon pelanggan yang bingung tidak langsung meninggalkan website (Secondary Task Hub).

---

## 2. Checklist Aksesibilitas FAQ (WAI-ARIA Accordion Pattern)
Komponen Accordion FAQ wajib mematuhi standar W3C ARIA:
1. **Tombol Trigger**:
   - Tag `<button>` dengan atribut `aria-expanded="true|false"`.
   - `aria-controls="faq-answer-id"` menghubungkan tombol ke panel jawabannya.
2. **Panel Jawaban**:
   - Kontainer dengan atribut `id="faq-answer-id"` dan `role="region"`.
   - `aria-labelledby="faq-button-id"` menunjuk kembali ke judul pertanyaan.
3. **Keyboard Nav**:
   - `Enter` atau `Space` untuk toggle buka/tutup.
   - `Tab` berpindah ke pertanyaan berikutnya secara berurutan.
4. **Target Sentuh Mobile**:
   - Tinggi baris tombol pertanyaan minimal 48px dengan padding vertikal yang cukup untuk mematuhi Fitts's Law dan WCAG 2.2.

---

## 3. Implementasi Komponen (HTML / Alpine.js / Tailwind v4)

Berikut contoh implementasi Blade-ready dengan Alpine.js untuk pola Accordion standar tinggi:

```html
<section class="py-24 bg-[#090d16] text-white">
  <div class="max-w-3xl mx-auto px-6" x-data="{ activeAccordion: null }">
    
    <div class="text-center mb-16">
      <h2 class="text-3xl font-bold tracking-tight mb-4">Frequently Asked Questions</h2>
      <p class="text-slate-400">Semua yang perlu Anda ketahui tentang sistem dan akses voucher kami.</p>
    </div>

    <div class="divide-y divide-slate-800 border-y border-slate-800">
      
      <!-- FAQ Item 1 -->
      <div class="py-5">
        <button 
          @click="activeAccordion = (activeAccordion === 1 ? null : 1)"
          :aria-expanded="activeAccordion === 1"
          class="flex w-full items-center justify-between text-left text-base font-semibold text-slate-100 group focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-[#090d16] rounded-sm"
        >
          <span>Bagaimana cara kerja voucher akses GPT di Berlayar Cafe?</span>
          <span 
            class="ml-4 transition-transform duration-300 text-slate-500 group-hover:text-indigo-400 flex-shrink-0" 
            :class="{ 'rotate-180 text-indigo-400': activeAccordion === 1 }"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </span>
        </button>
        <div 
          x-show="activeAccordion === 1" 
          x-collapse.duration.300ms
          x-cloak 
          class="pt-3 pr-8 text-sm text-slate-400 leading-relaxed font-normal"
        >
          Setiap pembelian kopi akan mendapatkan struk thermal dengan 8 karakter kode unik. Masukkan kode tersebut di portal web kami untuk satu sesi akses AI tanpa perlu kartu kredit.
        </div>
      </div>

      <!-- FAQ Item 2 -->
      <div class="py-5">
        <button 
          @click="activeAccordion = (activeAccordion === 2 ? null : 2)"
          :aria-expanded="activeAccordion === 2"
          class="flex w-full items-center justify-between text-left text-base font-semibold text-slate-100 group focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-[#090d16] rounded-sm"
        >
          <span>Apa yang terjadi jika akses tiba-tiba terputus?</span>
          <span 
            class="ml-4 transition-transform duration-300 text-slate-500 group-hover:text-indigo-400 flex-shrink-0" 
            :class="{ 'rotate-180 text-indigo-400': activeAccordion === 2 }"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </span>
        </button>
        <div 
          x-show="activeAccordion === 2" 
          x-collapse.duration.300ms
          x-cloak 
          class="pt-3 pr-8 text-sm text-slate-400 leading-relaxed font-normal"
        >
          Riwayat sesi Anda akan tersimpan sementara berdasarkan cache browser lokal. Jika terputus sebelum batas waktu habis, Anda bisa melanjutkan sesi dari perangkat yang sama.
        </div>
      </div>

    </div>

    <!-- Fallback Support Card (Secondary Task Hub) -->
    <div class="mt-16 bg-slate-900/50 border border-slate-800 rounded-2xl p-6 text-center flex flex-col items-center gap-4">
      <div class="w-12 h-12 bg-indigo-500/10 text-indigo-400 rounded-full flex items-center justify-center">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
      </div>
      <div>
        <h3 class="font-semibold text-slate-200">Masih belum menemukan jawaban?</h3>
        <p class="text-sm text-slate-400 mt-1">Tim dukungan kami siap membantu Anda via WhatsApp dari jam 09:00 - 22:00.</p>
      </div>
      <a href="#" class="mt-2 inline-flex items-center justify-center px-6 py-2.5 rounded-full bg-slate-100 hover:bg-white text-slate-900 text-sm font-semibold transition-colors">
        Chat via WhatsApp
      </a>
    </div>

  </div>
</section>
```