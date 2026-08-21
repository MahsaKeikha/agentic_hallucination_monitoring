# Agentic Hallucination Monitoring

F63 in the Agentic AI Library.

A standalone multi-agent workflow for structured observation logging, pattern review, context correlation, caregiver communication, escalation, and human review around hallucination-related observations.

This system does not diagnose causes, prescribe treatment, determine emergency status autonomously, or replace qualified clinical judgment.

## Core agents

- [`observation_intake_agent.py`](AGENTS/observation_intake_agent.py)
- [`pattern_review_agent.py`](AGENTS/pattern_review_agent.py)
- [`context_correlation_agent.py`](AGENTS/context_correlation_agent.py)
- [`caregiver_communication_agent.py`](AGENTS/caregiver_communication_agent.py)
- [`risk_escalation_agent.py`](AGENTS/risk_escalation_agent.py)
- [`human_review_agent.py`](AGENTS/human_review_agent.py)

## Architecture

[`TOOLS/`](TOOLS/) | [`SKILLS/`](SKILLS/) | [`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Run

```bash
python run.py
```
