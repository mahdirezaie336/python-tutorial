users = {}
albums = {}

n = int(input())
buffer = ''
for i in range(n):
    if buffer == '':
        name = input().split()[2]
    else:
        name = buffer.split()[2]
    age = input().split()[1]
    city = input().split()[1]
    album = set()
    input()
    buffer2 = ''
    while not (buffer2 := input()).startswith('-'):
        if buffer2.isdecimal():
            break
        album.add(buffer2.split()[1])
    buffer = buffer2
    users[name] = [age, city, album]

m = int(buffer)
for i in range(m):
    name = input().split()[2]
    singer = input().split()[1]
    genre = input().split()[1]
    tracks = int(input().split()[1])
    albums[name] = [singer, genre, tracks]

p = int(input())
for i in range(p):
    opcode, operand1, operand2 = input().split()

    # case: number of musics that a specific user bought from a specific singer
    if opcode == '1':
        
