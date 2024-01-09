

# class User:
#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username
#
# user_1 = User("001","karl")
#
#
#
# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# col1 = ["Pikachu","Squirtle","Charmander"]
# col2 = ["Electric","WAter","Fire"]
# table.add_column("Pokemon Name",col1)
# table.add_column("Type",col2)
# table.align="l"
# print(table)


import turtle

# Initialize the Turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a Turtle object
t = turtle.Turtle()

# Draw and fill the first circle
t.penup()
t.goto(-50, 0)
t.pendown()
t.begin_fill()
t.shape("circle")
t.color("red")  # Set the fill color
t.circle(50)
t.end_fill()

# Draw and fill the second circle
t.penup()
t.goto(50, 0)
t.pendown()
t.begin_fill()
t.shape("circle")
t.color("blue")  # Set the fill color
t.circle(50)
t.end_fill()

# Keep the window open
turtle.mainloop()
