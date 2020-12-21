file = open('./sample.txt', 'w')

file.write('Hello there baby\n')
file.close()
file = open('./sample.txt', 'r')
print(file.readline())
file.close()
