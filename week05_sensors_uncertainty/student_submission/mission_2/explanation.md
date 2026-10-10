# Mission 2

## comparison

For my 3 windows in moving aveage, the respnse delay was 1.3. The max errors where 1.087202950738813, 1.1598219983578608, and 1.21417264770851

## fusion_choice

I did three test,  with weights 0.25, 0.50, and 0.75. The lower the weight the lower the response the delay. We can see sensor A's noisy characteristic as we increase the weight of A. But because sensor B is steady, we see that we are always ontop of the truth.

## manual_average

4.167

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

These values will decrease the error because our N is high, and thus we have more sample values. 

## responsiveness

A delay could mean a late stop for a nearby person. Smoothing reffers to having less noise, mening less random inputs. For example, when calculating the median, N of 15 gave 0.02 lower max error. Responsiveness is how quick sensor data is reacted to. Note that the higher the sensor weighr, the less the delay was. 

## selected

9
