# 21st.dev Master Profile & Avatar Templates

Analisis pola dan blueprint komponen Profile & Avatar berdasarkan 200+ komponen di 21st.dev (React + Tailwind v4 + Framer Motion / Radix UI).

---

## 1. Empat Arketipe Profile & Avatar Modern

### Arketipe 1: The Avatar with Status / Verified Indicator
- **Fungsi**: Menampilkan identitas pengguna dengan indikator status kehadiran (Online / Busy / Away) atau status verifikasi akun.
- **Karakteristik Visual**:
  - Foto profil melingkar (`rounded-full`) dengan border halus.
  - Titik status kecil di sudut kanan bawah berbingkai warna background (`ring-2 ring-[#090d16]`) agar tidak bertabrakan dengan foto.
  - Opsi lencana centang (*Verified Badge*) biru/emas.
- **Inspirasi**: `Avatar Online (Origin UI)`, `Avatar Verified (Origin UI)`.

### Arketipe 2: The Overlapping Avatar Group (Stack)
- **Fungsi**: Menampilkan daftar kolaborator proyek, peserta rapat, atau *social proof* pelanggan.
- **Karakteristik Visual**:
  - Deretan foto yang saling bertumpuk sebagian (`-space-x-2.5`).
  - Efek *hover scale*: Avatar yang disentuh kursor mouse otomatis naik ke lapisan teratas (`hover:z-10 hover:scale-110`).
  - Lingkaran terakhir berupa chip hitungan sisa anggota (misal: `+5`).
- **Inspirasi**: `Reverse Order Avatar Group (shadcn)`, `HeroUI Avatar Group`.

### Arketipe 3: The Interactive Profile Hover Card
- **Fungsi**: Menampilkan kartu ringkasan pengguna saat nama atau avatar di-hover (*micro-profile*).
- **Karakteristik Visual**:
  - Memuat Avatar besar, Nama Lengkap, @username, Bio singkat, dan statistik (Followers / Repos).
  - Tombol aksi langsung (Follow / Message / Connect).
- **Inspirasi**: `Card Studio (ShadcnStudio)`.

### Arketipe 4: The Navbar Profile Dropdown Trigger
- **Fungsi**: Menu profil di pojok kanan atas dashboard.
- **Karakteristik Visual**: Menampilkan foto pengguna mungil bersama nama depan dan ikon panah bawah (*ChevronDown*). Saat diklik, membuka dropdown navigasi (Account Settings, Billing, Log Out).

---

## 2. Blueprint Kode Master

### A. The Overlapping Avatar Stack (Interactive)
```tsx
const AVATARS = [
  { id: 1, name: "Alex R.", src: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" },
  { id: 2, name: "Sarah K.", src: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&auto=format&fit=crop&q=80" },
  { id: 3, name: "David M.", src: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80" },
];

export function AvatarGroup({ countExtra = 4 }: { countExtra?: number }) {
  return (
    <div className="flex items-center -space-x-2.5 overflow-hidden p-1">
      {AVATARS.map((user) => (
        <div 
          key={user.id} 
          className="relative inline-block transition-transform duration-200 ease-out hover:scale-115 hover:z-10 cursor-pointer"
        >
          <img
            src={user.src}
            alt={user.name}
            className="w-8 h-8 rounded-full ring-2 ring-slate-900 object-cover"
          />
        </div>
      ))}
      
      {/* Excess Count Badge */}
      {countExtra > 0 && (
        <div className="flex items-center justify-center w-8 h-8 rounded-full ring-2 ring-slate-900 bg-slate-800 text-[11px] font-mono font-medium text-slate-300 z-0">
          +{countExtra}
        </div>
      )}
    </div>
  );
}
```

### B. The User Profile Card (Rich Hover Surface)
```tsx
import { Mail, Calendar, CheckCircle } from "lucide-react";

export function UserProfileCard() {
  return (
    <div className="w-full max-w-xs p-5 rounded-2xl border border-slate-800 bg-slate-900/90 shadow-2xl backdrop-blur-xl">
      {/* Header: Avatar + Status */}
      <div className="flex items-start justify-between">
        <div className="relative">
          <img
            src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80"
            alt="User profile"
            className="w-14 h-14 rounded-2xl object-cover ring-1 ring-slate-700"
          />
          {/* Online Indicator */}
          <span className="absolute -bottom-1 -right-1 w-3.5 h-3.5 rounded-full bg-emerald-500 ring-2 ring-slate-900" />
        </div>
        
        <button className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 border border-slate-700/80 transition-colors">
          Follow
        </button>
      </div>

      {/* Name & Bio */}
      <div className="mt-3">
        <div className="flex items-center gap-1.5">
          <h4 className="text-sm font-bold text-white">Firman</h4>
          <CheckCircle className="w-3.5 h-3.5 text-indigo-400 fill-indigo-500/20" />
        </div>
        <p className="text-xs font-mono text-slate-500">@firman_dev</p>
        <p className="text-xs text-slate-400 mt-2 leading-relaxed">
          Lead Frontend Engineer. Spesialis antarmuka deterministik, React 19, & Tailwind v4.
        </p>
      </div>

      {/* Meta Detail */}
      <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center gap-4 text-[11px] text-slate-500 font-mono">
        <div className="flex items-center gap-1">
          <Calendar className="w-3.5 h-3.5 text-slate-600" />
          <span>Joined 2024</span>
        </div>
        <div className="flex items-center gap-1">
          <Mail className="w-3.5 h-3.5 text-slate-600" />
          <span>Available</span>
        </div>
      </div>
    </div>
  );
}
```

---

## 3. Checklist UX Avatar & Profil
1. **Fallback Initial**: Selalu sediakan teks inisial dua huruf (misal: "FR" dari Firman) dengan background warna acak/konsisten jika tautan gambar avatar gagal dimuat (*image broken*).
2. **Hover Ring Padding**: Pada tumpukan avatar (*Avatar Stack*), gunakan `ring-2 ring-slate-900` dengan warna cincin yang sama persis seperti warna background container untuk menciptakan ilusi potongan melengkung yang rapi.
3. **Target Aksesibilitas**: Jika avatar dapat diklik (berfungsi sebagai tombol navigasi atau pemicu dropdown), pastikan dibungkus dalam tag `<button>` dengan atribut `aria-label="User menu"`.
