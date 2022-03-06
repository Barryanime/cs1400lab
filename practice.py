# value = 0
# for val in [1,2,3,4]:
#     for val2 in range(val):
#         value += 1
#
# print(value)
#
# numbers = [-1, 0, 1, 3]
# less_zero = 0
# for num in numbers:
#     if num < 0:
#         less_zero += 1
# print(less_zero)

# numbers = [1, 2, 4, 3, 5]
# for numbers in numbers:
#     if numbers <= 5 and numbers >= -5:
#         print(numbers)
#
# def multiply(num1, num2):
#     solution = 0
#     for x in range(num2):
#         solution += num1
#     return solution
#
#
# solution1 = multiply(123, 123)
# print(solution1)
#
# def multiply(factor1, factor2):
#     product = 0
#     for iteration in range(factor2):
#         product = product + factor1
#     return product
#
#
# product1 = multiply(5, 3)
# print(product1)
#
# value = 5
# count = 1
# for count in range(value):
#     count += 1
#     value = value - 2
# print(count)
# print(value)
#
# vals = [1, 2, 3, 4]
# # for val in vals:
# #     val += 1
# for index in range(len(vals)):
#     vals[index] += 1
# print(vals)

# def A(val):
#     val = val + 1


# def B(val):
#     return val + 2
#
# val = 1
# A(2)
# B(val)
# print(val)
# print(B(val))

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num >= -5 and num <= 5:
#         print(num)

# for num in range(10, 41):
#     num_str = str(num)
#     if num_str[0] == '2' or num_str[1] == '2':
#         print(num)
#
# for number in range(10, 41):
#     number_string = str(number)
#     if number_string[0] == '2' or number_string[1] == '2':
#         print(number)
#
# sum = 0
# for number in range(2, 10, 2):
#     sum = sum + number
# print(sum)
value = 0
for num in range(1, 6):
    value = value + input('type in a number')
    print(value)