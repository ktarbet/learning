from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
# https://colorhunt.co

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(start_count):
    minutes = math.floor(start_count / 60)
    seconds = start_count % 60
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if start_count >= 0:
        window.after(1000, count_down, start_count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro (tomato)")
window.config(padx=100, pady=50, bg=YELLOW, )

label = Label(text="Timer", fg=GREEN, font=("Times New Roman", 22, "bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start, font=(FONT_NAME, 16, "bold"), bg="white")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset, font=(FONT_NAME, 16, "bold"), bg="white")
reset_button.grid(column=2, row=2)

check = Label(text=CHECK_MARK, fg=GREEN, font=("Times New Roman", 12, "bold"))
check.grid(column=1, row=3)

window.mainloop()
