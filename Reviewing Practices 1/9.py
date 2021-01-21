def check_wsd(c):
    return c == ' ' or str(c).isdecimal() or 'a' <= c <= 'z' or 'A' <= c <= 'Z'


message_id = input()
message_content = input().lower()

# Checking validity of id
id_valid = not str.isdecimal(message_id)

# Checking validity of content
num_of_wsd = 0
for ch in message_content:
    if check_wsd(ch):
        num_of_wsd += 1
message_valid = (num_of_wsd > len(message_content) // 2) or ('spam' not in message_content)

# Results
if message_valid and id_valid:
    print('Not Spam')
elif message_valid and not id_valid:
    print('Invalid Sender')
elif not message_valid and id_valid:
    print('Invalid Content')
elif not message_valid and not id_valid:
    print('Fully Invalid')
