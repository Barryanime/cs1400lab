
def lines_from_file(filename):
    file = open(filename)
    lines = file.readlines()
    # Throw away the first line
    print(lines[1:])
    return lines[1:]


def votes_from_lines(lines):
    votes = []
    for line in lines:
        parts = line.split(',')
        print("part", parts)
        # Remove \n and ""
        name = parts[1].strip()
        name = name.strip('"')
        votes.append(name)
    print(votes)
    return votes


def count_votes(votes):
    tally = {}
    for vote in votes:
        tally[vote] = tally.get(vote, 0) + 1
    print(tally)
    return tally


def pick_winner(tally):
    highest_count = -1
    winner = ""
    for name, count in tally.items():
        if count > highest_count:
            highest_count = count
            winner = name
    return winner


def main():
    # scores = {"David": 62, "Anya": 98}
    # for score_key in scores:
    #
    #     # value = scores[score_key]
    #     # value += 5
    #     # scores[score_key] = value
    #
    #     # same thing as above
    #     scores[score_key] += 5
    # print(scores)
    filename = "CS1400 Vote.csv"
    lines = lines_from_file(filename)
    votes = votes_from_lines(lines)
    vote_count = count_votes(votes)
    winner = pick_winner(vote_count)
    print("The winner is", winner)


if __name__ == "__main__":
    main()
