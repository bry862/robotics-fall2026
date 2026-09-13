# Mission 1

## Command Path Explanation

Student_cmd_vel is the intended input. But we need to verify if that intended input is appropriate. Our safety check will determine whether it is and make a final decision, which is the cmd_vel. 

## Graph Explanation

A ROS 2 graph shows how different running components interact with each other. 

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found some distances to be infinite. I assume that it is because nothing was found in that direction. I would say this is outside of the robot, while the numerical measurements are taken within the robot.

## Tools Explanation

Gazebo is responsible for simulating the robot. RViz is responsible for displaying the data from the sensors of the robot in Gazebo. 
