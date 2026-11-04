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
   - 1 cell for metrics calculation (MAE, MSE, RMSE, R2).
   - 1 cell for evaluation plot (Actual vs Predicted).
   - 1 cell for deployment dump (e.g., `joblib.dump`).
3. **Markdown Commentary**: Every step MUST be preceded or followed by a Markdown cell explaining what the code does or interpreting the results.
