from __future__ import annotations

from typing import Any


class RiskEscalationAgent:
    name = "risk_escalation"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        risk_keys = (
            "sudden_onset",
            "new_neurologic_symptoms",
            "possible_delirium",
            "command_hallucinations",
            "self_harm_risk",
            "violence_risk",
            "wandering_risk",
            "fall_risk",
        )
        active = [key for key in risk_keys if context.get(key)]
        return {
            "agent": self.name,
            "active_risks": active,
            "urgent_human_escalation": bool(active),
        }
