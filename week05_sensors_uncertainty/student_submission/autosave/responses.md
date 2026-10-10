# Week 5: Sensors, Noise, and Uncertainty

- name: Brayhan Morrobel
- email: Brayhan.morrobel32@hunter.cuny.edu
- course_id: 24243032

## concepts.observation

Increasing noise increased the number of readings. Increasing bias only chnaged the truth. 

## final.course_reflection

Before this activity, I mostly thought about robotics in terms of building a robot and programming it to perform certain tasks. However, I learned that there is a lot more going on behind the scenes. Robots need to collect information from their surroundings, and that information is not always accurate. This made me realize how important it is to process sensor readings before using them to make decisions. I found the different filtering methods interesting because they showed me that there are several ways to handle noisy measurements. For example, a moving average uses recent readings to smooth out changes, while a median filter can help deal with an unusual reading. I also learned about sensor fusion, which combines estimates from different sources. Understanding RMSE helped me see how we can measure the accuracy of these methods instead of just guessing which one works best. This activity made me more interested in learning how robots use sensor data to interact with the world. I liked being able to experiment with different options and think about how the results would affect a robot's behavior. It also showed me that concepts from statistics and mathematics have practical uses in engineering. Another thing I thought about was safety. If a robot receives an incorrect measurement, it could make the wrong decision, especially if it is moving near people or obstacles. This is why engineers need to think about reliability and the possible consequences of their designs, not just whether the technology works. Overall, I learned that even a small part of a robotic system, such as processing a distance measurement, can have a significant impact on its performance. I would like to explore more robotics projects in the future and get a better understanding of how these systems work in real world situations.

## final.synthesis

Across the three missions, I learned that reliable robotics depends on understanding sensor measurements, choosing appropriate estimation methods, and considering the environment where a robot will operate. These factors are connected because inaccurate measurements can lead to poor estimates and, ultimately, incorrect decisions. In mission one, I saw that readings could have noise, that could affect our meassurements. This showed me that a measurement should not automatically be treated as the true value. For example, the mean was 2, but the readings ranged from 1.8 to 2.4. In mission 2, I examined how estimation methods can improve the usefulness of sensor data. For example, increasing the weight of sensor A from 0.5 to 0.75, the response delay droped from 1.5 to 0.3 Mission 3 connected these concepts to deployment context by emphasizing that a robot must operate reliably under real conditions. Overall, the three missions demonstrated that successful robotics requires more than collecting data.

## mission_1.bias

0.03

## mission_1.bias_vs_variance

Variance describes spread, which could be caused by incorrect meassuremnts. Bias hints towards a sensor malfunction. 

## mission_1.dropouts

9

## mission_1.mean

2

## mission_1.median

2

## mission_1.more_samples

No, bcause the issue is that it has too much spread. The variance is 0.01, and we want it as close to 0 as possible

## mission_1.outliers

4

## mission_1.prediction

The mean will achieve this. Because a noisy sensor will have many scattered random meassurements throughout, while a consistently biased sensor will be around the same meassurements.

## mission_1.prediction_draft

The mean will achieve this. Because a noisy sensor will have many scattered random meassurements throughout, while a consistently biased sensor will be around the same meassurements. 

## mission_1.profile

noisy

## mission_1.robot_consequence

For example, say we want to count how many people are in a room, because the spread is too wide, we will get the incorrect number. Say someone needs this information, to take attendance for example, the attendance will be incorrect. 

## mission_1.variance

0.04043308518538645

## mission_2.comparison

For my 3 windows in moving aveage, the respnse delay was 1.3. The max errors where 1.087202950738813, 1.1598219983578608, and 1.21417264770851

## mission_2.fusion_choice

I did three test,  with weights 0.25, 0.50, and 0.75. The lower the weight the lower the response the delay. We can see sensor A's noisy characteristic as we increase the weight of A. But because sensor B is steady, we see that we are always ontop of the truth.

## mission_2.manual_average

4.167

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

These values will decrease the error because our N is high, and thus we have more sample values. 

## mission_2.responsiveness

A delay could mean a late stop for a nearby person. Smoothing reffers to having less noise, mening less random inputs. For example, when calculating the median, N of 15 gave 0.02 lower max error. Responsiveness is how quick sensor data is reacted to. Note that the higher the sensor weighr, the less the delay was. 

## mission_2.selected

9

## mission_3.Assistive.prediction_draft

If we need to navigate through many people. This will be challenged. 

## mission_3.Warehouse.prediction_draft

Stocking, for example, will challenge this policy, as the stoping threshold is too high for aproaching a shelf. 

## mission_3.context_comparison

I will test two different policies, and between them will differ Stopping threshold, Caution margin, and Weight on Sensor A. The forst one will have lower values for all three of those fields. This one resulted with a lower inecessary stop rate (0.02). My second policy here will have ghigher values for those three fields, and it resulted in a higher unecessary stop rate of 0.081. I hypothize this occured because of the higher caution manrgin, which could cause a stop earlier than needed. 

## mission_3.error_costs

In stationary danger, the robot faces the danger
In near threashold, the person or item near faces the danger. 
In fast approach and receeding, the person and or object also faces the danger, as we are getting too close. 


## mission_3.limitations

These seven test establish the effects of the wieght of the sensor, which seem to influence the values a lot. They do not establish context. We do not know if when the assistive robot stopped, what it was doing, so we could know if the stop was needed or not. 
