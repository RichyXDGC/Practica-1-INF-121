'''
9. Crea un POO para un carrito de compras y sus productos. El carrito contiene productos, pero los productos pueden existir independientemente del carrito. Además, el carrito no puede contener más de 10 productos.
   Producto \  <nombre, precio>
   Métodos: mostrar\_info() (muestra el nombre y el precio del producto)
   CarritoCompras\<productos (lista de objetos de tipo Producto)>
   Métodos: agregar\_producto(producto), mostrar\_carrito() (muestra la información de todos los productos en el carrito)
   a)	Implementa las clases con sus constructores, getters y setters.
   b)	Crea un carrito de compras y agrega varios productos, validando que no se exceda el límite de 10 productos.
   c)	Muestra la información del carrito y sus productos.
'''
# ----------------------------------------
# a) Clases con constructores, getters y setters
# ----------------------------------------

class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def mostrar_info(self):
        print(f"Producto: {self._nombre}, Precio: ${self._precio:.2f}")

class CarritoCompras:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        if len(self._productos) < 10:
            self._productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado al carrito.")
        else:
            print("No se puede agregar más de 10 productos al carrito.")

    def mostrar_carrito(self):
        print("Carrito de Compras:")
        if not self._productos:
            print("El carrito está vacío.")
        else:
            for p in self._productos:
                p.mostrar_info()
            print(f"Total de productos: {len(self._productos)}")

# ----------------------------------------
# b) Crear carrito y productos, validar límite
# ----------------------------------------

producto1 = Producto("Laptop", 1200)
producto2 = Producto("Mouse", 25)
producto3 = Producto("Teclado", 45)
producto4 = Producto("Monitor", 300)
producto5 = Producto("USB", 10)
producto6 = Producto("Auriculares", 60)
producto7 = Producto("Webcam", 75)
producto8 = Producto("Impresora", 150)
producto9 = Producto("Router", 80)
producto10 = Producto("Tablet", 400)
producto11 = Producto("Silla Gamer", 250)  # producto extra

carrito = CarritoCompras()

# Agregamos 11 productos (el último debe ser rechazado)
for producto in [producto1, producto2, producto3, producto4, producto5, producto6,
                 producto7, producto8, producto9, producto10, producto11]:
    carrito.agregar_producto(producto)

# ----------------------------------------
# c) Mostrar el contenido del carrito
# ----------------------------------------

print("\n>>> Contenido final del carrito:")
carrito.mostrar_carrito()
