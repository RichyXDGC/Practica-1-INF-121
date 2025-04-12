'''
1. Sea la clase Videojuego:

a) Instanciar al menos 2 videojuegos
b) Sobrecargar el constructor 2 veces
c) Implementar un método mostrar()
d) Sobrecargar el método agregarJugadores() donde en el primero se agregue
solo 1 jugador y en otro se ingrese una cantidad de jugadores a aumentar.
'''
class Videojuego:
    def __init__(self, nombre="Desconocido", plataforma="Genérica", cantidadJugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores

    def mostrar(self):
        print(f"Videojuego: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Jugadores: {self.cantidadJugadores}")

    def agregarJugadores(self, *args):
        if len(args) == 0:
            self.cantidadJugadores += 1
            print(f"Se agregó 1 jugador. Total ahora: {self.cantidadJugadores}")
        elif len(args) == 1 and isinstance(args[0], int):
            self.cantidadJugadores += args[0]
            print(f"Se agregaron {args[0]} jugadores. Total ahora: {self.cantidadJugadores}")
        else:
            print("Parámetros inválidos para agregar jugadores.")
v1 = Videojuego("Hollow Knight", "PC", 1)
v2 = Videojuego("It Takes Two", "PS5", 2)

v1.mostrar()
v1.agregarJugadores()
v1.agregarJugadores(3)

print("............")

v2.mostrar()
v2.agregarJugadores(2)
