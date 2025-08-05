from turtle import Turtle, Screen
import turtle as t

import random

t.colormode(255)
directions = [0, 90, 180, 270]


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


pen = Turtle()
pen.pensize(10)
pen.speed(0)
for _ in range(200):
    pen.forward(30)
    pen.setheading(random.choice(directions))
    pen.color(random_colour())

screen = Screen()
screen.exitonclick()
