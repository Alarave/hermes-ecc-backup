# Performance Optimization Advisor

## Positioning

Treat this skill as an explicit/manual advisor for prioritizing optimization work.

## When to Use

Use this skill when:
- Prioritizing known or suspected performance bottlenecks from existing logs, traces, benchmarks, or user reports.
- Get recommendations for improving website loading speed.
- Optimize database query performance.
- Improve API response times.
- Reduce infrastructure costs.

## Not For / Boundaries

- Build-to-build regression detection: use `detecting-performance-regressions`
- Raw benchmark execution or profiling capture: use `performance-testing`
- Test-result packaging for QA audiences: use `generating-test-reports`

## Typical Outputs

- A ranked optimization backlog by impact and effort
- Concrete hotspots by layer: frontend, backend, infra, or database
- Suggested validation steps to prove the optimization worked

## Related Skills

- `detecting-performance-regressions` to prove there is a real regression
- `performance-testing` to collect the measurements behind the advice
