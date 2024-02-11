import json
import os
import tkinter
from tkinter import Label, Button, Entry, END, messagebox
from random import randint, choice, shuffle
import pyperclip

FILENAME = 'data.json'


def make_password():
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)] \
                    + [choice(symbols) for _ in range(nr_symbols)] \
                    + [choice(numbers) for _ in range(nr_numbers)]

    print(password_list)
    shuffle(password_list)

    return "".join(password_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entry(url: str, username: str, password: str):
    if len(url.strip()) == 0 or len(username.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo("oops", "can't have empty entries!")
        return

    new_data = {
        url: {
            "email": username,
            "password": password,
        }
    }
    try:
        with open(FILENAME, 'r') as file:
            data = json.load(file)
            data.update(new_data)
    except FileNotFoundError:
        print("created new file")
        data = new_data

    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


def find_password(website_name: str):
    if os.path.isfile(FILENAME):
        with open(FILENAME, 'r') as file:
            data = json.load(file)
            if website_name in data:
                return data[website_name]

    else:
        return None


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
width = 200
height = 200
window.title("Driving Tkinter")
window.minsize(width=width, height=height)
window.config(padx=20, pady=20)

LABEL_WIDTH=33

canvas = tkinter.Canvas(width=width, height=height)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(width / 2, height / 2, image=img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:",width=LABEL_WIDTH)
web_label.grid(column=0, row=1)

web_url = Entry(width=LABEL_WIDTH)
web_url.grid(column=1, row=1, columnspan=1)
web_url.focus()


def on_search(url: str):
    p = find_password(url)
    if p:
        password.delete(0, END)
        password.insert(0, p["password"]),
        pyperclip.copy(p["password"])


search = Button(text="Search", width=int(LABEL_WIDTH/2), command=lambda: on_search(web_url.get()))
search.grid(row=1, column=2)

user_label = Label(text="Email/Username",width=LABEL_WIDTH)
user_label.grid(column=0, row=2)

username = Entry(width=LABEL_WIDTH)
username.grid(row=2, column=1, columnspan=1)
username.insert(0, "karl@learning-python.now")

password_label = Label(text="Password:",width=LABEL_WIDTH)
password_label.grid(column=0, row=3)

password = Entry(width=LABEL_WIDTH)
password.grid(row=3, column=1)

generate_password = Button(text="Generate Password", width=int(LABEL_WIDTH/2), command=lambda: (
    password.delete(0, END),
    password.insert(0, make_password()),
    pyperclip.copy(password.get())
))
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=36, command=lambda: (
    save_entry(web_url.get(), username.get(), password.get()),
    password.delete(0, END),
    web_url.delete(0, END)
))

add.grid(row=4, column=1, columnspan=2)

window.mainloop()
