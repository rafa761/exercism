class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.buffer = []
        for num in range(capacity):
            self.buffer.append([])

    def read(self):
        return max(self.buffer)

    def write(self, data):
        for num in range(len(self.buffer)):
            if str(self.buffer[num]).isalnum():
                pass
            else:
                self.buffer[num] = data

    def overwrite(self, data):
        pass

    def clear(self):
        pass
