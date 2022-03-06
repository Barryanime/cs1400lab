"""
    A8 starter code written by David Johnson. All derived works must not
    be posted publicly.

    A8 assignment completed by
"""
# import random
# import random

# Fill in the required assignment functions here.


def curve_scores(numbers):
    """
    Return a new list that change the highest number in the list to 100
    and the other numbers move up the same amount

    :param numbers: List of integer number that range from 0 to 100
    :return: A list of numbers with the highest being 10 and all others moving up the same amount
    """
    biggest_number = 0
    curve_list = []
    for num in numbers:
        if num > biggest_number:
            biggest_number = num
    value = 100 - biggest_number
    for num in numbers:
        curve_list.append(num + value)
    return curve_list


def contains_duplicate(words):
    """
    Return True if the list contains the same string two or more times
    and false if it only contains the string once

    :param words: A list of string values
    :return: True if list contains same string, otherwise false
    """
    for index in range(len(words)):
        for index2 in range(index + 1, len(words)):
            if words[index2] == words[index]:
                return True
    return False


def list_to_string(numbers):
    """
    Return string that contains text representation of a list.
    Same as if we do print(list).

    :param numbers: List of integer values
    :return:String containing text representation of a list
    """
    string_list = ""
    string_list += '['
    for number in numbers[:-1]:
        string_list += str(number) + ',' + ' '
    for number in numbers[-1:]:
        string_list += str(number)
    string_list += ']'
    return string_list


def lines_from_file(filename):
    """
    Return a new list of strings where each string is a line from the file

    :param filename: String with name of file to read the lines
    :return: New list where each string is a line from the file
    """
    file = open(filename)
    lines = file.readlines()
    return lines


def binary_search_for_key(key, values):
    """
    Return the location of key in values, or None if no match. This function uses
    binary search to efficiently search a sorted list.

    :param key: The item to search for
    :param values: A sorted list of values
    :return: The location of the matching item or None if no match.
    """
    lo = 0
    hi = len(values) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if values[mid] == key:
            return mid
        elif values[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def binary_search_for_matching_string(key, values):
    """
    Return the full string from the list if a string in the list starts with the key string.
    Otherwise return None

    :param key: The item to search for
    :param values: A sorted list of values
    :return: The full string from the list or none if it doesn't start with the key string
    """
    lo = 0
    hi = len(values) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if values[mid].startswith(key):
            return values[mid]
        elif values[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def main():
    print("Testing the curve scores function")
    print("Testing curve_scores([10, 20, 30, 40])", "Expecting a result of [70, 80, 90, 100]")
    print("Got the result of", curve_scores([10, 20, 30, 40]))
    print("Testing curve_scores([0, 100, 25, 30, 32])", "Expecting a result of [0, 100, 25, 30, 32]")
    print("Got the result of", curve_scores([0, 100, 25, 30, 32]))
    print("Testing curve_scores([5, 12, 0])", "Expecting a result of [93, 100, 88]")
    print("Got the result of", curve_scores([5, 12, 0]))
    print()
    print("Testing the contains duplicate function")
    print("Testing contains_duplicate(['the', 'boy', 'the'])", "Expecting a result of True")
    print("Got the result of", contains_duplicate(['the', 'boy', 'the']))
    print("Testing contains_duplicate(['hi', 'how', 'are', 'you'])", "Expecting a result of False")
    print("Got the result of", contains_duplicate(['hi', 'how', 'are', 'you']))
    print("Testing contains duplicate(['am', 'I', 'to', 'am', 'am', 'you'])", "Expecting a result of True")
    print("Got the result of", contains_duplicate(['am', 'I', 'to', 'am', 'am', 'you']))
    print()
    print("Testing the list to string function")
    print("Testing list_to_string([1, 2, 3])", "Expecting a result of [1, 2, 3]")
    print("Got the result of", list_to_string([1, 2, 3]))
    print("Testing list_to_string([0, 3, -5, 71, 3])", "Expecting a result of [0, 3, -5, 71, 3]")
    print("Got the result of", list_to_string([0, 3, -5, 71, 3]))
    print("Testing list_to_string([])", "Expecting a result of []")
    print("Got the result of", list_to_string([]))
    print()
    print("Testing the binary search for matching string function")
    print("Testing binary_search_for_matching_string('ca', ['apple', 'cat', 'dog'])", "Expecting a result of cat")
    print("Got the result of", binary_search_for_matching_string("ca", ["apple", "cat", "dog"]))
    print("Testing binary_search_for_matching_string('do', ['dog', 'mouse', 'bird'])", "Expecting a result of dog")
    print("Got the result of", binary_search_for_matching_string("do", ["dog", "mouse", "bird"]))
    print("Testing binary_search_for_matching_string('bu', ['butterfly', 'cat', 'dog'])", "Expecting: butterfly")
    print("Got the result of", binary_search_for_matching_string("bu", ["butterfly", "cat", "dog"]))


if __name__ == "__main__":
    main()
