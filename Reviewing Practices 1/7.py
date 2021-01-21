def check(x, y):
    if x == y:
        return 2 * x + (0 if x % 2 == 0 else -1)
    if x - 2 == y:
        return 2 * y + (2 if y % 2 == 0 else 1)
    return -1


for i in range(int(input())):
    a, b = [int(j) for j in input().split()]
    print(check(a, b))
