# EXERCISE 2 :
# check the number entered by the user is prime or not.


# WRITE YOUR CODE HERE :
def prime_checker(number):
    is_prime = True

    for nums in range(2, number):
        if number % nums == 0:
            is_prime = False
    if is_prime == True:
        print("Prime")
    else:
        print("Not Prime")


# DON'T CHANGE THE CODE BELOW :
n = int(input("Check this number : "))
prime_checker(number=n)
