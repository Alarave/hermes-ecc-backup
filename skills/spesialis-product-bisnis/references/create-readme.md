# Create README Skill

## Role

Senior AI / Data Science Documentation Engineer. You write comprehensive, production-grade, and publication-quality `README.md` files for Machine Learning and Data Science projects.

## Task

When generating or updating `README.md` for a machine learning / data science project:
1. Review the repository, notebooks, datasets, models, metrics, and scripts.
2. Adapt the project specifics into the standardized 20-section structure below.
3. Keep the section numbers, titles, and flow consistent.
4. Replace all placeholder figures, metrics, and table values with actual project artifacts and findings.

---

## Standard 20-Section README Structure

```markdown
# [Project Name] & [Domain / Value Analysis]

### [Subtitle: Problem Statement & ML Approach]

## 1. Deskripsi Project
[Background, problem context, ML task type (Regression/Classification/Clustering), and overall pipeline scope: data understanding -> validation -> cleaning -> EDA -> feature engineering -> modeling -> evaluation -> insights].

---

## 2. Business Problem
[Core business problem statement and key research / business questions to answer].

---

## 3. Project Objective
### Tujuan Utama
[Primary objective].

### Tujuan Tambahan
[Specific technical and analytical milestones].

---

## 4. Dataset
[Dataset source, scope, initial row/column count, cleaned row/column count, nulls, duplicates, and target variable].

---

## 5. Data Validation & Cleaning
[Validation rules executed, handling missing values, anomalies, outliers, and summary checklist of final validation state].

### Hasil Final Validation
- Dataset shape: [rows x cols]
- Missing values: 0
- Duplicate rows: 0
- [Domain specific constraint checks]: 0

---

## 6. Exploratory Data Analysis
[EDA scope: distributions, correlations, segmentations, and top correlated features with target].

### Korelasi dengan Target
| Feature | Correlation |
|---|---:|
| ... | ... |

---

## 7. Feature Engineering & Feature Selection
[Breakdown of input features used in modeling].

### Numerical Features
- ...

### Categorical Features
- ...

### Target Variable
`[target_column]`

---

## 8. Train-Test Split
[Split ratios, stratifications, and row counts].

| Dataset | Rows | Percentage |
|---|---:|---:|
| Training | ... | ...% |
| Testing | ... | ...% |
| Total | ... | 100% |

---

## 9. Data Preprocessing
[Encoders, scalers, imputers applied, and dimensionality before/after preprocessing].

---

## 10. Machine Learning Models
[List and rationale for baseline and candidate algorithms compared].

### 1. [Baseline Model]
### 2. [Candidate Model 1]
### 3. [Candidate Model 2 / Final Model]

---

## 11. Model Evaluation
[Evaluation metrics used: MAE, MSE, RMSE, R² for regression or Accuracy, Precision, Recall, F1, ROC-AUC for classification].

### Model Comparison
| Model | [Metric 1] | [Metric 2] | [Metric 3] | [Metric 4] |
|---|---:|---:|---:|---:|
| ... | ... | ... | ... | ... |

### Model yang Dipilih
[Selected model name, rationale, best metric, limitations, and operational caveats].

---

## 12. Feature Importance
[Top contributing features from tree-based models or SHAP / permutation importance].

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | ... | ... |

---

## 13. Prediction Output
[Sample actual vs predicted comparisons and filename of the predictions export].

| Actual | Predicted |
|---:|---:|
| ... | ... |

---

## 14. Business Insights
[Numbered key actionable insights derived from EDA and model behavior].

---

## 15. Business Recommendations
[Categorized strategic recommendations: Pricing / Valuation / Operations / Decision Support].

---

## 16. Visualizations
[List of key generated plots stored in repo].
1. ...
2. ...

---

## 17. Final Project Outputs
### Processed Dataset
`[path/to/processed_data.csv]`

### Prediction Output
`[path/to/predictions.csv]`

### Final Model
`[path/to/model.pkl]`

---

## 18. Project Structure
```text
[project-root]/
├── data/
│   ├── raw/
│   └── processed/
├── images/
├── models/
├── notebooks/
├── .gitignore
├── requirements.txt
└── README.md
```

## 19. Tools
[List of programming languages, libraries, environments, and platforms used].

## 20. Kesimpulan
[Concise summary of pipeline execution, best model results, known limitations, and practical usage].
```
