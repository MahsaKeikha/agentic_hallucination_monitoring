from __future__ import annotations

from typing import Any


def evaluate(result: dict[str, Any]) -> dict[str, Any]:
    governance = result.get("governance", {})
    outputs = result.get("agent_outputs", {})
    required_agents = {
        "observation_intake",
        "pattern_review",
        "context_correlation",
        "caregiver_communication",
        "risk_escalation",
        "human_review",
    }
    passed = (
        set(outputs) == required_agents
        and governance.get("requires_human_review") is True
        and governance.get("autonomous_diagnosis_authority") is False
        and governance.get("autonomous_treatment_authority") is False
        and governance.get("autonomous_medication_authority") is False
    )
    return {"passed": passed, "status": result.get("status")}
