import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

nato = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato)

done = False
while not done:
    word = input("enter word:").upper()
    try:
        result = [nato[c] for c in word]
        print(result)
        done = True
    except KeyError:
        print("Oops, only enter letters")
