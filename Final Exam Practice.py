def change_things(val1, val2, list1, list2):
    val1 = 5
    val2 = 10
    list1[0] = 20
    list2 = [30, 40]
    return val2


def highest_score(grades):
    highest = None
    for name in grades:
        if not highest or grades[name] > grades[highest]:
            highest = name
    return highest


def main():
    num1 = 1
    num2 = 2
    list0 = [1, 2]
    num2 = change_things(num1, num2, list0, list0)
    print(num1, num2, list0)

    grades = {"David": 10, "Sally": 100, "Frank": 80}
    print(highest_score(grades))


if __name__ == "__main__":
    main()

