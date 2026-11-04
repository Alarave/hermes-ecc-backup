# Observability & OpenTelemetry

## 1. Tiga Pilar Observabilitas
- **Logging**: Rekaman terstruktur per kejadian (JSON format, bukan teks polos).
- **Metrics**: Data aggregat numerik (CPU, RPM, Error Rate). Pakai RED Method.
- **Tracing**: Pelacakan request lintas layanan via Trace ID.

## 2. RED Method (Metrics)
Monitor 3 hal ini di dashboard:
- **Rate**: Jumlah request per detik (RPS).
- **Errors**: Jumlah request gagal (HTTP 5xx).
- **Duration**: Waktu latensi request (P50, P90, P99). Jangan pakai rata-rata (Average)!

## 3. Distributed Tracing (Trace ID & Span ID)
- Wajib inject `X-B3-TraceId` atau `traceparent` (W3C standard) di API Gateway / Edge Proxy.
- Teruskan header Trace ID ke semua internal call (HTTP/gRPC/Message Queue).
- Include Trace ID di setiap log output. (Misal: `{"level": "info", "trace_id": "xyz", "msg": "doing work"}`).

## 4. Structured Logging
- Jangan: `log.info(f"User {user_id} bought {item}")`
- Lakukan: `log.info("user_purchase_success", user_id=user_id, item=item)`
- **Alasan**: JSON log mudah diquery, digroup, dan dianalisis mesin (ELK/Loki).
