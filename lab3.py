from turtle import *
# set up turtle
window = Screen()

# drawing picture
my_turtle = Turtle()

my_turtle.forward(100)
my_turtle.setposition(100, -100)
my_turtle.penup()

for number in range(10):
    print('Hi!')
    print('The count is', number)
print("Done with the loop")

# wait to finish
window.exitonclick()
