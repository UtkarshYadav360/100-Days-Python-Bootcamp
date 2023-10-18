import datetime as dt

# getting the current year,month,date and time
current_info = dt.datetime.now()
print(current_info)

# getting the current year
current_year = current_info.year
print(current_year)

# getting the current date
current_date = current_info.day
print(current_date)

# getting the current day
current_day = current_info.weekday()
print(current_day)


# creating our own day time object
DOB = dt.datetime(year=2005, month=6, day=10)
print(DOB)
