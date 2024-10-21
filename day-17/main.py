from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions_bank = []
for item in question_data:
    new_question = Question(item["text"],item["answer"])
    questions_bank.append(new_question)


brain = QuizBrain(questions_bank)

while brain.still_has_questions():
    brain.next_question()

print('You\'ve completed the quiz!')
print(f"Your final score was: {brain.score}/{brain.question_number}")