---
name: splitting-datasets
description: "[omh] Split datasets into training, validation, and test partitions with stratification and anti-leakage rules. Use when the user says: splitting-datasets, split dataset, train test split, dataset partition."
license: MIT
author: "Jeremy Longshore <jeremy@intentsolutions.io>"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, dataset-split, train-test, validation, ml]
    category: data-ai
    phase: dataset-preparation
    role: operator
    quality_tier: evidence-gated
    related_skills: [ml-data-leakage-guard, preprocessing-data-with-automated-pipelines, spesialis-data-ai-agentic]
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
---
# Dataset Splitter

## Positioning

Treat this skill as a narrow helper for partition strategy.

## When to Use

Use this skill when:
- Prepare a dataset for machine learning model training.
- Create training, validation, and testing sets.
- Partition data to evaluate model performance.

## Not For / Boundaries

- Full preprocessing-pipeline ownership: use `preprocessing-data-with-automated-pipelines`
- Leakage audits and prediction-time checks: use `ml-data-leakage-guard`
- Model training and tuning after the split: use `scikit-learn`

## Typical Outputs

- Partition strategy with ratios, random seeds, and stratification rules
- Notes on temporal or grouped split constraints
- Handoff guidance for leakage review and downstream training

## Related Skills

- `preprocessing-data-with-automated-pipelines` for the broader preprocessing sequence
- `ml-data-leakage-guard` to verify the split does not leak future or test information


## Linked References
- `references/README.md`
