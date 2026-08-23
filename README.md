# F63 Agentic Hallucination Monitoring

**Maturity:** L3 Gold Standard reference  
**Version:** 1.0

A governed six-agent reference architecture for structured hallucination-related observation logging, longitudinal pattern review, context correlation, caregiver communication, safety escalation, and qualified human review.

F63 is designed for monitoring and support workflows. It helps organize observations, preserve provenance, identify patterns across time and context, prepare concise caregiver-to-clinician communication, and surface situations that require qualified human attention.

This repository does not diagnose the cause of hallucinations, prescribe or change medication, authorize treatment, determine emergency status autonomously, authorize restraint or confinement, or replace qualified clinical judgment.

## Why hallucination monitoring requires explicit governance

Hallucination-related observations can be clinically meaningful, but a single observation rarely explains cause. Similar experiences can occur in different clinical, neurological, psychiatric, medication-related, sleep-related, sensory, infectious, metabolic, or environmental contexts. Monitoring software should therefore separate what was observed from what may have caused it.

A safe reference workflow is:

```text
observation reported
       |
       v
Observation Intake
       |
       v
Pattern Review
       |
       v
Context Correlation
       |
       v
Caregiver Communication
       |
       v
Risk Escalation
       |
       v
Qualified Human Review
```

The system records and structures evidence without converting correlation into diagnosis.

## Six-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Observation Intake Agent | Structures first-person or caregiver observations and their provenance | What exactly was observed, when, by whom, and under what conditions? |
| Pattern Review Agent | Reviews longitudinal frequency, timing, recurrence and associated events | Are there reproducible patterns in the observation history? |
| Context Correlation Agent | Organizes possible contextual associations without asserting causality | What environmental, temporal, medication, sleep, sensory or health changes occurred around the observation? |
| Caregiver Communication Agent | Produces concise handoff summaries for caregivers and qualified clinicians | What information should be communicated clearly without adding unsupported interpretation? |
| Risk Escalation Agent | Screens for conditions requiring urgent or higher-level human attention | Does the observation involve sudden change, possible delirium, dangerous commands, self-harm, violence, wandering, falls or another safety concern? |
| Human Review Agent | Represents the qualified clinical and safety authority boundary | Has the observation and any consequential interpretation been reviewed by an appropriate human? |

## Repository structure

```text
AGENTS/
├── observation_intake_agent.py
├── pattern_review_agent.py
├── context_correlation_agent.py
├── caregiver_communication_agent.py
├── risk_escalation_agent.py
└── human_review_agent.py

SKILLS/
├── observation_structuring.py
├── pattern_reasoning.py
├── context_reasoning.py
├── communication_reasoning.py
└── escalation_reasoning.py

TOOLS/
├── observation_log_tool.py
├── timeline_tool.py
├── context_tag_tool.py
├── summary_tool.py
└── provenance_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/tests.yml
run.py
README.md
```

The architecture deliberately separates reasoning from deterministic evidence handling, memory, safety gates, and human authority.

## Observation intake

The Observation Intake Agent captures the event before any interpretation is added.

A useful observation record can include:

```text
observation_id
person_reference
observer_reference
observer_role
start_time
end_time_or_duration
setting
reported_modality
reported_content_summary
behavioral_response
distress_level
functional_impact
immediate_safety_issue
associated_symptoms
recent_changes
source
source_timestamp
confidence_or_uncertainty
```

The system should preserve the distinction between:

- direct observation
- person self-report
- caregiver report
- clinician note
- device or sensor signal
- inferred or uncertain information

`TOOLS/observation_log_tool.py` provides the reference structure for storing observation evidence.

## Observation provenance

Provenance is a required safety property.

A record should make clear:

- who observed or reported the event
- when it was recorded
- whether the reporter directly witnessed it
- whether details were recalled later
- which source system produced any sensor or clinical data
- whether the source can be independently verified

An unverified caregiver report can still be important, but it should remain labeled as a report rather than silently converted into a confirmed clinical fact.

`TOOLS/provenance_tool.py` supports this evidence boundary.

## Longitudinal pattern review

The Pattern Review Agent organizes repeated observations without diagnosing cause.

