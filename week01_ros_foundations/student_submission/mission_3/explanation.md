# Mission 3

## Data To Command

My two functions turn a list of LiDAR distances into move or stop commands by checking the entries of that list. We have different if statements to handle different cases, such as missing distance information (where we stop the robot). 

## Missing Data Safety

The robot stops because there is a lack of information, and to have a fail-safe system, we go to a "safer" state, which is a stop. We need to figure out why information is missing. 

## System Layers

The three components work together to instruct the robot. Command guard reads the obstacles in front, the ROS node works with the decision functions to decide on a velocity for the robot. 
