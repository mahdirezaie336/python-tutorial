users = {}
albums = {}

n = int(input())
inputs = []
line = ''
while not (line := input()).isdecimal():
    inputs.append(line)

index = 0
for i in range(n):
    name = inputs[index].split()[2]
    index = index + 1
    age = inputs[index]
    