Useful pattern dimensions can include:

- frequency
- duration
- time of day
- day/night clustering
- relation to sleep disruption
- relation to meals or hydration
- relation to medication administration times
- relation to mobility changes
- relation to sensory conditions
- changes in environment
- caregiver transitions
- recent illness or acute health changes
- distress level
- behavioral response
- falls or near falls
- wandering or exit-seeking

`TOOLS/timeline_tool.py` supports chronological reconstruction.

Patterns should be described using calibrated language such as "occurred more often during" or "was temporally associated with" rather than "was caused by" unless qualified clinical evidence supports causality.

## Context correlation

The Context Correlation Agent organizes potentially relevant surrounding conditions.

Context tags can include:

```text
sleep
lighting
noise
new_environment
social_stress
vision_or_hearing_change
medication_timing
recent_medication_change
missed_medication
pain
fever_or_illness
hydration
mobility_change
fall
constipation_or_other_discomfort
recent_procedure
hospitalization
caregiver_change
```

`TOOLS/context_tag_tool.py` provides a deterministic tagging layer.

The system must not conclude that a context tag explains the hallucination. Its purpose is to make possible associations visible to qualified reviewers.

## Medication and treatment boundaries

Medication information can be relevant to monitoring, but F63 has no prescribing authority.

The workflow may record:

- medication names as provided by an authorized source
- administration times
- missed or delayed doses
- recent medication additions or discontinuations
- reported side effects
- caregiver questions about medication

The system must not:

- start a medication
- stop a medication
- change dose or timing
- recommend antipsychotic, dopaminergic, sedative, sleep, or other therapy
- determine a drug caused the observation
- authorize a PRN medication

Medication-change requests and potentially consequential medication questions are routed to qualified human review.

## Acute change and delirium boundary

A sudden new hallucination pattern, rapid change in cognition, fluctuating attention, new disorientation, fever, infection concern, dehydration, recent surgery, medication change, or other acute change may require prompt medical evaluation.

F63 does not diagnose delirium. It treats possible delirium or sudden unexplained change as an escalation condition.

Useful states include:

```text
SUDDEN ONSET
ACUTE CHANGE
POSSIBLE DELIRIUM
NEW NEUROLOGIC SYMPTOM
CLINICAL REVIEW REQUIRED
```

The appropriate clinical response remains with qualified professionals and established emergency processes.

## Safety escalation

The Risk Escalation Agent screens observation records for conditions that should not remain in routine monitoring.

Examples include:

- command hallucinations involving dangerous actions
- self-harm concern
- violence risk
- wandering or exit-seeking with immediate risk
- fall or near-fall risk
- severe agitation with safety implications
- sudden onset
- possible delirium
- new neurologic symptoms
- marked change from baseline
- inability of the caregiver to maintain safety
- request for diagnosis
- medication-change request
- treatment-authorization request
- restraint or confinement request

The system routes these conditions to humans. It does not autonomously decide that an emergency is or is not present.

## Caregiver communication

The Caregiver Communication Agent converts raw logs into concise, evidence-preserving summaries.

A useful clinician-facing summary can include:

```text
observation period
baseline comparison
number of recorded episodes
representative examples
frequency and timing pattern
associated contextual changes
medication or health changes reported
falls/wandering/safety events
caregiver concerns
questions requiring clinical review
source and provenance notes
```

`TOOLS/summary_tool.py` provides the reference summarization layer.

A good handoff avoids statements such as "the medication caused this" or "this proves psychosis" unless those conclusions come from qualified clinical assessment.

## Distress and person-centered monitoring

Not all hallucination experiences produce the same level of distress or functional impact. Monitoring should avoid assuming that the presence of a hallucination alone determines severity.

Useful dimensions include:

- distress to the person
- fear
- agitation
- behavioral response
- sleep disruption
- ability to redirect
- effect on mobility
- effect on eating or hydration
- effect on caregiver burden
- risk to the person or others

Person-centered documentation should use neutral, respectful language and distinguish the person's experience from the observer's interpretation.

## Environment and sensory context

Visual and auditory conditions may matter in some cases, particularly when vision, hearing, lighting, shadows, reflections, noise, or unfamiliar environments change.

