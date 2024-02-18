import os.path
from tkinter import PhotoImage, Tk, Canvas, Button
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")
FONT_BIG = ("Ariel", 60, "italic")
filename = 'data/words_to_learn.csv'
if not os.path.exists(filename):
    filename = 'data/spanish-words.csv'
data = pandas.read_csv(filename)
language_list = data.to_dict(orient='records')
global word


def new_word():
    global flip_timer, word
    window.after_cancel(flip_timer)
    word = random.choice(language_list)
    canvas.itemconfig(text_title, text="Spanish", fill='black')
    canvas.itemconfig(text_word, text=word['Spanish'], fill='black')
    canvas.itemconfig(img, image=card_front)
    flip_timer = window.after(3000, flip)


def wrong():
    new_word()


def ok():
    language_list.remove(word)
    df = pandas.DataFrame(language_list)
    df.to_csv('data/words_to_learn.csv', index=False)
    new_word()


def flip():
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(text_title, text='English', fill="white")
    canvas.itemconfig(text_word, text=word['English'], fill="white")
    canvas.itemconfig(img, image=card_back)
    flip_timer = window.after(3000, flip)


window = Tk()
window.title("Spanish Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
img = canvas.create_image(400, 263, image=card_front)
flip_timer = window.after(3000, flip)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
text_title = canvas.create_text(400, 150, text="Spanish", font=FONT)
text_word = canvas.create_text(400, 263, text="word", font=FONT_BIG)

canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
oops_button = Button(command=wrong, image=wrong_img, highlightthickness=0)
oops_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
ok_button = Button(command=ok, image=right_img, highlightthickness=0)
ok_button.grid(column=1, row=1)

new_word()
window.mainloop()
