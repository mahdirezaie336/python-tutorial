file = open('./sample.txt', 'r+')

file.truncate(0)
file.write('Hello from the children of planet Earth\n')
file.flush()
file.seek(0)
print(file.readline())
file.close()
