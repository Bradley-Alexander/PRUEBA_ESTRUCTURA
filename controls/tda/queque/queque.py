from controls.tda.queque.quequeOperations import QuequeOperation

class Queque:
    def __init__(self, tope):
        self.__queque = QuequeOperation(tope)

    def push(self, data):
        self.__queque.queque(data)

    def pop(self):
        self.__queque.dequeque
    
    @property
    def print(self):
        self.__queque.print
    
    @property
    def verify(self):
        return self.__queque.verifyTop