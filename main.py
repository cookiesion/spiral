
turtle.set_position(0, 0)
turtle.turn_right()

def on_forever():
    for index in range(5):
        turtle.forward(4 - index)
        turtle.turn_right()
    for index2 in range(5):
        turtle.turn_left()
        turtle.back(index2)
basic.forever(on_forever)