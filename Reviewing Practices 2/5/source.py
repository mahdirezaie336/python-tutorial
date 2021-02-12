import os


class File:

    def __init__(self, file_name, file_address):
        self.name = file_name
        self.address = file_address

    def __eq__(self, other):
        return (self.name == other.name) and (self.address == other.address)

    def __hash__(self):
        return hash(self.address + '/' + self.name)


class FileManager:
    trash_dir = './.trash/'

    def __init__(self):
        self.trashed_origins = {}
        if not os.path.exists(FileManager.trash_dir):
            os.mkdir(FileManager.trash_dir)

    def create_dir(self, name, address):
        path = os.path.join(address, name)
        if not os.path.exists(path):
            os.mkdir(path)

    def create_file(self, name, address):
        path = os.path.join(address, name)
        if not os.path.exists(path):
            with open(path, 'a') as file:
                pass

    def delete(self, name, address):
        path = os.path.join(address, name)
        if os.path.exists(path):
            if name not in self.trashed_origins:
                self.trashed_origins[name] = []
            index = len(self.trashed_origins[name])
            os.rename(path, os.path.join(FileManager.trash_dir, name + '.' + str(index)))
            self.trashed_origins[name].append(path)

    def find(self, name, address):
        pass

    def restore(self, name):
        if name in self.trashed_origins:
            origin = self.trashed_origins[name].pop()
            index = len(self.trashed_origins[name])
            os.rename(os.path.join(FileManager.trash_dir, name + '.' + str(index)), origin)
            if index == 0:
                del self.trashed_origins[name]
