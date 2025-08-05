from turtle import Turtle, Screen

pen = Turtle()
colors = [
    "#FF5733",  # Red-Orange
    "#33FF57",  # Bright Green
    "#3357FF",  # Bright Blue
    "#FF33F1",  # Magenta
    "#FFD700",  # Gold
    "#FF6B35",  # Orange
    "#8A2BE2",  # Blue Violet
    "#00CED1"   # Dark Turquoise
]
sides = 3
for i in range(0, 7):
    for _ in range(sides):
        pen.color(colors[i])
        pen.right(360/sides)
        pen.forward(100)
    sides += 1
screen = Screen()


screen.exitonclick()