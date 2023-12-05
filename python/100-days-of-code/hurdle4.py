def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
 
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
    
#for i in range(6):
#    jump()
#    if at_goal():
#        break;
