# Universal Capability & Skill Registry for Pram Orchestrator

> Peta navigasi hierarkis 720+ kapabilitas lokal Hermes untuk orkestrasi presisi.
> Pram membaca peta ini untuk menentukan rute spesialis dan skill atomik yang tepat.

## 1. Aturan Two-Stage Dynamic Routing
1. **Tahap 1 (Domain Filtering)**: Cocokkan masalah pengguna dengan salah satu dari 10 Domain Kapabilitas.
2. **Tahap 2 (Atomic Retrieval)**: Panggil spesialis PIC atau skill atomik spesifik via `skill_view("<nama-skill>")`.
3. **Zero Duplication**: Jangan muat semua skill sekaligus; panggil maksimal 1-3 skill per sub-task.

---
## 2. Taksonomi 10 Domain Kapabilitas Utama

### Domain: Software Engineering & Architecture (332 Skills)
- **Lead PIC Spesialis**: `spesialis-backend / spesialis-frontend`
- **Daftar Lengkap Skill**:
  - `academic-researcher`, `accessibility`, `adaptyv`, `agency-grade-ui`, `agent-architecture-audit`, `agent-harness-construction`, `agent-merge-conflict-arbiter`, `agent-sort`
  - `agentic-os`, `ai-regression-testing`, `android-clean-architecture`, `angular-developer`, `anti-ui-slop`, `api-connector-builder`, `api-design`, `architecture-decision-records`
  - `architecture-design`, `architecture-patterns`, `article-writing`, `astropy`, `autonomous-agent-harness`, `autonomous-builder`, `autonomous-loops`, `backend-patterns`
  - `benchmark`, `bio-database-evidence`, `biopython`, `brainstorming`, `brand-voice`, `browser-agent`, `browser-qa`, `bun-runtime`
  - `campus-repository-scraper`, `chembl-database`, `cisco-ios-patterns`, `ck`, `claude-template-importer`, `clickhouse-io`, `clinicaltrials-database`, `clinpgx-database`
  - `code-reviewer`, `codebase-graph-audit`, `codebase-onboarding`, `codehealth-mcp`, `coding-standards`, `coding-tutor`, `commit-with-reflection`, `competitive-platform-analysis`
  - `compose-multiplatform-patterns`, `content-engine`, `context-fundamentals`, `context-hunter`, `continuous-agent-loop`, `contract-freezer`, `cost-aware-llm-pipeline`, `cpp-coding-standards`
  - `cpp-testing`, `crisp-dm-dgx-notebook`, `crosspost`, `cs-foundations`, `csharp-testing`, `dart-flutter-patterns`, `dashboard-builder`, `data-quality-frameworks`
  - `data-scraper-agent`, `data-storytelling`, `database-migrations`, `datacommons-client`, `defi-amm-security`, `delivery-gate`, `dependency-management`, `deployment-patterns`
  - `deslop`, `detecting-performance-regressions`, `diagnosing-bugs`, `digital-brain`, `django-celery`, `django-patterns`, `django-security`, `django-tdd`
  - `django-verification`, `dmux-workflows`, `dnanexus-integration`, `docker-patterns`, `documentation-lookup`, `docx`, `dotnet-patterns`, `e2e-testing`
  - `edgartools`, `ena-database`, `enterprise-agent-ops`, `error-handling`, `eval-harness`, `everything-claude-code`, `exploratory-data-analysis`, `fastapi-patterns`
  - `fda-database`, `flox-environments`, `fluidsim`, `flutter-dart-code-review`, `fred-economic-data`, `frontend-a11y`, `frontend-design-direction`, `frontend-patterns`
  - `frontend-slides`, `fsharp-testing`, `g2-legend-expert`, `gan-style-harness`, `generating-python-installer`, `geo-database`, `geopandas`, `gh-address-comments`
  - `gh-fix-ci`, `git-workflow`, `github-ops`, `github-repo-safety-audit`, `golang-patterns`, `golang-testing`, `growth-log`, `gstack-benchmark`
  - `gstack-codex`, `gstack-context-restore`, `gstack-cso`, `gstack-deslop-shared-libs`, `gstack-devex-review`, `gstack-document-generate`, `gstack-freeze`, `gstack-ios-clean`
  - `gstack-ios-design-review`, `gstack-ios-sync`, `gstack-learn`, `gstack-pair-agent`, `gstack-review`, `gstack-setup-browser-cookies`, `gstack-unfreeze`, `gtars`
  - `healthcare-cdss-patterns`, `healthcare-emr-patterns`, `healthcare-phi-compliance`, `hedgefundmonitor`, `hexagonal-architecture`, `hipaa-compliance`, `histolab`, `homelab-vlan-segmentation`
  - `hypothesis-generation`, `hypothesis-testing`, `imagegen`, `ios-icon-gen`, `ito-compute`, `ito-trade-planner`, `java-coding-standards`, `jpa-patterns`
  - `jupyter-notebook`, `knowledge-ops`, `kotlin-coroutines-flows`, `kotlin-exposed-patterns`, `kotlin-ktor-patterns`, `kotlin-patterns`, `kotlin-testing`, `kubernetes-patterns`
  - `laporan-generator-thesis`, `laravel-patterns`, `laravel-plugin-discovery`, `laravel-security`, `laravel-tdd`, `laravel-verification`, `latchbio-integration`, `latex-submission-pipeline`
  - `liquid-glass-design`, `literature-review`, `llm-trading-agent-security`, `mailtrap-email-integration`, `manim-video`, `manuscript-as-code`, `mathematical-logic-expert`, `mcp-server-patterns`
  - `mermaid-expert`, `mermaid-visualizer`, `metabolomics-workbench-database`, `ml-pipeline-workflow`, `mlops-zoomcamp-scaffold`, `motion-advanced`, `motion-foundations`, `motion-patterns`
  - `motion-ui`, `multi-platform-scraper`, `mysql-patterns`, `nestjs-patterns`, `netmiko-ssh-automation`, `network-bgp-diagnostics`, `networkx`, `nextjs-turbopack`
  - `nodejs-keccak256`, `note`, `nutrient-document-processing`, `nuxt4-patterns`, `obsidian-bases`, `obsidian-mind`, `omero-integration`, `openai-docs`
  - `openai-knowledge`, `openalex-database`, `orch-add-feature`, `orch-build-mvp`, `orch-pipeline`, `orch-refine-code`, `peer-review`, `performance-optimization`
  - `performance-testing`, `performing-causal-analysis`, `perl-patterns`, `perl-security`, `perl-testing`, `perplexity-search`, `plankton-code-quality`, `playbook-replica`
  - `playwright`, `plotly`, `pm-decision-log`, `pm-vault-manager`, `postgres-patterns`, `prisma-patterns`, `product-lens`, `project-flow-ops`
  - `project-guidelines-example`, `property-based-testing`, `providing-performance-optimization-advice`, `pubmed-database`, `pufferlib`, `pydeseq2`, `pydicom`, `pyhealth`
  - `pymatgen`, `pymc`, `pyopenms`, `python-patterns`, `python-testing`, `pytorch-patterns`, `pyzotero`, `quality-nonconformance`
  - `quarkus-patterns`, `quarkus-security`, `quarkus-tdd`, `quarkus-verification`, `ralph-loop`, `rdkit`, `react-native-patterns`, `react-patterns`
  - `react-performance`, `react-testing`, `receiving-code-review`, `redis-patterns`, `remotion-video-creation`, `requesting-code-review`, `research-grants`, `research-lookup`
  - `research-title-formulator`, `rowan`, `rust-patterns`, `rust-testing`, `scientific-brainstorming`, `scientific-db-pubmed-database`, `scientific-db-uspto-database`, `scientific-pkg-gget`
  - `scientific-slides`, `scikit-learn`, `scikit-survival`, `scrapling`, `scrapling-official`, `search-first`, `security-best-practices`, `security-bounty-hunter`
  - `security-ownership-map`, `security-review`, `security-reviewer`, `security-scan`, `security-threat-model`, `senior-data-scientist`, `senior-ml-engineer`, `senior-prompt-engineer`
  - `similarity-search-patterns`, `simpy`, `slides-as-code`, `social-publisher`, `speckit-analyze`, `speckit-implement`, `speckit-taskstoissues`, `spesialis`
  - `spesialis-backend`, `spesialis-devops-infrastruktur`, `spesialis-frontend`, `spesialis-mobile`, `spesialis-produktivitas-workspace`, `spesialis-research-akademik`, `spesialis-security-qa`, `spesialis-ui-templates`
  - `springboot-patterns`, `springboot-security`, `springboot-tdd`, `springboot-verification`, `stable-baselines3`, `swift-actor-persistence`, `swift-concurrency-6-2`, `swift-protocol-di-testing`
  - `swiftui-patterns`, `sympy`, `systematic-debugging`, `taste`, `tdd-guide`, `tdd-workflow`, `team-builder`, `tensorboard`
  - `tinystruct-patterns`, `transformer-lens-interpretability`, `transformers`, `treatment-plans`, `ui-design`, `ui-to-vue`, `unified-notifications-ops`, `uniprot-database`
  - `usfiscaldata`, `uspto-database`, `venue-templates`, `vite-patterns`, `vue-patterns`, `windows-desktop-e2e`, `windows-hook-debugging`, `x-api`
  - `xan`, `xlsx`, `yeet`, `zarr-python`

