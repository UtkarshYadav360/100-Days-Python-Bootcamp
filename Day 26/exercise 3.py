# EXERCISE 3 :
# DATA OVERLAP


with open("file 1.txt") as file1:
    data1 = file1.readlines()


with open("file 2.txt") as file2:
    data2 = file2.readlines()

result = [int(number) for number in data1 if number in data2]
print(result)
