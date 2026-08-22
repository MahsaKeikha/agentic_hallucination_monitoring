# Agentic Hallucination Monitoring

**F63 | L3 Gold Standard | v1.0**

A standalone governed multi-agent workflow for structured hallucination-related observation logging, pattern review, context correlation, caregiver communication, risk escalation, and qualified human review.

This system is for monitoring and support workflows only. It does not diagnose causes, prescribe or change medication, authorize treatment, authorize restraint or confinement, determine emergency status autonomously, or replace qualified clinical judgment.

## Core agents

- [`observation_intake_agent.py`](AGENTS/observation_intake_agent.py)
- [`pattern_review_agent.py`](AGENTS/pattern_review_agent.py)
- [`context_correlation_agent.py`](AGENTS/context_correlation_agent.py)
- [`caregiver_communication_agent.py`](AGENTS/caregiver_communication_agent.py)
- [`risk_escalation_agent.py`](AGENTS/risk_escalation_agent.py)
- [`human_review_agent.py`](AGENTS/human_review_agent.py)

## Governance contract

The workflow fails closed when required observation provenance, medical-change screening, risk review, privacy review, or qualified human approval is missing. It also routes sudden onset, new neurologic symptoms, possible delirium, command hallucinations, self-harm or violence risk, wandering risk, fall risk, diagnosis requests, medication requests, treatment authorization, and restraint authorization to human review or escalation.

Autonomous diagnosis authority: **False**  
Autonomous medication authority: **False**  
Autonomous treatment authority: **False**

## Architecture

[`AGENTS/`](AGENTS/) | [`TOOLS/`](TOOLS/) | [`SKILLS/`](SKILLS/) | [`orchestration/`](orchestration/) | [`memory/`](memory/) | [`state/`](state/) | [`schemas/`](schemas/) | [`prompts/`](prompts/) | [`config/`](config/) | [`safety/`](safety/) | [`observability/`](observability/) | [`evals/`](evals/) | [`benchmarks/`](benchmarks/) | [`examples/`](examples/) | [`tests/`](tests/) | [`docs/`](docs/)

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check .
python -m pytest -q
python evals/heldout_suite.py
python examples/example.py
python run.py
```

The held-out suite covers approved baseline behavior plus fail-closed cases for missing approval, sudden onset, possible delirium, command hallucinations, self-harm risk, violence risk, wandering risk, medication changes, and unverified observations.

## Run

```bash
python run.py
```
