import json

with open('./seen_content.json', 'r') as file, open('./sorted.json', 'w') as wr:
    data = json.load(file)
    for i in data:
        wr.write(str(i) + '\n\n')
        for j in data[i]:
            wr.write(str(j) + '\n')
        wr.write('\n\n*******************************************************\n\n\n')
print('Done!')
