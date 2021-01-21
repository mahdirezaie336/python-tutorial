r, c = [int(i) for i in input().split()]
a = 11 - r
print('Left ' + str(a) + ' ' + str(21 - c) if c > 10 else 'Right ' + str(a) + ' ' + str(c))
