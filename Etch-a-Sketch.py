"""
Press W for forward
Press S for backward
Press A for ACW
Press D for CW
Press C to clear the Screen
"""


from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
pen.color("#ff5370")

def forward():
    pen.forward(10)


def backward():
    pen.backward(10)


def anti_clockwise():
    pen.speed(0)
    pen.left(10)


def clockwise():
    pen.speed(0)
    pen.right(20)

def clear():
    pen.reset()
screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=anti_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
