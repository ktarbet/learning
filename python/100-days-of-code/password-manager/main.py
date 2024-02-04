import tkinter
from tkinter import Label, Button, Entry

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry(url:str,username:str,password:str):
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
width = 200
height = 200
window.title("Driving Tkinter")
window.minsize(width=width, height=height)
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=width, height=height)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(width / 2, height / 2, image=img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_url = Entry(width=35)
web_url.grid(column=1, row=1, columnspan=2)
web_url.focus()

user_label = Label(text="Email/Username")
user_label.grid(column=0, row=2)

username = Entry(width=35)
username.grid(row=2, column=1, columnspan=2)
username.insert(0,"karl@learning-python.now")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password = Entry(width=21)
password.grid(row=3, column=1)

generate_password = Button(text="Generate Password")
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=36,command=)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
