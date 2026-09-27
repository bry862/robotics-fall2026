"""AI-assisted motion pattern implementation.

Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by ``build_pattern``.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Segment:
    linear_x: float
    angular_z: float
    duration: float

def build_pattern(pattern_name: str) -> list[Segment]:
    """Return ordered, bounded motion segments for the assigned pattern.

    Supported assignments are ``rounded_rectangle``, ``l_path``, and
    ``alternating_arcs``. Do not include the final stop; the ROS wrapper always
    publishes it and the evaluator verifies it.
    """

    if pattern_name == "alternating_arcs":
        linear_x = 0.20
        angular_z = linear_x / 0.30
        duration = (3.141592653589793 / 4) / angular_z

        return [
            Segment(linear_x, +angular_z, duration),
            Segment(linear_x, -angular_z, duration),
            Segment(linear_x, +angular_z, duration),
            Segment(linear_x, -angular_z, duration),
        ]

    raise ValueError(f"Unknown pattern name: {pattern_name}")
