from turtle import *
# set up turtle
window = Screen()

# drawing picture
my_turtle = Turtle()

for side in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

my_turtle.penup()
my_turtle.setposition(75, -150)
my_turtle.pendown()

# Make another square
for side in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

# wait to finish
window.exitonclick()

def print_star():
    print(" *")
    print(" ***")
    print(" *")

for i in range(10):
    print_star()

def draw_square(drawing turtle):

