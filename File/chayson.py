import json
import re

data = {}
s = int(input())
for i in range(s):
    line = input()
    if line.startswith('print'):
        line_elements = line.split()
        args = line_elements[1].split('[')
        name = args[0]
        value = args[1].split(']')[0]
        if value.startswith('"') or value.startswith("'"):
            value = value.split('"')[1]
            print(data[name][value])
        else:
            print(data[name][int(value)])
    else:
        args = re.split('[\s]*:=[\s]*', line)
        data[args[0]] = json.loads(args[1])
