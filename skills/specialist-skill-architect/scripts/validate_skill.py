import sys
import io
from pathlib import Path
import re
import argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def validate_skill(skill_dir: Path, strict: bool = False):
    skill_file = skill_dir / "SKILL.md"
    errors = []
    warnings = []

    if not skill_file.exists():
        print(f"[FAIL] SKILL.md not found in {skill_dir}")
        return False

    content = skill_file.read_text(encoding="utf-8", errors="ignore")

    # 1. Frontmatter check
    if not content.startswith("---"):
        errors.append("SKILL.md must start with YAML frontmatter (---).")
    else:
        parts = content.split("---", 2)
        if len(parts) < 3:
            errors.append("Invalid YAML frontmatter: missing closing ---.")
        else:
            fm = parts[1]
            # name
            name_m = re.search(r"^name:\s*([a-zA-Z0-9_-]+)", fm, re.MULTILINE)
            if not name_m:
                errors.append("Missing or invalid 'name' in frontmatter.")
            else:
                skill_name = name_m.group(1)
                if skill_name != skill_dir.name and not strict:
                    warnings.append(f"Frontmatter name '{skill_name}' does not match directory name '{skill_dir.name}'.")

            # description
            desc_m = re.search(r'^description:\s*"([^"\r\n]+)"', fm, re.MULTILINE)
            if not desc_m:
                desc_m = re.search(r"^description:\s*'([^'\r\n]+)'", fm, re.MULTILINE)
            if not desc_m:
                desc_m = re.search(r"^description:\s*([^\r\n]+)", fm, re.MULTILINE)

            if not desc_m:
                errors.append("Missing 'description' in frontmatter.")
            else:
                desc = desc_m.group(1).strip()
                if "Aturan Gemini" in desc:
                    errors.append("Description contains generic fallback 'Aturan Gemini'.")
                if len(desc) < 20:
                    warnings.append(f"Description is very short ({len(desc)} chars).")

    # 2. Typography check (No em-dash or en-dash)
    if "\u2014" in content:
        errors.append("Found em-dash (—) in file. Use standard hyphens (-) per specification.")
    if "\u2013" in content:
        errors.append("Found en-dash (–) in file. Use standard hyphens (-) per specification.")

    # 3. Check linked references existence
    refs_matches = re.findall(r"-\s*[`'\"]?([^`'\"\r\n]+\.md)[`'\"]?", content)
    for ref in refs_matches:
        if ref.startswith("skills/"):
            rel = ref[len("skills/"):]
            ref_path = skill_dir.parent / rel
            if not ref_path.exists():
                warnings.append(f"Linked reference file not found on disk: {ref}")
        elif ref.startswith("references/"):
            ref_path = skill_dir / ref
            if not ref_path.exists():
                warnings.append(f"Linked reference file not found on disk: {ref}")

    # 4. Strict checks (RCCO sections)
    if strict:
        if not re.search(r"^#+\s+.*(Role|R\b)", content, re.MULTILINE | re.IGNORECASE):
            warnings.append("Strict: Missing Role (R) section.")
        if not re.search(r"^#+\s+.*(Context|When to Use|C\b)", content, re.MULTILINE | re.IGNORECASE):
            warnings.append("Strict: Missing Context (C) or When to Use section.")
        if not re.search(r"^#+\s+.*(Constraints|Boundaries|C\b)", content, re.MULTILINE | re.IGNORECASE):
            warnings.append("Strict: Missing Constraints (C) or Boundaries section.")
        if not re.search(r"^#+\s+.*(Output|O\b)", content, re.MULTILINE | re.IGNORECASE):
            warnings.append("Strict: Missing Output Format (O) section.")

    # Output report
    if errors:
        print(f"[FAIL] {skill_dir.name}: {len(errors)} error(s), {len(warnings)} warning(s)")
        for err in errors:
            print(f"  ERROR: {err}")
        for w in warnings:
            print(f"  WARN:  {w}")
        return False
    elif warnings:
        print(f"[PASS with WARNINGS] {skill_dir.name}: {len(warnings)} warning(s)")
        for w in warnings:
            print(f"  WARN:  {w}")
        return True
    else:
        print(f"[PASS 100/100] {skill_dir.name}: All checks passed cleanly.")
        return True

def main():
    parser = argparse.ArgumentParser(description="Validate skill structure and compliance.")
    parser.add_argument("skill_dir", type=str, help="Path to skill directory")
    parser.add_argument("--strict", action="store_true", help="Enforce strict RCCO layout checks")
    args = parser.parse_args()

    target = Path(args.skill_dir).resolve()
    success = validate_skill(target, strict=args.strict)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
