numbers = [1, 2, 3]

# new_list = [new_item for item in list]
new_list = [item + 1 for item in numbers]

print(numbers)
print(new_list)

name = "Karl"

letters = [c for c in name]

print(letters)

x = range(1, 5)
print(x)
y = [n ** 2 for n in x]
print(y)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [sn for sn in names if len(sn) <= 4]
print(short_names)

long_names = [ln.upper() for ln in names if len(ln) > 4]
print(long_names)

numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
