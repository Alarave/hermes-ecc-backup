#!/usr/bin/env python3
# Daily Learning Curator script for Firman
# Fetches 3 fresh internet resources across his learning domains and writes a markdown summary.

from hermes_tools import web_search, write_file
import datetime, random, os, json

# Domains and sample queries (adjust dates for recency)
domains = [
    ("Machine Learning & Deep Learning", "latest advancements in time-series forecasting 2024"),
    ("Data Science", "new data visualization techniques 2024"),
    ("MCP & Agentic AI Systems", "model context protocol updates 2024"),
    ("System Analyst & Software Engineering", "microservices design patterns 2024"),
    ("Project Management", "agile project management trends 2024"),
    ("Personal Development", "decision making frameworks 2024"),
]

# Pick 3 distinct domains for today (rotate randomly)
random.seed(datetime.date.today().toordinal())
selected = random.sample(domains, 3)

lines = ["Selamat pagi Firman! Materi hari ini:\n"]
for idx, (domain, query) in enumerate(selected, 1):
    # Search the web, ask for 3 results but take the first fresh one
    result = web_search(query=query, limit=3)
    # Fallback if no results
    if not result.get('data') or not result['data'].get('web'):
        continue
    entry = result['data']['web'][0]
    title = entry.get('title', 'Untitled')
    url = entry.get('url', '')
    # Simple relevance note
    why = f"Relevan dengan bidang {domain.lower()}, memberikan insight terbaru."
    # Prepare three bullet points (placeholder, real extraction would need more processing)
    points = ["Poin utama 1", "Poin utama 2", "Poin utama 3"]
    micro = "Lakukan pencarian singkat di Google dengan judul artikel dan catat satu insight yang paling menarik (≤5 menit)."
    lines.append(f"{idx}. {title}\nLink: {url}\nKenapa penting: {why}\nPoin utama:\n  - {points[0]}\n  - {points[1]}\n  - {points[2]}\nMicro-action: {micro}\n---\n")

# Write to markdown file in the learning folder, date-stamped
out_path = os.path.abspath(r"E:\BELAJAR BANGET\SKILL BELAJAR\daily_learning_" + datetime.date.today().isoformat() + ".md")
write_file(path=out_path, content="\n".join(lines))
print(f"Wrote daily learning summary to {out_path}")