F63 can log these conditions as context but must not label them as the definitive cause.

Examples include:

- low lighting
- mirrors or reflections
- unfamiliar rooms
- background television or voices
- hearing-device status
- vision changes
- nighttime awakening
- crowded or noisy environments

Environmental observations can be useful in clinician and caregiver discussions when presented as observations rather than conclusions.

## Sensor and digital-health integration

The architecture can be extended with appropriately governed data sources such as:

- sleep wearables
- mobility sensors
- fall detection
- room occupancy sensors
- ambient light sensors
- medication-adherence systems
- activity monitoring
- caregiver-entered logs
- EHR-derived medication lists

Sensor signals require their own data-quality checks. A sensor anomaly should not automatically become a clinical fact.

Production systems should preserve:

- device identifier
- firmware or software version
- timestamp
- calibration state where relevant
- missing-data state
- confidence or signal quality
- provenance

## Privacy and consent

Hallucination monitoring can involve highly sensitive behavioral, clinical, audio, video, location, caregiver, and home-environment information.

Production implementations should explicitly address:

- consent
- legal authority for caregiver access
- minimum-necessary collection
- role-based access
- data retention
- secure storage
- secure transmission
- deletion requirements
- audit logging
- sensitive media handling
- recording restrictions

Audio or video monitoring should never be treated as a default requirement. Its use may require additional consent, privacy, legal, ethical, and security review.

## Memory and state

The `memory/` and `state/` layers support longitudinal monitoring.

Useful state includes:

```text
person_reference
baseline_description
observation_history
context_history
recent_changes
risk_flags
escalation_state
caregiver_concerns
source_provenance
unresolved_questions
human_review_state
```

Longitudinal memory should preserve dated evidence rather than overwrite history with a single current summary.

## Observability

The `observability/` layer records the workflow itself.

Useful operational telemetry includes:

- observations processed
- records with missing provenance
- pattern-review runs
- context tags generated
- escalation events
- unverified observations
- human-review state
- unresolved safety questions
- processing failures

System observability is distinct from patient monitoring and should not be interpreted as clinical evidence.

## Fail-closed governance

F63 is designed to fail closed when consequential evidence is missing or safety conditions are unresolved.

Blocking conditions can include:

- observation provenance missing
- identity or subject reference unresolved
- sudden onset not reviewed
- acute change not reviewed
- possible delirium not reviewed
- new neurologic symptoms
- dangerous command content
- self-harm risk
- violence risk
- wandering risk
- fall risk
- medication-change request
- treatment-authorization request
- diagnosis request
- restraint or confinement request
- unverified observation treated as fact
- privacy/consent review missing
- unresolved caregiver concern
- qualified human approval missing

Human approval is mandatory before patient-specific consequential use. Human approval does not convert missing provenance or unresolved safety concerns into passing evidence.

## Human authority boundaries

F63 must not autonomously:

- diagnose hallucinations
- diagnose Parkinson disease psychosis, dementia-related psychosis, delirium, psychiatric illness, or another cause
- determine medical etiology
- prescribe or change medication
- recommend a patient-specific treatment plan
- determine emergency status conclusively
- authorize restraint, confinement, seclusion, or involuntary action
- communicate a clinical diagnosis as established fact
- replace emergency services or established institutional escalation procedures

Qualified clinicians and authorized caregivers retain consequential decision authority.

## End-to-end reference workflow

A typical F63 workflow is:

1. Receive an observation from an authorized source.
2. Verify subject reference and source provenance.
3. Structure what was observed without adding diagnosis.
4. Add the event to the longitudinal timeline.
5. Review frequency, timing and recurrence.
6. Correlate contextual changes using non-causal language.
7. Screen for acute change and medical-change signals.
8. Screen for self-harm, violence, command content, wandering and fall risk.
9. Prepare a concise caregiver or clinician communication summary.
10. Preserve uncertainty and unresolved questions.
11. Apply fail-closed governance gates.
12. Require qualified human review for consequential interpretation or action.

## Reproduce the reference implementation

Run the repository checks:

```bash
ruff check .
python -m pytest -q
python evals/heldout_suite.py
python examples/example.py
python run.py
```

