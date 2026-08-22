from __future__ import annotations

from typing import Any


class PatternReviewAgent:
    name = "pattern_review"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent": self.name,
            "patterns": list(context.get("patterns", [])),
            "uncertainty_noted": True,
        }
