# Week 6: SLAM and Mapping

- email: brayhan.morrobel32@myhunter.cuny.edu
- name: Brayhan Morrobel

## final.course_reflection

This lab made me think about, regarding my own interest, about how robotics combines different areas of engineering and computing to solve problems. When I explored the TurtleBot3 House world, I saw how the robot uses its movement and LiDAR observations to build a map of its surroundings. Exploring the same world twice also showed me that changing the exploration strategy can affect the results. This made me more interested in understanding how robots make decisions and interact with their environments. The experience also reminded me of Proverbs 16:3: “Commit to the LORD whatever you do, and he will establish your plans”,  I understand this verse as a reminder to approach my work with purpose and put effort into what I am trying to accomplish. In engineering, things do not always work as expected, so patience and a willingness to learn from mistakes are important. I would like to continue working on similar projects because they allow me to apply what I learn instead of only studying the concepts. I also believe that engineering should be about more than making technology work. We should consider how people will use it, whether it is safe, and how it can benefit others. Overall, this activity helped me see that robotics requires experimentation, problem-solving, and continuous improvement. It also reminded me that learning takes time and that mstakes can help me understand a system better. I want to keep developing my technical skills and use them in ways that can make a positive difference. As well as, I shoudl dedicate my work towards doing good, and using my time to prodice good work. 

## final.synthesis

After exploring the house with TutrleBot3 twice,  both exploration gave me different numerical results via a JSON file and visual results via a map. The first exploration lasted 10 minutes using the explore strategy and got a quality score of 80.8. The map showed 63.38% of the area as known, with only 36.62% remaining unknown. It also had a low speckle fraction of 1.68%, meaning there were fewer isolated occupied cells. A good score overall. The second exploration lasted 8 minutes using the along_walls strategy and got a quality score of 58.8. Even though this map had larger dimensions, only 39.57% of the area was known, while 60.43% remained unknown. Its speckle fraction also increased to 8.61%, and the number of occupied components went from 55 to 274. A bad score compared to the previous attempt. But still beter than I thought. Based on these results, the first exploration created a more complete and consistent map. This shows that a larger map does not always mean better results. Motion estimates help the robot track its movement, while LiDAR observations detect obstacles and open spaces. Together, they help the robot build an occupancy-grid map. Comparing both explorations helped me understand how different strategies and exploration times can affect map quality. I confirmed that the wider the range of a scanner, the better explorations will be. 

## mission_1.drift_and_revisit

When I visited aread that I had alrady been in, nothign changed. Although, sometimes when I walked away, the walls behid me would change. s

## mission_1.limitations

There is a table. It was poorly mapped. In my screen shot it is behind me. It was poorly mapped because the table is abve the robots scanners. 

## mission_1.route.original_prediction

I will visit the room in (2,2), I think the weakness will be in the scan faraway.

## mission_1.route.prediction_draft

I will visit around the house, then go room by room. The coverage will be limited in the range of the radars/ Hwo fat out meassuremtns will reach, as well as objects above the robot (like tables).

## mission_2.comparison

Map one took 10  minutes, and map two took 8 minutes. I  thought map two would come out worse, but it actually shaded well. I did make a mistake, there is a room i thought i went all around the wall, but I did not. Map 1 was better, as it filled out the house more. 

## mission_2.map_choice

I would definitely trust map one more. It is more shaded in. Map two also has a duplicated room at the bottom right. This proves we should spin around inside the room rather than along the walls. 

## mission_2.strategy.original_prediction

i will dirve round the inside of the house, along the inner walls.

## mission_2.strategy.prediction_draft

i will dirve round the inside of the house, along the inner walls. 
