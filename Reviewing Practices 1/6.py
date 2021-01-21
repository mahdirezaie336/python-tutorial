a = []
for i in range(5):
    s = input()
    if 'MOLANA' in s or 'HAFEZ' in s:
        a.append(i + 1)

if len(a) == 0:
    print('NOT FOUND!')
else:
    for i in a:
        print(i)
