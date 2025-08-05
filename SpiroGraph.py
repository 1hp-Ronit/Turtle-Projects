from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
pen = Turtle()
pen.speed(0)  # Fastest speed = 0
pen.pensize(2)
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour
def spiro_graph(gap):
    """The Entire circle is 360, if everytime turns left by 3 degree entire rotation in 360/3"""
    for _ in range(int(360/gap)):

        pen.color(random_colour())
        pen.circle(100)
        pen.left(gap)
gap = int(input("Enter the gap angle:\n"))
spiro_graph(gap)
screen = Screen()
screen.exitonclick()