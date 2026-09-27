import os
import unittest
import math

from week03_pattern.pattern import build_pattern


class MyPatternTests(unittest.TestCase):

    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])

        self.assertEqual(len(segments), 4)

        expected_radius = 0.30
        expected_angle = math.pi / 4

        for segment in segments:
            radius = abs(segment.linear_x / segment.angular_z)
            angle = abs(segment.angular_z * segment.duration)

            self.assertAlmostEqual(radius, expected_radius, delta=0.02)
            self.assertAlmostEqual(angle, expected_angle, delta=0.04)

    def test_my_pattern_order(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])

        # my order: +45°, -45°, +45°, -45°
        self.assertGreater(segments[0].angular_z, 0)
        self.assertLess(segments[1].angular_z, 0)
        self.assertGreater(segments[2].angular_z, 0)
        self.assertLess(segments[3].angular_z, 0)