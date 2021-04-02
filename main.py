class Stack():
    def __init__(self, val, prev=None):
        self.data = val
        self.prev = prev
    def Next(self, val):
        s = Stack(self.data, self.prev)
        self.prev = s
        self.data = val
        
# version 2
import copy

class Stack():
    def __init__(self, val, prev=None):
        self.prev = prev
        self.data = val
    def Next(self, val):
        self.__init__(val, copy.deepcopy(self))
#version 3
import copy

class Stack():
    def __init__(self, val, prev=None):
        self.prev = prev
        self.data = val
    def Next(self, val):
        self.__init__(val, copy.deepcopy(self))

    def Prev(self,iter=0):
        if iter == 0:
            print(str(self.data))
        else:
            self.prev.Prev(iter - 1)
