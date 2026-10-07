import os
import time
import shutil
from pathlib import Path

HERMES_DIR = Path(r"C:\Users\HP\AppData\Local\hermes\skills")
GEMINI_DIR = Path(r"C:\Users\HP\.gemini\config\rules")

def ensure_dirs():
    HERMES_DIR.mkdir(parents=True, exist_ok=True)
    GEMINI_DIR.mkdir(parents=True, exist_ok=True)

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
    match = re.search(r"-\s*\*\*Keahlian\*\*\s*:\s*(.+)", content, re.IGNORECASE)
    if match:
        desc = match.group(1).strip()
        desc = re.sub(r'[*_`]', '', desc)
        if len(desc) > 150:
            desc = desc[:147] + "..."
        return f"Gunakan untuk: {desc}"
    
    match = re.search(r"-\s*\*\*Fokus Kerja\*\*\s*:\s*(.+)", content, re.IGNORECASE)
    if match:
        desc = match.group(1).strip()
        desc = re.sub(r'[*_`]', '', desc)
        if len(desc) > 150:
            desc = desc[:147] + "..."
        return f"Gunakan untuk: {desc}"

    return f"Aturan Gemini {name}"

def generate_frontmatter(name, content):
    if has_frontmatter(content):
        content = strip_frontmatter(content)
    desc = extract_description(name, content).replace('"', "'")
    return f"---\nname: {name}\ndescription: \"{desc}\"\n---\n\n{content}"

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
                # Antigravity CLI does not mind frontmatter, but let's just keep it simple and pass exactly what Hermes has
                # Actually, wait. Stripping frontmatter for Gemini is cleaner.
                gemini_content = strip_frontmatter(content)
                gemini_file.write_text(gemini_content, encoding="utf-8")
                # match mtimes
                os.utime(gemini_file, (h_mtime, h_mtime))
            else:
                # Gemini is newer, update Hermes
                content = gemini_file.read_text(encoding="utf-8")
                hermes_content = generate_frontmatter(name, content)
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

if __name__ == "__main__":
    sync()
