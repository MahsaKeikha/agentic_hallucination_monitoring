from pathlib import Path

from orchestration.orchestrator import AGENTS, governance_gate, orchestrate
from safety.clinical_gate import clinical_gate


def approved_context():
    return {
        "observations": ["visual experience reported in evening"],
        "observation_source_verified": True,
        "medical_change_screened": True,
        "risk_review_complete": True,
        "privacy_reviewed": True,
        "human_approval": True,
    }


def test_reference_structure():
    required = [
        "AGENTS", "TOOLS", "SKILLS", "orchestration", "memory", "state",
        "schemas", "prompts", "config", "safety", "observability", "evals",
        "benchmarks", "examples", "docs",
    ]
    for name in required:
        assert Path(name).exists()
    assert len(list(Path("AGENTS").glob("*.py"))) >= 6
    assert len(list(Path("TOOLS").glob("*.py"))) >= 5
    assert len(list(Path("SKILLS").glob("*.py"))) >= 5


def test_all_specialists_execute():
    result = orchestrate(approved_context())
    assert set(result["agent_outputs"]) == {agent.name for agent in AGENTS}
    assert result["status"] == "approved_for_support"


def test_missing_human_approval_fails_closed():
    context = approved_context()
    context["human_approval"] = False
    assert not governance_gate(context)["allowed"]


def test_command_hallucinations_trigger_escalation():
    context = approved_context()
    context["command_hallucinations"] = True
    gate = governance_gate(context)
    assert not gate["allowed"]
    assert any("command hallucinations" in reason for reason in gate["reasons"])


def test_possible_delirium_fails_closed():
    context = approved_context()
    context["possible_delirium"] = True
    assert not governance_gate(context)["allowed"]


def test_medication_change_is_not_authorized():
    context = approved_context()
    context["medication_change"] = True
    assert not governance_gate(context)["allowed"]


def test_clinical_gate_has_no_autonomous_authority():
    result = clinical_gate(approved_context())
    assert result["autonomous_diagnosis_authority"] is False
    assert result["autonomous_treatment_authority"] is False
    assert result["autonomous_medication_authority"] is False


def test_source_verification_is_required():
    context = approved_context()
    context["observation_source_verified"] = False
    assert not governance_gate(context)["allowed"]
