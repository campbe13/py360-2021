# lab exercise
# create calculators for perimiter/tip/volum& Surface
# user input for values as needed
# 2022-01-27
# pmcampbell

# Perimeter Calculator​
'''
Write the code that asks the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. ​

write down test data + calculate results  & run your code a few times with that data
Test data:
w 5, l 7 perimiter 24
w 3, l 17 perimiter 40
'''
print("\nperimiter calculator")

width = int(input("enter width: "))
length = int(input("enter length: "))
perimeter = 2*width + 2*length
print(f'A rectangle of length {length} width {width} has a perimeter of {perimeter}')

# Restaurant Tip Calculator ​
'''
Write the code that asks the user to enter the price of a meal at a restaurant (remember those  ?? ). The program calculates the amount of the tip to be paid at 18%. The tip and total price are then displayed separately.​

write down test data + calculate results  & run your code a few times with that data
Test data:
meal 12.44 with tip 14.6792
meal 45.51 with tip 53.7018
'''
print("\ntip  calculator")

meal_cost = float(input("enter the cost of your meal: "))
tip = meal_cost * 0.18
meal_plus_tip = meal_cost  + tip
perimeter = 2*width + 2*length
print(f'A meal costing {meal_cost} with an 18% tip comes to  {meal_plus_tip}')
# using a formatter  ( don't lose the extra preciIson)
print(f'A meal costing {meal_cost} with an 18% tip comes to  {meal_plus_tip:.2f}')
# rounding
meal_plus_tip = round(meal_plus_tip, 2)
print(f'A meal costing {meal_cost} with an 18% tip comes to  {meal_plus_tip}')

# Volume and Surface Area Calculator ​
''''
Write the code that asks the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. ​

write down test data + calculate results  & run your code a few times with that data
ref https://keisan.casio.com/exec/system/1223336888
Test data:
l = 5 w = 9 h = 7 volume 315 surface area: 286
l = 10 w = 3 h = 77 volume 2310 surface area: 2062
'''
print("\ncuboid vol/surface area calculator")

length = float(input("enter length: "))
width = float(input("enter width: "))
height = float(input("enter height: "))

surface_area = 2 * (length*width + height*length + height*width)
volume  = width * length * height

print(f'A cuboid of length {length} width {width} and height {height}')
print(f'Has a surface area of {surface_area}')
print(f'Has a volume of {volume}')