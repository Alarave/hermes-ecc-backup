---
name: document-extraction-workflow
description: "Use when reading scanned PDFs. Runs markitdown OCR."
---

# Rule: document-extraction-workflow

## Role / Identity
- **Role**: Data Extraction Specialist

## Context & Constraints
- Use this workflow when `read_file` fails with `NeedsOcrError` or when dealing with image-only PDFs.

## Workflow
1. **Extraction**: Use the `markitdown` CLI to extract text.
   - Command: `markitdown "path/to/file.pdf" > "path/to/scratch/out.md"`
2. **Read**: Use `read_file` to read the extracted markdown file.
3. **Pitfalls**: 
   - Avoid manual scripts with `pypdf`/`fitz`. Missing system packages cause issues. `markitdown` has OCR pre-configured via `markitdown-ocr`.
