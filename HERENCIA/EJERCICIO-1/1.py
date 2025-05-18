'''1.	Modelar diferentes tipos de vehículos. Las clases deben tener las siguientes características:
Vehículo<marca, modelo, año, precio_base>
Métodos: mostrar_info() muestra la información básica del vehículo
Coche (hereda de Vehículo)< num_puertas, tipo_combustible>
Métodos: mostrar_info() debe mostrar la información básica más los atributos adicionales
Moto (hereda de Vehículo)< cilindrada, tipo_motor>
Métodos: mostrar_info() debe mostrar la información básica más los atributos adicionales

a)	Implementa las clases con sus constructores, getters y setters. 
b)	Crea instancias de Coche y Moto y muestra su información usando el método mostrar_info().
c)	Muestra todos los coches que tienen más de 4 puertas.
d)	Mostrar los coches y motos actuales (gestión 2025)
'''
class Vehiculo:
    def __init__(self, marca, modelo, año, precio_base):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_base = precio_base

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio Base: {self.precio_base}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, precio_base, num_puertas, tipo_combustible):
        super().__init__(marca, modelo, año, precio_base)
        self.num_puertas = num_puertas
        self.tipo_combustible = tipo_combustible

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self.num_puertas}, Tipo de combustible: {self.tipo_combustible}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, precio_base, cilindrada, tipo_motor):
        super().__init__(marca, modelo, año, precio_base)
        self.cilindrada = cilindrada
        self.tipo_motor = tipo_motor

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada}, Tipo de motor: {self.tipo_motor}")


# b) Instancias
c1 = Coche("Toyota", "Corolla", 2025, 20000, 4, "Gasolina")
c2 = Coche("Ford", "Explorer", 2025, 30000, 5, "Diesel")
m1 = Moto("Yamaha", "R1", 2025, 15000, 1000, "4T")

print("---- Coche 1 ----")
c1.mostrar_info()

print("\n---- Coche 2 ----")
c2.mostrar_info()

print("\n---- Moto ----")
m1.mostrar_info()

# c) Más de 4 puertas
print("\n--- Coches con más de 4 puertas ---")
for coche in [c1, c2]:
    if coche.num_puertas > 4:
        coche.mostrar_info()

# d) Vehículos del año 2025
print("\n--- Vehículos del año 2025 ---")
for v in [c1, c2, m1]:
    if v.año == 2025:
        v.mostrar_info()


