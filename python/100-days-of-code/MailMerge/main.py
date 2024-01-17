
def read_file(file_name):
    with open(file_name, "r") as f:
        return f.readlines()


def create_invitation(name):
    letter_template = read_file("Input/Letters/starting_letter.txt")
    doc = []
    for line in letter_template:
        doc.append(line.replace("[name]", name.strip()))
    return doc


def write_invitation(doc, fn):
    with open(fn, "w") as f:
        f.writelines(doc)


friends = read_file("Input/Names/invited_names.txt")

print(friends)
for name in friends:
    letter = create_invitation(name)
    file_name = f"Output/ReadyToSend/{name.strip()}.txt"
    write_invitation(letter,file_name)
