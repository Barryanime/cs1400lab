from turtle import *
from random import *

window = Screen()
my_turtle = Turtle()

my_turtle.begin_fill()
my_turtle.pencolor(1.0, 0.0, 1.0)
my_turtle.fillcolor(0.0, 0.0, 0.0)
my_turtle.circle(100)


for count in range(0, 10):
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)

my_turtle.speed(0)
for count in range(0, 10):
    turn = randint(-180, 179)
    my_turtle.left(turn)
    my_turtle.forward(10)

window.exitonclick()
