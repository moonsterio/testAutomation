i = 0
def remove(item):
    global i
    if i == 0:
        list.remove(item)
        i = 1


if __name__ == '__main__':
    list = []

    if command[0] == 'insert':
        list.insert(command[1], command[2])
    elif command[0] == 'print':
        print(list)
    elif command[0] == 'remove':
        [remove(item) for item in list if item == command[1]]
    elif command[0] == 'append':
        list.append(command[1])
    elif command[0] == 'sort':
        list.sort()
    elif command[0] == 'pop':
        list.pop()
    elif command[0] == 'reverse':
        list.reverse()

