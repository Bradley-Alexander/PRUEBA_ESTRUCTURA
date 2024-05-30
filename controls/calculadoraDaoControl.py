from models.calculadora import Calculadora
from controls.dao.daoAdapter import DaoAdapter
from controls.tda.stack.stack import Stack

class CalculadoraDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Calculadora)
        self.__calculadora = None

    @property
    def _calculadora(self):
        if self.__calculadora == None:
            self.__calculadora = Calculadora()
        return self.__calculadora

    @_calculadora.setter
    def _calculadora(self, value):
        self.__calculadora = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__calculadora._id = self._lista._length +1
        self._save(self.__calculadora)


        
    def calcular_expresion(self):
        pila = Stack(10)
        numElementos = self.__calculadora._expresion.split()
        
        for elemento in numElementos:
            
            
            if elemento.isalpha():
                res = "EXPRESIÓN INVÁLIDA"
                break
            

            if elemento.isdigit():
                pila.push(elemento)
            else:
                b = pila.pop
                a = pila.pop
                A = float(a)
                B = float(b)
                if elemento == "+":
                    res = A + B
                elif elemento == "-":
                    res = A - B
                elif elemento == "*":
                    res = A * B
                elif elemento == "/":
                    res = A / B
                elif elemento == "^":
                    res = A ** B
                else:
                    res = "ERROR"
                    break
                pila.push(res)
            

        self.__calculadora._resultado = res
        self.save
        



    
