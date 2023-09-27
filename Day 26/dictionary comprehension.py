import random

# dictionary comprehension :
# SYNTAX = new_dict = {new_key:new_value    for item in list}

names = ["Angela", "Alexa", "Yuri", "Maya", "Harry"]
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)


# conditional dictionary comprehension
# SYNTAX = new_dict = {new_key:new_value    for (key value) in dict.items()    if test}
passed_students = {
    student: score for (student, score) in student_scores.items() if score > 60
}
print(passed_students)
