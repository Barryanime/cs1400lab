from random import *
# Functions to process audio.
# For CS 1400, written by David E. Johnson.
# Function implementations by

# Add your functions below this line


def make_reversed_samples(numbers):
    """
    Return the list in reverse.

    :param numbers:a list of numbers
    :return: The list in reverse
    """
    reverse_number = []
    for number in numbers:
        reverse_number = [number] + reverse_number
    return reverse_number


def make_louder_samples(numbers, scale):
    """
    Return with a new list that is multiplies by the scale parameter.

    :param numbers: a list of zero or more numbers
    :param scale: a number
    :return: new scaled list of numbers
    """
    scale_list = []
    for number in numbers:
        scale_list.append(number * scale)
    return scale_list


def make_clipped_samples(numbers, clip):
    """
    Make a new list with values of new elements set to be within a certain range.

    :param numbers: a list of zero or more numbers
    :param clip: a number
    :return: new list of clipped values
    """
    clip_list = []
    for number in numbers:
        if number >= clip:
            clip_list.append(clip)
        elif number <= -clip:
            clip_list.append(-clip)
        else:
            clip_list.append(number)
    return clip_list


def make_noisy_samples(numbers, noise):
    """
    Make a new list with some noise added to each value

    :param numbers: a list of zero or more numbers
    :param noise: a number
    :return: new list of noisy samples
    """
    noisy_list = []
    for number in numbers:
        value = randint(-noise, noise)
        noisy_list.append(number + value)
    return noisy_list


def make_smoothed_samples(numbers):
    """
    Make a new list with the same elements and each element of the new list is the average of the values around it

    :param numbers: list of three or more values
    :return: new list with the average of the elements around it
    """
    smooth_list = []
    for number in range(len(numbers)):
        if number == 0:
            smooth_list.append((numbers[0] + numbers[1])//2)
        elif number == len(numbers) - 1:
            smooth_list.append((numbers[-1] + numbers[-2])//2)
        else:
            smooth_list.append((numbers[number - 1] + numbers[number] + numbers[number + 1])//3)
    return smooth_list


# You can add small test examples here and see results from running this file instead
# of the SoundApp
def main():
    print("Testing the make reversed samples function")
    print("Testing make_reversed_samples([1, 2, 3, 4, 5])", "Expecting a result of [5, 4, 3, 2, 1]")
    print("Got the result of", make_reversed_samples([1, 2, 3, 4, 5]))
    print("Testing make_reversed_samples([0, 34, 0, 67, 8])", "Expecting a result of [8, 67, 0, 34, 0]")
    print("Got the result of", make_reversed_samples([0, 34, 0, 67, 8]))
    print("Testing make_reversed_samples([-1, 0, 65, -23, 5])", "Expecting a result of [5, -23, 65, 0, -1]")
    print("Got the result of", make_reversed_samples([-1, 0, 65, -23, 5]))
    print()
    print("Testing the make louder samples function")
    print("Testing making_louder_samples([1, 2, 3], 2)", "Expecting a result of [2, 4, 6]")
    print("Got a result of", make_louder_samples([1, 2, 3], 2))
    print("Testing making_louder_samples([1, 3, 5], 4)", "Expecting a result of [4, 12, 20]")
    print("Got a result of", make_louder_samples([1, 3, 5], 4))
    print("Testing making_louder_samples([5, 6, -3], -5)", "Expecting a result of [-25, -30, 15]")
    print("Got a result of", make_louder_samples([5, 6, -3], -5))
    print()
    print("Testing the make clipped_samples function")
    print("Testing make_clipped_samples([-5, -1, 2, 5, 10], 4)", "Expecting a result of [-4, -1, 2, 4, 4]")
    print("Got a result of", make_clipped_samples([-5, -1, 2, 5, 10], 4))
    print("Testing make_clipped_samples([12, 1, 5, 6, -1], 6)", "Expecting a result of [6, 1, 5, 6, -1]")
    print("Got a result of", make_clipped_samples([12, 1, 5, 6, -1], 6))
    print("Testing make_clipped_samples([14, 6, 34, 10, -16], -30)", "Expecting a result of [0, -3, -1, 3, 3]")
    print("Got a result of", make_clipped_samples([0, -12, -1, 19, 3], 3))
    print()
    print("Testing the make noisy samples function")
    print("Testing make_noisy_samples([10,20,20], 2)", "Expecting a result of number within the noisy level number")
    print("Got a result of", make_noisy_samples([10, 20, 30], 2))
    print("Testing make_noisy_samples([3,12,-20], 6)", "Expecting a result of number within the noisy level number")
    print("Got a result of", make_noisy_samples([3, 12, -20], 6))
    print("Testing make_noisy_samples([2,20,20], 3)", "Expecting a result of number within the noisy level number")
    print("Got a result of", make_noisy_samples([2, 20, 20], 3))
    print()
    print("Testing the make smoothed samples function")
    print("Testing make_smoothed_samples([3, 5, 7, 3, 5]", "Expecting a result of [4, 5, 5, 5, 4]")
    print("Got a result of", make_smoothed_samples([3, 5, 7, 3, 5]))
    print("Testing make_smoothed_samples([4, 2, 4, 12, 32]", "Expecting a result of [3, 3, 6, 16, 22]")
    print("Got a result of", make_smoothed_samples([4, 2, 4, 12, 32]))
    print("Testing make_smoothed_samples([-3, -15, 37, 3, 5]", "Expecting a result of [-9, 6, 8, 15, 4]")
    print("Got a result of", make_smoothed_samples([-3, -15, 37, 3, 5]))


if __name__ == "__main__":
    main()
