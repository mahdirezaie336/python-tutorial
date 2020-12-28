a = [0]*11
a[0] = 1
a[1] = 2

for i in range(9):
    a[i+2] = a[i+1] + a[i]

n = int(input())
for i in range(1, n+1):
    if i in a:
        print('+', end='')
    else:
        print('-', end='')
