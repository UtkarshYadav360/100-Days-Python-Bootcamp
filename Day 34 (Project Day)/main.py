from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# all questions and their answers will be stored here
question_bank = []

# appending the questions and their answers in the above list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# calling the classes
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
