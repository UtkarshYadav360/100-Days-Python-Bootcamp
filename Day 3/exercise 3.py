# EXERCISE 3 :
# check the year entered by the user is a leap year or not

# DON'T CHANGE THE CODE BELOW :
year = int(input("Which year do you want to check? "))


# WRITE YOUR CODE HERE :
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
