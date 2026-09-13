# Mission 2

## Predictions

{'straight': 'I predict that the robot will finish 0.45 meters away from the starting point', 'rotation': 'I predict the robots position will be the same, but its direction will chnage 1.50 radians to the left from its starting position. ', 'curve': 'I predict that the shape to be a semi-circle type of shape, as the robot turns right because the turning speed is negative. ', 'curve_modified': 'This curve should be sharper and the end point deeper, because the angle of turn is much higher than before, and the robot is moving faster.'}

## Prediction Locks

{'straight': '2026-09-11T20:52:29.080240+00:00', 'rotation': '2026-09-11T20:57:20.181152+00:00', 'curve': '2026-09-11T21:00:47.517908+00:00', 'curve_modified': '2026-09-11T21:04:24.636754+00:00'}

## Motion Comparison

I chose the last trial, where I chose my own rotation and linear movement. I imagines the robot would turn about 180 degrees, and it came close as the direction chnage was 176 degrees. I though the tobot would travel more, since the cirve was sharper, but the start to end distance was only 0.374 meters

## Measurement Explanation

For the cirved path, I believ the start to end distance is less because the estimated meassurement does nto account for the turning. That is why on the other trials with no rotation the estimated traveled path is the same as the start to end distance. 

## Safety Explanation

The command guard checks if the incoming commands are appropriate. 
The final zero command stops the robot once it reaches the goal.
The timeout is needed if we ever lose connection with the command center. 

## Modified Settings

{'linear_x': 0.15, 'angular_z': 0.8, 'duration': 4.0}
