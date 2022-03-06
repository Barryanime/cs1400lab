# def sum_two_values(value1, value2):
# summed = value1, value2
#  return summed


# def main():
#    first_sum = sum_two_values(10, 20)
#    total = sum_two_values(first_sum, 50)
#    print(total)

import turtle
window = turtle.Screen()
circle = turtle.Turtle()
circle.speed(0)

def main():
    for x in range(-200, 201, 50):
        for y in range(-200, 201, 50):
            circle.penup()
            circle.goto(x, y)
            circle.pendown()
            circle.circle(20)
if  __name__=="__main__":
    main()


window.exitonclick()
