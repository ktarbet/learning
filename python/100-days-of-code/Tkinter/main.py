from tkinter import *

window = Tk()
window.title("Driving Tkinter")
window.minsize(width=400, height=300)
window.config(padx=60, pady=60)

txt_input = Entry(width=35)
txt_input.grid(column=1, row=0)

label_miles = Label(text="miles")
label_miles.grid(column=2, row=0)

label_eq = Label(text="is equal to")
label_eq.grid(column=0, row=1)

label_result = Label(text="?")
label_result.grid(column=1, row=1)

label_km = Label(text="km")
label_km.grid(column=2, row=1)
def calc_click():
    miles = float(txt_input.get())
    km = 1.60934* miles
    str_km = f"{km}"
    label_result.config(text=str_km)


calc_button = Button(text="Calculate", command=calc_click)
calc_button.grid(column=1, row=2)





window.mainloop()
