import os


def count_files(folder):
    count = 0
    for item in os.listdir(folder):
        full_name = os.path.join(folder, item)
        print("checking", full_name)
        if os.path.isfile(full_name):
            count += 1
    return count


print(count_files("exampleFolder"))
