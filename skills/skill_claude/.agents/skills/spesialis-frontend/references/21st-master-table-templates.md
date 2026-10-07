# 21st.dev Master Table Templates

Analisis pola dan blueprint komponen Table / Data Grid berdasarkan 200+ komponen di 21st.dev (React + Tailwind v4 + integrasi Headless UI seperti TanStack Table).

---

## 1. Empat Arketipe Table Modern

### Arketipe 1: The Complex Data Table (SaaS / Admin Dashboard)
- **Fungsi**: Menampilkan data dengan fitur lengkap (Sorting, Filtering, Pagination, Row Selection).
- **Karakteristik Visual**:
  - Kolom pertama berupa Checkbox untuk *bulk actions*.
  - Header tabel menempel di atas (Sticky Header) dengan ikon pengurutan (Sort Icon).
  - Kolom terakhir biasanya memuat aksi tersembunyi (Dropdown menu via ikon tiga titik / Ellipsis).
  - Penggunaan *Status Badges* (Chip template) di kolom status.
- **Inspirasi**: `Complex Data Table (felipemenezes098)`.

### Arketipe 2: The Excel-Style / Spreadsheet Table
- **Fungsi**: Entri data secara massal dan cepat (Bulk Data Entry).
- **Karakteristik Visual**:
  - Border penuh di setiap sel (grid cell borders).
  - Mendukung pengeditan inline (klik sel langsung berubah menjadi input).
  - Interaksi navigasi keyboard ala Excel (Arrow keys, Tab, Copy/Paste massal).
- **Inspirasi**: `Excel-Style Table (Ravi Katiyar)`.

### Arketipe 3: The Reorderable / Drag-and-Drop Table
- **Fungsi**: Daftar yang urutannya bisa disesuaikan oleh pengguna (seperti urutan antrean atau prioritas tugas).
- **Karakteristik Visual**:
  - Terdapat kolom khusus ikon "Grip / Drag Handle" (enam titik/garis sejajar) di ujung kiri setiap baris.
  - Baris yang ditarik (*dragged*) akan melayang dengan bayangan tebal (shadow) dan memudarkan (*opacity*) tempat asalnya.
- **Inspirasi**: `Reorderable Table (Ruixen)`.

### Arketipe 4: The Minimalist / Financial Table
- **Fungsi**: Laporan mutasi bank, tagihan (*billing*), atau data analitik murni.
- **Karakteristik Visual**:
  - Tanpa garis vertikal (no vertical borders).
  - Baris dipisahkan dengan garis abu-abu tipis (subtle border-bottom).
  - Angka nominal selalu rata kanan (*right-aligned*).

---

## 2. Praktik Terbaik UI/UX Table (TanStack Table & Tailwind)

### A. Format dan Konten Sel
- **Rata Kanan untuk Angka**: Semua mata uang, persentase, dan angka desimal wajib menggunakan `text-right` agar mudah di-scan secara vertikal.
- **Empty State**: Ketika data kosong, tabel jangan menghilang. Tampilkan border tabel dengan satu baris penuh (`colSpan="100%"`) berisi ilustrasi *Empty State* dan teks penjelas.
- **Sticky Actions**: Pada tabel yang lebar (harus scroll horizontal), pastikan kolom Aksi (kanan) dan/atau Nama/ID (kiri) dibuat sticky (misalnya `sticky right-0 bg-slate-900`) agar aksi selalu terlihat.

### B. Desain Responsif Mobile
Tabel HTML standar sangat buruk di mobile. Terapkan pola ini:
- **Pola Card-View**: Di bawah breakpoint `md:`, baris `<tr>` diubah menjadi blok kotak berjejer (Card), dan kolom tabel `<td>` berubah menjadi format Key-Value per baris (menggunakan Flexbox).

---

## 3. Blueprint Kode Master (The Minimalist Data Table)

Berikut template dasar tabel *clean & modern* (SaaS style) dengan gaya baris tanpa border vertikal dan interaksi *hover* yang lembut. Ideal dikembangkan menggunakan **TanStack Table**.

