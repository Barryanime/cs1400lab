def double_it(numbers):
    numbers = [2*number for number in numbers]
    return numbers


my_list = [1, 2, 3]
my_list = double_it(my_list)
print(my_list)
