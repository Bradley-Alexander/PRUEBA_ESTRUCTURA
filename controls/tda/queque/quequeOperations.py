from controls.tda.linked.linkedList import Linked_List
from controls.tda.linked.node import Node

class QuequeOperation(Linked_List):
    def __init__(self, top):
        super().__init__()
        self.__top = top
        

    @property
    def _top(self):
        return self.__top

    @_top.setter
    def _top(self, value):
        self.__top = value

    @property
    def verifyTop(self):
        return self._lenght < self._top
    
    
    def queque(self, data):
        if self.verifyTop:
            self.__addLast__(data)
        else:
            print("La cola esta llena")

    
    @property
    def dequeque(self):
        if self.isEmpty:
            print("La cola esta vacia")
        else:
            return self.delete(0)

    #qué hace el ._next en el anterior funcion?
    # ._next es una propiedad de la clase Node que se encarga de retornar el siguiente nodo de la lista enlazada.
    #porqué no lo reconoce al ._next?
    # ._next es una propiedad privada de la clase Node, por lo que no se puede acceder a ella desde otra clase.
    #cómo la llamo?
    #Para poder acceder a ._next se debe crear un método en la clase Node que retorne el valor de ._next.
    #como lo hag0?
    #Se debe crear un método en la clase Node que retorne el valor de ._next, por ejemplo:
    #def returnNode(self):
    #    return self.__next
    #Cómo lo uso?
    #Para usar el método se debe instanciar un objeto de la clase Node y llamar al método, por ejemplo:
    #node = Node("data")
