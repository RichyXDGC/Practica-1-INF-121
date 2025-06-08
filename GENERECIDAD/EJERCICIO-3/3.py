'''
3. Crea una clase genérica Catalogo<T> que almacene productos o libros.
a) Agrega métodos para agregar y buscar elemento
b) Prueba el catálogo con libros
c) Prueba el catálogo con productos
'''
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Catalogo(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def agregar(self, item: T):
        self.elementos.append(item)

    def buscar(self, item: T) -> bool:
        return item in self.elementos

    def mostrar_todos(self):
        for item in self.elementos:
            print(item)

catalogo_libros = Catalogo[str]()
catalogo_libros.agregar("El Quijote")
catalogo_libros.agregar("1984")
catalogo_libros.mostrar_todos()
print("¿Contiene '1984'?", catalogo_libros.buscar("1984"))

catalogo_productos = Catalogo[str]()
catalogo_productos.agregar("Laptop")
catalogo_productos.agregar("Teléfono")
catalogo_productos.mostrar_todos()
print("¿Contiene 'Tablet'?", catalogo_productos.buscar("Tablet"))