```tsx
import { MoreHorizontal, ArrowUpDown } from "lucide-react";

const DATA = [
  { id: "#INV-001", client: "Acme Corp", amount: "$1,250.00", status: "Paid", date: "Oct 24, 2024" },
  { id: "#INV-002", client: "Globex Inc", amount: "$840.50", status: "Pending", date: "Oct 26, 2024" },
  { id: "#INV-003", client: "Initech", amount: "$4,500.00", status: "Overdue", date: "Oct 15, 2024" },
];

export function MinimalistDataTable() {
  return (
    <div className="w-full overflow-hidden rounded-xl border border-slate-800 bg-slate-900">
      <div className="overflow-x-auto no-scrollbar">
        <table className="w-full text-sm text-left whitespace-nowrap">
          
          {/* Header */}
          <thead className="bg-slate-800/50 text-slate-400 font-medium border-b border-slate-800">
            <tr>
              <th scope="col" className="px-6 py-3">
                <div className="flex items-center gap-2 cursor-pointer hover:text-slate-200 transition-colors">
                  Invoice ID
                  <ArrowUpDown className="w-3.5 h-3.5" />
                </div>
              </th>
              <th scope="col" className="px-6 py-3">Client</th>
              <th scope="col" className="px-6 py-3">Date</th>
              <th scope="col" className="px-6 py-3 text-right">Amount</th>
              <th scope="col" className="px-6 py-3 text-center">Status</th>
              <th scope="col" className="px-6 py-3 text-right">Action</th>
            </tr>
          </thead>
          
          {/* Body */}
          <tbody className="divide-y divide-slate-800/60">
            {DATA.map((row) => (
              <tr key={row.id} className="hover:bg-slate-800/30 transition-colors group">
                <td className="px-6 py-4 font-mono font-medium text-slate-300">
                  {row.id}
                </td>
                <td className="px-6 py-4 text-slate-300">
                  {row.client}
                </td>
                <td className="px-6 py-4 text-slate-400">
                  {row.date}
                </td>
                <td className="px-6 py-4 text-right font-mono text-slate-200">
                  {row.amount}
                </td>
                <td className="px-6 py-4 text-center">
                  {/* Reuse the Status Badge (Chip) Component here */}
                  <span className={`inline-flex px-2 py-0.5 rounded-md text-xs font-medium border ${
                    row.status === "Paid" ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20" :
                    row.status === "Pending" ? "bg-amber-500/10 text-amber-400 border-amber-500/20" :
                    "bg-rose-500/10 text-rose-400 border-rose-500/20"
                  }`}>
                    {row.status}
                  </span>
                </td>
                <td className="px-6 py-4 text-right">
                  <button className="p-1.5 rounded-md text-slate-500 hover:text-slate-300 hover:bg-slate-700 transition-colors focus:outline-none">
                    <MoreHorizontal className="w-4 h-4" />
                  </button>
                </td>
              </tr>
            ))}
            
            {/* Contoh Empty State (dikomentari agar bisa digunakan jika DATA.length === 0) */}
            {/* 
            {DATA.length === 0 && (
              <tr>
                <td colSpan={6} className="px-6 py-12 text-center text-slate-500">
                  <div className="flex flex-col items-center justify-center gap-2">
                    <span className="text-4xl block mb-2">📂</span>
                    <p className="font-medium text-slate-300">Belum ada data tersedia.</p>
                    <p className="text-xs">Buat invoice baru untuk memulai.</p>
                  </div>
                </td>
              </tr>
            )} 
            */}
          </tbody>
        </table>
      </div>
      
      {/* Footer / Pagination Area */}
      <div className="px-6 py-3 border-t border-slate-800 bg-slate-900/50 flex items-center justify-between text-xs text-slate-400">
        <span>Menampilkan 3 dari 128 hasil</span>
        <div className="flex items-center gap-2">
          <button className="px-3 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors disabled:opacity-50">Prev</button>
          <button className="px-3 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors">Next</button>
        </div>
      </div>
    </div>
  );
}
```
