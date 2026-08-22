from __future__ import annotations

from typing import Any


class HumanReviewAgent:
    name = "human_review"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        approved = bool(context.get("human_approval", False))
        return {
            "agent": self.name,
            "requires_human_review": True,
            "approved": approved,
        }
