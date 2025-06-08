'''
5: Crea una clase genérica Pila<T>
a) Implementa un método para apilar
b) Implementa un método para des apilar
c) Prueba la pila con diferentes tipos de datos
d) Muestra los datos de la pila
'''
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def apilar(self, item: T):
        self.elementos.append(item)

    def desapilar(self) -> T:
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            raise IndexError("La pila está vacía")

    def esta_vacia(self) -> bool:
        return len(self.elementos) == 0

    def mostrar(self):
        print("Contenido de la pila:", list(reversed(self.elementos)))

pila_enteros = Pila[int]()
pila_enteros.apilar(10)
pila_enteros.apilar(20)
pila_enteros.apilar(30)
pila_enteros.mostrar()
print("Desapilado:", pila_enteros.desapilar())
pila_enteros.mostrar()

pila_cadenas = Pila[str]()
pila_cadenas.apilar("uno")
pila_cadenas.apilar("dos")
pila_cadenas.apilar("tres")
pila_cadenas.mostrar()
print("Desapilado:", pila_cadenas.desapilar())
pila_cadenas.mostrar()
