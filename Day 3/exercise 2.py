# EXERCISE 2 :
# calculate user's BMI and give interpretations to them.

# DON'T CHANGE THE CODE BELOW :
height = float(input("What is your height in (meters)? "))
weight = float(input("What is your weight in (Kg)? "))


# WRITE YOUR CODE HERE :
bmi = round(weight / (height**2))


if bmi < 18.5:
    print(f"Your BMI is {bmi} and your are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are over weight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are obese.")
elif bmi > 35:
    print(f"Your bmi is {bmi} and you are clinically obese.")
