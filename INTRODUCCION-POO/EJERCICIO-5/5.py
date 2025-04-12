'''
5. Crea una clase Estudiante con nombre, nota_1, nota_2
a) Agrega un método para calcular el promedio
b) Agrega un método para verificar si aprobó (promedio >=6)
c) Crea tres estudiantes, muestra sus promedios y si aprobaron
'''
class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def promedio(self):
        return (self.nota_1 + self.nota_2) / 2

    def aprobo(self):
        return self.promedio() >= 6
est1 = Estudiante("Camila", 7.5, 6.0)
est2 = Estudiante("Iker", 5.5, 4.0)
est3 = Estudiante("Samira", 8.0, 9.5)

for estudiante in [est1, est2, est3]:
    promedio = estudiante.promedio()
    estado = "Aprobó" if estudiante.aprobo() else "No aprobó"
    print(f"{estudiante.nombre}: Promedio = {promedio:.2f}--> {estado}")
