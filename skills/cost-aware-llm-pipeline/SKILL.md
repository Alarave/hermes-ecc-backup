---
name: cost-aware-llm-pipeline
description: "[omh] Cost optimization patterns for LLM API usage: model routing by task complexity, budget tracking, retry logic, and prompt caching. Use when the user says: cost-aware-llm-pipeline, llm cost, optimize llm cost, reduce api cost."
license: MIT
author: "oh-my-hermes maintainers"
metadata:
  hermes:
    tags: [workflow, oh-my-hermes, llm, cost-optimization, ai]
    category: data-ai
    phase: cost-management
    role: planner
    quality_tier: evidence-gated
    related_skills: [spesialis-data-ai-agentic, mle-workflow]
---

# Cost-Aware LLM Pipeline

## R (Role & Identity)
- **Peran**: LLM Cost Optimization Architect & Pipeline Engineer.
- **Misi**: Mengendalikan biaya token API LLM, mencegah pemborosan anggaran (*burn rate*), dan mempertahankan kualitas output melalui perutean model, prompt caching, dan batch orchestration.

## C (Context & Activation)
Gunakan saat:
- Membangun aplikasi yang memanggil API LLM (Claude, GPT, dll.).
- Memproses ribuan item atau dataset besar secara berkala.
- Menetapkan pagu anggaran (*budget guardrails*) ketat sebelum proses berjalan.

## C (Constraints & Optimization Patterns)

### 1. Model Routing by Task Complexity

Automatically select cheaper models for simple tasks, reserving expensive models for complex ones.

```python
MODEL_SONNET = "claude-sonnet-4-6"
MODEL_HAIKU = "claude-haiku-4-5-20251001"

_SONNET_TEXT_THRESHOLD = 10_000  # chars
_SONNET_ITEM_THRESHOLD = 30     # items

def select_model(
    text_length: int,
    item_count: int,
    force_model: str | None = None,
) -> str:
    """Select model based on task complexity."""
    if force_model is not None:
        return force_model
    if text_length >= _SONNET_TEXT_THRESHOLD or item_count >= _SONNET_ITEM_THRESHOLD:
        return MODEL_SONNET  # Complex task
    return MODEL_HAIKU  # Simple task (3-4x cheaper)
```

### 2. Immutable Cost Tracking

Track cumulative spend with frozen dataclasses. Each API call returns a new tracker: never mutates state.

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CostRecord:
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float

@dataclass(frozen=True, slots=True)
class CostTracker:
    budget_limit: float = 1.00
    records: tuple[CostRecord, ...] = ()

    def add(self, record: CostRecord) -> "CostTracker":
        """Return new tracker with added record (never mutates self)."""
        return CostTracker(
            budget_limit=self.budget_limit,
            records=(*self.records, record),
        )

    @property
    def total_cost(self) -> float:
        return sum(r.cost_usd for r in self.records)

    @property
    def over_budget(self) -> bool:
        return self.total_cost > self.budget_limit
```

### 3. Narrow Retry Logic with Full Jitter

Retry only on transient errors. Use exponential backoff with full jitter to avoid the thundering herd problem. Fail fast on authentication or validation errors.

```python
import random
import time
from anthropic import APIConnectionError, InternalServerError, RateLimitError

_RETRYABLE_ERRORS = (APIConnectionError, RateLimitError, InternalServerError)
_MAX_RETRIES = 3
_BASE_DELAY = 1.0
_MAX_DELAY = 20.0

def call_with_retry(func, *, max_retries: int = _MAX_RETRIES):
    """Retry with full jitter backoff on transient errors."""
    for attempt in range(max_retries):
        try:
            return func()
        except _RETRYABLE_ERRORS:
            if attempt == max_retries - 1:
                raise
            # Full Jitter formula: sleep = random(0, min(cap, base * 2^attempt))
            sleep_time = random.uniform(0, min(_MAX_DELAY, _BASE_DELAY * (2 ** attempt)))
            time.sleep(sleep_time)
```

### 4. Prompt Caching & Static Prefix Discipline

Cache long system prompts and reference documentation. Keep static content strictly at the beginning of the prompt. Dynamic variables (timestamps, user IDs, questions) MUST be appended at the end to prevent cache invalidation.

```python
# Anthropic Ephemeral Breakpoint
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": static_system_instructions,
                "cache_control": {"type": "ephemeral"},  # Cache breakpoint
            },
            {
                "type": "text",
                "text": dynamic_query,  # Variable payload at the tail
            },
        ],
    }
]
```

### 5. Asynchronous Batch API (-50% Cost Discount)

For non-blocking tasks (evaluasi data, ekstraksi dokumen, batch scraping, summarization offline), gunakan endpoint Batch API (OpenAI `/v1/batches` atau Anthropic Message Batches).

- **Keuntungan**: Diskon 50% biaya token input dan output, limit rate terpisah.
- **SLA**: Hasil dikembalikan dalam rentang 24 jam.

```python
# Pola Orkestrasi OpenAI Batch API
import json
from openai import OpenAI

client = OpenAI()

def submit_batch_job(requests_list: list[dict], batch_file: str = "batch_input.jsonl"):
    with open(batch_file, "w") as f:
        for r in requests_list:
            f.write(json.dumps(r) + "\n")
            
    file_batch = client.files.create(file=open(batch_file, "rb"), purpose="batch")
    batch_job = client.batches.create(
        input_file_id=file_batch.id,
        endpoint="/v1/chat/completions",
        completion_window="24h"
    )
    return batch_job.id
```

## Composition

Combine all four techniques in a single pipeline function:

```python
def process(text: str, config: Config, tracker: CostTracker) -> tuple[Result, CostTracker]:
    # 1. Route model
    model = select_model(len(text), estimated_items, config.force_model)

    # 2. Check budget
    if tracker.over_budget:
        raise BudgetExceededError(tracker.total_cost, tracker.budget_limit)

    # 3. Call with retry + caching
    response = call_with_retry(lambda: client.messages.create(
        model=model,
        messages=build_cached_messages(system_prompt, text),
    ))

    # 4. Track cost (immutable)
    record = CostRecord(model=model, input_tokens=..., output_tokens=..., cost_usd=...)
    tracker = tracker.add(record)

    return parse_result(response), tracker
```

## Pricing Reference (2025-2026)

| Model | Input ($/1M tokens) | Output ($/1M tokens) | Relative Cost |
|-------|---------------------|----------------------|---------------|
| Haiku 4.5 | $0.80 | $4.00 | 1x |
| Sonnet 4.6 | $3.00 | $15.00 | ~4x |
| Opus 4.5 | $15.00 | $75.00 | ~19x |

## Best Practices

- **Start with the cheapest model** and only route to expensive models when complexity thresholds are met
- **Set explicit budget limits** before processing batches: fail early rather than overspend
- **Log model selection decisions** so you can tune thresholds based on real data
- **Use prompt caching** for system prompts over 1024 tokens: saves both cost and latency
- **Never retry on authentication or validation errors**: only transient failures (network, rate limit, server error)

## Anti-Patterns to Avoid

- Using the most expensive model for all requests regardless of complexity
- Retrying on all errors (wastes budget on permanent failures)
- Mutating cost tracking state (makes debugging and auditing difficult)
- Hardcoding model names throughout the codebase (use constants or config)
- Ignoring prompt caching for repetitive system prompts

## When to Use

- Any application calling Claude, OpenAI, or similar LLM APIs
- Batch processing pipelines where cost adds up quickly
- Multi-model architectures that need intelligent routing
- Production systems that need budget guardrails
