# EXERCSIE 3 :
# print the sum of all even numbers lies between first 100 natural numbers.

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)
