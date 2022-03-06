def sum_numbers(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_numbers(numbers[1:])


# print(sum_numbers([1, 2, 3]))

# print(sum_numbers([1, 2, 3, [4, 5]]))


def sum_nested(numbers):
    sum = 0
    for item in numbers:
        if type(item) != list:
            sum += item
        else:
            sum += sum_nested(item)
    return sum


print(sum_nested([1, 2, [4, 5, [8, 9]]]))
print(sum_nested([1, 2, [4, 5, [8, 9, 9, [6, 5, 4]]]]))
