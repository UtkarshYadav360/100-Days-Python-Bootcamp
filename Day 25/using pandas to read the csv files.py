import pandas

# reading the csv file
data = pandas.read_csv("weather_data.csv")
print(data)


print()


# accessing the temperature from the csv file
temperatures = data["temp"]
print(temperatures)
