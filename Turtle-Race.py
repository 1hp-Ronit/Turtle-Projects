from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
y_positions = [-70, -40, -10, 20, 50, 80]
screen = Screen()
screen.setup(width=500, height=400)
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")
if user_input:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
