---
name: explaining-machine-learning-models
description: "[omh] Explain trained machine learning models through feature attribution, SHAP/LIME, and behavior summaries. Use when the user says: explaining-machine-learning-models, explain model, model interpretability, feature attribution."
license: MIT
author: "Jeremy Longshore <jeremy@intentsolutions.io>"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, model-explainability, shap, interpretability, ml]
    category: data-ai
    phase: model-explainability
    role: reviewer
    quality_tier: evidence-gated
    related_skills: [shap, evaluating-machine-learning-models, spesialis-data-ai-agentic]
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
---
# Model Explainability Tool

## Positioning

Treat this skill as an explicit/manual helper for interpretability work.

## When to Use

Use this skill when:
- Understand why a machine learning model made a specific prediction.
- Identify the most important features influencing a model's output.
- Debug model performance issues by identifying unexpected feature interactions.
- Communicate model insights to non-technical stakeholders.
- Ensure fairness and transparency in model predictions.

## Not For / Boundaries

- Model training and hyperparameter search: use `scikit-learn`
- Benchmark comparison and threshold selection: use `evaluating-machine-learning-models`
- Leakage or prediction-time audits: use `ml-data-leakage-guard`

## Typical Outputs

- Feature importance or attribution summaries
- Local explanation workflow for a concrete prediction
- Notes on caveats, instability, or misleading explanations

## Related Skills

- `shap` for SHAP-specific workflows
- `evaluating-machine-learning-models` when the question is whether the model is good enough


## Linked References
- `references/README.md`
