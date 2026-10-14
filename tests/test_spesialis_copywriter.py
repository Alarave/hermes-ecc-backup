#!/usr/bin/env python3
"""
tests/test_spesialis_copywriter.py
Automated verification test for the newly created spesialis-copywriter skill.
"""

import sys
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SKILL_DIR = BASE_DIR / "skills" / "spesialis-copywriter"
SKILL_MD = SKILL_DIR / "SKILL.md"

def test_linter_audit():
    """Verify that audit_incoming_skills.py scores 100/100."""
    import importlib.util
    audit_script = BASE_DIR / "scripts" / "audit_incoming_skills.py"
    spec = importlib.util.spec_from_file_location("audit_incoming_skills", str(audit_script))
    assert spec is not None and spec.loader is not None
    audit_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit_module)

    verdict = audit_module.audit_skill_file(SKILL_MD)
    print(f"Linter Score: {verdict['score']}/100")
    if verdict["errors"]:
        print("Errors:", verdict["errors"])
    if verdict["warnings"]:
        print("Warnings:", verdict["warnings"])
    assert verdict["passed"] is True, "Audit failed"
    assert verdict["score"] == 100, f"Expected score 100, got {verdict['score']}"
    print("Test Linter Audit: PASS")

def test_no_em_or_en_dashes():
    """Verify zero em-dash (—) or en-dash (–) in all files under the skill directory."""
    em_dash = "\u2014"
    en_dash = "\u2013"
    
    files = list(SKILL_DIR.glob("**/*.md"))
    for f in files:
        text = f.read_text(encoding="utf-8")
        assert em_dash not in text, f"Em-dash found in {f}"
        assert en_dash not in text, f"En-dash found in {f}"
    print(f"Test Zero Em/En Dashes across {len(files)} files: PASS")

def test_linked_references_exist():
    """Verify all linked references physically exist."""
    content = SKILL_MD.read_text(encoding="utf-8")
    matches = re.findall(r"- `references/([a-zA-Z0-9_\-\.]+)\.md`", content)
    assert len(matches) >= 5, f"Expected at least 5 references, found {len(matches)}"
    for ref in matches:
        ref_path = SKILL_DIR / "references" / f"{ref}.md"
        assert ref_path.is_file(), f"Missing linked reference: {ref_path}"
    print(f"Test Linked References ({len(matches)} files): PASS")

def test_pram_integration():
    """Verify integration into skills/pram/SKILL.md and skills/spesialis/SKILL.md."""
    pram_md = BASE_DIR / "skills" / "pram" / "SKILL.md"
    assert pram_md.is_file()
    pram_text = pram_md.read_text(encoding="utf-8")
    assert "/spesialis-copywriter" in pram_text, "Missing /spesialis-copywriter in pram/SKILL.md"

    spesialis_router = BASE_DIR / "skills" / "spesialis" / "SKILL.md"
    assert spesialis_router.is_file()
    router_text = spesialis_router.read_text(encoding="utf-8")
    assert "/spesialis-copywriter" in router_text, "Missing /spesialis-copywriter in spesialis/SKILL.md"
    print("Test Pram & Router Integration: PASS")

if __name__ == "__main__":
    test_linter_audit()
    test_no_em_or_en_dashes()
    test_linked_references_exist()
    test_pram_integration()
    print("\nALL VERIFICATION CHECKS PASSED (100% OK)")
