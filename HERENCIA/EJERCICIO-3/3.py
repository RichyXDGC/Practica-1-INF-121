'''
3.	Definir las clases: 
Persona <ci, nombre, apellido, celular, fecha_Nac>
Estudiante (heredado de persona) <ru, fecha_Ingreso, semestre>
Docente (heredado de persona) <nit, profesión, especialidad>

a)	Diseñar el diagrama UML de las clases anteriores.
b)	Implementa las clases con sus constructores, datos por defecto y mostrar.
c)	Mostrar los estudiantes mayores de 25 años.
d)	Mostrar al docente que tiene la profesión de “Ingeniero”, es del sexo masculino y es el mayor de todos.
e)	Mostrar a los estudiantes y docentes que tienen el mismo apellido.
'''
from datetime import date

# --------------------------
# a) Definición de clases
# --------------------------

class Persona:
    def __init__(self, ci, nombre, apellido, celular, fecha_Nac):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.fecha_Nac = fecha_Nac

    def mostrar(self):
        print(f"{self.nombre} {self.apellido} - CI: {self.ci}")

    def edad(self):
        today = date.today()
        return today.year - self.fecha_Nac.year - ((today.month, today.day) < (self.fecha_Nac.month, self.fecha_Nac.day))

class Estudiante(Persona):
    def __init__(self, ci, nombre, apellido, celular, fecha_Nac, ru, fecha_Ingreso, semestre):
        super().__init__(ci, nombre, apellido, celular, fecha_Nac)
        self.ru = ru
        self.fecha_Ingreso = fecha_Ingreso
        self.semestre = semestre

    def mostrar(self):
        super().mostrar()
        print(f"RU: {self.ru}, Semestre: {self.semestre}")

class Docente(Persona):
    def __init__(self, ci, nombre, apellido, celular, fecha_Nac, nit, profesion, especialidad, sexo):
        super().__init__(ci, nombre, apellido, celular, fecha_Nac)
        self.nit = nit
        self.profesion = profesion
        self.especialidad = especialidad
        self.sexo = sexo  # "M" o "F"

    def mostrar(self):
        super().mostrar()
        print(f"NIT: {self.nit}, Profesión: {self.profesion}, Especialidad: {self.especialidad}, Sexo: {self.sexo}")

# --------------------------
# b) Crear listas de ejemplo
# --------------------------

estudiantes = [
    Estudiante("123", "Ana", "López", "789456", date(1997, 5, 3), "RU001", date(2020, 2, 1), 8),
    Estudiante("124", "Luis", "Pérez", "789457", date(2002, 6, 10), "RU002", date(2022, 3, 1), 4),
    Estudiante("125", "Carlos", "Martínez", "789458", date(1995, 9, 20), "RU003", date(2018, 8, 1), 10)
]

docentes = [
    Docente("456", "Carlos", "Ramírez", "123456", date(1980, 1, 1), "NIT01", "Ingeniero", "Sistemas", "M"),
    Docente("457", "Marta", "García", "123457", date(1985, 7, 15), "NIT02", "Licenciada", "Educación", "F"),
    Docente("458", "Jorge", "Martínez", "123458", date(1975, 3, 20), "NIT03", "Ingeniero", "Civil", "M")
]

# --------------------------
# c) Estudiantes mayores de 25 años
# --------------------------

print(">>> Estudiantes mayores de 25 años:")
for est in estudiantes:
    if est.edad() > 25:
        est.mostrar()
        print()

# --------------------------
# d) Docente hombre más viejo con profesión "Ingeniero"
# --------------------------

mayor_docente = None
for d in docentes:
    if d.profesion == "Ingeniero" and d.sexo == "M":
        if mayor_docente is None or d.edad() > mayor_docente.edad():
            mayor_docente = d

print(">>> Docente hombre con profesión 'Ingeniero' y mayor edad:")
if mayor_docente:
    mayor_docente.mostrar()
    print()

# --------------------------
# e) Estudiantes y docentes con el mismo apellido
# --------------------------

print(">>> Estudiantes y docentes con el mismo apellido:")
encontrado = False
for est in estudiantes:
    for doc in docentes:
        if est.apellido == doc.apellido:
            print("Coincidencia encontrada:")
            est.mostrar()
            doc.mostrar()
            print()
            encontrado = True

if not encontrado:
    print("No hay coincidencias de apellidos.")
