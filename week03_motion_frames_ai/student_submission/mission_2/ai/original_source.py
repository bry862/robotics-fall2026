#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

import tf2_ros
import tf2_geometry_msgs  # Registers geometry message transforms.
from geometry_msgs.msg import PointStamped


class HallwayPointTransformer(Node):
    def __init__(self):
        super().__init__("hallway_point_transformer")

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(
            self.tf_buffer, self
        )

        # Assumes another node publishes a 3D detected point in the camera frame.
        self.subscription = self.create_subscription(
            PointStamped,
            "/hallway_detection_point",
            self.point_callback,
            10,
        )

    def point_callback(self, point_in_camera: PointStamped):
        try:
            point_in_base = self.tf_buffer.transform(
                point_in_camera,
                "base_link",
                timeout=Duration(seconds=0.2),
            )

            self.get_logger().info(
                "Point in base_link: "
                f"x={point_in_base.point.x:.3f}, "
                f"y={point_in_base.point.y:.3f}, "
                f"z={point_in_base.point.z:.3f} m"
            )

        except tf2_ros.TransformException as error:
            self.get_logger().warn(
                f"Could not transform point to base_link: {error}"
            )


def main():
    rclpy.init()
    node = HallwayPointTransformer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()