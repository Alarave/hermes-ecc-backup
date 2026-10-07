# API Security & Rate Limiting

## 1. Rate Limiting
- **Token Bucket Algorithm**: Cocok untuk burst rate yang diizinkan sesaat. Standard rate limiter Redis.
- **Leaky Bucket**: Request keluar pada kecepatan konstan. Bagus untuk sistem stabil.
- **Penempatan**: Pasang di API Gateway (Kong/KrakenD/Nginx) atau layer Middleware paling awal. Jangan sampai masuk ke business logic.
- Target block berdasar IP, User ID, atau API Key.

## 2. Circuit Breaker
- **Masalah**: Service A panggil Service B yang mati/sangat lambat. Koneksi Service A menumpuk (resource exhaustion).
- **Solusi**: Jika fail rate tinggi, "buka sirkuit" (Open) dan langsung return error (fail fast).
- Coba kirim pancingan 1 request setelah jeda waktu (Half-Open). Jika sukses, tutup sirkuit (Closed).

## 3. JWT Security & Revocation
- **Sifat JWT**: Stateless, tidak bisa dibatalkan dari sisi server sampai expired (kecuali signature dirotasi).
- **Solusi Log Out**: Gunakan Redis Blocklist untuk menyimpan JWT ID (JTI) atau token signature sampai batas TTL (waktu expired).
- Middleware cek token di Redis. Jika ada, tolak (HTTP 401).
- Jangan taruh JWT sensitif di LocalStorage. Gunakan HTTP-Only, Secure Cookies.

## 4. Input Validation (Defense in Depth)
- Percayai payload = Nol.
- Validasi strict boundaries: Panjang string max, regex format, batas angka.
- Cegah Mass Assignment: Jangan bind raw JSON body langsung ke ORM entity. Pakai DTO (Data Transfer Object) spesifik.
