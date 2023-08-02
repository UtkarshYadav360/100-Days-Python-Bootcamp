# if - elif - else statements :

height = float(input("What is your height in (cm)? "))
if height > 120:
    print("You can ride the roller coster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5 ticket price.")
    elif age <= 18:
        print("Please pay $7 ticket price.")
    else:
        print("Please pay $12 ticket price")
else:
    print("You cannot ride the roller coster.")
