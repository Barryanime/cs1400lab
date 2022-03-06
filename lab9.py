def is_word_in_list(word_to_find, words):
    for word in words:
        if word == word_to_find:
            print("We are finding", word_to_find, "and the word is", word)
            return True
    return False


def is_num_in_list(number_to_find, numbers):
    for num in numbers:
        if num == number_to_find:
            print("We are finding", number_to_find, "and the number is", num)
            return True
    return False


def is_nums_in_list(number_to_find, numbers):
    for num in numbers:
        print("We are finding", number_to_find, "and the number is", num)
        if num <= number_to_find + 5 and num >= number_to_find - 5:
            return True
    return False


def location_of_num(number_to_find, num):
    for index in range(len(num)):
        print("We are finding", number_to_find, "and the number is", num[index])
        if num[index] <= number_to_find + 5 and num[index] >= number_to_find - 5:
            return True
    return False


print(is_word_in_list("Sally", ["David", "Sally", "Maria"]))
print(is_nums_in_list(1, [3, 5, 3, 5, 3, 1]))
print(location_of_num(1, [3, 5, 3, 5, 3, 1]))


def shortest_word_in_list(words):
    short_word = words[0]
    for word in words:
        print("Shortest word so far is", short_word, "and the word is", word)
        if len(word) < len(short_word):
            short_word = word
    return short_word

print(shortest_word_in_list(["cat", "an", "dogs", "I", "you"]))