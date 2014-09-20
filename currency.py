#Marc Gonzalez
#18/9/14
#Curency exchange

total = int(input("Please enter the amount of money you wish to convert: "))

amount_20 = total // 20

remainder_20 = total % 20

amount_10 = remainder_20 // 10

remainder_10 = remainder_20 % 10

amount_5 =  remainder_10 // 5

remainder_5 = remainder_10 % 5

amount_2 = remainder_5 // 2

remainder_2 = remainder_5 % 2

amount_1 = remainder_2

print(" The minimum change needed is {0} £20 notes, {1} £10 notes, {2} £5 notes, {3} £2 coins, {4} £1 coins".format(amount_20, amount_10, amount_5, amount_2, amount_1))
            

        
                  
