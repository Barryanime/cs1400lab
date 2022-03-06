"""
    A8 starter code written by David Johnson. All derived works must not
    be posted publicly.

    A8 assignment completed by
"""
# import random
import random


def curve_scores(list1):
    """
    Take a list of integer numbers that can
    range from 0 to 100 and curve them from
    the original list into a new list.
    :param list1:A list containing integer numbers
    ranging from 0 to 100.
    :return: A new list of numbers so the highest number
    in the list is 100 and the other numbers move up by
    the same amount.
    """
    biggest_so_far = 0
    for number in list1:
        if number > biggest_so_far:
            biggest_so_far = number
    added_value = 100 - biggest_so_far
    new_score = []
    for index in range(len(list1)):
        # changed_scores = added_value + list1[index]
        # new_score.append(changed_scores)

        new_score.append(added_value + list1[index])

    return new_score


def contains_duplicate(my_list):
    """
    Takes a list with string values and checks
    if there are duplicates.
    :param my_list: A list of string values.
    :return: Returns True if the list contains
    a duplicate, otherwise it's False.
    """
    for index in range(len(my_list)):
        for i in range(index, len(my_list)-1):
            if my_list[index] == my_list[i+1]:
                return True
    return False


def list_to_string(my_list):
    """
    Take a list of integer values and return it as
    a string.
    :param my_list: A list of integer values
    in a list.
    :return: Return the list of integer values
    as a string.
    """
    new_string = "["
    for index in range(len(my_list)):
        new_string = new_string + str(my_list[index])
        if index != len(my_list)-1:
            new_string = new_string + ", "
    new_string = new_string + "]"
    return new_string


def lines_from_file(file_name):
    """
    Imports file from city.txt and reads each line.
    :param file_name: File named city.txt.
    :return: The lines from the file.
    """
    cities = open(file_name,encoding='utf-8')
    lines = cities.readlines()
    return lines

def binary_search_for_matching_string(key, list):
    """
    Return the location of key in list, or None if no match. This function uses
    binary search to efficiently search a sorted list.

    :param key: The item to search for.
    :param list: List of words.
    :return: The location of the matching item or None if there
    is no match.
    """
    lo = 0
    hi = len(list) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if list[mid].startswith(key):
            return list[mid]
        elif list[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

def main():
    print(curve_scores([45, 85, 90]))
    print(contains_duplicate(["hi", "bye"]))
    print(contains_duplicate(["hi", "bye", "the", "the"]))
    print(list_to_string([1, 2, 3]))
    print(list_to_string([4, 5, 6]))
    print(list_to_string([7, 8, 9]))
    print(binary_search_for_matching_string("ca",["apple","cat","dog"]))
    print(binary_search_for_matching_string("ap", ["apple", "cat", "dog"]))
    print(binary_search_for_matching_string("liz", ["pear", "lizard", "duck"]))


if __name__ == "__main__":
    main()
