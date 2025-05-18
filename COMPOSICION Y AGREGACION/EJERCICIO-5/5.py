'''5.	Desarrolla un POO para un equipo de fútbol y sus jugadores. El equipo está compuesto por jugadores, y si el equipo se destruye, los jugadores también se destruyen. Además, los jugadores pueden ser de diferentes tipos (portero, defensa, mediocampista, delantero).
Clase Padre: Jugador<nombre, número, posición>
Métodos: mostrar_info() (muestra el nombre, número y posición del jugador)
Clases Derivadas: Portero, Defensa, Mediocampista, Delantero (heredan de Jugador)
Atributos adicionales: habilidad_especial (ej: "Atajadas", "Marcaje", "Pases", "Goles")
Clase: Equipo<nombre, jugadores (lista de objetos de tipo Jugador)>
Métodos: agregar_jugador(jugador), mostrar_equipo() (muestra el nombre del equipo y la información de todos los jugadores)
a)	Implementa las clases con sus constructores, getters y setters.
b)	Crea un equipo y agrega varios jugadores de diferentes tipos.
c)	Muestra la información del equipo y sus jugadores.
'''
# ----------------------------------------
# a) Clases base y derivadas con métodos
# ----------------------------------------

class Jugador:
    def __init__(self, nombre, numero, posicion):
        self._nombre = nombre
        self._numero = numero
        self._posicion = posicion

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    def get_posicion(self):
        return self._posicion

    def set_posicion(self, posicion):
        self._posicion = posicion

    def mostrar_info(self):
        print(f"{self._posicion} - Nombre: {self._nombre}, Número: {self._numero}")

class Portero(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Portero")
        self._habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidad especial: {self._habilidad_especial}")

class Defensa(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Defensa")
        self._habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidad especial: {self._habilidad_especial}")

class Mediocampista(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Mediocampista")
        self._habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidad especial: {self._habilidad_especial}")

class Delantero(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Delantero")
        self._habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidad especial: {self._habilidad_especial}")

# ----------------------------------------
# Clase Equipo (composición)
# ----------------------------------------

class Equipo:
    def __init__(self, nombre):
        self._nombre = nombre
        self._jugadores = []

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def agregar_jugador(self, jugador):
        self._jugadores.append(jugador)

    def mostrar_equipo(self):
        print(f"Equipo: {self._nombre}")
        print("Jugadores:")
        for j in self._jugadores:
            j.mostrar_info()
            print("-" * 30)

# ----------------------------------------
# b) Crear equipo y agregar jugadores
# ----------------------------------------

equipo = Equipo("Tigres del Norte")

jug1 = Portero("Carlos Pérez", 1, "Atajadas espectaculares")
jug2 = Defensa("Luis Gómez", 5, "Marcaje agresivo")
jug3 = Mediocampista("Ana Torres", 8, "Pases precisos")
jug4 = Delantero("Marco Rivas", 9, "Goles potentes")

equipo.agregar_jugador(jug1)
equipo.agregar_jugador(jug2)
equipo.agregar_jugador(jug3)
equipo.agregar_jugador(jug4)

# ----------------------------------------
# c) Mostrar información del equipo
# ----------------------------------------

print(">>> Información del equipo:")
equipo.mostrar_equipo()
