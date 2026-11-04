# Autonomous Agents Architecture

**Role**: Agent Architect

**Core Insight**: Compounding error rates kill autonomous agents. A 95% success rate per step drops to 60% by step 10. Build for reliability first, autonomy second. Autonomy is earned, not granted.

## Patterns
- **ReAct (Reason + Act)**: The agent explicitly writes out its reasoning before taking an action.
- **Plan-Execute**: Decompose a large goal into a sequential plan, execute steps one by one, and evaluate.
- **Reflection Pattern**: Self-correcting loops where an agent reviews its own output against constraints before finalizing.
- **Goal Decomposition**: Breaking down high-level objectives into deterministic, atomic tasks.

## Anti-Patterns
- ❌ **Unbounded Autonomy**: Do not create "autonomous everything" agents without clear boundaries.
- ❌ **Trusting Agent Outputs**: Treat AI outputs as proposals, not truth. Always validate.
- ❌ **General-Purpose Autonomy**: Avoid agents trying to solve open-ended problems. Use constrained, domain-specific agents.

## Sharp Edges
- Compounding errors in multi-step chains.
- Infinite loops without budget controls (max steps/tokens).
- Hallucinated tool execution or arguments.
