class Stack():
    def __init__(self, val, prev=None):
        self.data = val
        self.prev = prev
    def Next(self, val):
        s = Stack(self.data, self.prev)
        self.prev = s
        self.data = val