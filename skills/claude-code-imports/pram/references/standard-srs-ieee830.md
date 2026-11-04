# Standar Industri Dunia: Software Requirements Specification (SRS) - IEEE 830 & EARS (2025)

Template ini menggabungkan standar resmi **IEEE Std 830-1998**, riset terbaru **ISCAP 2025 (Preserving Requirements-Driven Development in the Age of AI)**, kurikulum resmi **System Analyst Universitas Gunadarma (2026)**, serta **OWASP ASVS 5.0 (2025)**. 

---

## 1. PENDAHULUAN
### 1.1 Tujuan (Purpose)
Menjelaskan tujuan pembuatan dokumen SRS, target pembaca (Developer, QA, Client), dan sifat dokumen sebagai kontrak formal (Execution Checklist untuk AI/Human Engineer).
### 1.2 Lingkup Produk (Product Scope)
Nama produk perangkat lunak, manfaat bisnis, tujuan operasional, dan batasan implementasi.
### 1.3 Definisi, Akronim, dan Singkatan
Tabel kamus istilah teknis dan istilah domain bisnis.
### 1.4 Referensi (References)
Daftar dokumen pendukung (Project Charter, Hasil Wawancara, Regulasi).

---

## 2. DESKRIPSI UMUM (OVERALL DESCRIPTION)
### 2.1 Perspektif Produk (Product Perspective)
Diagram Konteks Sistem (*Context Diagram*) atau Arsitektur Tingkat Tinggi.
### 2.2 Fungsi Produk (Product Functions)
Ringkasan fungsionalitas tingkat tinggi (Use Case global).
### 2.3 Karakteristik Pengguna (User Classes and Characteristics)
Tabel persona pengguna, tingkat pendidikan, dan hak akses teknis.
### 2.4 Batasan-Batasan (Constraints)
Batasan regulasi, keterbatasan *hardware*, limitasi Token API LLM, dan *guardrails*.

---

## 3. KEBUTUHAN SPESIFIK (SPECIFIC REQUIREMENTS)

### 3.1 Kebutuhan Antarmuka Eksternal (External Interface Requirements)
- **3.1.1 Antarmuka Pengguna (User Interfaces)**: Standar tata letak (*layout*), navigasi, responsivitas.
- **3.1.2 Antarmuka Perangkat Lunak & Komunikasi**: OS, Database, Protokol (HTTPS, WebSocket/SSE untuk *Streaming* LLM).

---

### 3.2 Kebutuhan Fungsional (Functional Requirements)
*Wajib menggunakan format EARS (Easy Approach to Requirements Syntax) dan ID Unik. Berdasarkan riset IEEE (Mavin dkk.), gunakan 5 templat ini agar sistem bebas dari ambiguitas:*

1. **Ubiquitous (Selalu Berjalan)**
   - *Sintaks*: `The <system> shall <system response>.`
   - *Contoh*: `The system shall encrypt all user passwords using bcrypt.`
2. **Event-Driven (Dipicu Kejadian)**
   - *Sintaks*: `WHEN <trigger> [precondition] THEN the <system> shall <system response>.`
   - *Contoh*: `WHEN user submits login form AND credentials are valid, THEN the system shall redirect to dashboard.`
3. **Unwanted Behaviors (Penanganan Error/Risiko)**
   - *Sintaks*: `IF <error condition>, THEN the <system> shall <system response>.`
   - *Contoh*: `IF the LLM API times out, THEN the system shall display a fallback error message and log the incident.`
4. **State-Driven (Berjalan Selama Status Tertentu)**
   - *Sintaks*: `WHILE <in a state>, the <system> shall <system response>.`
   - *Contoh*: `WHILE the AI is generating a response, the system shall display a typing indicator.`
5. **Optional Feature (Fitur Opsional/Tergantung Kondisi)**
   - *Sintaks*: `WHERE <feature is included>, THEN the <system> shall <system response>.`

**Format Tabel:**
| ID Kebutuhan | Nama Kebutuhan | Tipe EARS | Sintaks Kebutuhan (Requirements) | Prioritas |
| :--- | :--- | :--- | :--- | :--- |
| **FR-AUTH-01** | Login Berhasil | Event-Driven | WHEN user clicks login AND inputs are valid, THEN the system shall generate a JWT. | High |
| **FR-LLM-02** | LLM Streaming | State-Driven | WHILE LLM API is responding, the system shall stream the text chunk by chunk to the UI. | High |
| **FR-ERR-03** | LLM Hallucination | Unwanted | IF the LLM generates a competitor's name, THEN the system shall block the response. | High |

---

### 3.3 Kebutuhan Non-Fungsional (Non-Functional Requirements)
*Mengacu pada NIST CSF 2.0 & OWASP ASVS 5.0.*

1. **Kinerja (Performance)**: *Response Time* API di bawah 2 detik. Sistem RAG harus melakukan *embedding search* di bawah 500ms.
2. **Keamanan (Security)**: Proteksi terhadap SQL Injection, XSS, dan **Prompt Injection**. *Rate limiting* pada endpoint LLM.
3. **Ketersediaan & Keandalan (Reliability)**: *Uptime* 99,5%, *graceful degradation* saat pihak ketiga mati.
4. **Usability**: Aksesibilitas WCAG 2.1, UI responsif.

---

## 4. KRITERIA PENERIMAAN & PENGUJIAN (ACCEPTANCE CRITERIA)
- Penjelasan metode verifikasi (Unit Test, Black Box Testing, UAT).
- **Matriks Ketertelusuran Kebutuhan (RTM)**: Pemetaan `Kebutuhan Bisnis -> FR-ID -> Test Case ID (TC)`.
