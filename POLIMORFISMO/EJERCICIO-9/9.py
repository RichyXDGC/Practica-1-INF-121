'''
9. Para los bloques del juego Minecraft se usará los siguientes objetos:

a) Crear e instanciar al menos 2 bloques de cada tipo
b) Sobrescribe accion() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando
distintos mensajes según el tipo de bloque.
c) Sobrecarga colocar() para permitir colocar un bloque en diferentes
orientaciones (por ejemplo, en el suelo o en la pared).
d) Sobrescribe romper() en BloqueCofre, BloqueTnt y BloqueHorno, mostrando
distintos mensajes según el tipo de bloque y que puede suceder al romperlos.
'''
class Bloque:
    def colocar(self, orientacion="suelo"):
        print(f"Bloque colocado en la orientación: {orientacion}")

    def accion(self):
        print("Este bloque no tiene acción específica.")

    def romper(self):
        print("El bloque ha sido destruido.")


class BloqueCofre(Bloque):
    def __init__(self, capacidad, resistencia, tipo):
        self.capacidad = capacidad
        self.resistencia = resistencia
        self.tipo = tipo

    def accion(self):
        print(f"Se abre un cofre tipo {self.tipo} con capacidad de {self.capacidad} items.")

    def romper(self):
        print("El cofre se rompe y caen todos los objetos guardados.")

class BloqueTnt(Bloque):
    def __init__(self, tipo, dano):
        self.tipo = tipo
        self.dano = dano

    def accion(self):
        print(f"La TNT tipo {self.tipo} está activada... ¡Corre!")

    def romper(self):
        print(f"La TNT explota causando {self.dano} de daño.")

class BloqueHorno(Bloque):
    def __init__(self, color, capacidadComida):
        self.color = color
        self.capacidadComida = capacidadComida

    def accion(self):
        print(f"El horno color {self.color} comienza a cocinar comida...")

    def romper(self):
        print("El horno se rompe y pierde toda la comida en su interior.")

cofre1 = BloqueCofre(30, 100, "madera")
cofre2 = BloqueCofre(50, 150, "hierro")

tnt1 = BloqueTnt("básica", 20)
tnt2 = BloqueTnt("potente", 50)

horno1 = BloqueHorno("gris", 5)
horno2 = BloqueHorno("negro", 10)

bloques = [cofre1, cofre2, tnt1, tnt2, horno1, horno2]

for bloque in bloques:
    bloque.colocar("pared" if isinstance(bloque, BloqueTnt) else "suelo")
    bloque.accion()
    bloque.romper()
    print("******************************************************************")
