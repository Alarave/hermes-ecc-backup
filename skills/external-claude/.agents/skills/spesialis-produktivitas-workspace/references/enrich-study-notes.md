# Enrich Study Notes

Use this skill when enriching, expanding, or updating Indonesian study notes — especially in Firman's knowledge base at `E:\BELAJAR BANGET\SKILL BELAJAR`. The goal is richer, more detailed materi with consistent Obsidian formatting.

## Procedure

1. **Identify Destination Folder**: Check `E:\BELAJAR BANGET\SKILL BELAJAR` subdirectories (e.g. `Finance`, `Personal Development`, `04_PROJECTS/Pengantar Bisnis TI`) to determine the exact path. Never just output the note into chat without writing the markdown file to disk.
2. **Read target file** with `read_file` if updating an existing note (full content, note total_lines). If creating a new note, verify target path.
3. **Survey sibling files** with `search_files` (target=files, *.md in same folder) — needed for accurate `[[wikilinks]]` at the bottom.
4. **Web search for supplementary material** — run 2–3 parallel searches covering:
   - The core topic at beginner/intermediate depth.
   - Practical examples, checklists, code snippets, or real-world applications.
   - Any career/industry context if the note touches applied skills.
5. **Compose enriched content** in full (overwrite, not append) using `write_file`.
6. **Verify** write succeeded (`verified: true` in result).

## Output Format (mandatory for every file)

### YAML Frontmatter
```yaml
---
title: <judul lengkap dalam bahasa Indonesia>
course: <nama kursus jika ada>
platform: <platform jika ada>
source_url: <URL sumber asli>
tags:
  - <topik-utama>
  - learning-notes
date_created: <YYYY-MM-DD asli>
date_updated: <YYYY-MM-DD hari ini>
---
```

