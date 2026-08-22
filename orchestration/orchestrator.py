from __future__ import annotations

from typing import Any

from AGENTS.caregiver_communication_agent import CaregiverCommunicationAgent
from AGENTS.context_correlation_agent import ContextCorrelationAgent
from AGENTS.human_review_agent import HumanReviewAgent
from AGENTS.observation_intake_agent import ObservationIntakeAgent
from AGENTS.pattern_review_agent import PatternReviewAgent
from AGENTS.risk_escalation_agent import RiskEscalationAgent

AGENTS = [
    ObservationIntakeAgent(),
    PatternReviewAgent(),
    ContextCorrelationAgent(),
    CaregiverCommunicationAgent(),
    RiskEscalationAgent(),
    HumanReviewAgent(),
]


def governance_gate(context: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []

    high_risk_flags = {
        "sudden_onset": "sudden or acute onset requires prompt clinical evaluation",
        "new_neurologic_symptoms": "new neurologic symptoms require clinical evaluation",
        "possible_delirium": "possible delirium or medical trigger requires clinical evaluation",
        "command_hallucinations": "command hallucinations require immediate human risk review",
        "self_harm_risk": "self-harm risk requires immediate human escalation",
        "violence_risk": "violence risk requires immediate human escalation",
        "wandering_risk": "wandering risk requires human safety planning",
        "fall_risk": "fall risk requires human safety planning",
    }
    for key, reason in high_risk_flags.items():
        if context.get(key):
            reasons.append(reason)

    forbidden_requests = {
        "diagnosis": "the system cannot diagnose the cause of hallucinations",
        "prescription": "the system cannot prescribe medication",
        "medication_change": "medication changes require a qualified clinician",
        "treatment_authorization": "the system cannot authorize treatment",
        "restraint_authorization": "the system cannot authorize restraint or confinement",
    }
    for key, reason in forbidden_requests.items():
        if context.get(key):
            reasons.append(reason)

    required_checks = {
        "observation_source_verified": "observation source or provenance is not verified",
        "medical_change_screened": "recent medical or medication changes have not been screened",
        "risk_review_complete": "risk review is incomplete",
        "privacy_reviewed": "privacy review is incomplete",
        "human_approval": "qualified human approval is required",
    }
    for key, reason in required_checks.items():
        if not context.get(key, False):
            reasons.append(reason)

    return {
        "allowed": not reasons,
        "requires_human_review": True,
        "reasons": reasons,
        "autonomous_diagnosis_authority": False,
        "autonomous_treatment_authority": False,
        "autonomous_medication_authority": False,
    }


def orchestrate(context: dict[str, Any]) -> dict[str, Any]:
    outputs = {agent.name: agent.run(context) for agent in AGENTS}
    governance = governance_gate(context)
    return {
        "system": "F63 Agentic Hallucination Monitoring",
        "version": "1.0",
        "agent_outputs": outputs,
        "governance": governance,
        "status": "approved_for_support" if governance["allowed"] else "human_review_required",
    }
