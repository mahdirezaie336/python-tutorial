import os
import sys
import datetime


def is_photo(file_name):
    file_type = str(file_name).lower().split('.')[-1]
    if file_type in ['jpg', 'jpeg', 'png']:
        return True
    return False


def is_video(file_name):
    file_type = str(file_name).lower().split('.')[-1]
    if file_type in ['mp4', 'avi', '3gp', 'mpeg', 'mkv', 'wmv', 'mov']:
        return True
    return False


def copy_file(source, destination):
    with open(source, 'rb') as src_file, open(destination, 'wb') as dst_file:
        while (buffer := src_file.read(1024)) != b'':
            dst_file.write(buffer)

    mod_time = os.path.getmtime(source)
    #print(destination, mod_time, ' <- ', os.path.getmtime(destination))
    os.utime(destination, (mod_time, mod_time))


args = sys.argv
src = args[1]
dst = args[2]
# src = './file_test'
# dst = './file_test/organized'
if not os.path.exists(dst):
    os.mkdir(dst)

for i in os.walk(src):
    if i[0] == dst:
        continue
    for src_file_name in i[2]:
        src_file_address = os.path.join(i[0], src_file_name)
        year = datetime.datetime.fromtimestamp(os.path.getmtime(src_file_address)).year
        dst_file_address = os.path.join(dst, str(year))

        # Existence check conditions
        if is_photo(src_file_name):
            if not os.path.exists(dst_file_address):
                os.mkdir(dst_file_address)
            dst_file_address = os.path.join(dst_file_address, 'photos')
            if not os.path.exists(dst_file_address):
                os.mkdir(dst_file_address)
        elif is_video(src_file_name):
            if not os.path.exists(dst_file_address):
                os.mkdir(dst_file_address)
            dst_file_address = os.path.join(dst_file_address, 'videos')
            if not os.path.exists(dst_file_address):
                os.mkdir(dst_file_address)
        else:
            continue

        dst_file_address = os.path.join(dst_file_address, src_file_name)

        copy_file(src_file_address, dst_file_address)
