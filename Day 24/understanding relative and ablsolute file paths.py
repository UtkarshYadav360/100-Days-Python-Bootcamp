# opening the file using absolute path
with open("D:/Programming/understanding_paths.txt") as file:
    contents = file.read()
    print(contents)

# opening the file using relative path
with open("../../understanding_paths.txt") as new_file:
    new_contents = new_file.read()
    print(new_contents)
