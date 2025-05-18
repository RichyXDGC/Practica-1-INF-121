'''7.	Crea un POO para una universidad y sus estudiantes. La universidad contiene estudiantes, pero los estudiantes pueden existir independientemente de la universidad.
Estudiante< nombre, carrera, semestre>
Métodos: mostrar_info() (muestra el nombre, carrera y semestre del estudiante)
Universidad<nombre, estudiantes (lista de objetos de tipo Estudiante)>
Métodos: agregar_estudiante(estudiante), mostrar_universidad() (muestra el nombre de la universidad y la información de todos los estudiantes)
a)	Implementa las clases con sus constructores, getters y setters.
b)	Crea una universidad y agrega varios estudiantes.
c)	Muestra la información de la universidad y sus estudiantes.'''
# ----------------------------------------
# a) Clases con constructores, getters y setters
# ----------------------------------------

class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        self._nombre = nombre
        self._carrera = carrera
        self._semestre = semestre

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_carrera(self):
        return self._carrera

    def set_carrera(self, carrera):
        self._carrera = carrera

    def get_semestre(self):
        return self._semestre

    def set_semestre(self, semestre):
        self._semestre = semestre

    def mostrar_info(self):
        print(f"Estudiante: {self._nombre}, Carrera: {self._carrera}, Semestre: {self._semestre}")

class Universidad:
    def __init__(self, nombre):
        self._nombre = nombre
        self._estudiantes = []

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def agregar_estudiante(self, estudiante):
        self._estudiantes.append(estudiante)

    def mostrar_universidad(self):
        print(f"Universidad: {self._nombre}")
        print("Estudiantes:")
        for e in self._estudiantes:
            e.mostrar_info()
            print("-" * 30)

# ----------------------------------------
# b) Crear universidad y estudiantes
# ----------------------------------------

est1 = Estudiante("Lucía Pérez", "Ingeniería", 3)
est2 = Estudiante("Javier Torres", "Arquitectura", 5)
est3 = Estudiante("Mateo Rojas", "Medicina", 2)

universidad = Universidad("Universidad Nacional")

universidad.agregar_estudiante(est1)
universidad.agregar_estudiante(est2)
universidad.agregar_estudiante(est3)

# ----------------------------------------
# c) Mostrar información de la universidad
# ----------------------------------------

print(">>> Información de la universidad:")
universidad.mostrar_universidad()
