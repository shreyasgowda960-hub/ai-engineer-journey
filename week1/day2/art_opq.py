#Find Area of Circle
#A=pi*r^2

import math

pi=math.pi

print(pi)
pi=round(pi,2)

radius=float(input("Enter radius of circle: "))

Area_Circle=pi * round((pow(radius,2)))

print(f"Area of Circle is {Area_Circle}cm^2")
        