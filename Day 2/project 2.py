# PROJECT 2 :
# TIP CALCULATOR :

# NOTE : "{:.2f}".format(final_bill/people) makes 2 decimal digits


# greeting to the user
print("Welcome To The Tip Calculator :")

# total bill
bill = float(input("What was the total bill? $"))

# tip percent
tip = int(input("What percent tip would you like to give? 10, 12 or 15 : "))

# people to split the bill
people = int(input("How many people to split the bill? "))

# tip amount
tip_percent = tip / 100
tip_amount = bill * tip_percent

# bill with tip
final_bill = bill + tip_amount

# bill per person
splitted_bill = "{:.2f}".format(final_bill / people)

# final output
print(f"Each person should pay ${splitted_bill}")
