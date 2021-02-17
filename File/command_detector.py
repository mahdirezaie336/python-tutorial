def solve(args):
    number = 0
    with open(args, 'r') as file:
        for row in file:
            row = row.strip()
            if row != '' and not row.startswith('#'):
                number = number + 1
    return number


print(solve('./sample.txt'))