### Domain: Machine Learning, AI & Data Science (112 Skills)
- **Lead PIC Spesialis**: `spesialis-data-ai-agentic`
- **Daftar Lengkap Skill**:
  - `aeon`, `agent-eval`, `agent-self-evaluation`, `agentic-engineering`, `ai-job-search`, `alpha-vantage`, `benchmark-methodology`, `benchmark-optimization-loop`
  - `ceemdan-lstm-forecasting`, `citation-management`, `create-readme`, `creating-data-visualizations`, `crispdm-lstm-forecasting`, `dask`, `data-artist`, `data-throughput-accelerator`
  - `datavis`, `dazai`, `denario`, `detecting-data-anomalies`, `docx-comment-reply`, `dynamic-workflow-mode`, `eda-data-ai-agentic`, `embedding-strategies`
  - `evals-context`, `evaluating-code-models`, `evaluating-llms-harness`, `evaluating-machine-learning-models`, `explaining-machine-learning-models`, `fal-ai-media`, `flashrag-evidence`, `foundation-models-on-device`
  - `gateguard`, `gradient-methods`, `gstack-autoplan`, `gstack-benchmark-models`, `gstack-design-html`, `gstack-scrape`, `gstack-setup-deploy`, `gstack-test-audit`
  - `healthcare-eval-harness`, `hermes-ecc-templating`, `imaging-data-commons`, `impeccable`, `iterative-retrieval`, `ito-data-atlas-agent`, `lamindb`, `latency-critical-systems`
  - `laya-text-classifier`, `lead-intelligence`, `markitdown`, `matlab`, `matplotlib`, `ml-adoption-playbook`, `ml-data-leakage-guard`, `mle-workflow`
  - `neurokit2`, `neuropixels-analysis`, `nowait-reasoning-optimizer`, `openrig-team-assembly`, `opensource-pipeline`, `parkinson-speech-progression`, `pathml`, `plan-canvas`
  - `pm-discovery-memo`, `pm-eda-analytics`, `pm-prd-versioning`, `polars`, `pptx-posters`, `prediction-market-oracle-research`, `prediction-market-risk-review`, `preprocessing-data-with-automated-pipelines`
  - `pymoo`, `pytorch-lightning`, `ralphinho-rfc-pipeline`, `recsys-pipeline-architect`, `recursive-decision-ledger`, `regex-vs-llm-structured-text`, `reverse-engineer-anything`, `scanpy`
  - `scholar-evaluation`, `scholarly-publishing`, `scientific-critical-thinking`, `scientific-data-preprocessing`, `scientific-reporting`, `scientific-thinking-scholar-evaluation`, `scientific-visualization`, `scientific-writing`
  - `scikit-bio`, `seaborn`, `senior-computer-vision`, `sentry`, `seo`, `shap`, `skypilot-multi-cloud-orchestration`, `sparse-autoencoder-training`
  - `spesialis-data-ai-agentic`, `splitting-datasets`, `statistics-math`, `structured-content-storage`, `submission-checklist`, `theme-factory`, `tiledbvcf`, `timesfm-forecasting`
  - `torch-geometric`, `torchdrug`, `ultra-think`, `umap-learn`, `unsloth`, `ux-researcher-designer`, `vaex`, `weights-and-biases`

