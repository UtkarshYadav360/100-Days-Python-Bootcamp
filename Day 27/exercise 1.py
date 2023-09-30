import tkinter

# EXERCISE 1 :


# making the tkinter window
window = tkinter.Tk()
window.title("Exercise 1")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)  # sets the padding for the tkinter window

# making a label
label = tkinter.Label(text="Label 1", font=("Cacadia Code", 24, "bold"))
label.grid(row=0, column=0)


# making a button
button1 = tkinter.Button(text="Click Me")
button1.grid(row=0, column=2)

button2 = tkinter.Button(text="Click Me")
button2.grid(row=1, column=1)


# making a entry box
user_input = tkinter.Entry(width=10)
user_input.grid(row=2, column=3)

window.mainloop()
