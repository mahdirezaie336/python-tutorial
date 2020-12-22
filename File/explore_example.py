import os


def explore(file_type, file_address):
    dic = {}
    for i in os.walk(file_address):
        number = 0
        for j in i[2]:
            if j.lower().endswith('.' + file_type.lower()):
                number = number + 1
        if number != 0:
            dic[i[0]] = number
    return dic


print(explore('jpeeg', '../../00tmp'))
