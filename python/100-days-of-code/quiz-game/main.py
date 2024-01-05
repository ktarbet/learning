from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qd in question_data:
     q = Question(qd["text"],qd["answer"])
     question_bank.append(q)



qb = QuizBrain(question_bank)

while qb.still_has_questions():
     qb.next_question()

print("your done!")
print(f"Final Score {qb.score}/{len(question_bank)}")
