# Mission 3

## Assistive.prediction_draft

If we need to navigate through many people. This will be challenged. 

## Warehouse.prediction_draft

Stocking, for example, will challenge this policy, as the stoping threshold is too high for aproaching a shelf. 

## context_comparison

I will test two different policies, and between them will differ Stopping threshold, Caution margin, and Weight on Sensor A. The forst one will have lower values for all three of those fields. This one resulted with a lower inecessary stop rate (0.02). My second policy here will have ghigher values for those three fields, and it resulted in a higher unecessary stop rate of 0.081. I hypothize this occured because of the higher caution manrgin, which could cause a stop earlier than needed. 

## error_costs

In stationary danger, the robot faces the danger
In near threashold, the person or item near faces the danger. 
In fast approach and receeding, the person and or object also faces the danger, as we are getting too close. 


## limitations

These seven test establish the effects of the wieght of the sensor, which seem to influence the values a lot. They do not establish context. We do not know if when the assistive robot stopped, what it was doing, so we could know if the stop was needed or not. 
