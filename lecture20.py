# def sum_numbers(numbers):
#     print(numbers)
#
#     if len(numbers) == 0:
#         return 0
#     sum = numbers[0] + sum_numbers(numbers[1:])
#     return sum
#
#
# print(sum_numbers([1, 2, 3]))
#
#
# def factorial(n):
#     # base case
#     if n == 1 or n == 0:
#         return 1
#     # recursive step
#     return n * factorial(n-1)
#
#
# print(factorial(50))
#
#
# def fibo(n):
#     global count
#     count = count + 1
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)
#
#
# def reverse_list(values):
#     if len(values) == 0:
#         return values
#     return [values[-1]] + reverse_list(values[0:-1])
#
#
# print(reverse_list([1, 2, 3, 4]))

#
# for n in range(1, 20):
#     print("Trying fibo of", n, "result was", fibo(n), "count was", count)


import turtle


def draw_tree(branch_length, tree_turtle):
    if branch_length > 1:
        # draw trunk
        tree_turtle.pendown()
        tree_turtle.forward(branch_length)
        tree_turtle.right(20)
        # draw a branch
        draw_tree(branch_length - 5, tree_turtle)
        # tree_turtle.forward(branch_length - 10)
        # tree_turtle.backward(branch_length - 10)
        tree_turtle.left(40)
        draw_tree(branch_length - 5, tree_turtle)
        # tree_turtle.forward(branch_length - 10)
        # tree_turtle.backward(branch_length - 10)
        tree_turtle.right(20)
        tree_turtle.backward(branch_length)


def main():
    t = turtle.Turtle()
    t.speed(0)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_tree(60, t)

    myWin.exitonclick()


if __name__ == "__main__":
    main()
