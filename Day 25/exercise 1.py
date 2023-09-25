# EXERCISE 1 :
# SQUIRREL CENSUS DATA ANALYSIS

import pandas

# reading the csv file
squirrel_data = pandas.read_csv("2018_squirrel_census.csv")

# counting the gray fur color
gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])

# counting the red fur color
red_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Red"])

# counting the black fur color
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

# creating a new DataFrame
squirrel_data = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_count, red_count, black_count],
}
squirrel_count = pandas.DataFrame(squirrel_data)
squirrel_count.to_csv("squirrel_count.csv")
