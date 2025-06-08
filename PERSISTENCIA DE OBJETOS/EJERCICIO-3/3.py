'''3.- Sea el siguiente diagrama de clases:
a) Implementar el diagrama de clases.
b) Implementa buscarCliente(int c) a través del id.
c) Implementa buscarCelularCliente(int c), que devuelva los datos del cliente
junto al número de celular.
'''
import pickle
import os

class Cliente:
    def __init__(self, id: int, nombre: str, telefono: int):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Cliente(id={self.id}, nombre={self.nombre}, telefono={self.telefono})"

class ArchivoCliente:
    def __init__(self, nombre_archivo: str):
        self.nomA = nombre_archivo
        self.crear_archivo()

    def crear_archivo(self):
        if not os.path.exists(self.nomA):
            with open(self.nomA, 'wb') as f:
                pickle.dump([], f)

    def guarda_cliente(self, c: Cliente):
        clientes = self._leer_clientes()
        clientes.append(c)
        with open(self.nomA, 'wb') as f:
            pickle.dump(clientes, f)

    def buscar_cliente(self, id_cliente: int):
        for c in self._leer_clientes():
            if c.id == id_cliente:
                return c
        return None

    def buscar_celular_cliente(self, id_cliente: int):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            return f"Cliente: {cliente.nombre}, Teléfono: {cliente.telefono}"
        return "Cliente no encontrado"

    def _leer_clientes(self):
        with open(self.nomA, 'rb') as f:
            return pickle.load(f)

archivo = ArchivoCliente("clientes.dat")
archivo.guarda_cliente(Cliente(1, "Ana", 987654321))
archivo.guarda_cliente(Cliente(2, "Luis", 123456789))

print(archivo.buscar_cliente(1))
print(archivo.buscar_celular_cliente(2))
