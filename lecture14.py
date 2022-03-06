def add_greater_than_90(numbers):
    """

    Sum up the numbers greater than 90
    :param numbers:
    :return: the summed numbers greater than 90
    """

    sum = 0
    for number in numbers:
        if number > 90:
            sum += number
        return sum

    def first_multiple_of_five(numbers):
        """
        Return the first number in numbers that is a multiple of 5


        :param numbers: list of numbers
        :return: the first multiple of five
        """

        for number in numbers:
            if number%5 == 0:
                return number
        return None

    def biggest_multiple_of_five(numbers):
        # search for the first multiple
        biggest = first_multiple_of_five(numbers)
        # If no multiples of 5 in list, return None
        if biggest == None:
            return None
        # Look for the biggest multiple of five
        for number in numbers:
            if number%5 == 0 and number > biggest:
                biggest = number
        return biggest


    def biggest_multiple_of_five2(numbers):
        biggest = None
        # Look for the biggest multiple of five
        for number in numbers:
            if number%5 == 0 and (biggest == None or number > biggest):
                biggest = number
        return biggest

