with open('./sample.txt', 'r+') as file:
    file.truncate(0)
    file.write('Hello from all of the children of planet Earth\n')
    file.flush()
    file.seek(0)
    print(file.readline())
