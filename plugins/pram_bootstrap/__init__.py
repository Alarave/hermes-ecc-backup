"""
pram_bootstrap: Plugin Pribadi Hermes
Menyuntikkan instruksi wajib pemanggilan Pram Orchestrator dan Asep
ke giliran pertama setiap sesi menggunakan hook pre_llm_call.

Pola diadaptasi dari obra/superpowers MIT License.
Tidak memerlukan koneksi jaringan.
"""

import os
import re
from pathlib import Path
from typing import Any

BOOTSTRAP_MARKER = "pram_bootstrap:injected"

BOOTSTRAP_TEXT = """\
<SANGAT_PENTING>
{marker}

Kamu adalah Hermes Agent yang dilengkapi trio kepemimpinan orkestrasi:
- Pram Orchestrator (TPM, Arsitek, MLOps, Career Lead)
- Asep / spesialis-skills (Arsitek Skill AI & Rekayasa Prompt)
- Ahli Riset Akademik (spesialis-research-akademik: Penulisan Ilmiah, Brief, Format Naskah)

ATURAN MUTLAK SEBELUM MERESPONS PENGGUNA:

1. Jika permintaan menyangkut rekayasa software, koding, desain fitur, debugging,
   arsitektur, pipeline, refactor, review kode, atau tugas teknis lainnya:
   WAJIB panggil skill_view("pram-orchestrator") TERLEBIH DAHULU.

2. Jika permintaan menyangkut pembuatan, perbaikan, audit, atau evaluasi skill AI:
   WAJIB panggil skill_view("spesialis-skills") TERLEBIH DAHULU.

3. Jika permintaan menyangkut riset akademik, skripsi, tesis, paper, proposal, brief penelitian,
   format naskah atau dokumen, sitasi, atau penulisan bab:
   WAJIB panggil skill_view("spesialis-research-akademik") TERLEBIH DAHULU.
   STANDAR PENULISAN BAKU MUTLAK:
   - Format Geometri Fisik: A4 margin 4-4-3-3 cm, Times New Roman 12 pt, spasi 1.5, rata kiri-kanan (justified), indentasi awal paragraf 36 pt (1,27 cm).
   - Penomoran: Bab Arab (1. PENDAHULUAN, 2. TINJAUAN PUSTAKA), sub-bab tanpa titik penutup (1.1 Latar Belakang, 2.1 Penelitian Terdahulu).
   - Sitasi Harvard Author-Date & Aturan First-Mention: 3-5 penulis wajib disebut lengkap pada pemunculan pertama ('Ramadhani, Dewanta, dan Gunawan (2026)'), baru pemunculan berikutnya 'dkk.'.
   - Bahasa Indonesia Baku: WAJIB 'dkk.', DILARANG 'et al.' atau tanda '&'.
   - Eliminasi AI Slop Kurung: DILARANG pola terjemahan ganda padanan_indonesia (*istilah_asing*). Pilih satu istilah teknis murni cetak miring (*deep learning*, *backbone*, *bounding box*).
   - Tabel dan Gambar: Judul tabel di ATAS (Tabel X.Y Judul), judul gambar di BAWAH (Gambar X.Y Judul), keduanya tanpa titik penutup.
   - Plaintext Siap Salin: Sajikan draf naskah dalam blok kode plaintext bersih (```text) agar siap disalin langsung ke Word atau Google Docs tanpa kerusakan format.

4. Jangan mulai merespons, bertanya, atau menulis kode atau naskah sebelum skill yang relevan
   dibuka dan instruksinya dibaca.

5. DISIPLIN OPERASIONAL OH MY HERMES (OMH WORKFLOW DISCIPLINE):
   - Evidence-Based Gating: Status "Prepared" BUKAN "Observed". DILARANG mengklaim pekerjaan selesai tanpa bukti eksekusi nyata terminal, laporan test runner hijau, atau berkas fisik di disk.
   - Pelacakan Multi-Langkah: Pada tugas rekayasa atau analisis multi-tahap (3 langkah atau lebih), deklarasikan dan sinkronkan progres kerja secara terstruktur (omh_todo).
   - Pemisahan Siklus: Pisahkan secara tegas antara persiapan handoff (ulw-maestro / ulw-work), eksekusi, verifikasi mandiri (verification-gate), review kode (code-review), dan penutupan tugas (omh_run_summary).

Red Flags: pikiran di bawah ini adalah tanda rasionalisasi, HARUS DITOLAK:

| Pikiran | Respons |
|---|---|
| "Ini cuma pertanyaan singkat" | Pertanyaan teknis/penulisan = tugas. Panggil skill. |
| "Saya mau intip kode/brief dulu" | Skill mengatur cara eksplorasi. Panggil dulu. |
| "Tidak ada kata 'pram' atau 'skripsi'" | Intent teknis/penulisan = pemicu. Nama panggilan opsional. |
| "Saya ingat prosedurnya" | Memori rentan halusinasi. Buka dan baca skill. |
| "Format penulisan pakai markdown biasa saja" | Ditolak: Terapkan standar naskah baku spesialis-research-akademik. |
| "Langsung klaim berhasil tanpa cek terminal" | Ditolak: Wajib bukti nyata terminal (OMH Evidence Gate). |
| "Langsung tanya clarify saja" | Pram yang memandu clarify. Panggil Pram dulu. |

Cara memanggil skill & bundle domain:
- skill_view("pram-orchestrator") -- untuk semua tugas teknis & proyek
- skill_view("spesialis-skills")  -- untuk rekayasa dan audit skill
- skill_view("spesialis-research-akademik") -- untuk riset, skripsi, brief, paper, sitasi, dan naskah
- Navigasi 720+ skill atomik: baca references/skill-registry.md di dalam Pram
- Shortcut Bundle Domain (12 Klaster):
  /backend, /frontend, /mobile, /ml, /devops, /security,
  /pm, /research, /workspace, /scraper, /creative, /skill-arch
</SANGAT_PENTING>
""".format(marker=BOOTSTRAP_MARKER)


