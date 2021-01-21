class Reverse:
    def __init__(self):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == -1 * len(self.data):
            raise StopIteration

        index -= 1
        return self.data[index + 1]
