# EXERCISE 3 :
# life in weeks :
# print the number of days, weeks and months left in the user life till they becomes 90

# DON'T CHANGE THE CODE BELOW :
age = input("What is your current age? ")


# WRITE YOUR CODE HERE :
int_age = int(age)
age_left = 90 - int_age

days_left = age_left * 365
weeks_left = age_left * 52
months_left = age_left * 12

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")
