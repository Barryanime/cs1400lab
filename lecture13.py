def count_as(text):
    count = 0
    for letter in text:
        print("current count is", count, "letter is", letter)
        if letter == "A":
            count += 1
    return count


print(count_as("An A is in A string"))
print(count_as("there is no a's in this"))


def collect_As(text):
    As = ""
    for letter in text:
        if letter == "A":
            As = As + "A"
    return As


print(collect_As("An A is in A string"))
print(collect_As("there is no a's in this"))


def is_letter_in_text(letter_to_find, text):
    for letter in text:
        print("letter to find", letter_to_find, "current letter", letter)
        if letter == letter_to_find:
            return True
    return False


print(is_letter_in_text("a", "David"))


def location_of_letter_in_text(letter_to_find, text):
    for index in range(len(text)):
        print("letter to find", letter_to_find, "current index", index, "letter", text[index])
        if text[index] == letter_to_find:
            return index
    return "Letter not found"


print(location_of_letter_in_text("a", "David"))

name = "David"
location = location_of_letter_in_text("z", name)
if location != "Letter not found":
    print(name[location])
else:
    print("Not Found")


def biggest_positive_number(numbers):
    biggest_so_far = 0
    for number in numbers:
        print("Biggest so far", biggest_so_far, "current number", number)
        if number > biggest_so_far:
            biggest_so_far = number
    return biggest_so_far


print(biggest_positive_number([5, 10, 2, 20, 4]))


def smallest_positive_number(numbers):
    smallest_so_far = numbers[0]
    for number in numbers:
        print("Smallest so far", smallest_so_far, "current number", number)
        if number < smallest_so_far:
            smallest_so_far = number
    return smallest_so_far


print(smallest_positive_number([5, 10, 2, 20, 4]))
