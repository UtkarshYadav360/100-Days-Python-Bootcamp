# logical operators :

# and
print(5 > 2 and 3 > 1)

# or
print(5 > 2 or 3 > 4)

# not
print(not 5 > 2)


# ROLLER COSTER PROGRAM UPGRADED VERSION :
height = int(input("What is your height in (cm)? "))
if height > 120:
    print("You can ride the roller coster.")

    age = int(input("What is your age? "))
    if age < 12:
        ticket_price = 5
        print(f"Your ticket price is ${ticket_price}")
    elif age < 18:
        ticket_price = 7
        print(f"Your ticket price is ${ticket_price}")
    elif age >= 45 and age <= 55:
        ticket_price = 0
        print(f"Don't Worry! Have a free ride from us.")
    else:
        ticket_price = 12
        print(f"Your ticket price is ${ticket_price}")

    want_photos = input("Do you want photos of your ride? y/n : ")
    if want_photos == "y":
        ticket_price += 3
        print(f"The total bill is ${ticket_price}")
    else:
        print(f"Please pay ${ticket_price}")

else:
    print("You cannot ride the roller coster.")
