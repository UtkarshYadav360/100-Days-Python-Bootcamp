# BY-DEFAULT any file opens in "readonly" mode.
# NOTE : it's a good practice to always close the file, that you've opened.
# NOTE : # by using "with" keyword to open a file there's no need to close the file manually.
# NOTE : mode="w" deletes the previous text in the file and adds the new text to it.
# NOTE : mode="a" appends the new text to the file in the same line.
# NOTE : if we try to open an un-existing file in, mode="w", the file with the specified name will be created and then opened in the writable mode.

# opening the file
file = open("my_file.txt")

# reading the file as a string
contents = file.read()

# printing the contents inside the file
print(contents)

# closing the file
file.close()


# opening the file using with keyword in "writeable" mode
with open(file="my_file.txt", mode="w") as file:
    # writing new text to the file
    file.write("Previous text is deleted and new text is added to the file.")

# opening the file using with keyword in "append" mode
with open(file="my_file.txt", mode="a") as file:
    # appending new text to the file
    file.write("New text is appended to the file in the same line.")
    file.write("\nNew text is appended to the file in the new line.")

# opening an un-existing file in the "writable" mode
with open(file="new_file.txt", mode="w") as new_file:
    new_file.write("New file is created.")
