def rev(og_string):
    reverse_string = ""
    for letter in og_string:
        reverse_string = letter + reverse_string
    return reverse_string


def main():
    name = "barry"
    print(rev(name))


if __name__ == "__main__":
    main()
