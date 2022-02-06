# calculate distance to sea bed
# pmcampbell
# 2022-02-06
# test data: 
# length = 30 m 
# angle = 51 degrees 
# answer: 18.88 m
# length = 100 m 
# angle = 31 degrees 
# answer: 85.72 m
# for others use https://www.calculator.net/right-triangle-calculator.html
import math

# code here

cable_length = float(input("What is your anchor cable length: "))
cable_angle = float(input("What is the angle between your anchor cable & perpindicular: "))

# given the angle seen by sailors 
# cable_ angle + theta = 90 
# calculate theta  (seabed & cable angle)
theta = 90 -  cable_angle
print (f'seabed & cable angle is {theta}')

# sine(theta)   =   opposite / hypotenuse
# opposite = sine(theta)  * hypotenuse
# opposite = sine(theta)  * cable_length
distance_to_seabed = math.sin(theta) * cable_length

print (f'(wrong)distance to seabed {distance_to_seabed:.2f}')

# problem!! wrong answer
# look at math.sin it takes radians as an argument
`# need to convert is there a function ??? yes !!!
# https://docs.python.org/3/library/math.html#angular-conversion
theta_in_radians = math.radians(theta)
distance_to_seabed = math.sin(theta_in_radians) * cable_length

print (f'distance to seabed {distance_to_seabed:.2f}')
