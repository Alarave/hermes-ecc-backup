---
name: mlops-zoomcamp-scaffold
description: "MLOps Zoomcamp pipeline builder, orchestration, experiment tracking, and deployment scaffold."
---

# MLOps Zoomcamp Pipeline Builder

## When to use this skill
Whenever the user asks to productionize a machine learning model, transition from a notebook to scripts, or build an MLOps pipeline.

## Rules & Standards
1. **Pipeline Architecture**: Implement tracking, orchestration, and serving.
   - Experiment Tracking: `MLflow` (Backend and Artifact store).
   - Orchestration: `Prefect` or `Mage` for DAGs (Data Ingestion, Preparation, Training, Registration).
   - Deployment: `FastAPI` / `Flask` inside a Docker container, or Serverless (AWS Lambda).
   - Monitoring: `Evidently AI` for Data Drift and Concept Drift.
2. **Code Structure**:
   - `data/`
   - `models/`
   - `scripts/` or `orchestration/` (for modularized python scripts)
   - `tests/` (unit testing with Pytest)
   - `Dockerfile`, `requirements.txt` or `Pipfile`/`pyproject.toml`
   - `Makefile` for CI/CD commands.
3. **Best Practices**:
   - Enforce reproducible environments.
   - Isolate configs via environment variables.
   - Provide pre-commit hooks (Black, flake8, isort).
