import os
import sys
import time
import shutil
from pathlib import Path

# Auto-detect root directory based on script location
BASE_DIR = Path(__file__).resolve().parent
HERMES_DIR = BASE_DIR / "skills"
GEMINI_DIR = Path.home() / ".gemini" / "config" / "rules"
CONFIG_SKILLS_DIR = Path.home() / ".gemini" / "config" / "skills"
IDE_SKILLS_DIR = Path.home() / ".gemini" / "antigravity-ide" / "skills"
CLI_SKILLS_DIR = Path.home() / ".gemini" / "antigravity-cli" / "skills"

def ensure_dirs():
    HERMES_DIR.mkdir(parents=True, exist_ok=True)
    GEMINI_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    IDE_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    if not CLI_SKILLS_DIR.exists():
        try:
            import subprocess
            subprocess.run(["cmd", "/c", "mklink", "/J", str(CLI_SKILLS_DIR), str(HERMES_DIR)], capture_output=True)
        except Exception:
            pass

def has_frontmatter(content):
    return content.startswith("---")

def strip_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip()
    return content

import re

def extract_description(name, content):
    content_clean = content.replace("\u2014", "-").replace("\u2013", "-")
    match = re.search(r"-\s*\*\*Keahlian\*\*\s*:\s*(.+)", content_clean, re.IGNORECASE)
    if match:
        desc = match.group(1).strip()
        desc = re.sub(r'[*_`]', '', desc)
        if len(desc) > 150:
            desc = desc[:147] + "..."
        return f"Gunakan untuk: {desc}"
    
    match = re.search(r"-\s*\*\*Fokus Kerja\*\*\s*:\s*(.+)", content_clean, re.IGNORECASE)
    if match:
        desc = match.group(1).strip()
        desc = re.sub(r'[*_`]', '', desc)
        if len(desc) > 150:
            desc = desc[:147] + "..."
        return f"Gunakan untuk: {desc}"

    # Check for command or purpose in header
    cmd_match = re.search(r"^#+\s+(/[a-zA-Z0-9_-]+[^\n]*)", content_clean, re.MULTILINE)
    if cmd_match:
        desc = re.sub(r'[*_`#]', '', cmd_match.group(1)).strip()
        if len(desc) > 150:
            desc = desc[:147] + "..."
        return f"Gunakan saat menjalankan {desc}"

    # Check first substantive heading
    title_match = re.search(r"^#+\s+([^#\n]+)", content_clean, re.MULTILINE)
    if title_match:
        desc = re.sub(r'[*_`#]', '', title_match.group(1)).strip()
        if desc and not desc.lower().startswith("preamble"):
            if len(desc) > 140:
                desc = desc[:137] + "..."
            return f"Gunakan untuk: {desc}"

    return f"Gunakan untuk panduan dan kapabilitas {name.replace('-', ' ')}"

def generate_frontmatter(name, content):
    if has_frontmatter(content):
        content = strip_frontmatter(content)
    desc = extract_description(name, content).replace('"', "'")
    return f"---\nname: {name}\ndescription: \"{desc}\"\n---\n\n{content}"

def update_hermes_content(existing_hermes_path, new_body, name):
    if existing_hermes_path.exists():
        existing = existing_hermes_path.read_text(encoding="utf-8")
        if existing.startswith("---"):
            parts = existing.split("---", 2)
            if len(parts) >= 3:
                return f"---{parts[1]}---\n\n{new_body.lstrip()}"
    return generate_frontmatter(name, new_body)

def sync():
    ensure_dirs()
    
    # Track which skills we processed to handle deletions or one-way creations
    hermes_skills = {d.name: d for d in HERMES_DIR.iterdir() if d.is_dir() and not d.name.startswith(".")}
    gemini_skills = {f.stem: f for f in GEMINI_DIR.glob("*.md")}
    
    all_names = set(hermes_skills.keys()) | set(gemini_skills.keys())
    
    for name in all_names:
        # Ignore skills with special names or symlinks if needed
        hermes_file = HERMES_DIR / name / "SKILL.md"
        gemini_file = GEMINI_DIR / f"{name}.md"
        
        h_exists = hermes_file.exists()
        g_exists = gemini_file.exists()
        
        if h_exists and g_exists:
            h_mtime = hermes_file.stat().st_mtime
            g_mtime = gemini_file.stat().st_mtime
            
            if abs(h_mtime - g_mtime) < 2:
                continue  # In sync
                
            if h_mtime > g_mtime:
                # Hermes is newer, update Gemini
                content = hermes_file.read_text(encoding="utf-8")
                gemini_content = strip_frontmatter(content)
                gemini_file.write_text(gemini_content, encoding="utf-8")
                # match mtimes
                os.utime(gemini_file, (h_mtime, h_mtime))
            else:
                # Gemini is newer, update Hermes while preserving frontmatter
                content = gemini_file.read_text(encoding="utf-8")
                hermes_content = update_hermes_content(hermes_file, content, name)
                hermes_file.write_text(hermes_content, encoding="utf-8")
                os.utime(hermes_file, (g_mtime, g_mtime))
                
        elif h_exists and not g_exists:
            # Create in Gemini
            content = hermes_file.read_text(encoding="utf-8")
            gemini_content = strip_frontmatter(content)
            gemini_file.write_text(gemini_content, encoding="utf-8")
            h_mtime = hermes_file.stat().st_mtime
            os.utime(gemini_file, (h_mtime, h_mtime))
            
        elif g_exists and not h_exists:
            # Create in Hermes
            hermes_dir = HERMES_DIR / name
            hermes_dir.mkdir(parents=True, exist_ok=True)
            content = gemini_file.read_text(encoding="utf-8")
            hermes_content = generate_frontmatter(name, content)
            hermes_file.write_text(hermes_content, encoding="utf-8")
            g_mtime = gemini_file.stat().st_mtime
            os.utime(hermes_file, (g_mtime, g_mtime))

    # Synchronize skills to Antigravity config/skills and antigravity-ide/skills
    for skill_dir in HERMES_DIR.iterdir():
        if skill_dir.is_dir() and not skill_dir.name.startswith(".") and (skill_dir / "SKILL.md").exists():
            for dest_root in (CONFIG_SKILLS_DIR, IDE_SKILLS_DIR):
                dest_dir = dest_root / skill_dir.name
                if not dest_dir.exists():
                    try:
                        shutil.copytree(skill_dir, dest_dir, dirs_exist_ok=True)
                    except Exception:
                        pass

if __name__ == "__main__":
    sync()
