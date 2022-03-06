fruit = {}
while True:
    print("commands are:")
    print("  - set kind_of_fruit number")
    print("  - print kind_of_fruit")
    print("  - print")
    print("  - stop")

    text = input('What do you want to do? ')
    commands = text.split()
    print(commands)
    if commands[0] == 'stop':
        break
    elif commands[0] == 'set':
        # check second word and add ti t o the dictionary with the third work
        fruit[commands[1]] = int(commands[2])
        print('Done adding', commands[1], 'to the dictionary')
        # print statement saying we're done
    elif commands[0] == 'print':
        if len(commands) == 1:
            for key in fruit:
                print("There are " + str(fruit[key]) + " " + key)
        else:
            print("There are", fruit.get(commands[1], 0), commands[1])