### Domain: Research, Academic, Bio & Scientific Computing (52 Skills)
- **Lead PIC Spesialis**: `spesialis-research-akademik`
- **Daftar Lengkap Skill**:
  - `academic-note-coach`, `ai-first-engineering`, `clinical-decision-support`, `comprehensive-research-agent`, `content-research-writer`, `deep-research`, `design-system`, `designing-experiments`
  - `etetoolkit`, `exa-search`, `excalidraw-diagram`, `figgenie-paper-diagram`, `generate-image`, `generating-test-reports`, `geomaster`, `get-available-resources`
  - `gstack-design-shotgun`, `gstack-diagram`, `gstack-make-pdf`, `homelab-wireguard-vpn`, `ito-basket-compare`, `ito-market-intelligence`, `laporan-generator`, `latex-posters`
  - `market-research`, `market-research-reports`, `marketing-campaign`, `math`, `math-model-selector`, `math-tools`, `orch-fix-defect`, `paper-2-web`
  - `pm-ab-test-design`, `pm-churn-retention`, `pm-file-ops`, `pm-interview-synthesis`, `pm-lightweight-spec`, `pm-weekly-digest`, `prd`, `propositional-logic`
  - `pymc-bayesian-modeling`, `report-generator`, `research-ops`, `scientific-schematics`, `scientific-thinking-literature-review`, `speckit-checklist`, `speckit-plan`, `speech`
  - `statistical-analysis`, `statsmodels`, `ui-radar`, `webthinker-deep-research`

