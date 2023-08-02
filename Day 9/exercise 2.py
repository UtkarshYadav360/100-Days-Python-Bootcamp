# EXERCSIE 2 :
# write a program that adds to a "travel_log".

# DON'T CHANGE THE CODE BELOW :
travel_log = [
    {"country": "France", "visits": 12, "cities_": ["Paris", "lille", "Dijon"]},
    {
        "country": "Germany",
        "total_visits": 15,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]


# TODO 1 :
# write a function that allows new countries to be added in the "travel_log".
def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["total_visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)


# DON'T CHANGE THE CODE BELOW :
add_new_country("Russia", 2, ["Moscow", "Saint Petersberg"])
print(travel_log)
