'''
7. Se hace referencia a algunos animales mediante las siguientes clases:

a) Instanciar 1 Perro, 1 Gato y 1 Pájaro.
b) Sobrecargar el método hacerSonido() para que cada animal emita su sonido
característico.
c) Implementar un método moverse() que indique cómo se mueve cada animal
(correr, saltar, volar, etc.).
'''
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        print(f"{self.nombre} hace un sonido.")

    def moverse(self):
        print(f"{self.nombre} se mueve.")


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre)
        self.edad = edad
        self.raza = raza

    def hacerSonido(self):
        print(f"{self.nombre} dice: ¡Guau guau!")

    def moverse(self):
        print(f"{self.nombre} corre con sus cuatro patas.")


class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def hacerSonido(self):
        print(f"{self.nombre} dice: Miau~")

    def moverse(self):
        print(f"{self.nombre} salta con elegancia.")


class Pajaro(Animal):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

    def hacerSonido(self):
        print(f"{self.nombre} canta: Pío pío")

    def moverse(self):
        print(f"{self.nombre} vuela por los cielos.")


perro1 = Perro("Rocky", 4, "Labrador")
gato1 = Gato("Minina", "Gris")
pajaro1 = Pajaro("Piquito", "Canario")

animales = [perro1, gato1, pajaro1]

for animal in animales:
    animal.hacerSonido()
    animal.moverse()
    print("*************************")
