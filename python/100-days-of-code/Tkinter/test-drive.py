import tkinter

window = tkinter.Tk()
window.title("Driving Tkinter")

window.minsize(width=400, height=300)

label1 = tkinter.Label(text="Input prompt:", font=("Times New Roman", 18, "bold"))
label1.pack()

label1["text"] = "updated."


def button_click():
    label1.config(text=txt_input.get())

button = tkinter.Button(command=button_click)

button["text"] = "Push me"
button.pack()

txt_input = tkinter.Entry(width=35)
txt_input.pack()

def add(*args):
    sum = 0
    for n in args:
        sum += n

    return sum


print(add(5, 6, -1))


def calc(**kwargs):
    pass


calc(operation="add", values=(1, 2, 3))

window.mainloop()
