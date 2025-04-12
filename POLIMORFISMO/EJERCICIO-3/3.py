'''
3. Un restaurante organiza a su personal mediante las siguientes clases:

a) Instanciar 1 Cocinero, 2 objetos Mesero y 2 objetos Administrativo.
b) Sobrecargar el método SueldoTotal para mostrar el sueldo total,
sumándole las horas extra, considerando el sueldo por hora y la propina
en caso de los meseros.
c) Sobrecargar el método para mostrar a aquellos Empleados que tengan
SueldoMes igual a X.
'''
class Empleado:
    def __init__(self, nombre, sueldoMes):
        self.nombre = nombre
        self.sueldoMes = sueldoMes

    def sueldo_total(self):
        return self.sueldoMes

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Sueldo Base: {self.sueldoMes}")


class Cocinero(Empleado):
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora):
        super().__init__(nombre, sueldoMes)
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora

    def sueldo_total(self):
        return self.sueldoMes + (self.horasExtra * self.sueldoHora)

    def mostrar(self):
        print(f"[Cocinero] {self.nombre} - Sueldo total: {self.sueldo_total()}")


class Mesero(Empleado):
    def __init__(self, nombre, sueldoMes, horasExtra, sueldoHora, propina):
        super().__init__(nombre, sueldoMes)
        self.horasExtra = horasExtra
        self.sueldoHora = sueldoHora
        self.propina = propina

    def sueldo_total(self):
        return self.sueldoMes + (self.horasExtra * self.sueldoHora) + self.propina

    def mostrar(self):
        print(f"[Mesero] {self.nombre} - Sueldo total: {self.sueldo_total()}")


class Administrativo(Empleado):
    def __init__(self, nombre, sueldoMes, cargo):
        super().__init__(nombre, sueldoMes)
        self.cargo = cargo

    def mostrar(self):
        print(f"[Administrativo] {self.nombre}, Cargo: {self.cargo} - Sueldo total: {self.sueldo_total()}")

cocinero1 = Cocinero("Luis", 2000, 10, 15.5)
mesero1 = Mesero("Ana", 1500, 5, 10, 100)
mesero2 = Mesero("Pedro", 1500, 3, 10, 50)
admin1 = Administrativo("Sofía", 2500, "Gerente")
admin2 = Administrativo("Marco", 2000, "Contador")

empleados = [cocinero1, mesero1, mesero2, admin1, admin2]

print("SUELDOS TOTALES*******************************************************")
for emp in empleados:
    emp.mostrar()

print("\nEmpleados con sueldo base = 1500 *************************************")
for emp in empleados:
    if emp.sueldoMes == 1500:
        emp.mostrar()
