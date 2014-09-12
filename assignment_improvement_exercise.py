#john bain
#variable improvement exercise
#05-09-12

import math

circle_radius = int (input("please enter the radius of the circle: "))

circumfrence = 2* math.pi * circle_radius
final_circumfrence = round(circumfrence,2)

area = math.pi * circle_radius**2
final_area = round(area,2)

print("The circumference of this circle is {0}.".format(final_circumfrence))
print("The area of this circle is {0}.".format(final_area))
