# Event-Driven Architecture (EDA) & Streaming

## 1. Konsep Dasar Broker
- **Kapan Pakai Broker (Kafka/RabbitMQ)**:
  - Proses asinkron lambat (kirim email, generate PDF).
  - Integrasi antar service tanpa tight-coupling (Event Choreography).
  - Meredam lonjakan traffic (Spike leveling / Backpressure).

## 2. Kafka vs RabbitMQ
- **RabbitMQ**: Smart broker, dumb consumer. Bagus untuk routing kompleks (topic/direct exchange) dan task queue. Message hilang setelah ACK.
- **Kafka**: Dumb broker, smart consumer. Bagus untuk event streaming, log aggregasi, dan high-throughput. Message persisten, consumer track offset.

## 3. Aturan Main Consumer
- **Idempotency Wajib**: Consumer harus siap terima message yang sama berkali-kali (At-Least-Once delivery).
- **Dead Letter Queue (DLQ)**:
  - Jika pesan error saat diproses berulang (misal limit retry 3x), buang pesan ke antrean DLQ.
  - Tujuannya agar pesan cacat (poison pill) tidak menyumbat queue (Head-of-Line Blocking).
- **Graceful Shutdown**:
  - Stop menerima pesan baru saat SIGTERM.
  - Selesaikan message in-flight, ACK.
  - Putus koneksi bersih.
