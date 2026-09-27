# Mission 2

## Frame Context

The fixed camera trasnform changes as the robot moves becasue the robot moves around the camera. 

## Improved Changes

Well first, we are givign the LMM a more norrowed task, where it only needs to complete one function. We also add specifc requieremts for values, such as "Accept only a point whose header.frame_id is hall_camera", and fall back options. 

## Initial Analysis

From inspecting the code provided by ChatGPT, I can see that it assumed the header.frame_id is the cameras optical frame. Also, that the x,y , z values use the camera optical-frame convention. + x means right, positive y is down and positive z is forward. 

## Initial Output

Use a PointStamped: its header.frame_id must be the camera optical frame, and its timestamp must match the image/depth detection time.
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
For example, a detected point must look like this before publishing:
point = PointStamped()
point.header.stamp = image_msg.header.stamp
point.header.frame_id = "camera_color_optical_frame"
point.point.x = 2.0
point.point.y = 0.3
point.point.z = 0.0
This requires a valid TF chain such as:
base_link → camera_link → camera_color_optical_frame
Also, a camera pixel \((u,v)\) alone is not a 3D point—you need depth or another method to obtain camera-frame \(x,y,z\) first. TF2 transforms the stamped point into the requested target frame. ROS TF2 geometry-message reference

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Source

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

## Live Pending

True

## Snapshot

{'captured_at': '2026-09-26T21:49:12.346392+00:00', 'description': 'Instructor-defined frame geometry. No live ROS transforms were measured.', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'source': 'reference', 'transforms': {'base_scan_to_base_link': {'translation': {'x': 0.2, 'y': 0.0, 'z': 0.14}, 'yaw': 0.0}, 'hall_camera_to_base_link': {'translation': {'x': -1.5, 'y': 0.5, 'z': 1.2}, 'yaw': -1.5707963267948966}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': 3.141592653589793}}}

## Synthesis

The forst AI script did nto verify the camera frame handled the points observation timestamp. While in the improved response specifically transformed a PointStamped from hall camera to base link using the points timestamp, and it returned None if the trasnform was unavailable. Using the wrong transfrom coudl place a detected person at the wrogn position. When transfrom data is unavailable, it shoudl fail sefely; it should stop. 

## Live Issue

I ran both commands from above. I get two error like messages: 
source differs from original true and passed: false. 
