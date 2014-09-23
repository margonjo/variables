#Marc Gonzalez
#23/09/14
#exercise 3.1

length = float(input("please enter the length of you garden: "))

width = float(input("please enter the width of your garden: "))

grass_length = length - 1

grass_width = width -1

area = grass_length * grass_width

total = area * 10

print(" The area of your lawn in {0}, meaning that to turf you lawn it will cost £{1}".format(area, total))
