# EXERCISE 1 :
# write a function takes year and month as input and return how many days are there in that month.


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Input!"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# DON'T CHANGE THE CODE BELOW :
year = int(input("Year : "))
month = int(input("Month : "))
days = days_in_month(year, month)
print(days)
