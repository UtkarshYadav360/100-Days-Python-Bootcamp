from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# PROJECT 17 :
# QUIZ GAME :


# question and answers are stored here
question_bank = []

# looping through the questions and answers in the question_data
for question in question_data:
    question_text = question["text"]  # getting questions
    question_answer = question["answer"]  # getting answers
    new_question = Question(question_text, question_answer)  # making a new question
    question_bank.append(new_question)  # appending new question to the question_bank

# getting the questions for the quiz
quiz = QuizBrain(question_bank)

# loop runs till the qiuiz has questions left
while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
