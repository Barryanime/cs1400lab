"""
Initial code by David Johnson. This code and derived works may not be posted publicly.

Code finished by
"""

# Add your critical thinking sentences and example review here.

# Add your functions here.


def make_lowercase_lines_from_file(filename):
    file = open(filename)
    lines = file.readlines()
    new_list = []
    for word in lines:
        lower = word.lower()
        new_list.append(lower)
    return new_list


def make_word_total_value_dict_from_lines(values):
    dict_list = {}
    for value in values:
        new_list = value.split()
        score = int(new_list[0])
        # print("new lists", new_lists)
        for word in new_list[1:]:
            dict_list[word] = dict_list.get(word, 0) + score
    return dict_list


def make_word_total_count_dict_from_lines(values):
    dict_list = {}
    for value in values:
        new_list = value.split()
        for word in new_list[1:]:
            dict_list[word] = dict_list.get(word, 0) + 1
    return dict_list


def make_word_avg_value_from_total_and_count(value1, value2):
    dict_list = {}
    for number in value1:
        # grab score by number(key)
        # grab count by number(key)
        total_value = value1.get(number)
        total_count = value2.get(number)
        avg_value = total_value / total_count
        if avg_value < 1.75 or avg_value > 2.25:
            dict_list[number] = avg_value
    return dict_list


def predict_review(review, avg_value_dict):
    review = review.split()
    total_score, total_count = 0, 0
    for word in review:
        if word in avg_value_dict:
            total_count += 1
            total_score += avg_value_dict.get(word)
    avg = total_score/total_count
    return avg


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

    # You should not need to change the code below here. You can comment out some of the print statements if
    # they are producing so much text it is confusing.

    # read the reviews into a list
    # lines = make_lowercase_lines_from_file("smallReviews.txt")
    lines = make_lowercase_lines_from_file("MovieReviews.txt")
    print(lines)  # examine the result

    # total_value = value_from_lines(lines)
    # print(total_value)

    # Make a dict with words from reviews and their summed up values from the reviews they are in
    total_value_dict = make_word_total_value_dict_from_lines(lines)
    print(total_value_dict)  # examine the dict to see if it looks correct

    # Count up how often a word appears in all the reviews
    total_count_dict = make_word_total_count_dict_from_lines(lines)
    print(total_count_dict)  # examine the dict to see if it looks correct

    # Get the average value per word from the total value and their count
    avg_value_dict = make_word_avg_value_from_total_and_count(total_value_dict, total_count_dict)
    print(avg_value_dict)  # examine the dict to see if it looks correct

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
