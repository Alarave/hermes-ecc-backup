---
name: creating-data-visualizations
description: "[omh] Create analytical charts and plots from existing data: bars, lines, scatters, and dashboards. Use when the user says: creating-data-visualizations, create chart, plot data, data visualization."
license: MIT
author: "Jeremy Longshore <jeremy@intentsolutions.io>"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, data-visualization, charts, analytics]
    category: data-ai
    phase: visualization
    role: operator
    quality_tier: evidence-gated
    related_skills: [datavis, matplotlib, seaborn, spesialis-data-ai-agentic]
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
---
# Data Visualization Creator

Use this skill when the user needs a chart from data that already exists.

## Overview

This skill focuses on everyday analytical visualization choices: bars, lines, scatters, distributions, comparisons, and simple dashboards.

## When to Use This Skill

- Plotting trends, distributions, comparisons, or correlations from structured data
- Turning query output or CSV tables into charts for analysis or slides
- Choosing a sensible chart type and axis treatment for a non-specialist audience

## Not For / Boundaries

- Journal-ready figures, multi-panel publication layouts, TIFF/600dpi exports: use `scientific-visualization`
- Structural diagrams, flowcharts, and mechanism illustrations: use `scientific-schematics` or `markdown-mermaid-writing`
- Full research-report ownership: use `scientific-reporting`

## Integration

- Pair with `exploratory-data-analysis` before plotting questionable data
- Hand off to `scientific-visualization` if the chart must meet publication standards

## Example Requests

- "Plot monthly conversion rate with a confidence band"
- "Make a scatter plot of latency vs throughput"
- "Turn this CSV summary into a small dashboard"


## Linked References
- `references/README.md`
