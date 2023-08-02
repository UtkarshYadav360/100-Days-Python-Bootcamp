# EXERCISE 1 :
# take a list of heights of students and print the average height.

# DON'T CHANGE THE CODE BELOW :
student_heights = input(
    "Input a list of student heights, seperated by space : "
).split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


# WRITE YOUR CODE HERE :
heights_sum = 0
for height in student_heights:
    heights_sum += height

total_students = 0
for student in student_heights:
    total_students += 1

average_height = round(heights_sum / total_students)
print(f"The average height is {average_height}")
