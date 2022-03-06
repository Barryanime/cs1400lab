"""
    A8 starter code written by David Johnson. All derived works must not
    be posted publicly.

    A8 assignment completed by Jonah Garner
"""
#import random
import random

# Fill in the required assignment functions here.

def curve_scores(scores):
    """
    Return adjusted scores such that the max score is 100

    :param scores: A list of scores
    :return: A list where top score has been increased to 100 and all other scores similarly increased
    """
    maximum = scores[0]
    for score in scores:
        if score > maximum:
            maximum = score
    increase = 100 - maximum
    for index in range(len(scores)):
        scores[index] += increase
    return scores

def contains_duplicate(list):
    """
    True if there is a duplicate list entry, false otherwise

    :param list: A list of anything
    :return: True if any two entries in the list are identical, otherwise False
    """
    for index_1 in range(len(list)-1):
        for index_2 in range(index_1+1, len(list)):
            if list[index_1] == list[index_2]:
                return True
    return False

def list_to_string(list):
    """
    convert a list into a string that appears identical

    :param list: a list of integers
    :return: a string that looks identical to the input list
    """
    if list == []:
        return '[]'
    string_of_list = '['
    string_of_list += str(list[0])
    for index in range(1, len(list)):
        string_of_list += ',' + str(list[index])
    string_of_list += ']'
    return string_of_list

def lines_from_file(filename):
    """Read the lines from a file"""
    file = open(filename, encoding="utf-8")
    lines = file.readlines(5)
    return(lines)

def binary_search_for_matching_string(key, words):
    """
    Return a word from words that starts with the input string

    :param key: The string to search for
    :param words: A sorted list of words
    :return: The word that starts with the input string or None if no match.
    """
    lo = 0
    hi = len(words) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if words[mid].startswith(key):
            return words[mid]
        elif words[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


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


def main():
    print("Testing curve_scores")
    print("Testing curve_scores([50, 70, 90]). The expected result is [60, 80, 100], the actual result is", curve_scores([50, 70, 90]))
    print("Testing curve_scores([75, 100, 85]). The expected result is [75, 100, 85], the actual result is", curve_scores([75, 100, 85]))
    print()
    print("Testing contains_duplicate")
    print("Testing contains_duplicate(['a', 'b', 'c', 'd']). The expected result is False, the actual result is", contains_duplicate(['a', 'b', 'c', 'd']))
    print("Testing contains_duplicate(['a', 'b', 'c', 'b']). The expected result is True, the actual result is", contains_duplicate(['a', 'b', 'c', 'b']))
    print()
    print("Testing list_to_string")
    print("Testing list_to_string([1, 2, 3, 4]). The expected result is [1, 2, 3, 4], the actual result is", list_to_string([1, 2, 3, 4]))
    print("Testing list_to_string([]). The expected result is [], the actual result is", list_to_string([]))
    print()
    print("Testing binary_search_for_matching_string")
    print("Testing binary_search_for_matching_string('hello',['hello', 'there', 'sir']). The expected result is hello, the actual result is", binary_search_for_matching_string('hello',['hello', 'there', 'sir']))
    print("Testing binary_search_for_matching_string('missing', ['key', 'not', 'present']). The expected result is None, the actual result is", binary_search_for_matching_string('missing', ['key', 'not', 'present']))


if __name__ == "__main__":
    main()

