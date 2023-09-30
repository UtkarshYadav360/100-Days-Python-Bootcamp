import tkinter

# PROJECT 27 :
# MILES TO KILOMETER CONVERTER

# function to be triggered when button clicked
def calculate():
    """Convert the miles into kilometers and assign the value to label4."""
    label4.config(text=round(int(miles.get()) * 1.609344, 2))


# making the tkinter window
windows = tkinter.Tk()
windows.title("Miles to Km Converter")
windows.minsize(width=300, height=200)
windows.config(padx=20, pady=20)

# taking the entry
miles = tkinter.Entry(width=10, font=("Cascadia Code", 10, "normal"))
miles.focus()
miles.grid(row=1, column=3)

# making labels
label1 = tkinter.Label(text="Miles", font=("Cascadia Code", 14, "normal"))
label1.grid(row=1, column=4)
label1.config(padx=10)

label2 = tkinter.Label(text="is equal to", font=("Cascadia Code", 14, "normal"))
label2.grid(row=2, column=2)

label3 = tkinter.Label(text="Km", font=("Cascadia Code", 14, "normal"))
label3.grid(row=2, column=4)

label4 = tkinter.Label(text="", font=("Cascadia Code", 14, "normal"))
label4.grid(row=2, column=3)

# making buttons
button = tkinter.Button(
    text="Calculate", command=calculate, font=("Cascadia Code", 10, "normal")
)
button.grid(row=3, column=3)


# keeps the window open
windows.mainloop()
