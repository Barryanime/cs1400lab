"""
Initial code by David Johnson. This code and derived works may not be posted publicly.

Code finished by Barry lin
"""

# Add your critical thinking sentences and example review here.
# When I looked at teh predictions, they all seemed to be lower than the actual value.
# When I actually type in a review, it gives me a really low value as well.
# Add your functions here.


def make_lowercase_lines_from_file(filename):
    """
    A list where each item is a line from the filename.
    Make each line lower case by calling the string lower() method

    :param filename: a string
    :return: list with lower case letters
    """
    file = open(filename)
    lines = file.readlines()
    new_list = []
    for word in lines:
        lower = word.lower()
        new_list.append(lower)
    return new_list


def make_word_total_value_dict_from_lines(values):
    """
    Return a dict that has words every word from list as keys and the total value

    :param values: lowercase string values. Starts with number with words following.
    :return:A dict with words as keys and total value of the word as value
    """
    dict_list = {}
    for value in values:
        new_list = value.split()
        score = int(new_list[0])
        for word in new_list[1:]:
            dict_list[word] = dict_list.get(word, 0) + score
    return dict_list


def make_word_total_count_dict_from_lines(values):
    """
    Returns a dict with every word from list as keys and the total number
    of times it appears in the review.

    :param values: lowercase string values. Starts with number with words following.
    :return:A dict of words as key and how many times it appears
    """
    dict_list = {}
    for value in values:
        new_list = value.split()
        for word in new_list[1:]:
            dict_list[word] = dict_list.get(word, 0) + 1
    return dict_list


def make_word_avg_value_from_total_and_count(value1, value2):
    """
    A dict with every word from the parameter and the average of the total value.
    Any word with an average between 1.75 and 2.25 should not be added.

    :param value1: word total dict
    :param value2: word count dict
    :return: A dict of the average of total value and count.
    """
    dict_list = {}
    for number in value1:
        total_value = value1.get(number)
        total_count = value2.get(number)
        avg_value = total_value / total_count
        if avg_value < 1.75 or avg_value > 2.25:
            dict_list[number] = avg_value
    return dict_list


def predict_review(review, avg_value_dict):
    """
    Return a predicted movie rating for the string.

    :param review: a string
    :param avg_value_dict: words and value
    :return: Number score predicting the movie rating.
    """
    review = review.split()
    total_score, total_count = 0, 0
    for word in review:
        if word in avg_value_dict:
            total_count += 1
            total_score += avg_value_dict.get(word)
    average = total_score/total_count
    return average


def compare_prediction_with_actual(lines, avg_value_dict):
    """
    Given a list of movie reviews and a dictionary of words and their avg value, compare
    the predicted rating with the actual rating.
    :param lines: a list of movie reviews. Each review starts with a 0 to 4 movie rating.
    :param avg_value_dict: A dict of words and their average value in a movie review rating
    :return: None. This prints out some predicted and actual score for movie reviews.
    """
    for line in lines:
        words = line.split()
        actual_score = int(words[0])
        predicted_score = predict_review(" ".join(words[1:]), avg_value_dict)
        print("predicted:", predicted_score, "actual:", line)


def main():
    """
    Read a file of movie reviews, develop a dict of word values, and use
    those to make movie rating predictions.
    """
    # Add some testing code below here. Make a small list of reviews by hand or read in a small
    # file. Make small total value and count dicts to test the avg function. Make a small
    # avg dict to test the prediction function. Make these by hand to make the tests be as independent
    # from each other as possible.
    testing = make_lowercase_lines_from_file("test_reviews.txt")
    print("Testing make word total value dict from lines function")
    print("Testing", make_word_total_value_dict_from_lines(testing))
    test_value = make_word_total_value_dict_from_lines(testing)
    print()
    print("Testing make word total count dict from lines function")
    print("Testing", make_word_total_count_dict_from_lines(testing))
    test_count = make_word_total_count_dict_from_lines(testing)
    print()
    print("Testing make word avg value from total and count")
    print("Testing", make_word_avg_value_from_total_and_count(test_value, test_count))

    # You should not need to change the code below here. You can comment out some of the print statements if
    # they are producing so much text it is confusing.

    # read the reviews into a list
    # lines = make_lowercase_lines_from_file("smallReviews.txt")
    lines = make_lowercase_lines_from_file("MovieReviews.txt")
    # print(lines)  # examine the result

    # total_value = value_from_lines(lines)
    # print(total_value)

    # Make a dict with words from reviews and their summed up values from the reviews they are in
    total_value_dict = make_word_total_value_dict_from_lines(lines)
    # print(total_value_dict)  # examine the dict to see if it looks correct

    # Count up how often a word appears in all the reviews
    total_count_dict = make_word_total_count_dict_from_lines(lines)
    # print(total_count_dict)  # examine the dict to see if it looks correct

    # Get the average value per word from the total value and their count
    avg_value_dict = make_word_avg_value_from_total_and_count(total_value_dict, total_count_dict)
    # print(avg_value_dict)  # examine the dict to see if it looks correct

    # Compare actual and predicted movie ratings for a small number of reviews
    if len(lines) < 110:
        compare_prediction_with_actual(lines, avg_value_dict)  # use all for small review files
    else:
        compare_prediction_with_actual(lines[100:110], avg_value_dict)

    # Ask the user for a movie review and predict a rating. It should be without punctuation.
    personal_review = input("Please enter a review with no punctuation: ")
    personal_review = personal_review.lower()
    prediction = predict_review(personal_review, avg_value_dict)
    print("The predicted review score is", prediction)


if __name__ == "__main__":
    main()
