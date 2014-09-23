#Marc Gonzalez
#23/09/14
#assignment statement spotr check 1.1

pool_width = float(input("please enter the width of your pool: "))

pool_depth = float(input("please enter the depth of your pool: "))

pool_length = float(input("please enter the length of your pool: "))

main_volume = pool_length * pool_width * pool_depth

circle_radius = pool_width / 2

circle_area = 3.14 * (circle_radius * circle_radius)

half_circle_volume = (circle_area / 2) * pool_depth

pool_volume = main_volume + half_circle_volume

print("your pool volume is {0} ".format(pool_volume))
