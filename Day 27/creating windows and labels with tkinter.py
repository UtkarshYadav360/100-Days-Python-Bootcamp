import tkinter


# making the tkinter window
window = tkinter.Tk()  # makes the tkinter window
window.title("Tkinter GUI Program")  # sets the title for the window
window.minsize(width=500, height=300)  # sets the minimum size for the tkinter window


# making a label for the tkinter window
my_label = tkinter.Label(
    text="I am a label", font=("Cascadia Code", 24, "bold")
)  # specifies the label text for the tkinter window
my_label.pack(
    side="right"
)  # pack/show the text to the "right-center" of the tkinter window, Bydefault it is in the "top-center"


window.mainloop()  # keeps the window open
