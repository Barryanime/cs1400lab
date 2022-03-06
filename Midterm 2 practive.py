# dict = {3: 1, 4: 2, 5: 3}
# print(dict.get(1, 0))
# print(dict.get(5, dict[2]))

def mystery(number):
    if number <= 1:
        return 1
    return 1 + mystery(number // 2)


print(mystery(40))
