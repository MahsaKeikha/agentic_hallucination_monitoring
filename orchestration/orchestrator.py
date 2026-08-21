ORDER=["observation_intake","pattern_review","context_correlation","caregiver_communication","risk_escalation","human_review"]
def orchestrate(context): return {"workflow":ORDER,"context":context,"status":"review_required"}
