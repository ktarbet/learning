from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizUI:

    def create_button(self, img, row_index, column_index):
        rval = Button(image=img, highlightthickness=0)
        rval.grid(row=row_index, column=column_index)
        return rval

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        w = 300
        h = 250
        self.canvas = Canvas(width=w, height=h, bg="white")
        self.question_text = self.canvas.create_text(w / 2, h / 2,
                                                     width=w - 20,
                                                     text="Question1?:",
                                                     fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        img_true = PhotoImage(file="images/true.png")
        img_false = PhotoImage(file="images/false.png")

        self.true = self.create_button(img_true, 2, 0)
        self.true.config(command=self.true_click)
        self.false = self.create_button(img_false, 2, 1)
        self.false.config(command=self.false_click)
        self.get_next_question()

        self.window.mainloop()

    def true_click(self):
        self.feedback(self.quiz.check_answer(str(True)))

    def false_click(self):
        self.feedback(self.quiz.check_answer(str(False)))

    def feedback(self, good):
        if good:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q)
        else:
            self.canvas.itemconfig(self.question_text, text="End of Quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")