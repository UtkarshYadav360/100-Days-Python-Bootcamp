import pandas

student_dict = {"student": ["Angela", "James", "Lilly"], "score": [56, 76, 98]}

student_data = pandas.DataFrame(student_dict)

# iterating over pandas DataFrame using for loop
# WARNING ==> this method is completely useless.
for key, value in student_data.items():
    print(key)
    print(value)
print()

# iterating over pandas DataFrame using iterrows() method
for index, row in student_data.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    print(row.score)
