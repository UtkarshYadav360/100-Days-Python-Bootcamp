# EXERCSIE 2 :
# take a list of student scores as input and print the highest score.

# DON'T CHANGE THE CODE BELOW :
student_scores = input("Input a list of student scores, seperated by space : ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


# WRITE YOUR CODE HERE :
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is {highest_score}.")
