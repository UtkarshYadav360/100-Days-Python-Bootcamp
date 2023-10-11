# Raising own Exceptions :

height = float(input("Enter your height in meters : "))
weight = int(input("Enter your weight in Kg : "))
bmi = weight / (height**2)

if height > 3:
    # raise ValueError
    raise ValueError("Human height should not be over 3 meters.")

print(bmi)
