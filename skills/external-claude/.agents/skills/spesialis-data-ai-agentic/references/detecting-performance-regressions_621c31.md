# Performance Regression Detector

## Positioning

Treat this skill as an explicit/manual helper for benchmark comparison work.

## When to Use

Use this skill when:
- Identify performance regressions in a CI/CD pipeline.
- Analyze performance metrics for potential degradation.
- Compare current performance against historical baselines.

## Not For / Boundaries

- Broad optimization roadmap or tuning backlog: use `providing-performance-optimization-advice`
- Root-cause debugging of a specific slow path: use `systematic-debugging`
- General test artifact packaging without regression judgment: use `generating-test-reports`

## Typical Outputs

- A baseline-vs-current regression summary
- Severity-ranked regressed metrics
- Follow-up questions for deeper profiling or investigation

## Related Skills

- `performance-testing` for benchmark generation
- `providing-performance-optimization-advice` after the regression is confirmed
