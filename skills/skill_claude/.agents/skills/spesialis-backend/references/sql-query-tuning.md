# SQL Query Tuning & Optimization

## 1. EXPLAIN ANALYZE
- Selalu gunakan `EXPLAIN ANALYZE` untuk mengecek *query execution plan*.
- Jangan tebak-tebakan. Jika query lama, lihat apakah DB pakai *Seq Scan* (Full Table Scan) atau *Index Scan*.

## 2. Aturan Indexing
- **Left-Prefix Rule**: Pada composite index `(A, B, C)`, pencarian `A`, atau `A, B` akan pakai index. Pencarian hanya `B` atau `C` tidak akan pakai index (tergantung skip scan engine, tapi umumnya tidak optimal).
- **Kardinalitas**: Jangan pasang index di kolom bernilai seragam (misal: boolean `is_active` dengan 99% `true`).
- **Covering Index**: Masukkan kolom yang sering diselect ke index untuk menghindari heap fetch (hanya berlaku jika db mendukung).

## 3. Connection Pooling
- Jangan buka koneksi DB mentah di tiap HTTP request pada framework concurrency tinggi (terutama serverless/Go/Rust).
- Gunakan Pooler: HikariCP (Java), PgBouncer (Postgres global).
- Tentukan `max_connections` logis. Rumus kasar Postgres: `(cores * 2) + effective_spindle_count`.

## 4. N+1 Problem
- Jangan panggil query di dalam loop.
- **Solusi**: Gunakan Eager Loading (ORM `Select In`, `JOIN FETCH`) atau DataLoader pattern (GraphQL).
- **Contoh Buruk**:
  `users = db.get_users()` -> 1 query
  `for u in users: p = db.get_profile(u.id)` -> N query.
- **Contoh Baik**:
  `profiles = db.get_profiles(user_ids_array)` -> 1 query.
