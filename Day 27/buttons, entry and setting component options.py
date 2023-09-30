import tkinter

# making the tkinter window
window = tkinter.Tk()
window.title("Tkinter GUI Program")
window.minsize(width=500, height=300)


# making a label
my_label = tkinter.Label(text="I am a label", font=("Cascadia Code", 24, "bold"))
my_label.pack()


# methods to configure or change or update the properties of a particular component
my_label["text"] = "New Text"  # change the text of the label
my_label.config(text="Newer Text")  # also, change the text of the label


# creating a button
def clicked():
    # my_label.config(text="Button got clicked.")
    my_label.config(text=user_input.get())  # returns the input as a string


button = tkinter.Button(text="Click Me", command=clicked)
button.pack()


# taking input/entry
user_input = tkinter.Entry(width=10)
user_input.pack()

# keeps the window open
window.mainloop()
