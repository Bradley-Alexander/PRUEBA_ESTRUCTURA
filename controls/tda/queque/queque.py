from controls.tda.queque.quequeOperation import QuequeOperation
class Queque:
    def __init__(self, top):
        self.__queque = QuequeOperation(top)

    def push(self, data):
        self.__queque.queque(data)
    
    @property
    def pop(self):
        return self.__queque.dequeque
    
    @property
    def print(self):
        self.__queque.print

    @property
    def verify(self):
        return self.__queque.verifyTop