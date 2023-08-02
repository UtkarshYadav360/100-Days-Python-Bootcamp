# EXERCSIE 1 :
# write a program that converts students scores into grades.

# NOTE : only use print statement to print the final output.

# DON'T CHANGE THE CODE BELOW :
student_scores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62}


# TODO 1 :
# create an empty dictionary called "student_grades"
student_grades = {}

# WRITE YOUR CODE HERE :
for score in student_scores:
    student = score
    marks = student_scores[score]

    if marks > 90:
        student_grades[student] = "Outstanding"
    elif marks > 80:
        student_grades[student] = "Exceeds Expetations"
    elif marks > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
