inputs = input().split()

n = int(inputs[0])
st = set(inputs[1])

for i in range(n):
    p = input()
    if set(p) == st:
        print('yes')
    else:
        print('no')
