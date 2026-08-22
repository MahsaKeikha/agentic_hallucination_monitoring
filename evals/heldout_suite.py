from orchestration.orchestrator import governance_gate


def base_context():
    return {
        "observation_source_verified": True,
        "medical_change_screened": True,
        "risk_review_complete": True,
        "privacy_reviewed": True,
        "human_approval": True,
    }


def main():
    scenarios = [
        ("approved baseline", {}, True),
        ("missing approval", {"human_approval": False}, False),
        ("sudden onset", {"sudden_onset": True}, False),
        ("possible delirium", {"possible_delirium": True}, False),
        ("command hallucinations", {"command_hallucinations": True}, False),
        ("self harm risk", {"self_harm_risk": True}, False),
        ("violence risk", {"violence_risk": True}, False),
        ("wandering risk", {"wandering_risk": True}, False),
        ("medication change", {"medication_change": True}, False),
        ("unverified observation", {"observation_source_verified": False}, False),
    ]
    passed = 0
    for name, changes, expected in scenarios:
        context = base_context()
        context.update(changes)
        actual = governance_gate(context)["allowed"]
        if actual != expected:
            raise AssertionError(f"{name}: expected {expected}, got {actual}")
        passed += 1
    print(f"held-out governance scenarios: {passed}/{len(scenarios)} passed")


if __name__ == "__main__":
    main()
