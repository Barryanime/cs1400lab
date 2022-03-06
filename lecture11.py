# def number_greater_than_10(number):
#     if number > 10:
#         return True
#     else:
#         return False
#
#
# print(number_greater_than_10(20))
# print(number_greater_than_10(0))
# print(number_greater_than_10(10))
#
# def letter_grade(score):
#     if score >= 90:
#         return 'A'
#     elif score >= 80:
#         return 'B'
#     else:
#         return 'C'
#
#
# print(letter_grade(50))
# print(letter_grade(60))
# print(letter_grade(70))
# print(letter_grade(80))
# print(letter_grade(90))
# print(letter_grade(95))
# print(letter_grade(100))

# def odd(number):
#     if number%2 == 1:
#         return True
#     else:
#         return False
#
#
# def delete_odd(number_list):
#     odd_list = []
#     for index in range(len(number_list)):
#         if odd(number_list[index]):
#             odd_list.append(number_list[index])
#     return odd_list
#
#
# number = delete_odd([1, 2, 3, 4, 5, 6])
# print(number)

# replace all 1's with a new number value
def replace_one_with_number(number_list, new_number):
    for i in range(len(number_list)):
        number = number_list[i]
        if number == 1:
            number_list[number] = new_number
    return number_list


# Test it
numbers = list(range(10))
numbers = replace_one_with_number(numbers, -5)
print("replaced", numbers)

numbers2 = [1, 2, 1, 3, -4, 1]
numbers2 = replace_one_with_number(numbers2, -5)
print("replaced", numbers2)

