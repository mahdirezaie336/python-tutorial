a, b, l = [int(x) for x in input().split()]
result = (a + b) * (l // 2)
if l % 2 == 1:
    result = result + a
print(result)
