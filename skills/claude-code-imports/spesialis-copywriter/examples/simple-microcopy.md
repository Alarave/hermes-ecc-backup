# CONTOH PENULISAN TEKS MIKRO (SIMPLE MICROCOPY EXEMPLAR)

Contoh nyata penerapan penulisan teks mikro antarmuka pengguna pada sistem software kasir toko retail.

---

## 1. Konteks Skenario
- **Produk**: Aplikasi Kasir & Manajemen Stok Multi-Cabang.
- **Pengguna**: Staf kasir dan pemilik toko retail harian.
- **Karakteristik Teks**: Ringkas, langsung ke solusi, tanpa basa-basi, dan ramah pengguna.

---

## 2. Perbandingan Naskah Mikro

### A. Tombol Aksi Utama (Call to Action)
- *Format Lama (Pasif & Generik)*: Submit / Kirim / Klik di Sini
- *Format Baru (Bernilai Aksi Nyata)*:
  - Tombol Checkout: `Selesaikan Transaksi (Rp185.000)`
  - Tombol Tambah Produk: `Tambah Produk Baru`
  - Tombol Ekspor Laporan: `Unduh Rekap Excel`

### B. Pesan Kesalahan Solutif (Constructive Error State)
- *Format Lama (Menyalahkan Pengguna)*: "Error! Stok barang tidak valid. Transaksi gagal diproses."
- *Format Baru (Solutif & Informatif)*:
  - *Judul*: Stok Kopi Arabika Tersisa 2 Bungkus
  - *Pesan*: Jumlah yang diminta melebihi sisa stok di rak. Kurangi jumlah pesanan atau lakukan penyesuaian stok gudang terlebih dahulu.
  - *Tombol Aksi*: `Sesuaikan Jumlah Pesanan`

### C. Status Layar Kosong (Empty State)
- *Format Lama*: "Tidak ada data transaksi."
- *Format Baru*:
  - *Judul*: Belum Ada Penjualan Hari Ini
  - *Subjudul*: Catat pesanan pertama pelanggan untuk mulai memantau arus kas harian Anda di layar ini.
  - *Tombol Aksi*: `Buka Kasir & Catat Pesanan`

### D. Konfirmasi Tindakan Berisiko (Destructive Action Modal)
- *Format Lama*: "Apakah Anda yakin ingin menghapus data ini?"
- *Format Baru*:
  - *Judul*: Hapus Data Cabang Tebet?
  - *Pesan*: Seluruh riwayat transaksi dan daftar inventaris cabang Tebet akan diarsipkan. Anda tetap dapat memulihkannya dalam 30 hari.
  - *Tombol Batal*: `Batal & Simpan Data`
  - *Tombol Hapus*: `Ya, Arsipkan Cabang`