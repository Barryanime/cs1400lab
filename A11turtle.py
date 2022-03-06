"""
Initial code written by David Johnson, University of Utah.
This, and all derived works may not be publicly shared.

Recursive versions written by Barry Lin
"""
import turtle


# def draw_spiral(line_length, turtle):
#     """
#     Draws a spiral with an initial line of line_length centered
#     at the current turtle location.
#
#     :param line_length: The inner part of the spiral length
#     :param turtle: A python turtle
#     :return: None
#     """
#     while line_length < 25:
#         turtle.forward(line_length)
#         turtle.left(10)
#         line_length *= 1.01


def draw_spiral_recursive(line_length, turtle):
    """
    Draw a spiral in a recursive way.

    :param line_length:The spiral length
    :param turtle: python turtle
    :return:none
    """
    if line_length < 25:
        turtle.forward(line_length)
        turtle.left(10)
        draw_spiral_recursive(line_length * 1.01, turtle)


def draw_centered_circle(circle_radius, turtle):
    """
    A helper function to make the circle fractal easier to
    draw with turtle. It draws a circle of size circle_radius
    centered at the current turtle location.
    :param circle_radius: The radius of the circle
    :param turtle: The Python turtle to draw the circle.
    :return: None
    """

    turtle.penup()
    turtle.forward(circle_radius)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(circle_radius)
    turtle.penup()
    turtle.right(90)
    turtle.backward(circle_radius)
    turtle.penup()


def draw_circles(circle_radius, turtle):
    """
    Draw a big circle with three half-sized circle up, left,
    and right of the big circle. Return the turtle to its
    original location and heading.

    :param circle_radius: The radius of the center circle
    :param turtle: The Python turtle to draw.
    :return: None.
    """

    draw_centered_circle(circle_radius, turtle)
    turtle.forward(circle_radius * 1.5)
    draw_centered_circle(circle_radius * 0.5, turtle)
    turtle.backward(circle_radius * 1.5)
    turtle.left(90)
    turtle.forward(circle_radius * 1.5)
    draw_centered_circle(circle_radius * 0.5, turtle)
    turtle.backward(circle_radius * 1.5)
    turtle.right(180)
    turtle.forward(circle_radius * 1.5)
    draw_centered_circle(circle_radius * 0.5, turtle)
    turtle.backward(circle_radius * 1.5)
    turtle.left(90)


def draw_fractal_circles(circle_radius, turtle):
    """
    draw a circle with smaller circles on the top, left, and right.
    There are smaller circles attached to the small circles and
    would keep adding circles until the radius is 1.

    :param circle_radius:the radius of the circle
    :param turtle: python turtle
    :return:none
    """
    if circle_radius > 1:
        draw_circles(circle_radius, turtle)
        turtle.right(90)
        turtle.forward(circle_radius + circle_radius/2)
        draw_fractal_circles(circle_radius/2, turtle)
        turtle.right(90)

    # turtle.right(90)
    # turtle.forward(circle_radius + circle_radius/2)
    # draw_fractal_circles(circle_radius/2, turtle)


def main():
    """
    Provide code to setup and test the spiral and circle
    fractal code.
    :return: None.
    """
    # Set up the turtle and window
    recursive_turtle = turtle.Turtle()
    recursive_turtle.speed(0)
    myWin = turtle.Screen()
    recursive_turtle.penup()
    recursive_turtle.left(90)
    recursive_turtle.backward(100)

    # Draw the spiral
    recursive_turtle.pendown()
    # draw_spiral(1, recursive_turtle)
    draw_spiral_recursive(1, recursive_turtle)

    # Draw the circles
    recursive_turtle.penup()
    recursive_turtle.goto(0, 100)
    recursive_turtle.setheading(90)
    # draw_circles(50, recursive_turtle)
    draw_fractal_circles(50, recursive_turtle)

    myWin.exitonclick()


if __name__ == "__main__":
    main()
