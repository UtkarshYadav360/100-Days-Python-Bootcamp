import csv

# opening the csv file
with open("weather_data.csv") as weather_data_file:
    # reader() is used to read the csv files
    weather_data = csv.reader(weather_data_file)

    # accessing the data inside the csv file
    for row in weather_data:
        print(row)


# opening the csv file
with open("weather_data.csv") as weather_data_file:
    # reader() is used to read the csv files
    weather_data = csv.reader(weather_data_file)

    # accessing temperatures as integer from the "weather_data_file"
    temperatures = []
    for data in weather_data:
        if data[1] != "temp":
            temperatures.append(int(data[1]))
    print(temperatures)
