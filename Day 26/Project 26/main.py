import pandas

# PROJECT 26 :
# NATO ALPHABETS


# reading the csv file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# creating a dictionary for the phonetic alphabets
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# taking user input
word = input("Enter a word : ").upper()

# creating a list for the user input
output_list = [phonetic_dict[letters] for letters in word]

# final output
print(output_list)
