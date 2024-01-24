import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

for n in student_scores:
    print(n)
    print(student_scores[n])

passed_students = {n:student_scores[n] for n in student_scores if student_scores[n] > 60}
print(passed_students)
# alternate method
passed_students = {n:s for (n,s) in student_scores.items() if s > 60}
print(passed_students)
#
# student_score ={
#     "Alex": 89,
#     'Beth': 33
# })
