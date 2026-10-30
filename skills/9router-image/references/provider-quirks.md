# 9Router Image Generation: Provider Quirks & Response Reference

> Referensi teknis parameter spesifik provider, skema respons, dan penanganan galat pada gateway 9Router (`/v1/images/generations`).

---

## 1. Skema Endpoint & Parameter Standar

Endpoint utama: `POST $NINEROUTER_URL/v1/images/generations` (default lokal: `http://127.0.0.1:20128/v1/images/generations`).

| Field | Wajib | Keterangan |
|:---|:---|:---|
| `model` | Ya | ID model dari `GET /v1/models/image` (contoh: `gemini/gemini-3-pro-image-preview`, `ag/gemini-3.1-flash-image`, `cx/gpt-image-2.5`). |
| `prompt` | Ya | Deskripsi teks gambar yang ingin dibuat. |
| `n` | Tidak | Jumlah gambar yang dihasilkan (bergantung dukungan provider). |
| `size` | Tidak | Resolusi gambar (`1024x1024`, `1792x1024`, `1024x1792`). |
| `quality` | Tidak | Tingkat kualitas (`standard` atau `hd`, khusus provider OpenAI). |
| `response_format` | Tidak | Format payload JSON: `url` (default) atau `b64_json`. |

Tambahkan query parameter `?response_format=binary` pada URL endpoint untuk menerima byte gambar mentah (`image/png` atau `image/jpeg`) secara langsung.

---

## 2. Matriks Perbedaan Parameter Antar-Provider (Provider Quirks)

| Provider | Field Tambahan / Perubahan | Catatan Operasional |
|:---|:---|:---|
| `openai`, `minimax`, `openrouter`, `recraft` | `quality`, `style`, `response_format` | Mengikuti spesifikasi standar OpenAI Images API. |
| `gemini` (`gemini-3-pro-image-preview`, `gemini-3.1-flash-image-preview`, `gemini-2.5-flash-image`) | Tidak ada | Hanya memproses `prompt`; mengabaikan parameter `size` dan `n`. |
| `ag` (`ag/gemini-3.1-flash-image`) | Tidak ada | Rute Antigravity untuk sintesis gambar Gemini Flash. |
| `codex` / `cx` (`gpt-5.4-image`, `cx/gpt-image-2.5`) | `image`, `images[]`, `image_detail`, `output_format`, `background` | Berbasis SSE stream; membutuhkan akun aktif pada 9Router. |
| `huggingface` | Tidak ada | Hanya menerima `prompt`; mengembalikan satu gambar tunggal. |
| `nanobanana` | `image`, `images[]` (mode edit) | `size` dikonversi menjadi rasio aspek; menggunakan async polling. |
| `fal-ai` | `image` (mode img2img) | `n` dipetakan ke `num_images`; `size` dipetakan ke rasio aspek; berjalan secara asinkron. |
| `stability-ai` | `style` (preset), `output_format` | Parameter `size` dipetakan ke `aspect_ratio`. |
| `black-forest-labs` (FLUX) | `image` (referensi) | Parameter `size` dipetakan ke dimensi `width` dan `height` presisi; berjalan asinkron. |
| `runwayml` | `image` (referensi) | Parameter `size` dipetakan ke rasio aspek; berjalan asinkron. |
| `sdwebui`, `comfyui` | Tidak ada | Instansi lokal tanpa autentikasi (`localhost:7860` atau `localhost:8188`). |

---

## 3. Skema Respons & Penanganan Galat

### A. Format Respons
1. **JSON URL (`response_format="url"`, default)**:
   ```json
   { "created": 1735000000, "data": [{ "url": "https://..." }] }
   ```
2. **JSON Base64 (`response_format="b64_json"`)**:
   ```json
   { "created": 1735000000, "data": [{ "b64_json": "iVBORw0KGgo..." }] }
   ```
3. **Binary Stream (`?response_format=binary`)**:
   Mengembalikan byte biner gambar langsung dengan header `Content-Type: image/png` atau `image/jpeg`.

### B. Penanganan Kode Galat (Error Troubleshooting)
| Kode HTTP | Penyebab Utama | Solusi Mitigasi |
|:---|:---|:---|
| `400 Invalid model format` | Nama model salah atau tidak terdaftar di katalog image. | Jalankan `curl -s $NINEROUTER_URL/v1/models/image` dan gunakan nilai persis dari `data[].id`. |
| `401 Unauthorized` | Gateway mengaktifkan `requireApiKey=true` tetapi header `Authorization` kosong/salah. | Ambil kunci dari 9Router Dashboard -> Keys dan kirim melalui header `Authorization: Bearer $NINEROUTER_KEY`. |
| `503 All accounts unavailable` | Kuota akun provider habis atau terkena rate-limit. | Tunggu sesuai header `retry-after`, ganti ke model provider alternatif (misal dari `gemini/` ke `ag/` atau `cx/`), atau tambah akun di 9Router. |