### Domain: DevOps, Cloud, Network & Infrastructure (41 Skills)
- **Lead PIC Spesialis**: `spesialis-devops-infrastruktur`
- **Daftar Lengkap Skill**:
  - `blender-motion-state-inspection`, `canary-watch`, `click-path-audit`, `connections-optimizer`, `council`, `create-plan`, `create-slack-agents`, `dispatching-parallel-agents`
  - `document-skills`, `ecc-recipes`, `evm-token-decimals`, `finance-billing-ops`, `finishing-a-development-branch`, `google-drive-ops`, `gstack-canary`, `gstack-land-and-deploy`
  - `gstack-landing-report`, `gstack-spec`, `homelab-network-readiness`, `homelab-network-setup`, `homelab-pihole-dns`, `investor-materials`, `make-interfaces-feel-better`, `medchem`
  - `netlify-deploy`, `network-config-validation`, `network-interface-health`, `obsidian-markdown`, `pm-narrative-analytics`, `rules-distill`, `screenshot`, `social-graph-ranker`
  - `specialist-skill-architect`, `speckit-clarify`, `speckit-constitution`, `speckit-specify`, `spesialis-skills`, `terminal-ops`, `uncloud`, `vercel-deploy`
  - `verification-loop`

### Domain: Security Audit, Pentest & Quality Assurance (21 Skills)
- **Lead PIC Spesialis**: `spesialis-security-qa`
- **Daftar Lengkap Skill**:
  - `automation-audit-ops`, `context-budget`, `customs-trade-compliance`, `docs-review`, `ecc-tools-cost-audit`, `gstack-design-consultation`, `gstack-ios-qa`, `gstack-qa`
  - `gstack-qa-only`, `independent-auditor`, `infographics`, `iso-13485-certification`, `metodologi-gstack`, `node-zombie-guardian`, `pm-prd-review`, `pm-project-state`
  - `production-audit`, `repo-scan`, `skill-stocktake`, `ui-demo`, `workspace-surface-audit`

### Domain: Product Management, Business & Career (36 Skills)
- **Lead PIC Spesialis**: `spesialis-product-bisnis / ai-job-search`
- **Daftar Lengkap Skill**:
  - `competitive-report-structure`, `customer-billing-ops`, `energy-procurement`, `figma-implement-design`, `gstack-ship`, `intent-driven-development`, `inventory-demand-planning`, `investor-outreach`
  - `job-application-assistant`, `job-scraper`, `kafka`, `lean-canvas-guide`, `logistics-exception-management`, `pm-competitive-intel`, `pm-deep-discovery`, `pm-executive-narrative`
  - `pm-jira-ops`, `pm-learning-tracker`, `pm-mcp-orchestration`, `pm-objection-simulation`, `pm-opportunity-sizing`, `pm-prd-to-jira`, `pm-qbr-packet`, `pm-roadmap-reasoning`
  - `pm-session-start`, `pm-slack-ops`, `pm-subagent-dispatch`, `pm-support-mining`, `pm-team-context`, `pram`, `product-capability`, `production-scheduling`
  - `returns-reverse-logistics`, `safety-guard`, `spesialis-product-bisnis`, `spesialis-project-manager`

