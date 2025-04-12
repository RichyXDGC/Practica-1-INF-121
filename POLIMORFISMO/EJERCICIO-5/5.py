'''
5. Se hace referencia a algunos de los diferentes ambientes de la Universidad
mediante las siguientes clases:

a) Instanciar 2 objetos Oficina, 2 Aulas y 1 Laboratorio
b) Crear un método mostrar() para mostrar los datos de cada objeto
c) Sobrecargar el método cantidadMuebles(), para conocer el número total de
muebles dentro de cada ambiente
'''
class Oficina:
    def __init__(self, nroSillas, nroEscritorios, nroEstanterias):
        self.nroSillas = nroSillas
        self.nroEscritorios = nroEscritorios
        self.nroEstanterias = nroEstanterias

    def mostrar(self):
        print(f"[Oficina] Sillas: {self.nroSillas}, Escritorios: {self.nroEscritorios}, Estanterías: {self.nroEstanterias}")

    def cantidadMuebles(self):
        return self.nroSillas + self.nroEscritorios + self.nroEstanterias


class Aula:
    def __init__(self, nombre, capacidad, nroPupitres):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nroPupitres = nroPupitres

    def mostrar(self):
        print(f"[Aula] Nombre: {self.nombre}, Capacidad: {self.capacidad}, Pupitres: {self.nroPupitres}")

    def cantidadMuebles(self):
        return self.nroPupitres


class Laboratorio:
    def __init__(self, nombre, capacidad, nroMesas, nroSillas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nroMesas = nroMesas
        self.nroSillas = nroSillas

    def mostrar(self):
        print(f"[Laboratorio] Nombre: {self.nombre}, Capacidad: {self.capacidad}, Mesas: {self.nroMesas}, Sillas: {self.nroSillas}")

    def cantidadMuebles(self):
        return self.nroMesas + self.nroSillas


of1 = Oficina(4, 2, 1)
of2 = Oficina(6, 3, 2)

aula1 = Aula("Aula Magna", 100, 95)
aula2 = Aula("Aula B", 40, 38)

lab1 = Laboratorio("Lab Física", 30, 15, 20)

ambientes = [of1, of2, aula1, aula2, lab1]

for amb in ambientes:
    amb.mostrar()
    print(f"Total muebles: {amb.cantidadMuebles()}")
    print("************************************************************")
