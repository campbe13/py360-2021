# find the root of a quadratic equation
# ask for input a b c
# 2022-02-24
# pmcampbell
# 2 roots    x^2 - 5x + 6 = 0 roots 3 & 2
# 1 root     x^2 + 3x - 18 = 0  root 1
# irrational x^2 + 6x + 11 = 0   irrational

import math

a = float(input("a "))
b = float(input("b "))
c = float(input("c "))

discriminant = (b*b) - (4*a*c)

if discriminant == 0:
    print("roots are real, equal")
    root = -b / (2*a)
    print(f"root {root}")
elif discriminant > 0:
    print("roots are real, 2 roots")
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"roots {root1} and {root2}")
else:
    print("roots are not real, complex")