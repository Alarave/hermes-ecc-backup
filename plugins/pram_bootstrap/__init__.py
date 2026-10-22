"""
pram_bootstrap — Plugin Pribadi Hermes
Menyuntikkan instruksi wajib pemanggilan Pram Orchestrator dan Asep
ke giliran pertama setiap sesi menggunakan hook pre_llm_call.

Pola diadaptasi dari obra/superpowers MIT License.
Tidak memerlukan koneksi jaringan.
"""

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


def hydrate_anchors(text: str) -> str:
    """
    Noēsis Two-Tier Context Hydration (arXiv:2609.07663):
    Mendeteksi path lokal dan URL secara deterministik dan menghidrasi
    fakta struktural tanpa biaya token LLM sebelum proses generasi dimulai.
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
    sections.append("Sistem mendeteksi referensi jangkar fisik dalam instruksi pengguna (Noēsis Two-Tier Context):")

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
                    preview = []
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        for _ in range(12):
                            line = f.readline()
                            if not line:
                                break
                            preview.append(line.rstrip())
                    snippet = "\n    ".join(preview[:8])
                    sections.append(
                        f"- 📄 [BERKAS FISIK TERVERIFIKASI]: `{p_str}` ({size_kb:.1f} KB)\n"
                        f"  - Cuplikan Konten Awal:\n    {snippet}"
                    )
            except Exception as e:
                sections.append(f"- ⚠️ [GAGAL MEMERIKSA PATH]: `{p_str}` ({e})")

    if urls:
        sections.append("\n[JANGKAR TAUTAN WEB/URL]:")
        for u in urls:
            if "youtube.com" in u or "youtu.be" in u:
                sections.append(f"- 🎥 [YOUTUBE RESOURCE]: `{u}` (Ekstrak transkrip/informasi langsung via transcribe/web_extract)")
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
