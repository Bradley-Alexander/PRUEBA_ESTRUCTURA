import sys
sys.path.append('../')
from controls.tda.linked.linkedList import Linked_List
from controls.tda.stack.stack import Stack
from controls.calculadoraDaoControl import CalculadoraDaoControl

# pc = PersonaControl()
# cd = CensoDao()


pila2 = Stack(10)

calculadora = CalculadoraDaoControl()

calculadora._calculadora._expresion = "90 10 +"
calculadora._calculadora._resultado = 0


numElementos = calculadora._calculadora._expresion.split()

calculadora.calcular_expresion()
