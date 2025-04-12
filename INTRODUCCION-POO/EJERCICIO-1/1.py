'''1. Crea una clase Persona con nombre, edad y ciudad
a) Agrega un método para mostrar el saludo: “Hola, soy {nombre} de {ciudad}”
b) Crea tres personas y muestra su saludo
c) Agrega un método para verificar si es mayor de edad'''
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludar(self):
        print(f"Hola, soy {self.nombre} de {self.ciudad}")

    def mayor(self):
        return self.edad >= 18
persona1 = Persona("Roger", 20, "Brasil")
persona2 = Persona("Luis", 15, "Chile")
persona3 = Persona("Ana", 33, "Bolivia")

persona1.saludar()
persona2.saludar()
persona3.saludar()
print(f"{persona1.nombre} es mayor de edad: {persona1.mayor()}")
print(f"{persona2.nombre} es mayor de edad: {persona2.mayor()}")
print(f"{persona3.nombre} es mayor de edad: {persona3.mayor()}")


