import requests
from tkinter import *

# EXERCISE 1 :
# KANYE QUOTES APP :


def get_quote():
    """Shows a Kanye quote when the button is pressed."""
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    all_quotes = response.json()
    quote = all_quotes["quote"]
    canvas.itemconfig(quote_text, text=quote)


# window setup
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# making canvas and setting up the images
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")

# making button
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
