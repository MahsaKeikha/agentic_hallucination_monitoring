from __future__ import annotations

from typing import Any


class CaregiverCommunicationAgent:
    name = "caregiver_communication"

    def run(self, context: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent": self.name,
            "caregiver_concerns": list(context.get("caregiver_concerns", [])),
            "communication_brief_required": True,
        }