### Content Structure
- **Heading 1**: emoji + judul utama (`# 📈 Judul`)
- **Sumber blockquote**: langsung di bawah H1
- **Sections**: numbered H2 headings (`## 📌 1. ...`, `## ❓ 2. ...`)
- **Callout boxes**: Obsidian syntax `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`, `> [!NOTE]`
- **Mermaid diagrams**: for flows, comparisons, taxonomies — prefer `flowchart TD` or `graph LR/TD`
- **Comparison tables**: for tools, roles, methods — columns: konsep | deskripsi | kapan digunakan
- **Code blocks**: language-tagged (```python, ```sql, ```text)
- **Math formulas**: LaTeX inline `$x$` or block `$$...$$`
- **Wikilinks block**: always last, inside `> [!NOTE]` callout

### Wikilinks Block (always last)
```markdown
> [!NOTE]
> **Catatan Terkait dalam Vault:**
> * [[Nama File Tetangga Tanpa .md]]
> * [[File Lainnya]]
```
Use actual sibling filenames from step 2 — never fabricate links.

## Language Rules
- **All prose in Bahasa Indonesia** — headings, descriptions, explanations, table content.
- **Technical terms**: keep English originals with Indonesian explanation on first use. Example: *"Overfitting (model terlalu hafal data latih)"*.
- **Code, file paths, terminal commands, math symbols**: always verbatim, no translation.
- **Emoji on every H2 heading** — pick semantically relevant ones.

## Content Enrichment Rules
- Add materi that was missing from the original: definitions, context, worked examples, formulas, code snippets, comparison tables, real-world use cases.
- Do NOT strip existing content — expand and reorganize it.
- Mermaid diagrams preferred over bullet-point lists for: workflows, taxonomies, decision trees, role comparisons.
- Add at least one code snippet if the topic is technical (Python/SQL/CLI).
- Add at least one comparison table if the topic involves multiple options, tools, or roles.
- **Visual Framework Transcription:** If the user uploads an image containing a business canvas, matrix, or flowchart (e.g., Startup Canvas, SWOT), transcribe every text block exactly as presented in the image, then map the user's specific project/context directly into those exact transcribed blocks using a table (`| Modul Canvas | Pertanyaan Kunci | Implementasi Proyek |`).
- **Narrative Storytelling for Business Canvases:** When asked to elaborate on business canvas blocks (e.g., Startup Canvas, Lean Canvas), avoid generic or purely bulleted feature lists. Use rich, paragraph-based storytelling from a Product Manager / Business Strategist perspective, integrating rigorous business concepts (*pain point, pricing wall, utilization rate, variable demand, willingness to pay / WTP, mental accounting, loss leader, data moat, unit economics*).
- **Sticky Active Note Continuity:** When working through class notes (e.g., `Pertemuan_1.md`), keep all incoming prompts and breakdowns in the *currently active session note* unless the user explicitly instructs to move to the next file (e.g., `Pertemuan_2.md`).
- For career/karier notes: include salary context, skill roadmap, and portfolio strategy sections.

## Bulk Translation of Course Notes (e.g., Zoomcamp, Coursera)

When translating an entire module folder of English course notes into engaging Indonesian:

1. **Inventory** all `.md` files in the folder with `search_files` (target=files).
2. **Separate original-Indonesian vs English** files — only process English ones.
3. **Batch reads**: Read multiple files in parallel in a single turn using parallel `read_file` calls. Pair files of similar size to avoid timeout.
4. **Delegate large batches** via `delegate_task` — spawn 4–5 subagent workers in parallel, one per file. Each worker: read file → compose Indonesian version → `write_file`.
5. **Verify each file** after delegation: check top 20 lines with `read_file(limit=20)` to confirm the frontmatter and language are correct.
6. **Handle delegation failures**: if a subagent wrote nothing or left English prose, rewrite that file directly in the parent session.

### Course-Note Translation Format
In addition to the standard output format above, translated course notes require:
- `title:` field in YAML (Indonesian title).
- `date_updated: YYYY-MM-DD` added to frontmatter.
- All original frontmatter fields (`video_url`, `prev_url`, `next_url`, `code:`) preserved verbatim.
- Image paths (`images/...`) preserved exactly — never translated.
- Mermaid diagram added for: workflows (flowchart), comparisons (graph LR), multi-step processes.
- `[!QUESTION]-` collapsible self-test blocks at end (minimum 2–3 questions with answers).
- Navigation block at bottom with wikilinks: prev/next note + hub index.

## Pitfalls
- **Escape Mermaid Braces in Python f-strings.** When generating Markdown containing Mermaid diagrams via Python (`execute_code`), Mermaid syntax containing single/double curly braces (e.g., `C{{Decision}}` or `C{Decision}`) will trigger a Python `SyntaxError: f-string: invalid syntax`. Use plain multiline strings with `.replace()`, `.format()`, or properly double-escape the braces.
- **Ground Heuristics in Academic & Scientific Frameworks.** Do not leave self-development or behavioral notes as surface-level motivational platitudes. Synthesize and ground them into formal cognitive/scientific theories (e.g., Kahneman's Dual-Process Theory, Gary Klein's Naturalistic Decision-Making & Premortem Analysis, Ebbinghaus Forgetting Curve, autonomic vagal modulation) to satisfy academic depth standards.
- **Write to disk immediately.** Do not dump finished notes into the chat response alone. Always determine the right folder under `E:\BELAJAR BANGET\SKILL BELAJAR` and write the `.md` file to disk.
- **Full read required before `write_file` overwrite.** If a file was read with pagination (e.g., `limit=20`), `write_file` will refuse to overwrite it to prevent partial-data loss. Always call `read_file` with `limit=2000` (or the full line count) before calling `write_file` (this applies to both the native `write_file` tool and the Python `write_file` helper inside `execute_code`).
- **Preserve asset paths in course notes.** In translated course notes (e.g., Zoomcamp), keep image links (`images/...`), video URLs (`video_url`), and code block inputs verbatim — translate prose and explanations only.
- **Include collapsible self-test questions.** Use `[!QUESTION]- **Soal X: ...**` callout blocks at the end of fundamental concepts for exam/interview prep.
- **Never rely on `execute_code` to re-read files read earlier.** `read_file` returns `content_returned: false` (dedup) when already read in session. Store the content or write directly from memory.
- **Don't append — rewrite.** Appending sections creates disjointed structure. Always overwrite the whole file via `write_file`.
- **Maintain Linear Flow (No Circular Explanations).** When synthesizing multiple theories or papers that explain the same phenomenon, integrate them into a single chronological/logical hierarchy. Do not create repetitive, overlapping sections for each theory (materi tidak boleh "muter-muter").
- **Anchor Edits to Active Context.** If the user introduces a new concept/theory in a follow-up prompt, integrate it into the *currently active file* (e.g., `Pertemuan_1.md`) instead of assuming it belongs in the next sequence (e.g., `Pertemuan_2.md`), unless explicitly told to switch files.
- **Don't fabricate wikilinks.** Run `search_files` to get actual sibling filenames before writing `[[...]]` links. A broken wikilink is worse than no link.
- **Batch independent web searches.** Fire 2–3 searches in one turn (parallel); don't serialize topic → subtopic → examples as separate turns.
- **Keep `date_created` from original.** Only `date_updated` changes to today.
