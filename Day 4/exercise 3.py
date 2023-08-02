# EXERCSIE 3 :

# DON'T CHANGE THE CODE BELOW :
row1 = [" ", "  ", "  "]
row2 = [" ", "  ", "  "]
row3 = [" ", "  ", "  "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


# WRITE YOUR CODE HERE :
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"


# DON'T CHANGE THE CODE BELOW :
print(f"{row1}\n{row2}\n{row3}")
