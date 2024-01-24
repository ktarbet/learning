# read file1.txt and file2.txt as lists of numbers

def read_numbers_from_file(file_name):
    with open(file_name, "r") as f:
        return [int(num) for num in f.readlines()]


file1 = read_numbers_from_file("file1.txt")
file2 = read_numbers_from_file("file2.txt")

# what numbers are in both files?
common = [x for x in file1 if x in file2]

print(common)
