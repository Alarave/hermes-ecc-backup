# OPERATIONAL REFERENCE: HYBRID RAG & STRUCTURED OUTPUTS ENGINE
> Resep produksi OpenAI Cookbook untuk retrieval akurasi tinggi (Hybrid Search + Cross-Encoder) dan jaminan 100% Structured Output (Pydantic).

---

## 1. Advanced Hybrid Retrieval (Dense Vector + BM25 Sparse)

Pendekatan vektor tunggal (Cosine Similarity) rentan gagal saat mencari istilah unik, ID produk, atau kode teknis spesifik. Standar produksi mewajibkan **Hybrid Retrieval**:

```text
                                  [USER QUERY]
                                       │
                 ┌─────────────────────┴─────────────────────┐
                 ▼                                           ▼
       [Dense Embeddings]                           [Sparse Keyword: BM25]
 (text-embedding-3-small/large)                    (Rank-BM25 / Elasticsearch)
                 │                                           │
                 └─────────────────────┬─────────────────────┘
                                       ▼
                       [Reciprocal Rank Fusion (RRF)]
                                       │
                                       ▼
                         [Cross-Encoder Re-Ranking]
                           (bge-reranker / Cohere)
                                       │
                                       ▼
                          [Top-K Context Payload]
```

### A. Algoritma Reciprocal Rank Fusion (RRF)
Gabungkan ranking dokumen dari pencarian Dense dan Sparse menggunakan formula standar RRF ($k=60$):

$$\text{Score}_{RRF}(d) = \frac{1}{60 + r_{\text{dense}}(d)} + \frac{1}{60 + r_{\text{sparse}}(d)}$$

```python
def reciprocal_rank_fusion(dense_ranks: list[str], sparse_ranks: list[str], k: int = 60) -> list[tuple[str, float]]:
    scores = {}
    for r, doc_id in enumerate(dense_ranks):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + r + 1)
    for r, doc_id in enumerate(sparse_ranks):
        scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + r + 1)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
```

### B. Cross-Encoder Re-Ranking
- Ambil Top-25 dokumen kandidat dari RRF.
- Hitung skor relevansi silang (*Cross-Attention*) menggunakan model Cross-Encoder:
  ```python
  from sentence_transformers import CrossEncoder

  reranker = CrossEncoder("BAAI/bge-reranker-base")
  pairs = [[query, doc.text] for doc in candidate_docs]
  scores = reranker.predict(pairs)
  top_docs = [doc for _, doc in sorted(zip(scores, candidate_docs), reverse=True)][:5]
  ```
- **Threshold Gate**: Jika skor relevansi dokumen teratas di bawah ambang batas (misal < 0.35), sistem WAJIB merespons: *"Informasi tidak ditemukan dalam basis pengetahuan terverifikasi"* untuk mencegah halusinasi.

---

## 2. Guaranteed Structured Outputs (Strict Mode)

Dilarang mengandalkan prompt biasa (*"respond only in JSON"*) karena rentan menghasilkan parsing crash. Wajib gunakan **OpenAI Structured Outputs** dengan `strict: true`.

### Implementasi Pydantic Schema
```python
from pydantic import BaseModel, Field
from openai import OpenAI

class EvidenceExtraction(BaseModel):
    key_finding: str = Field(description="Temuan utama dari konteks")
    confidence_score: float = Field(ge=0.0, le=1.0, description="Tingkat keyakinan 0.0 sampai 1.0")
    source_reference: str = Field(description="Kutipan langsung dari dokumen")

client = OpenAI()

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Ekstrak informasi penting secara presisi."},
        {"role": "user", "content": document_text},
    ],
    response_format=EvidenceExtraction,  # Menjamin 100% validitas skema
)

result: EvidenceExtraction = completion.choices[0].message.parsed
```

### Jaminan Keandalan:
1. Skema ditolak di level API jika tidak memenuhi validasi subset JSON Schema.
2. Tidak ada *extra keys* yang dihalusinasikan model.
3. Tipe data (integer, float, boolean, enum) dijamin sesuai spesifikasi kode aplikasi.
