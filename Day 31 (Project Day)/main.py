from tkinter import *
import pandas
import random

# NOTE : zip() function is used to combine multiple iterables into a single iterator. All elements are paired together according to their index positions.


# PROJECT 31 :
# FLASH CARD

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn = {}


# GENREATING THE RANDOM FRENCH WORDS WITH THEIR ENGLISH MEANING
def next_card():
    """Generates a random French word each time when a button is pressed."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    # flips the card after every 3 seconds
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flips the card and shows the English meaning of the shown French word."""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    """Removes the French word/card from the data called 'words_to_learn' which is a dictionary, when user clicks the check button, and stores the remaining words to a csv file called 'words_to_learn.csv'"""
    words_to_learn.remove(current_card)
    next_card()

    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# READING THE CSV FILE
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    # orient = "records" converts the dictionary like this ==> # [column:value],[column:value],[column:value]
    words_to_learn = data.to_dict(orient="records")

# MAKING THE TKINTER WINDOW
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# MAKING CANVAS
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# MAKING BUTTONS
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

# calling the function
next_card()

window.mainloop()
