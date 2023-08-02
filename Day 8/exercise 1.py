import math

# EXERCSIE 1 :
# take height and width of the wall and print the number of cans required to print the wall.

# NOTE : 1 can of paint, can cover 5 square meters of wall.
# NOTE : number of cans = (wall height * wall width) / coverage per can
# NOTE : the output should be rounded up.


# WRITE YOUR CODE HERE :
def paint_calc(height, width, cover):
    cans_required = (height * width) / cover
    print(f"You'll need {math.ceil(cans_required)} cans to paint the wall.")


# DON'T CHANGE THE CODE BELOW :
test_h = int(input("Height of the wall : "))
tesh_w = int(input("Width of the wall : "))
coverage = 5
paint_calc(height=test_h, width=tesh_w, cover=coverage)
