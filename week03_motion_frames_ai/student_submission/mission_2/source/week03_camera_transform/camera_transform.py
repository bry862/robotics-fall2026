# camera_transform.py

import tf2_geometry_msgs  # Registers PointStamped conversions with tf2_ros.
import tf2_ros

from geometry_msgs.msg import PointStamped
from rclpy.duration import Duration


def transform_camera_point(
    tf_buffer: tf2_ros.Buffer,
    point: PointStamped,
) -> PointStamped | None:
    """Transform a hall_camera point into base_link at its observation time."""
    if point.header.frame_id != "hall_camera":
        raise ValueError(
            "Expected point.header.frame_id to be 'hall_camera', "
            f"got {point.header.frame_id!r}"
        )

    try:
        # `point` includes its original timestamp. Buffer.transform uses that
        # stamp to obtain the matching hall_camera -> base_link transform.
        return tf_buffer.transform(
            point,
            "base_link",
            timeout=Duration(seconds=0.2),
        )
    except tf2_ros.TransformException:
        return None