def extract_code_symbols(p: Path, max_symbols=8):
    try:
        suffix = p.suffix.lower()
        content = p.read_text(encoding="utf-8", errors="ignore")
        symbols = []
        if suffix == ".py":
            import ast
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    methods = [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
                    m_str = f"({', '.join(methods[:3])})" if methods else ""
                    symbols.append(f"class {node.name}{m_str}")
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    args = [a.arg for a in node.args.args][:3]
                    symbols.append(f"def {node.name}({', '.join(args)})")
        elif suffix in [".ts", ".tsx", ".js", ".jsx"]:
            import re
            for m in re.finditer(r'(export\s+)?(class|interface|type)\s+([A-Za-z0-9_]+)', content):
                symbols.append(f"{m.group(2)} {m.group(3)}")
            for m in re.finditer(r'(export\s+)?(async\s+)?function\s+([A-Za-z0-9_]+)', content):
                symbols.append(f"fn {m.group(3)}()")
        elif suffix in [".md", ".markdown"]:
            import re
            for m in re.finditer(r'^(#{1,3})\s+(.+)$', content, re.MULTILINE):
                symbols.append(f"{m.group(1)} {m.group(2).strip()[:40]}")
        return list(dict.fromkeys(symbols))[:max_symbols]
    except Exception:
        return []


def get_youtube_transcript_snippet(url: str, timeout_sec=3) -> str:
    try:
        import re
        import socket
        from youtube_transcript_api import YouTubeTranscriptApi
        m = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
        if not m:
            return ""
        v_id = m.group(1)
        socket.setdefaulttimeout(timeout_sec)
        yt = YouTubeTranscriptApi()
        transcript: Any = yt.fetch(v_id, languages=['en', 'id'])
        snippets: Any = getattr(transcript, 'snippets', transcript)
        words = [getattr(s, 'text', str(s)) for s in snippets[:35]]
        return " ".join(words)
    except Exception as e:
        return ""


def hydrate_anchors(text: str) -> str:
    """
    Noēsis Two-Tier Context Hydration (arXiv:2609.07663) + Aider RepoMap Pattern:
    Mendeteksi path lokal, simbol AST, dan URL YouTube/Web secara deterministik
    tanpa biaya token LLM sebelum proses generasi dimulai.
    """
    if not text:
        return ""

    import re
    from pathlib import Path

    # 1. Deteksi path Windows dan POSIX
    paths = re.findall(r'(?<![A-Za-z0-9])[A-Za-z]:[\\/][^\s"\'<>|]+', text)
    posix_paths = re.findall(r'(?:^|\s)(\./[^\s"\'<>|]+|\.\./[^\s"\'<>|]+|/c/[^\s"\'<>|]+)', text)
    all_paths = list(dict.fromkeys(paths + [p.strip() for p in posix_paths]))

    # 2. Deteksi URL
    urls = list(dict.fromkeys(re.findall(r'https?://[^\s"\'<>]+', text)))

    if not all_paths and not urls:
        return ""

    sections = ["<AUTONOMOUS_ANCHOR_INGESTION>"]
    sections.append("Sistem mendeteksi referensi jangkar fisik dalam instruksi pengguna (Noēsis Two-Tier Context + AST RepoMap):")

    if all_paths:
        sections.append("\n[JANGKAR PATH LOKAL]:")
        for p_str in all_paths:
            try:
                p = Path(p_str)
                if not p.exists():
                    sections.append(f"- ❌ [TIDAK DITEMUKAN PADA DISK]: `{p_str}`")
                elif p.is_dir():
                    items = list(p.iterdir())
                    files = [i.name for i in items if i.is_file()][:10]
                    dirs = [i.name for i in items if i.is_dir()][:6]
                    sections.append(
                        f"- 📁 [DIREKTORI TERVERIFIKASI]: `{p_str}`\n"
                        f"  - Total: {len(items)} item ({len(files)} files, {len(dirs)} subfolder)\n"
                        f"  - Sampel Berkas: {files}\n"
                        f"  - Sampel Subfolder: {dirs}"
                    )
                elif p.is_file():
                    size_kb = p.stat().st_size / 1024
                    symbols = extract_code_symbols(p)
                    sym_info = f"\n  - AST Symbols / Struktur: {symbols}" if symbols else ""
                    preview = []
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        for _ in range(12):
                            line = f.readline()
                            if not line:
                                break
                            preview.append(line.rstrip())
                    snippet = "\n    ".join(preview[:8])
                    sections.append(
                        f"- 📄 [BERKAS FISIK TERVERIFIKASI]: `{p_str}` ({size_kb:.1f} KB){sym_info}\n"
                        f"  - Cuplikan Konten Awal:\n    {snippet}"
                    )
            except Exception as e:
                sections.append(f"- ⚠️ [GAGAL MEMERIKSA PATH]: `{p_str}` ({e})")

    if urls:
        sections.append("\n[JANGKAR TAUTAN WEB/URL]:")
        for u in urls:
            if "youtube.com" in u or "youtu.be" in u:
                yt_transcript = get_youtube_transcript_snippet(u)
                snippet_text = f"\n  - Spoken Transcript Snippet: \"{yt_transcript}\"" if yt_transcript else ""
                sections.append(f"- 🎥 [YOUTUBE RESOURCE]: `{u}`{snippet_text}")
            elif "github.com" in u:
                sections.append(f"- 🐙 [GITHUB REPOSITORY]: `{u}` (Pindai repositori/struktur kode)")
            elif "arxiv.org" in u:
                sections.append(f"- 📚 [ARXIV PAPER]: `{u}` (Ekstrak metadata/PDF via skill arxiv)")
            else:
                sections.append(f"- 🌐 [WEB RESOURCE]: `{u}` (Ambil konten bersih via web_extract)")

    sections.append("\nINSTRUKSI PRAM: Gunakan konteks fisik nyata di atas secara langsung. Jangan tanyakan ulang keberadaan berkas/folder yang sudah terverifikasi.")
    sections.append("</AUTONOMOUS_ANCHOR_INGESTION>")
    return "\n".join(sections)


# ---------------------------------------------------------------------------
# DOMAIN TAXONOMY & UNIVERSAL SKILL BINDING ENGINE
# ---------------------------------------------------------------------------

DOMAIN_TAXONOMY = {
    "research": {
        "name": "Riset Akademik, Skripsi & Naskah Ilmiah",
        "pic": "spesialis-research-akademik",
        "bundle": "/research",
        "keywords": [
            "skripsi", "tesis", "disertasi", "paper", "jurnal", "makalah", "proposal",
            "naskah", "tinjauan pustaka", "bab 1", "bab 2", "bab 3", "bab 4", "bab 5",
            "metodologi", "penelitian", "sitasi", "citation", "harvard", "daftar pustaka",
            "format penulisan", "paragraf", "margin", "4-4-3-3", "brief", "pedoman",
            "gunadarma", "upnvj", "sota", "state-of-the-art", "diebold-mariano", "academic", "thesis"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-research-akademik') SEBELUM merespons.\n"
            "- STANDAR FORMAT BAKU MUTLAK: A4 margin 4-4-3-3 cm, Times New Roman 12 pt, 1.5 spasi, rata kiri-kanan (justified), indentasi awal paragraf 36 pt (1,27 cm).\n"
            "- Penomoran: Bab Arab (1. PENDAHULUAN), sub-bab tanpa titik penutup (1.1 Latar Belakang).\n"
            "- Sitasi Harvard First-Mention: 3-5 penulis wajib disebut lengkap pada pemunculan pertama ('Ramadhani, Dewanta, dan Gunawan (2026)'), baru pemunculan berikutnya 'dkk.'.\n"
            "- Eliminasi AI Slop Kurung: DILARANG pola terjemahan ganda padanan (*istilah asing*). Gunakan istilah murni cetak miring (*deep learning*, *backbone*).\n"
            "- Format Draf Siap Salin: Sajikan draf naskah dalam blok kode plaintext bersih (```text) agar siap disalin langsung ke Word atau Google Docs tanpa kerusakan format."
        )
    },
    "backend": {
        "name": "Backend & REST API Engineering",
        "pic": "spesialis-backend",
        "bundle": "/backend",
        "keywords": [
            "backend", "api", "rest api", "endpoint", "database", "postgres", "postgresql",
            "mysql", "sqlite", "prisma", "migration", "fastapi", "express", "nest",
            "better-auth", "supabase", "jwt", "oauth", "crud"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-backend') atau skill_view('api-design').\n"
            "- SOP: Spec -> Plan -> TDD -> Code (DILARANG langsung koding tanpa kontrak DTO)."
        )
    },
    "frontend": {
        "name": "Frontend & UI Engineering",
        "pic": "spesialis-frontend",
        "bundle": "/frontend",
        "keywords": [
            "frontend", "ui", "ux", "tampilan", "slicing", "react", "next.js", "nextjs",
            "tailwind", "css", "html", "komponen", "component", "desain antarmuka",
            "landing page", "dashboard ui", "web design"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-frontend') dan terapkan anti-ui-slop.\n"
            "- Hindari template generik AI, WCAG contrast pass, status komponen lengkap (loading, empty, error)."
        )
    },
    "ml": {
        "name": "Machine Learning, AI & Data Science",
        "pic": "spesialis-data-ai-agentic",
        "bundle": "/ml",
        "keywords": [
            "machine learning", "deep learning", "data science", "ml", "ai model", "training",
            "dataset", "prediksi", "forecasting", "time series", "lstm", "ceemdan", "timesfm",
            "cnn", "yolo", "object detection", "vlm", "ocr", "eda", "data leakage",
            "data preparation", "scikit", "pytorch", "huggingface", "transformers", "unsloth"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-data-ai-agentic').\n"
            "- Wajib anti-leakage split (split sebelum scaling/dekomposisi), Diebold-Mariano test, dan evaluasi metrik empiris."
        )
    },
    "devops": {
        "name": "DevOps, Cloud & Deployment",
        "pic": "spesialis-devops-infrastruktur",
        "bundle": "/devops",
        "keywords": [
            "devops", "deploy", "deployment", "docker", "dockerfile", "compose", "ci/cd",
            "github actions", "pipeline", "kubernetes", "k8s", "infra", "infrastruktur",
            "server", "cloud", "vercel", "caddy", "nginx"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-devops-infrastruktur').\n"
            "- Pastikan konfigurasi aman tanpa hardcoded secret, minimal image size, multi-stage build."
        )
    },
    "security": {
        "name": "Security Review & QA Testing",
        "pic": "spesialis-security-qa",
        "bundle": "/security",
        "keywords": [
            "security", "keamanan", "vulnerability", "celah", "pentest", "sast",
            "audit kode", "qa", "testing", "test", "tdd", "unit test", "e2e", "playwright", "bug", "regression"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-security-qa') atau skill_view('security-review').\n"
            "- Terapkan TDD (Red-Green-Refactor) dan verifikasi bukti test pass di terminal."
        )
    },
    "mobile": {
        "name": "Mobile App Development",
        "pic": "spesialis-mobile",
        "bundle": "/mobile",
        "keywords": [
            "mobile", "android", "ios", "flutter", "dart", "react native", "swift",
            "swiftui", "kmp", "kotlin multiplatform", "aplikasi hp"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-mobile').\n"
            "- Terapkan Clean Architecture / BLoC / Provider."
        )
    },
    "pm": {
        "name": "Product Management & Karier",
        "pic": "spesialis-project-manager",
        "bundle": "/pm",
        "keywords": [
            "product manager", "pm", "prd", "bisnis", "wbs", "roadmap", "tpm", "proyek",
            "scrum", "sprint", "lean canvas", "business model", "cari kerja", "lowongan", "resume", "cv", "interview"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-project-manager') atau skill_view('spesialis-product-bisnis').\n"
            "- Alokasi PIC riil (Firman: Lead), batasan non-scope ketat."
        )
    },
    "workspace": {
        "name": "Obsidian Vault & Workspace",
        "pic": "spesialis-produktivitas-workspace",
        "bundle": "/workspace",
        "keywords": [
            "obsidian", "vault", "catatan", "note", "kuliah", "belajar", "materi", "rangkuman", "markitdown", "workspace"
        ],
        "rules": (
            "- WAJIB panggil skill_view('note') atau skill_view('cli-anything-obsidian').\n"
            "- Lokasi Vault: E:\\BELAJAR BANGET\\SKILL BELAJAR. Terapkan struktur 0-100."
        )
    },
    "scraper": {
        "name": "Web Scraping & Automation",
        "pic": "multi-platform-scraper",
        "bundle": "/scraper",
        "keywords": [
            "scrape", "scraping", "scraper", "crawl", "crawling", "ekstrak web", "scrapling", "browser automation", "unduh web"
        ],
        "rules": (
            "- WAJIB panggil skill_view('multi-platform-scraper') atau skill_view('scrapling').\n"
            "- Utamakan parser DOM cepat dibanding headless browser berat."
        )
    },
    "creative": {
        "name": "Copywriting & Creative Media",
        "pic": "spesialis-copywriter",
        "bundle": "/creative",
        "keywords": [
            "copywriter", "copywriting", "artikel", "konten", "media", "video", "animasi", "manim", "remotion", "social media"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-copywriter') atau skill_view('spesialis-kreatif-media').\n"
            "- Terapkan zero-slop naskah (eliminasi 96 kata klise AI)."
        )
    },
    "skill-arch": {
        "name": "Rekayasa Skill AI (Asep Engine)",
        "pic": "spesialis-skills",
        "bundle": "/skill-arch",
        "keywords": [
            "skill", "buat skill", "update skill", "edit skill", "audit skill", "asep",
            "prompt engineering", "rcco", "evals", "skill persistence"
        ],
        "rules": (
            "- WAJIB panggil skill_view('spesialis-skills') atau skill_view('skill-persistence').\n"
            "- Standar RCCO, description <= 60 karakter, lolos linter strict 100/100."
        )
    },
    "general-engineering": {
        "name": "Rekayasa Software Umum (Pram Engine & Karpathy Guidelines)",
        "pic": "pram-orchestrator",
        "bundle": "/pm",
        "keywords": [
            "bikin fitur", "buat fitur", "koding", "coding", "bantu koding", "rancang arsitektur",
            "desain sistem", "refactor", "pipeline", "buat aplikasi", "implementasi", "debugging", "fix bug",
            "karpathy", "karpathy-guidelines", "code review", "koding bersih", "anti slop koding"
        ],
        "rules": (
            "- WAJIB panggil skill_view('pram-orchestrator').\n"
            "- SOP MUTLAK: Spec -> Plan -> TDD -> Code.\n"
            "- TEGAKKAN PEDOMAN KARPATHY (skill_view('karpathy-guidelines')): 1) Think before coding (klarifikasi asumsi), 2) Simplicity first (YAGNI, no bloat), 3) Surgical changes (direct patch, zero collateral damage), 4) Goal-driven execution (looping hingga kriteria uji hijau)."
        )
    }
}

_EXACT_SKILL_REGEX = None


def get_exact_skill_regex():
    global _EXACT_SKILL_REGEX
    if _EXACT_SKILL_REGEX is None:
        try:
            skills_dir = Path(__file__).resolve().parent.parent.parent / "skills"
            if skills_dir.exists():
                skills = sorted([s.name for s in skills_dir.iterdir() if s.is_dir() and not s.name.startswith('.')], key=len, reverse=True)
                if skills:
                    _EXACT_SKILL_REGEX = re.compile(
                        r'(?<![a-zA-Z0-9_-])(' + '|'.join(re.escape(s) for s in skills if len(s) > 3) + r')(?![a-zA-Z0-9_-])',
                        re.IGNORECASE
                    )
        except Exception:
            pass
    return _EXACT_SKILL_REGEX


def detect_skill_intent(text: str) -> str:
    if not text:
        return ""

    lowered = text.lower()
    matched_domains = []

    for dom_key, conf in DOMAIN_TAXONOMY.items():
        for kw in conf["keywords"]:
            if re.search(r'(?<![a-z0-9_-])' + re.escape(kw) + r'(?![a-z0-9_-])', lowered):
                matched_domains.append(conf)
                break

    detected_exact_skills = []
    rgx = get_exact_skill_regex()
    if rgx:
        raw_found = rgx.findall(text)
        detected_exact_skills = list(dict.fromkeys(raw_found))

    if not matched_domains and not detected_exact_skills:
        return ""

    lines = ["<PERINTAH_ORCHESTRASI_SKILL_MUTLAK>"]
    lines.append("Sistem mendeteksi intent spesifik dalam pesan pengguna pada giliran ini:")

    if matched_domains:
        for d in matched_domains[:2]:
            lines.append(f"\n[DOMAIN: {d['name']} (Shortcut: {d['bundle']})]")
            lines.append(f"PIC Utama: skill_view(\"{d['pic']}\")")
            lines.append("Perintah Operasional:")
            lines.append(f"{d['rules']}")

    if detected_exact_skills:
        filtered_skills = [s for s in detected_exact_skills[:4] if not any(s.lower() == d['pic'].lower() for d in matched_domains)]
        if filtered_skills:
            lines.append(f"\n[SKILL SPESIFIK TERDETEKSI]: {', '.join(filtered_skills)}")
            lines.append("Panggil via skill_view() jika diperlukan untuk menyelesaikan instruksi.")

    lines.append(
        "\nATURAN MUTLAK:\n"
        "1. Agen DILARANG KERAS langsung merespons atau melompat koding tanpa memanggil skill terkait!\n"
        "2. Disiplin OMH: Pisahkan status 'Prepared' vs 'Observed'. Dilarang mengklaim selesai tanpa bukti uji fisik terminal.\n"
        "3. Jika tugas terdiri dari 3 langkah atau lebih, kelola progres menggunakan checklist terstruktur (omh_todo)."
    )
    lines.append("</PERINTAH_ORCHESTRASI_SKILL_MUTLAK>")
    return "\n".join(lines)


def register(ctx):
    def pre_llm_call(
        session_id=None,
        user_message=None,
        conversation_history=None,
        is_first_turn=None,
        model=None,
        platform=None,
        **kwargs,
    ):
        context_parts = []
        if is_first_turn:
            context_parts.append(BOOTSTRAP_TEXT)

        if user_message:
            intent_ctx = detect_skill_intent(user_message)
            if intent_ctx:
                context_parts.append(intent_ctx)

            anchor_ctx = hydrate_anchors(user_message)
            if anchor_ctx:
                context_parts.append(anchor_ctx)

        if context_parts:
            return {"context": "\n\n".join(context_parts)}
        return None

    ctx.register_hook("pre_llm_call", pre_llm_call)
