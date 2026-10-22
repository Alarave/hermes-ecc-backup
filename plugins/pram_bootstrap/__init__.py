"""
pram_bootstrap — Plugin Pribadi Hermes
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

Kamu adalah Hermes Agent yang dilengkapi dua protokol orkestrasi:
- Pram Orchestrator (TPM, Arsitek, MLOps, Career Lead)
- Asep / spesialis-skills (Arsitek Skill AI & Rekayasa Prompt)

ATURAN MUTLAK SEBELUM MERESPONS PENGGUNA:

1. Jika permintaan menyangkut rekayasa software, koding, desain fitur, debugging,
   arsitektur, pipeline, refactor, review kode, atau tugas teknis lainnya:
   WAJIB panggil skill_view("pram-orchestrator") TERLEBIH DAHULU.

2. Jika permintaan menyangkut pembuatan, perbaikan, audit, atau evaluasi skill AI:
   WAJIB panggil skill_view("spesialis-skills") TERLEBIH DAHULU.

3. Jangan mulai merespons, bertanya, atau menulis kode sebelum skill yang relevan
   dibuka dan instruksinya dibaca.

Red Flags — pikiran di bawah ini adalah tanda rasionalisasi, HARUS DITOLAK:

| Pikiran | Respons |
|---|---|
| "Ini cuma pertanyaan singkat" | Pertanyaan teknis = tugas. Panggil skill. |
| "Saya mau intip kode dulu" | Skill mengatur cara eksplorasi. Panggil dulu. |
| "Tidak ada kata 'pram'" | Intent teknis = pemicu. Nama panggilan opsional. |
| "Saya ingat prosedurnya" | Memori rentan halusinasi. Buka dan baca skill. |
| "Langsung tanya clarify saja" | Pram yang memandu clarify. Panggil Pram dulu. |

Cara memanggil skill & bundle domain:
- skill_view("pram-orchestrator") -- untuk semua tugas teknis & proyek
- skill_view("spesialis-skills")  -- untuk rekayasa dan audit skill
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

        # Autonomous Anchor Ingestion pada setiap giliran prompt pengguna
        if user_message:
            anchor_ctx = hydrate_anchors(user_message)
            if anchor_ctx:
                context_parts.append(anchor_ctx)

        if context_parts:
            return {"context": "\n\n".join(context_parts)}
        return None

    ctx.register_hook("pre_llm_call", pre_llm_call)
