# making a list :
states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersy",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermot",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "TExas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Neveda",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Oklahomo",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]
print(states_of_america)

# accessing the list items :
print(states_of_america[5])
print(states_of_america[-5])

# changing the list items at the specific index :
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# appending items to the end of the list :
states_of_america.append("Asguard")
print(states_of_america[-1])

# extending the list :
states_of_america.extend(["Sakar", "Vormir"])
print(states_of_america[-2])
print(states_of_america[-1])
