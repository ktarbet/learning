from tkinter import PhotoImage, Tk, Canvas, Button

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Ariel", 40, "italic")
FONT_BIG = ("Ariel", 60, "italic")


def wrong():
    pass


def ok():
    pass


window = Tk()
window.title("Spanish Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="abc", font=FONT)
canvas.create_text(400, 263, text="word", font=FONT_BIG)

canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
oops_button = Button(command=wrong, image=wrong_img, highlightthickness=0)
oops_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
ok_button = Button(command=ok, image=right_img, highlightthickness=0)
ok_button.grid(column=1, row=1)

window.mainloop()
