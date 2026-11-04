---
name: crisp-dm-dgx-notebook
description: "Standard CRISP-DM framework for structuring and refactoring data science and ML Jupyter notebooks."
---

# CRISP-DM DGX Notebook Standard

## When to use this skill
Whenever the user asks you to create, refactor, or structure a Jupyter Notebook (`.ipynb`) for Data Science or Machine Learning tasks.

## Rules & Standards
1. **CRISP-DM Phases**: The notebook must have clear Markdown headers for:
   - Business Understanding
   - Data Understanding
   - Data Preparation
   - Modelling
   - Evaluation Model
   - Deployment
2. **Super Atomic Cells**: EVERY single action must be in its own isolated cell. NEVER bundle multiple tasks.
   - 1 cell for library imports.
   - 1 cell for dynamic base dir detection (`resolve_base_dir()`).
   - 1 cell for loading data (`read_csv`).
   - 1 cell for `df.head()`.
   - 1 cell for `df.shape`.
   - 1 cell for `df.info()`.
   - 1 cell for `df.describe()`.
   - 1 cell for dropping or renaming columns.
   - 1 cell for checking duplicates.
   - 1 cell for checking nulls.
   - 1 cell per plot (e.g., one cell for histogram, another cell for boxplot, another for heatmap).
   - 1 cell for outlier handling.
   - 1 cell for train/test split.
   - 1 cell for scaling (StandardScaler/MinMaxScaler).
   - 1 cell for model initialization and fitting.
   - 1 cell for prediction (`y_pred`).
   - 1 cell for metrics calculation (MAE, MSE, RMSE, R2, CER, WER, McNemar).
   - 1 cell for evaluation plot (Actual vs Predicted / Confusion Matrix).
   - 1 cell for deployment dump (e.g., `joblib.dump` or structured JSON).
3. **Markdown Commentary (Tripartite Pattern)**:
   - Pre-code Markdown: States the theoretical rationale and specific objective of the step.
   - Code Cell: Clean, focused execution.
   - Post-code Markdown: Interprets the numerical facts and empirical findings (never just restating the code).
4. **Zero-Slop Key-Value Logging Format**:
   - Standard output pattern: `print(f"[{Category}] {Key}: {Value} | {Key}: {Value}")`.
   - Prohibited: decorative line banners (`print("="*80)`), decorative emojis (`🚀`, `✨`, `🎉`, `🔥`, `🤖`, `✅`), and chatty robotic filler phrases. Maximum allowed divider: one single ASCII line `print("-" * 50)`.
   - Loop hygiene: NEVER print per row inside loops over hundreds/thousands of samples; use `tqdm` or periodic interval logging (`if idx % 500 == 0:`).
5. **Ponytail Pattern for Deliberate Simplifications**:
   - If an intentional shortcut or device fallback is applied, mark it with `# ponytail: [current boundary], upgrade when [future condition]`.
6. **Dynamic Path Resolution**:
   - Never hardcode absolute host paths (`E:\...`, `/content/...`). Use an upward-traversal `resolve_base_dir()` helper function.
