from __future__ import annotations

from typing import Any


class ObservationIntakeAgent:
    name = "observation_intake"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent": self.name,
            "observations": list(context.get("observations", [])),
            "source_verified": bool(context.get("observation_source_verified", False)),
        }
