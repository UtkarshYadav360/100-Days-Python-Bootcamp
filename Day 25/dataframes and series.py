import pandas

# DataFrame :
# whole table is basically a DataFrame.

# Series :
# every single column in a table is series.


data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))
print()

# converting the data into a dictionary
data_dict = data.to_dict()
print(data_dict)
print()

# converting the specified data into a list
temp_list = data["temp"].to_list()
print(temp_list)
print()

# calculating the average of the temperature using pandas
print(data["temp"].mean())
print()

# calculating the maximum of the temperature
print(data["temp"].max())
print()

# getting data in columns
print(data["condition"])
print()
# or
print(data.condition)
print()

# get data in rows
print(data[data.day == "Monday"])
print()

# getting the data in row, which have the maximum temperature in the week
print(data[data.temp == data.temp.max()])
print()

# getting data in row using a variable
monday = data[data.day == "Monday"]
print(monday.condition)
print()

# converting the temperature of monday to celsius into fahrenheit
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9 / 5 + 32
print(monday_temp_f)
print()

# creating DataFrame from scratch
students_data = {"students": ["Mike", "James", "Max"], "scores": [65, 56, 79]}
students_df = pandas.DataFrame(students_data)
print(students_df)

# converting our DataFrame into a csv file
students_df.to_csv("students_df.csv")