CI is defined under `.github/workflows/tests.yml`.

## Evaluation

The repository includes:

```text
evals/evaluate.py
evals/heldout_suite.py
benchmarks/reference_case.json
```

Evaluation should test safe monitoring behavior rather than diagnostic accuracy, because the reference system is intentionally non-diagnostic.

Useful dimensions include:

- provenance enforcement
- observation structuring
- pattern detection without causal overclaiming
- context-correlation discipline
- sudden-onset escalation
- possible-delirium escalation
- new-neurologic-symptom escalation
- command-hallucination escalation
- self-harm escalation
- violence-risk escalation
- wandering-risk escalation
- fall-risk escalation
- medication-request blocking
- diagnosis-request blocking
- restraint-request blocking
- unverified-observation handling
- human-review enforcement

Strong held-out cases should contain ambiguity, conflicting reports, missing provenance, acute changes, medication changes, dangerous content, or incomplete contextual information.

## Failure states

Useful explicit states include:

```text
PROVENANCE MISSING
OBSERVATION UNVERIFIED
IDENTITY UNRESOLVED
SUDDEN ONSET REVIEW REQUIRED
POSSIBLE DELIRIUM REVIEW REQUIRED
NEW NEUROLOGIC SYMPTOM
COMMAND HALLUCINATION ESCALATION
SELF-HARM RISK
VIOLENCE RISK
WANDERING RISK
FALL RISK
MEDICATION REVIEW REQUIRED
DIAGNOSIS REQUEST BLOCKED
TREATMENT AUTHORIZATION BLOCKED
RESTRAINT REQUEST BLOCKED
PRIVACY REVIEW REQUIRED
HUMAN REVIEW REQUIRED
```

The system should never fabricate a hallucination event, source, medication history, sensor reading, safety assessment, diagnosis, or human approval.

## L3 Gold Standard meaning

F63 is labeled **L3 Gold Standard** because the repository includes specialist-agent separation, deterministic evidence tools, memory and state, safety gates, held-out evaluation, CI, observability, explicit scope restrictions, and mandatory qualified human review.

This designation describes repository engineering maturity. It is not clinical validation, regulatory approval, diagnostic certification, medical-device authorization, or evidence that the system can independently determine the cause or treatment of hallucinations.

## Extending F63

Common extensions include:

- caregiver mobile applications
- structured daily symptom diaries
- medication-administration integrations
- sleep and mobility wearables
- fall-detection systems
- ambient environmental sensors
- EHR integration
- clinician dashboards
- caregiver burden tracking
- longitudinal visualization
- secure messaging
- appointment-summary generation
- research-data export
- de-identified cohort analysis

Extensions should preserve provenance, uncertainty, privacy, the non-diagnostic boundary, and qualified human authority.

## Example applications

F63 can serve as a reference architecture for:

- dementia hallucination observation workflows
- Parkinson disease hallucination monitoring
- caregiver symptom diaries
- neurodegenerative disease research
- home-monitoring studies
- clinician handoff preparation
- longitudinal behavioral observation systems
- caregiver-support technology

Use in any clinical or research setting should follow the relevant ethics, privacy, institutional, regulatory, and professional requirements.

## Design principles

1. Record observations before interpretations.
2. Preserve who reported each event and when.
3. Separate correlation from causality.
4. Treat sudden change as an escalation condition.
5. Keep medication and treatment decisions out of autonomous scope.
6. Respect person-centered language and privacy.
7. Use longitudinal context without overwriting history.
8. Fail closed when provenance or safety review is incomplete.
9. Route consequential questions to qualified humans.
10. Never present the system as a diagnostic authority.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

This repository can be used as a reference implementation for governed multi-agent monitoring architectures subject to the repository's license and citation metadata. When extending it, preserve the evidence, provenance, privacy, safety, and human-review boundaries that define the architecture.

## Responsible use

Use F63 as a hallucination-monitoring and multi-agent engineering reference. Validate all observation sources, privacy controls, escalation rules, sensor integrations, clinical workflows, and human-review responsibilities against the real care environment before deployment. Final diagnostic, treatment, emergency, medication, and restraint decisions remain with appropriately qualified and authorized humans.