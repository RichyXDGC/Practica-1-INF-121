'''1. Crea una clase genérica Caja<T> para guardar algún tipo de objeto
a) Agrega métodos guardar() y obtener()
b) Crea dos instancias de la caja y almacena 2 datos de diferente tipo
c) Muestra el contenido de las cajas
'''
from typing import Generic, TypeVar

T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self.contenido: T = None

    def guardar(self, item: T):
        self.contenido = item

    def obtener(self) -> T:
        return self.contenido

caja_string = Caja[str]()
caja_string.guardar("Hola Mundo")

caja_entero = Caja[int]()
caja_entero.guardar(123456)

print("Contenido de caja_string:", caja_string.obtener())
print("Contenido de caja_entero:", caja_entero.obtener())
