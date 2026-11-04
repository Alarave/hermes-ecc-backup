---
name: evaluating-machine-learning-models
description: "[omh] Evaluate trained machine learning models with the right metrics, validation, and comparison logic. Use when the user says: evaluating-machine-learning-models, evaluate model, model metrics, model evaluation."
license: MIT
author: "Jeremy Longshore <jeremy@intentsolutions.io>"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, model-evaluation, metrics, validation, ml]
    category: data-ai
    phase: model-evaluation
    role: reviewer
    quality_tier: evidence-gated
    related_skills: [explaining-machine-learning-models, scikit-learn, spesialis-data-ai-agentic]
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
---
# Model Evaluation Suite

Use this skill when the model exists and the question is whether it is good enough.

## Overview

This skill focuses on choosing and interpreting the right evaluation metrics for the problem, then comparing candidate models or thresholds.

## When to Use This Skill

- Comparing candidate models with consistent metrics
- Reviewing precision/recall/F1/AUC, regression error, calibration, or ranking quality
- Stress-testing validation strategy before deployment or publication

## Not For / Boundaries

- Building the training pipeline itself: use `scikit-learn` for classical modeling or `ml-pipeline-workflow` for end-to-end workflow ownership
- Engineering features: use `preprocessing-data-with-automated-pipelines`
- Checking train/test contamination: use `ml-data-leakage-guard`

## Typical Outputs

- Metric suite recommendations
- Model comparison tables
- Notes on threshold tradeoffs, calibration, and validation weaknesses

## Related Skills

- `scikit-learn` for class-level error breakdowns and confusion matrices
- `scientific-reporting` when the evaluation must become a deliverable


## Linked References
- `references/README.md`
