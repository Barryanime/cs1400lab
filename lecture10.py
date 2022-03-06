def positives(numbers):
    # start somewhere
    positive_numbers = []
    # build up the answer
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    # return the answer
    return positive_numbers


vals = [3, 5, -2, -20, 0 ,1]
positive_vals = positives(vals)
print(positive_vals)
