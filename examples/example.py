from orchestration.orchestrator import orchestrate


context = {
    "observations": ["visual experience reported in evening"],
    "observation_source_verified": True,
    "medical_change_screened": True,
    "risk_review_complete": True,
    "privacy_reviewed": True,
    "human_approval": True,
}

print(orchestrate(context))
