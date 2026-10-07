---
name: ai-job-search
description: Use when searching for AI/tech jobs, tailoring resumes and cover letters for AI engineering or data science roles, analyzing job descriptions, preparing for AI technical interviews, or managing job application pipelines.
---

# AI Job Search & Career Assistant

## Overview

A comprehensive workflow skill designed to assist AI Engineers, Machine Learning Engineers, Data Scientists, and Software Engineers in searching for jobs, analyzing job postings, tailoring resumes/CVs, drafting targeted cover letters, preparing for AI system design & coding interviews, and tracking job applications.

## When to Activate

- Searching for job openings in AI, ML, Data Science, and Software Engineering.
- Analyzing job descriptions (JD) to extract required tech stacks, core responsibilities, and ATS keywords.
- Tailoring resumes/CVs for specific job applications with metric-driven accomplishments.
- Drafting personalized cover letters aligned with company mission and role requirements.
- Preparing for AI technical interviews (System Design, LLM/RAG architecture, ML theory, coding challenges).
- User mentions "job search", "AI jobs", "apply jobs", "tailor resume", "CV review", or "interview prep".

## Core Workflows

### 1. Job Description Analysis (`/ai-job-search analyze`)

Extract structured information from a job posting URL or text:
- **Required Hard Skills**: Frameworks (PyTorch, TensorFlow, LangChain, LlamaIndex), Languages (Python, C++, SQL), Infrastructure (Docker, Kubernetes, AWS/GCP, CUDA).
- **Core Responsibilities**: Fine-tuning, RAG pipelines, agentic workflows, model deployment, API development.
- **ATS Keywords**: Key terms to include in resume for Applicant Tracking Systems.
- **Role Seniority & Expectations**: Junior, Mid, Senior, Staff, Lead evaluation.

### 2. Resume & Portfolio Tailoring (`/ai-job-search resume`)

Adapt an existing resume to match the target job description:
- Highlight relevant AI/ML projects (e.g., fine-tuning LLMs, RAG, multi-agent frameworks, latency optimization).
- Quantify achievements using the STAR method (Situation, Task, Action, Result).
- Ensure 80%+ keyword overlap with target ATS expectations.
- Format cleanly in Markdown or LaTeX format.

### 3. Cover Letter Drafting (`/ai-job-search cover-letter`)

Create a compelling, professional cover letter:
- Hook statement connecting applicant's background to company's mission.
- Concrete examples of relevant AI projects and measurable business impact.
- Clear call-to-action for an interview.

### 4. Technical & AI Interview Prep (`/ai-job-search interview`)

Generate customized practice materials based on target role:
- **AI System Design**: RAG system design, LLM fine-tuning vs prompt engineering, agentic loop architectures, vector DB scaling.
- **ML/DL Theory**: Transformers, attention mechanisms, loss functions, optimization algorithms, quantization (GGUF, AWQ, FP8).
- **Coding & Algorithms**: Data structures, Python async patterns, PyTorch tensor manipulation.
- **Behavioral Questions**: Handling model failures, technical trade-offs, cross-functional collaboration.

### 5. Application Pipeline Management (`/ai-job-search track`)

Maintain an application tracking log (`data/job-applications.md` or `.json`):
- Date applied, Company name, Role title, Application status (Applied, Interviewing, Offer, Rejected), Follow-up reminders.

## Best Practices

- **Impact over Buzzwords**: Focus on actual metrics (e.g., "Reduced LLM inference latency by 45% using vLLM and TensorRT-LLM").
- **ATS Alignment**: Match exact terminology used in the job description without keyword stuffing.
- **Honesty & Quality**: Maintain accuracy in technical claims to ensure strong performance during technical deep-dives.
