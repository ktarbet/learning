import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# {"A": "Alfa", "B": "Bravo"}
nato = {row.letter: row.code for (index, row) in df.iterrows()}
print('startup')
word = input("enter word:").upper()
result = [nato[c] for c in word]
print(result)
# for letter in list(word):
#     print(f"{letter} : {nato[letter.upper()]}")
