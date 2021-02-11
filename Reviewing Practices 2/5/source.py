import os


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
            os.rename(path, os.path.join(FileManager.trash_dir, name))
            self.trashed_origins[name] = path

    def find(self, name, address):
        pass

    def restore(self, name):
        path = os.path.join(FileManager.trash_dir, name)
        if os.path.exists(path):
            os.rename(path, self.trashed_origins.pop(name))
