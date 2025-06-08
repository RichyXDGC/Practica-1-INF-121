'''
 Sea el siguiente diagrama de clases:
a) Implementa el método guardarEmpleado(Empleado e) para almacenar
empleados.
b) Implementa buscaEmpleado(String n) a traves del nombre, para ver los datos
del Empleado n.
c) Implementa mayorSalario(float sueldo), que devuelva al primer empleado con
sueldo mayor al ingresado.
'''
import pickle
import os

class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f"Empleado(nombre={self.nombre}, edad={self.edad}, salario={self.salario})"

class ArchivoEmpleado:
    def __init__(self, nombre_archivo: str):
        self.nomA = nombre_archivo
        self.crear_archivo()

    def crear_archivo(self):
        if not os.path.exists(self.nomA):
            with open(self.nomA, 'wb') as f:
                pickle.dump([], f)

    def guardar_empleado(self, e: Empleado):
        empleados = self._leer_empleados()
        empleados.append(e)
        with open(self.nomA, 'wb') as f:
            pickle.dump(empleados, f)

    def busca_empleado(self, nombre: str):
        empleados = self._leer_empleados()
        for e in empleados:
            if e.nombre == nombre:
                return e
        return None

    def mayor_salario(self, sueldo: float):
        empleados = self._leer_empleados()
        for e in empleados:
            if e.salario > sueldo:
                return e
        return None

    def _leer_empleados(self):
        with open(self.nomA, 'rb') as f:
            return pickle.load(f)

archivo = ArchivoEmpleado("empleados.dat")
archivo.guardar_empleado(Empleado("Ana", 30, 5000))
archivo.guardar_empleado(Empleado("Luis", 40, 7000))
archivo.guardar_empleado(Empleado("Marta", 28, 4500))

print("Buscar Ana:", archivo.busca_empleado("Ana"))
print("Mayor salario que 4800:", archivo.mayor_salario(4800))
