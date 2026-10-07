# Distributed Lock & Idempotency

## 1. Idempotency (Mencegah Double Mutation)
- **Konsep**: Request yang sama diproses berkali-kali memberikan hasil state yang sama.
- **Implementasi**: Wajibkan header `Idempotency-Key` (UUID) pada endpoint mutasi (POST/PUT/PATCH).
- **Alur**:
  1. Cek `Idempotency-Key` di Redis/DB.
  2. Jika ada dan status `COMPLETED`, kembalikan cached response (HTTP 200/201).
  3. Jika ada dan status `PROCESSING`, kembalikan HTTP `409 Conflict`.
  4. Jika belum ada, simpan key dengan status `PROCESSING` (TTL 60 detik).
  5. Jalankan transaksi bisnis.
  6. Simpan hasil response, ubah status menjadi `COMPLETED` (TTL 24 jam).

## 2. Distributed Lock
- **Konsep**: Cegah race condition ketika multiple worker mengakses resource bersama.
- **Implementasi**:
  - Redis: `SET resource_lock <unique_token> NX PX <timeout_ms>`
  - Release lock hanya jika value sama (pakai Lua script):
    ```lua
    if redis.call("get", KEYS[1]) == ARGV[1] then
      return redis.call("del", KEYS[1])
    else
      return 0
    end
    ```
  - Postgres Native: `SELECT pg_advisory_xact_lock(:id)` (otomatis release saat transaksi commit/rollback).

## 3. Transactional Outbox Pattern
- **Masalah**: Dual-write issue (DB commit sukses tapi publish message broker gagal).
- **Solusi**:
  1. Simpan entitas dan record event ke tabel `outbox` dalam 1 transaksi DB.
  2. Poller worker (atau CDC Debezium) baca `outbox` dan publish ke broker.
  3. Hapus/tandai record `outbox` setelah broker mengirim ACK.
