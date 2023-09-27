# EXERCISE 5 :

# DON'T CHANGE THE CODE BELOW
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# WRITE YOUR CODE HERE
weather_f = {day: (weather * 9 / 5) + 32 for (day, weather) in weather_c.items()}

# DON'T CHANGE THE CODE BELOW
print(weather_f)
