
student_dict ={
    "student": ["Joe", "Fred", "mary"],
    "score": [12,45,72],
}
#
# for (key,value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

df = pandas.DataFrame(student_dict)
#
# for (key, value) in df.items():
#     print(value)

for (index, row) in df.iterrows():
    print(row.student)