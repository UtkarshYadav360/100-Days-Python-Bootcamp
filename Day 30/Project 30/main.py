from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# PROJECT 29
# PASSWORD MANAGER :


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Finds the password in the "data.json" file."""
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="ERROR", message="No Data File Found!")
    else:
        if len(website) == 0:
            messagebox.showinfo(title="ERROR", message="You Didn't Type Anything!")
        elif website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email : {email}\nPassword : {password}"
            )
            pyperclip.copy(password)
        else:
            messagebox.showinfo(
                title="ERROR", message=f"No Details Are Saved For {website} "
            )


# ---------------------------- GENERATE PASSWORD ------------------------------- #
def generate_password():
    """Generates the password when click on the 'Generate' button and shows it in the password entry box."""
    nr_letters = 4  # number of letters
    nr_numbers = 2  # number of numbers
    nr_symbols = 2  # number of symbols

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Gets the data that user entered, and add it to the file called 'data.txt' and after user click the 'add button' it clears the 'website' and 'password' field."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    # showing a message related to empty fields
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="OOPS!", message="Please don't leave any input fields empty."
        )
    else:
        # UPDATING THE JSON FILE :
        try:
            with open("data.json", mode="r") as data_file:
                # reading the json file
                data = json.load(data_file)

        except:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating the new data in the json file
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
                messagebox.showinfo(title="Password Saved", message="Your Password Is Saved.")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# MAKING THE TKINTER SCREEN :
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#E4E4D0")


# MAKING CANVAS :
canvas = Canvas(width=200, height=200, bg="#E4E4D0", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)


# MAKING LABELS :
website_label = Label(text="Website :", font=("Arial", 10, "bold"), bg="#E4E4D0")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username :", font=("Arial", 10, "bold"), bg="#E4E4D0")
email_label.grid(row=2, column=0)

password_label = Label(text="Password :", font=("Arial", 10, "bold"), bg="#E4E4D0")
password_label.grid(row=3, column=0)


# MAKING ENTRIES :
website_entry = Entry(
    width=36,
    font=("Arial", 10, "normal"),
    bg="#DAD4B5",
    borderwidth=2,
)
website_entry.focus()
website_entry.grid(row=1, column=1, pady=5)

email_entry = Entry(
    width=46,
    font=("Arial", 10, "normal"),
    bg="#DAD4B5",
    borderwidth=2,
)
email_entry.insert(0, "inevitablestrangeutkarsh@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, pady=5)

password_entry = Entry(
    width=36,
    font=("Arial", 10, "normal"),
    bg="#DAD4B5",
    borderwidth=2,
)
password_entry.grid(row=3, column=1, pady=5)


# MAKING BUTTONS :
search_button = Button(
    text="Search",
    width=7,
    font=("Arial", 9, "bold"),
    bg="#DAD4B5",
    borderwidth=2,
    command=find_password,
)
search_button.grid(row=1, column=2)

generate_password = Button(
    text="Generate",
    width=7,
    font=("Arial", 9, "bold"),
    bg="#DAD4B5",
    borderwidth=2,
    command=generate_password,
)
generate_password.grid(row=3, column=2)

add_button = Button(
    text="Add",
    width=45,
    font=("Arial", 9, "bold"),
    bg="#DAD4B5",
    borderwidth=2,
    command=save,
)
add_button.grid(
    row=4,
    column=1,
    columnspan=2,
    padx=3,
    pady=5,
)

window.mainloop()
