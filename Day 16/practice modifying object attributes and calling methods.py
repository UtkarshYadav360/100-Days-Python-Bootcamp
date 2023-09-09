# importing PrettyTable class from prettytable package
from prettytable import PrettyTable

# creating a PrettyTable object and save it to a variable called table.
table = PrettyTable()


# adding data to the table by calling "methods"
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])


# modifying object "attributes"
table.align = "l"

print(table)
