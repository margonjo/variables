#Marc Gonzalez
#14/08/14
#R'n'R task 6.3

print("I will calculate the volume of water required to fill your swimming pool up")

print("But first I need the following measurements...")

pool_length = float(input("Enter your pool length in meters: "))

pool_width = float(input("Enter your pool width in meters: "))

pool_depth = float(input("Enter your pool depth in meters: "))

pool_volume = pool_length * pool_width * pool_depth

print("The volume of water required is {0} m cubed".format(pool_volume))
