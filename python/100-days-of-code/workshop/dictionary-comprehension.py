import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

for n in student_scores:
    print(n)
    print(student_scores[n])

passed_students = {n: student_scores[n] for n in student_scores if student_scores[n] > 60}
print(passed_students)
# alternate method
passed_students = {n: s for (n, s) in student_scores.items() if s > 60}
print(passed_students)
#
# student_score ={
#     "Alex": 89,
#     'Beth': 33
# })


# create a dictionary where each word below is key and value number of characters
input = "What is the Airspeed Velocity of an Unladen Swallow?"

tokens = input.split(' ')
dict_word_len = { x:len(x) for x in tokens}
print(tokens)
print(dict_word_len)


# convert these degC to degF
def degF(temp_c):
    return (temp_c * 9 / 5) + 32

str='{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}'
dC= eval(str)
print(dC)
dF = { day:degF(degC) for (day, degC) in dC.items() }

print(dF)