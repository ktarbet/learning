import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
states = df.state.to_list()

answers = []


def write_state_name(x, y, name):
    txt = turtle.Turtle()
    txt.hideturtle()
    txt.penup()
    txt.goto(x, y)
    txt.pendown()
    txt.write(f"{name}", align='center', font=("Courier", 12, "normal"))


def check_state_name(state_name: str):
    rows = df[df.state.str.contains(state_name, case=False)]
    if rows.empty:
        return
    else:
        x = float(rows.x)
        y = float(rows.y)
        print(f"x= {x} y = {y}")
        write_state_name(x, y, state_name)
        answers.append(state_name)


state_name = ""
while state_name is not None:
    state_name = screen.textinput(title=f"{len(answers)}/50 correct", prompt="Enter another State Name?")
    if state_name is None:
        break
    state_name = state_name.title()  # Title Case
    check_state_name(state_name)

# write missing states to a csv file


#remaining_states = df[~df['state'].str.lower().isin([s.lower() for s in answers])]
remaining_states = [ s for s in states if s not in answers]
remaining_states_df = pandas.DataFrame(remaining_states)
remaining_states_df.to_csv("remaining_states.csv")

print(remaining_states)

# turtle.mainloop()

# code to find coordinates based on click.
# def get_mouse_click_coord(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coord)
