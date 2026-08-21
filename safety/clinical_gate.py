def clinical_gate(context): return {"allowed": not any(k in context for k in ["diagnosis","prescription"]), "requires_human_review": True}
