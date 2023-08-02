# round() function :
print(round(99.999))
print(round(23.6666, 3))


# f strings :
name = "Anglo"
age = 47
gender = "Male"
print(f"Hello {name} your age is {age} and you are {gender}.")


# updated version of EXERCISE 2 :
height = float(input("What is your height in (meters)? "))
weight = float(input("What is your weight in (Kg)? "))

bmi = weight / (height**2)
print(f"Your BMI is {round(bmi)}")
