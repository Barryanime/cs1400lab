# Assignment A6
# CS 1400
# Starter code by Barry Lin

# Assignment completed by

# The multiply function computes the product of two factors
def multiply(factor1, factor2):
    product = 0
    for loop_counter in range(factor2):
        product += factor1
    return product


# The choose smaller function chooses the smaller number between the two
def choose_smaller(num1, num2):
    # set the value to 0
    value = 0
    # if first number is smaller, print first number
    if num1 < num2:
        value = num1
    # if second number is smaller, print second number
    elif num2 < num1:
        value = num2
    return value


# The describe number function states if the number is zero, positive or negative
def describe_number(number):
    # if number equals zero, return zero
    if number == 0:
        return 'zero'
    # if number is greater than zero, return positive
    elif number > 0:
        return 'positive'
    # returns negative if the number is not zero or greater than zero
    else:
        return 'negative'


# The add a or an to word function adds an if the first letter is a vowel and adds a if the first letter is not a vowel
def add_a_or_an_to_word(letter):
    # if the first letter is a vowel, add an in front of the word
    if letter[0] == 'a' or letter[0] == 'e' or letter[0] == 'i' or letter[0] == 'o' or letter[0] == 'u':
        word = 'an ' + letter
    # if the first letter is not a vowel, add a in front of the word
    else:
        word = 'a ' + letter
    return word


# The add a or an or any to word function adds any if the last letter is an s
def add_a_or_an_or_any_to_word(letter):
    # if the first letter is a vowel, add an in front of the word
    if letter[0] == 'a' or letter[0] == 'e' or letter[0] == 'i' or letter[0] == 'o' or letter[0] == 'u':
        word = 'an ' + letter
    # if the last letter is an s, add any in front of the word
    elif letter[-1] == 's':
        word = 'any ' + letter
    # else, add a in front of the word
    else:
        word = 'a ' + letter
    return word


# The pirate translate function replaces words with pirate speech
def pirate_translate(sentence):
    # Split it into list of words
    word_list = sentence.split()
    for i in range(len(word_list)):
        # if the word is my replace it with me
        if word_list[i] == 'my':
            word_list[i] = 'me'
        # if the word is you replace it with ye
        elif word_list[i] == 'you':
            word_list[i] = 'ye'
        # if the word is is or are, replace it with be
        elif word_list[i] == 'is' or word_list[i] == 'are':
            word_list[i] = 'be'
        # if the word is hello replace it with ahoy
        elif word_list[i] == 'hello':
            word_list[i] = 'ahoy'
        # if the word is friend replace it with matey
        elif word_list[i] == 'friend':
            word_list[i] = 'matey'
    # join the list of words to form a new sentence
    new_word_list = " ".join(word_list)
    return new_word_list


# Main tests all the functions and reports on their results
def main():
    print("Testing the multiply function")
    print("Testing multiply(2,3). Expecting a result of 6 and computed a result of", multiply(2, 3))
    print("Testing multiply(5,6). Expecting a result of 30 and computed a result of", multiply(5, 6))
    print()
    print("Testing the choose smaller function")
    print("Testing choose_smaller(10, 20). Expecting a result of 10 and got a result of", choose_smaller(10, 20))
    print("Testing choose_smaller(20, 0). Expecting a result of 0 and got a result of", choose_smaller(20, 0))
    print()
    print("Testing the describe number function")
    print("Testing describe_number(-12). Expecting a result of negative and got a result of", describe_number(-12))
    print("Testing describe_number(0). Expecting a result of zero and got a result of", describe_number(0))
    print("Testing describe_number(10). Expecting a result of positive and got a result of", describe_number(10))
    print()
    print("Testing the add a or an to word function")
    print("Testing add_a_or_an_to_word('ant'). Expecting: an ant and got", add_a_or_an_to_word("ant"))
    print("Testing add_a_or_an_to_word('bear'). Expecting: a bear and got", add_a_or_an_to_word("bear"))
    print()
    print("Testing the add a or an or any to word function")
    print("Testing add_a_or_an_or_any_to_word('cats'). Expecting: any cats and got", add_a_or_an_or_any_to_word("cats"))
    print("Testing add_a_or_an_or_any_to_word('animal'). Expecting: an animal and got", add_a_or_an_or_any_to_word("animal"))
    print("Testing add_a_or_an_or_any_to_word('bug'). Expecting: a bug and got", add_a_or_an_or_any_to_word("bug"))
    print("Testing add_a_or_an_or_any_to_word('snake'). Expecting: a snake and got", add_a_or_an_or_any_to_word("snake"))
    print()
    print("Testing the pirate translate function")
    print("Testing pirate_translate('you are a computer scientist'). Expecting: ye be a computer scientist and got",
          pirate_translate("you are a computer scientist"))
    print("Testing pirate_translate('hello friend'). Expecting: ahoy matey and got", pirate_translate("hello friend"))
    print("Testing pirate_translate('how are you'). Expecting: how be ye and got", pirate_translate("how are you"))


if __name__ == "__main__":
    main()
