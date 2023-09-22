# PROJECT 24 :
# MAIL MERGE PROJECT


# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: readlines() method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: replace() method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: strip() method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# placeholder to be replaced
PLACEHOLDER = "[name]"

# opening the invited_names.txt file
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # all names are stored as a list

# opening the starting_letter.txt file
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()  # all content is readed as a string

    # looping through each name in the "names list"
    for name in names:
        # stripping each name in order to remove extra spaces
        stripped_name = name.strip()
        # replacing the name with the placeholder
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # new files will be created with the names, to whom the letter belongs to
        with open(
            file=f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w"
        ) as completed_letter:
            completed_letter.write(new_letter)
