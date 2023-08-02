# EXERCISE 2 :
# bmi calculator :
# your output should not be in decimal.

# DON'T CHANGE THE CODE BELOW :
height = input("Enter your height in (meters) : ")
weight = input("Enter your weight in (Kg) : ")


# WRITE YOUR CODE HERE :
bmi = float(weight) / float(height) ** 2

print("Your BMI is", int(bmi))
