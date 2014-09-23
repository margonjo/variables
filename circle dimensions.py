#Marc Gonzalez
#23/09/14
#exercise 4.1

import math

radius = float(input("please enter your circle radius: "))

area = math.pi * (radius *radius)
average_area = round(area, 2)

circumfrence = 2 * math.pi * radius
average_circumfrence = round(circumfrence, 2)

print(" your circle area is {0}, your circle circumfrence is {1} ".format(average_area, average_circumfrence))
