---
name: detecting-data-anomalies
description: "[omh] Investigate outliers, rare events, spikes, and suspicious records in datasets. Use when the user says: detecting-data-anomalies, detect anomalies, find outliers, anomaly detection data."
license: MIT
author: "Jeremy Longshore <jeremy@intentsolutions.io>"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, data-anomalies, outliers, data-quality]
    category: data-ai
    phase: anomaly-detection
    role: reviewer
    quality_tier: evidence-gated
    related_skills: [scikit-learn, exploratory-data-analysis, spesialis-data-ai-agentic]
allowed-tools: Read, Bash(python:*), Grep, Glob
version: 1.0.0
---

# Detecting Data Anomalies

## Positioning

Treat this skill as an explicit/manual helper.
In governed ML routing, anomaly-detection ownership normally belongs to `scikit-learn`.

## When to Use

Use this skill when:
- Reviewing outlier transactions, fraud candidates, sensor spikes, or rare failures
- Comparing isolation forest, one-class SVM, LOF, or threshold-based anomaly workflows
- Turning suspicious records into a shortlist for human inspection

## Not For / Boundaries

- Null/duplicate/schema/range validation: use `exploratory-data-analysis`
- Full model training or end-to-end pipeline ownership: use `scikit-learn` or `ml-pipeline-workflow`
- Publication-grade figure production: use `scientific-visualization`

## Typical Outputs

- Candidate anomaly-detection methods and thresholds
- A review checklist for false positives and false negatives
- Suggested tables or plots for the suspicious subset

## Related Skills

- `scikit-learn` as the governed routed owner for classical anomaly-detection workflows
- `creating-data-visualizations` after anomalies are identified


## Linked References
- `references/README.md`
- `references/errors.md`
- `references/examples.md`
- `references/implementation.md`
