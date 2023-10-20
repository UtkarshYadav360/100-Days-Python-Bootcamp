from tkinter import *
from quiz_brain import QuizBrain

# CONSTANTS
THEME_COLOR = "#375362"


# creating a class
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # logic of the quiz
        self.quiz = quiz_brain

        # making tkinter window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # making score text
        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "normal")
        )
        self.score_label.grid(row=0, column=1)

        # making canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill="black",
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # making true button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        # making false button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Show the questions if there are quiz questions left."""
        self.canvas.config(bg="white")
        # if there are question left in the quiz then shows the next question and increase the score if the answer is correct
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            # buttons are disabled when the quiz is ended
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Works when the true button is pressed."""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Works when the false button is pressed."""
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Give feedback to the user, if they are right or wrong."""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
