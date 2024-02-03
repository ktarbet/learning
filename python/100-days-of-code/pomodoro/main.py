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
reps = 1
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps, timer, timer_text, check, label
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps, label
    if reps in [1, 3, 5, 7]:
        label.config(text="Working", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps in [8]:
        label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps in [2, 4, 6]:
        label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    reps += 1
    if reps > 8:
        reps = 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(start_count):
    minutes = math.floor(start_count / 60)
    seconds = start_count % 60
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")
    if start_count >= 0:
        global timer
        timer = window.after(1000, count_down, start_count - 1)
    else:
        start()
        num_checks = math.floor(reps / 2)
        print(CHECK_MARK * num_checks)
        check.config(text=CHECK_MARK * num_checks, fg=GREEN)


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

check = Label(text="", fg=GREEN, font=("Times New Roman", 12, "bold"))

check.grid(column=1, row=3)

window.mainloop()