### Domain: Workspace, Documents & Knowledge Management (23 Skills)
- **Lead PIC Spesialis**: `spesialis-produktivitas-workspace`
- **Daftar Lengkap Skill**:
  - `belajar`, `cli-anything-obsidian`, `doc`, `docs-write`, `document-extraction-workflow`, `email-ops`, `file-organizer`, `google-calendar-automation`
  - `google-workspace-ops`, `gstack-document-release`, `jira-integration`, `knowledge-steward`, `linear`, `obsidian-cli`, `obsidian-knowledge-curator`, `pdf`
  - `pptx`, `prowler-docs`, `spreadsheet`, `team-agent-orchestration`, `visa-doc-translate`, `vscode-release-notes-writer`, `writing-docs`

### Domain: Creative Media, Video, Art & Copywriting (14 Skills)
- **Lead PIC Spesialis**: `spesialis-kreatif-media / spesialis-copywriter`
- **Daftar Lengkap Skill**:
  - `algorithmic-art`, `brand-discovery`, `content-hash-cache-pattern`, `defuddle`, `logo-design`, `markdown-mermaid-writing`, `spesialis-copywriter`, `spesialis-kreatif-media`
  - `test-driven-development`, `transcribe`, `video-editing`, `video-studio`, `videodb`, `writing-plans`

### Domain: Skill Engineering & Meta-Orchestration (23 Skills)
- **Lead PIC Spesialis**: `spesialis-skills (Asep) / pram-orchestrator`
- **Daftar Lengkap Skill**:
  - `gstack-browse`, `gstack-careful`, `gstack-claude-code`, `gstack-context-save`, `gstack-design-review`, `gstack-guard`, `gstack-health`, `gstack-investigate`
  - `gstack-ios-fix`, `gstack-office-hours`, `gstack-open-gstack-browser`, `gstack-plan-ceo-review`, `gstack-plan-design-review`, `gstack-plan-devex-review`, `gstack-plan-eng-review`, `gstack-plan-tune`
  - `gstack-retro`, `gstack-setup-gbrain`, `gstack-skillify`, `gstack-sync-gbrain`, `gstack-upgrade`, `pram-orchestrator`, `skill-comply`

### Domain: General Utilities & System Tools (66 Skills)
- **Lead PIC Spesialis**: `general`
- **Daftar Lengkap Skill**:
  - `LQF_Machine_Learning_Expert_Guide`, `agent-introspection-debugging`, `agent-payment-x402`, `ai-proxy-interception`, `always-mcp-hermes`, `antigravity-cli`, `blueprint`, `cancel-ralph`
  - `carrier-relationship-management`, `claude-devfleet`, `clinical-reports`, `code-tour`, `confidence-check`, `config-gc`, `configure-ecc`, `continuous-learning-v2`
  - `cost-tracking`, `dialectic`, `ecc-guide`, `error-resolver`, `executing-plans`, `hermes-imports`, `hive-mind-advanced`, `hookify-rules`
  - `inherit-legacy-style`, `json-canvas`, `kiro-mode-router`, `kiro-workflow`, `local-vco-roles`, `loop-design-check`, `matchms`, `mcp-integration`
  - `messages-ops`, `metric-calculator`, `nanoclaw-repl`, `openclaw-persona-forge`, `openrig-skills`, `orch-change-feature`, `parallel-execution-optimizer`, `plan-orchestrate`
  - `planning-with-files`, `prompt-lookup`, `prompt-optimizer`, `qmd`, `santa-method`, `skill-lookup`, `smart-file-writer`, `socratic-intake-hygiene`
  - `spec-kit-vibe-compat`, `speckit-tasks`, `strategic-compact`, `subagent-driven-development`, `system-analyst-skkni`, `team-composition-analysis`, `think-harder`, `token-budget-advisor`
  - `track-management`, `trading-agent`, `upskill`, `using-superantigravity`, `verification-before-completion`, `verification-quality-assurance`, `visualization-best-practices`, `windows-hardware-diagnostics`
  - `windows-terminal-workflow`, `workspace-repo-template`
