# Peningkatan Tahap Data Preparation (CRISP-DM Fase 3)

Dokumen ini memuat referensi literatur ilmiah dan implementasi kode Python deterministik untuk meningkatkan mutu prapemrosesan citra, kanonisasi atribut katalog, dan partisi dataset bebas bocor pada sistem verifikasi iklan katalog kosmetik.

---

## 1. Landasan Literatur Ilmiah Primer

1. **Gong et al. (2025)** - *Visual Zero-Shot E-Commerce Product Attribute Value Extraction (ViOC-AG)*, Proceedings of NAACL 2025 (Industry Track).
   - Membuktikan bahwa ekstraksi atribut kemasan fisik membutuhkan koreksi token OCR terhadap luaran VLM untuk menangani nilai atribut *out-of-domain* (OOD) dan menuntut preservasi potongan citra resolusi asli (*native resolution crop*).
2. **Wu, Bouyarmane, & Tutar (2022/2023)** - *Catalog Phrase Grounding (CPG): Grounding of Product Textual Attributes in Product Images for E-Commerce Vision-Language Applications*, Amazon Science.
   - Formulasi *decoupled attribute queries* dan metrik fusi spasial *Intersection over Area* (IoA) untuk mengatasi disparitas skala antara teks kecil kemasan dan kotak pelacak visual.
3. **Yang et al. (2022)** - *MAVE: A Product Dataset for Multi-source Attribute Value Extraction*, Proceedings of ACM WSDM 2022, hlm. 1256-1265.
   - Standar taksonomi atribut e-commerce multi-sumber untuk normalisasi kuantitas numerik dan satuan metrik baku.
4. **Zhang et al. (2021)** - *Text-Aware Single Image Specular Highlight Removal*, Springer LNCS / ICCV.
   - Penghilangan pantulan kilap (*specular highlight*) pada citra berteks untuk mencegah penurunan *recall* detektor DBNet dan rekognizer SVTR.
5. **Tan & Ikeuchi (2005)** - *Separating Reflection Components of Textured Surfaces Using a Single Image*, IEEE TPAMI, 27(2), hlm. 178-193.
   - Pemisahan komponen pantulan difus dan specular pada permukaan kemasan melengkung/mengilap.
6. **Kaufman et al. (2012)** - *Leakage in Data Mining: Formulations, Detection, and Avoidance*, ACM TKDD, 6(4), hlm. 1-21.
   - Landasan teoritis pencegahan kebocoran fitur kelompok (merek) antara data latih dan data uji.
7. **Sechidis, Tsoumakas, & Vlahavas (2011)** - *On the Stratification of Multi-Label Data*, ECML PKDD 2011, hlm. 145-158.
   - Metode penyeimbangan distribusi kelas kategori secara simultan pada partisi berbasis kelompok.

---

## 2. Implementasi Kode Peningkatan Prapemrosesan

### A. Atenuasi Specular Glare dengan Proteksi Latar Putih Studio
Mereduksi pantulan cahaya studio pada botol kaca/plastik menggunakan deteksi luminansi tinggi dan saturasi rendah dalam ruang warna HLS, dilanjutkan rekonstruksi Navier-Stokes inpainting.
- **Pitfall Guard**: Batasi inpainting hanya jika piksel mask kilap mencakup `0 < nonzero <= 35%` dari total piksel citra. Tanpa batas atas ini, latar belakang putih studio murni `RGB(255, 255, 255)` atau kanvas uji seragam akan salah terdeteksi sebagai glare dan mengalami degradasi inpainting.

```python
import cv2
import numpy as np

def suppress_specular_highlights(image_rgb: np.ndarray, lum_threshold: int = 240, sat_threshold: int = 40) -> np.ndarray:
    """
    Mereduksi pantulan specular highlight pada kemasan kosmetik berbasis ruang warna HLS.
    """
    hls = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HLS)
    _, l_channel, s_channel = cv2.split(hls)

    glare_mask = ((l_channel >= lum_threshold) & (s_channel <= sat_threshold)).astype(np.uint8) * 255
    nonzero = cv2.countNonZero(glare_mask)
    total_pixels = image_rgb.shape[0] * image_rgb.shape[1]

    if nonzero == 0 or nonzero > int(0.35 * total_pixels):
        return image_rgb

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    glare_mask = cv2.dilate(glare_mask, kernel, iterations=1)
    bgr = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2BGR)
    restored_bgr = cv2.inpaint(bgr, glare_mask, inpaintRadius=3, flags=cv2.INPAINT_NS)
    return cv2.cvtColor(restored_bgr, cv2.COLOR_BGR2RGB)
```

### B. Penajaman Teks Mikro Sebelum Downscaling (Bilateral + Unsharp Masking)
Mempertegas kontur karakter kecil (< 8 piksel) tanpa memperkuat noise latar belakang sebelum citra ditingkatkan kontrasnya dengan CLAHE dan ditempatkan ke kanvas letterbox 640x640.

```python
def enhance_micro_text(image_rgb: np.ndarray, amount: float = 1.2, radius: int = 3) -> np.ndarray:
    """
    Menerapkan edge-preserving smoothing diikuti unsharp masking untuk teks kemasan mikro.
    """
    smooth = cv2.bilateralFilter(image_rgb, d=5, sigmaColor=50, sigmaSpace=50)
    blurred = cv2.GaussianBlur(smooth, (0, 0), radius)
    sharpened = cv2.addWeighted(smooth, 1.0 + amount, blurred, -amount, 0)
    return np.clip(sharpened, 0, 255).astype(np.uint8)
```

### C. Parser Netto Multi-Pack, Bundel Aditif, dan Konversi Satuan Ganda (MAVE Extension)
Menangani empat pola bertingkat secara berurutan agar tetap idempoten (`f(f(x)) == f(x)`):
1. Multi-pack (`"2 x 50 ml"`, `"3x15g"`): kalikan jumlah pak dengan nilai satuan.
2. Additive bundle / refill (`"15 g + Refill 15 g"`, `"50 ml + 50 ml"`): jumlahkan nilai kedua komponen yang bersatuan sama.
3. Prioritas satuan metrik standar (`"100 ml / 3.38 fl. oz."` -> `"100 ml"`): dievaluasi sebelum satuan imperial agar angka metrik bulat tidak tertimpa hasil konversi desimal.
4. Fallback satuan imperial fluid ounce (`"1.69 fl. oz."` -> `round(val * 29.5735, 2)` ml).

### D. Partisi Bebas Bocor dengan Defisiensi Komposit Merek & Kategori
Untuk menjaga presisi rasio jumlah sampel `70:15:15` sekaligus menyeimbangkan proporsi subkategori (Skincare, Makeup, Hair Care) tanpa menggunakan solver eksternal, gunakan skor defisiensi komposit saat mengalokasikan merek secara greedy:
$$\text{score}_P = 0.5 \cdot \frac{T_{\text{global}, P} - C_{\text{global}, P}}{T_{\text{global}, P}} + 0.5 \cdot \frac{T_{k, P} - C_{k, P}}{T_{k, P}}$$
di mana $k$ adalah kategori dominan merek tersebut dan $P \in \{\text{train}, \text{val}, \text{test}\}$.
