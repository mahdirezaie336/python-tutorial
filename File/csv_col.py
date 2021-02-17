import re


def process(args):
    with open(args, 'r') as file, open('./ans.csv', 'w') as ans:
        for row in file:
            result = 0
            for i in re.split(',[\s]?', row):
                result = result + int(i)
            row = row.strip() + ', ' + str(result)
            ans.write(row + '\n')


process('./csv_col_test.txt')
