from __future__ import annotations

from typing import Any


def clinical_gate(context: dict[str, Any]) -> dict[str, Any]:
    blocked_keys = (
        "diagnosis",
        "prescription",
        "medication_change",
        "treatment_authorization",
        "restraint_authorization",
    )
    urgent_keys = (
        "sudden_onset",
        "new_neurologic_symptoms",
        "possible_delirium",
        "command_hallucinations",
        "self_harm_risk",
        "violence_risk",
        "wandering_risk",
        "fall_risk",
    )
    blocked = any(context.get(key) for key in blocked_keys)
    urgent = any(context.get(key) for key in urgent_keys)
    approved = bool(context.get("human_approval", False))
    return {
        "allowed": not blocked and not urgent and approved,
        "requires_human_review": True,
        "urgent_human_escalation": urgent,
        "autonomous_diagnosis_authority": False,
        "autonomous_treatment_authority": False,
        "autonomous_medication_authority": False,
    }
