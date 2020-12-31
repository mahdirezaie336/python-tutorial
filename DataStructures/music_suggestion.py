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

    number = 0
    if opcode == '1':
        # case: number of musics that a specific user bought from a specific singer
        for album in users[operand1][2]:
            if albums[album][0] == operand2:
                number += albums[album][2]
    elif opcode == '2':
        # case: number of musics that a specific user bought from a specific type
        for album in users[operand1][2]:
            if albums[album][1] == operand2:
                number += albums[album][2]
    elif opcode == '3':
        # case: number of musics that users with specific age bought from a specific singer
        for user in users.keys():
            if users[user][0] == operand1:
                for album in users[user][2]:
                    if albums[album][0] == operand2:
                        number += albums[album][2]
    elif opcode == '4':
        # case: number of musics that users with specific age bought from a specific type
        for user in users.keys():
            if users[user][0] == operand1:
                for album in users[user][2]:
                    if albums[album][1] == operand2:
                        number += albums[album][2]
    elif opcode == '5':
        # case: number of musics that users from specific city bought from a specific type
        for user in users.keys():
            if users[user][1] == operand1:
                for album in users[user][2]:
                    if albums[album][0] == operand2:
                        number += albums[album][2]
    elif opcode == '6':
        # case: number of musics that users from specific city bought from a specific type
        for user in users.keys():
            if users[user][1] == operand1:
                for album in users[user][2]:
                    if albums[album][1] == operand2:
                        number += albums[album][2]
    print(number)
