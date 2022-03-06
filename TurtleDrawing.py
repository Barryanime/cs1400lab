from turtle import *

#
# CS 1400 Assignment 2. Written by David Johnson and
# This code, as it is now or after modification, may not be shared or uploaded to any public site.
# It may be uploaded to the course approved assignment submission system.


# Draw a square with a Python turtle.
# Do not modify this.
def draw_square():
    for side in range(4):
        turtle.forward(25)
        turtle.left(90)


# Draw a wall of ten blocks with a little space between each one.
def draw_wall():
    for square in range(10):
        draw_square()
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()


# Draw the eyes for the face
def draw_eye():
    turtle.begin_fill()
    turtle.fillcolor((0.0, 0.0, 0.0))
    turtle.circle(6)
    turtle.end_fill()


# Draw a simple face with a head and added color.
def draw_face():
    turtle.begin_fill()
    turtle.fillcolor((1.0, 1.0, 0.0))
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(20, 160)
    turtle.pendown()
    draw_eye()
    turtle.penup()
    turtle.goto(-20, 160)
    turtle.pendown()
    draw_eye()


# draw a box for the house.
def draw_box():
    for side in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)


# Draw windows and added color for the house
def draw_window():
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor((0.4, 0.8, 1.0))
    for windows in range(4):
        turtle.forward(45)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(22.5)
    turtle.left(90)
    turtle.backward(45)
    turtle.left(90)
    turtle.forward(22.5)
    turtle.right(90)
    turtle.forward(22.5)
    turtle.right(90)
    turtle.forward(45)
    turtle.penup()


# Draw a door for the house
def draw_door():
    turtle.begin_fill()
    turtle.fillcolor((1.0, 0.0, 0.0))
    for door in range(2):
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()


# Draw a simple house with windows and a door.
def draw_scene():
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.pensize(5)
    turtle.begin_fill()
    turtle.fillcolor((1.0, 0.9, 0.7))
    draw_box()
    turtle.end_fill()
    turtle.right(-45)
    turtle.begin_fill()
    turtle.fillcolor((0.7, 0.4, 0.3))
    turtle.forward(141.4)
    turtle.right(90)
    turtle.forward(141.4)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-70, -120)
    turtle.left(45)
    turtle.pendown()
    turtle.pensize(0)
    draw_window()
    turtle.penup()
    turtle.goto(25, -120)
    draw_window()
    turtle.goto(-70, -190)
    draw_window()
    turtle.goto(75, -250)
    turtle.left(90)
    turtle.pendown()
    draw_door()
    turtle.penup()
    turtle.goto(32, -220)
    turtle.pendown()
    turtle.circle(2)


# The following code uses the functions above to draw different things on the screen.
# You should not need to modify this code.


# Set up the window and turtle
window = Screen()
turtle = Turtle()
turtle.speed(0)

# Move to the top of the screen and draw a wall
turtle.penup()
turtle.goto(-150, 250)
turtle.pendown()
draw_wall()

# Move to the top middle and draw a face
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
draw_face()

# Move to the bottom middle and draw a scene
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
draw_scene()

turtle.hideturtle()  # Get rid of the arrow showing the turtle location.

window.exitonclick()
