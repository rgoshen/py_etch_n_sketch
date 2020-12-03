from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.forward(5)


def move_backwards():
    pen.backward(5)


def turn_clockwise():
    new_heading = pen.heading() - 10
    pen.setheading(new_heading)


def turn_counter_clockwise():
    new_heading = pen.heading() + 10
    pen.setheading(new_heading)


def clear_screen():
    pen.reset()


screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="Left", fun=turn_counter_clockwise)
screen.onkey(key="Right", fun=turn_clockwise)

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)

screen.exitonclick()
