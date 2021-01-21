a = input()
index = 0
for i in range(len(a)):
    for j in range(len(a)):
        if j < index:
            print(a[index], end='')
        else:
            print(a[j], end='')
    index = index + 1
    print()
