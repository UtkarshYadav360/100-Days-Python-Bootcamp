# EXERCSIE 4 :

# TO DO :
# 1) print first 100 natural numbers
# 2) when number is divisible by 3 print "FIZZ"
# 3) whn number is divisibe by 5 print "BUZZ"
# 4) when number is divisible by 3 and 5 both print "FIZZ BUZZ"

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FIZZ BUZZ")
    elif number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0:
        print("BUZZ")
    else:
        print(number)
