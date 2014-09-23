#Marc Gonzalez
#23/09/14
#assignment statement spot check 2.2

opposite_weight = int(input("please enter the weight on the other side of the scale: "))

number_100 = opposite_weight // 100

remainder_100 = opposite_weight % 100

number_50 = remainder_100 // 50

remainder_50 = remainder_100 % 50

number_10 = remainder_50 // 10

remainder_10 = remainder_50 % 10

number_5 = remainder_10 // 5

remainder_5 = remainder_10 % 5

number_2 = remainder_5 // 2

remainder_2 = remainder_5 % 2

number_1 = remainder_2

print(" the number of weights needed to balance are {0} 100g weights, {1} 50g weights, {2} 10g weights, {3} 5g weights, {4} 2g weights, {5} 1g weights".format(number_100, number_50, number_10, number_5, number_2, number_1))
