import tkinter

# NOTE : pack() and grid() cannot be used in a same program.


# making the tkinter window
window = tkinter.Tk()
window.title("Tkinter GUI Program")
window.minsize(width=500, height=300)


# making a label
label = tkinter.Label(text="I am label.", font=("Cascadia Code", 24, "bold"))
label.config(text="New Text")
# label.pack()
label.place(x=50, y=100)  # using place layout manager


# function to be triggered when the button is pressed
def clicked():
    label.config(text=user_input.get())


# making a button
button = tkinter.Button(text="Click Me", command=clicked)
# button.pack()
button.grid(row=0, column=1)


# making an entry/input box
user_input = tkinter.Entry(width=10)
print(user_input.get())
# user_input.pack()
user_input.grid(row=1, column=2)

window.mainloop()
