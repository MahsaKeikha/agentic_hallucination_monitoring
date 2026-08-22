from __future__ import annotations

from typing import Any


class ContextCorrelationAgent:
    name = "context_correlation"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent": self.name,
            "context_factors": list(context.get("context_factors", [])),
            "medical_change_screened": bool(context.get("medical_change_screened", False)),
        }
