def count_a_letters(text):
    letter_a_count = 0
    for index in range(len(text)):
        # instrument the code
        print("At index", index, "the letter is", text[index])
        if text[index] == 'a':
            letter_a_count = letter_a_count + 1
            print('Updated count to be', letter_a_count)
    return letter_a_count


def count_a_letters2(text):
    letter_a_count = 0
    for letter in text:
        print("At letter", letter)
    if letter == 'a':
        letter_a_count += 1
    return letter_a_count

def remove_a_letter(text):
    no_a_string = ""
    for letter in text:
        if letter != "a":
            no_a_string += letter
    return no_a_string

def main():
    no_a = remove_a_letter("a cat is a large animal")
    print(no_a)


if __name__ == "__main__":
    main()
