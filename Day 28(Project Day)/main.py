import tkinter
import math


# NOTE : math.floor() is used to round the given number to it's nearest integer. It returns the largest integer less than or equal to the input number.

# NOTE : after() is used to schedule the execution of a function after a specified delay in milliseconds.

# NOTE : after_cancel() is used to cancel the previously scheduled event that was set using the method. Used to remove the pending event from the event queue before it is executed.


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
timer = None


def reset_timer():
    """Reset the timer."""
    window.after_cancel(timer)  # stops the timer
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")

    global reps
    # sets the repetitions of the timer to 0, So the timer starts from the starting point.
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# number of repetitions in timer
reps = 0


def start_timer():
    """Makes the timer work and starts the timer."""
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    # conditions to set the the timer
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """sets the countdown."""
    # counting minutes and seconds
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    # seconds will shows in double digits ==> "09", "08"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    # changing the canvas text
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    # global reps

    # specifying the conditions
    if count > 0:
        global timer
        # starts the timer with delay of 1 second
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        # a check mark will be shown each time a working session is completed
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔️"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# MAKING THE TKINTER WINDOW
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# MAKING THE CANVAS :
# specifying the canvas dimensions
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# creating the image on the tkinter window
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
# creating the text on the image
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)


# MAKING THE LABELS
timer_label = tkinter.Label(
    text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW
)
timer_label.grid(row=0, column=1)

start_button = tkinter.Button(
    text="Start", font=(FONT_NAME, 10, "normal"), command=start_timer
)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(
    text="Reset", font=(FONT_NAME, 10, "normal"), command=reset_timer
)
reset_button.grid(row=2, column=2)

check_marks = tkinter.Label(fg=GREEN, font=5, bg=YELLOW)
check_marks.grid(row=2, column=1)


# KEEPS THE WINDOW OPEN
window.mainloop()
