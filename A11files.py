"""
Initial code written by David Johnson, University of Utah.
This, and all derived works may not be publicly shared.

Recursive versions written by Barry Lin
"""
import os


def find_target_in_nested_list(value, nested_list):
    """
    Return true if the value that we are searching for is in the list. False if not

    :param value: a number
    :param nested_list: single value, list, or nested list
    :return: True or False
    """
    if type(value) == int:
        for num in nested_list:
            if num == value:
                return True
            else:
                return False
    elif type(value) == list:
        for num in nested_list:
            if num == value:
                return False
            else:
                return True


def find_file_in_folder(file, folder, path):
    """
    return true if the folder is found in the second parameter, false otherwise.

    :param file:string with filename
    :param folder:folder name to look for
    :param path:path to look for
    :return:True or False
    """
    for item in os.listdir(folder):
        if item == file:
            if item == path:
                return True
        else:
            return False


def main():
    print("Testing the function find target in nested list")
    print("Expecting a result of True, Got a result of", find_target_in_nested_list(3, [1, [2, 3], 4]))
    print("Expecting a result of False, Got a result of", find_target_in_nested_list(3, 5))
    print()
    print("Testing the function find file in folder")
    print("Expecting a result of True, Got a result of", find_file_in_folder("A.txt", "f1", ""))
    print("Expecting a result of False, Got a result of", find_file_in_folder("f2", "f1", ""))


if __name__ == "__main__":
    main()
