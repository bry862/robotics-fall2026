# Mission 3

## Specification

Start, turn + 45 dgerees, turn +45 degrees, turn -45 degrees, turn -45 degrees, finsih (original position)

## Saved Specification

Start, turn + 45 dgerees, turn +45 degrees, turn -45 degrees, turn -45 degrees, finsih (original position)

## Assigned Pattern

alternating_arcs

## Original Prompt

Now lets work on this:
This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'alternating_arcs' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.

The turning arcs is this:
Start, turn + 45 dgerees, turn +45 degrees, turn -45 degrees, turn -45 degrees, finsih (original position), following these rules: 
Your pattern: alternating arcs. Four forward arcs: turn +45°, -45°, +45°, -45°, each of radius 0.30 m. Finish facing the initial direction.

And the class and function  is here:
"""AI-assisted motion pattern implementation.
Preserve the original AI response in Streamlit. Review it, then implement a safe
version here. The node accepts only segments returned by \`\`build_pattern\`\`.
"""
from \_\_future\_\_ import annotations
from dataclasses import dataclass
@dataclass(*frozen*=True)
*class* Segment:

```
linear_x: *float*

angular_z: *float*

duration: *float*
```

*def* build_pattern(*pattern_name*: *str*) -> list[Segment]:

```
"""Return ordered, bounded motion segments for the assigned pattern.

Supported assignments are \`\`rounded_rectangle\`\`, \`\`l_path\`\`, and

\`\`alternating_arcs\`\`. Do not include the final stop; the ROS wrapper always

publishes it and the evaluator verifies it.

"""

raise *NotImplementedError*("Mission 3: review the AI output and implement your assigned pattern")
```

## Original Output

Yes. We can implement this directly from the geometry.

The key relationship for a constant-radius arc is:

$$ r = \frac{v}{|\omega|} $$

You need:

radius = 0.30 m
each turn = 45° = π/4 radians
forward motion throughout
signs: +, -, +, -
final heading = initial heading
linear_x ≤ 0.22 m/s
angular_z ≤ 0.80 rad/s
no final stop in build_pattern()
Choose safe values

Let's use:

linear_x = 0.20
angular_z = 0.20 / 0.30

Therefore:

linear_x = 0.20 m/s
angular_z = ±0.6666667 rad/s

The radius is exactly:

$$ r = \frac{0.20}{0.6666667} = 0.30\text{ m} $$

For a 45° arc:

$$ t = \frac{\pi/4}{0.6666667} \approx 1.1781\text{ s} $$

So each segment is about 1.18 seconds.

Four segments give about:

$$ 4(1.1781) \approx 4.71\text{ s} $$

which is well below the 60-second total limit.

Implementation

Replace only the raise NotImplementedError(...) with:

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
Why this satisfies the specification
Segment	Linear velocity	Angular velocity	Turn
1	0.20 m/s	+0.667 rad/s	+45°
2	0.20 m/s	−0.667 rad/s	−45°
3	0.20 m/s	+0.667 rad/s	+45°
4	0.20 m/s	−0.667 rad/s	−45°

The positive/negative angular velocities cancel:

$$ +45^\circ-45^\circ+45^\circ-45^\circ=0^\circ $$

so the robot finishes with the same heading it started with.

One important correction to your earlier description: the specification says "Finish facing the initial direction," not necessarily "finish at the original position." The four arcs return the robot's orientation, but that does not by itself mean the robot returns to its starting (x,y) position.

Tests I'd run

Before running the course tests, I'd verify:

segments = build_pattern("alternating_arcs")

assert len(segments) == 4
assert all(abs(s.linear_x) <= 0.22 for s in segments)
assert all(abs(s.angular_z) <= 0.80 for s in segments)
assert all(s.duration <= 30.0 for s in segments)
assert sum(s.duration for s in segments) <= 60.0

assert [s.angular_z > 0 for s in segments] == [True, False, True, False]

assert all(abs(s.linear_x / abs(s.angular_z) - 0.30) < 1e-9
           for s in segments)

assert build_pattern("something_invalid")  # should instead raise ValueError

For that last test, you'd actually use pytest.raises(ValueError) rather than the assertion shown.

One thing I would check before you paste this in: if the starter file already imports math, use math.pi instead of the literal 3.141592653589793. If it doesn't, adding import math would be reasonable, but since the instruction says implement only build_pattern, the version above avoids modifying anything else.

## Original Source

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

## Assumptions

The AI assumed the motion is describes using ROS2 geometry_msgs/msg/Twist, where linear_x is measured in meters per second (m/s) and angular_z is measured in radians per second (rad/s).

## Problems

I checked that the proposed velocities stayed within the required limits of 0.22 m/s and 0.80 rad/s. The proposed values were approximately 0.20 m/s and ±0.667 rad/s, so they are within the limits.

## Test Plan

Pattern: Run the alternating_arcs pattern and observe the robot's motion. Expected result: +45° → -45° → +45° → -45°


## Modifications

Segment(linear_x=0.15, angular_z=0.50, duration=1.571), Segment(linear_x=0.15, angular_z=-0.50, duration=1.571), Segment(linear_x=0.15, angular_z=0.50, duration=1.571), Segment(linear_x=0.15, angular_z=-0.50, duration=1.571)

## Live Pending

False

## Evidence Analysis

The important tests establish that the the amgular and linear speeds produce valid movements, as our robot executed them sucessfully. They do not establish a correct output of "Facing oyr original direction". To achieve that goal, we need to account for the fact that each time we turn, simply turing the opposite way wont bring us to face the same way.  

## Ai Disclosure

I used ChatGPT for the parts that asked for AI, I verified all the code, and its overall intentions. I also used it to set up the lab, as some parts where confusing. 
