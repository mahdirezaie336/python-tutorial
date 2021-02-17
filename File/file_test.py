def solve(args):
    with open(args, 'r') as file:
        for row in file:
            yield row


for i in solve('./sample.txt'):

