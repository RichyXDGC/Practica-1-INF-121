'''
5.	Definir las siguientes clases:
Empleado<nombre, apellido, salario_base, años_antigüedad
Métodos: calcular_salario() (retorna el salario base más un bono del 5% por cada año de antigüedad)
 Gerente (hereda de Empleado)< departamento, bono_gerencial>Métodos: calcular_salario() (debe sumar el bono gerencial al salario calculado en la clase base)
 Desarrollador (hereda de Empleado) <lenguaje_programación, horas_extras>
Métodos: calcular_salario() (debe sumar un monto adicional por horas extras al salario calculado en la clase base)

a)	Implementa las clases con sus constructores, getters y setters.
b)	Crea instancias de Gerente y Desarrollador y muestra su salario calculado.
c)	Muestra todos los gerentes que tienen un bono gerencial mayor a 1000.
d)	Muestra todos los desarrolladores que trabajan más de 10 horas extras.
'''
# -----------------------------
# a) Definición de clases
# -----------------------------

class Empleado:
    def __init__(self, nombre, apellido, salario_base, años_antigüedad):
        self._nombre = nombre
        self._apellido = apellido
        self._salario_base = salario_base
        self._años_antigüedad = años_antigüedad

    # Getters y Setters
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_salario_base(self):
        return self._salario_base

    def set_salario_base(self, salario):
        self._salario_base = salario

    def get_años_antigüedad(self):
        return self._años_antigüedad

    def set_años_antigüedad(self, años):
        self._años_antigüedad = años

    def calcular_salario(self):
        bono_antigüedad = self._salario_base * 0.05 * self._años_antigüedad
        return self._salario_base + bono_antigüedad

class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario_base, años_antigüedad, departamento, bono_gerencial):
        super().__init__(nombre, apellido, salario_base, años_antigüedad)
        self._departamento = departamento
        self._bono_gerencial = bono_gerencial

    def get_bono_gerencial(self):
        return self._bono_gerencial

    def set_bono_gerencial(self, bono):
        self._bono_gerencial = bono

    def calcular_salario(self):
        salario_base = super().calcular_salario()
        return salario_base + self._bono_gerencial

class Desarrollador(Empleado):
    def __init__(self, nombre, apellido, salario_base, años_antigüedad, lenguaje_programacion, horas_extras):
        super().__init__(nombre, apellido, salario_base, años_antigüedad)
        self._lenguaje_programacion = lenguaje_programacion
        self._horas_extras = horas_extras

    def get_horas_extras(self):
        return self._horas_extras

    def set_horas_extras(self, horas):
        self._horas_extras = horas

    def calcular_salario(self):
        salario_base = super().calcular_salario()
        pago_extras = self._horas_extras * 50  # suponemos 50 por hora extra
        return salario_base + pago_extras

# -----------------------------
# b) Crear instancias y mostrar salario
# -----------------------------

g1 = Gerente("Ana", "López", 4000, 10, "Finanzas", 1500)
g2 = Gerente("Luis", "Paredes", 3500, 5, "Marketing", 800)

d1 = Desarrollador("Carlos", "Martínez", 3000, 4, "Python", 12)
d2 = Desarrollador("Marta", "Ríos", 3200, 3, "Java", 8)

print(">>> Salarios calculados:")
print(f"{g1.get_nombre()} {g1.get_apellido()} (Gerente): ${g1.calcular_salario():.2f}")
print(f"{d1.get_nombre()} {d1.get_apellido()} (Desarrollador): ${d1.calcular_salario():.2f}")
print()

# -----------------------------
# c) Gerentes con bono > 1000
# -----------------------------

print(">>> Gerentes con bono gerencial mayor a 1000:")
for g in [g1, g2]:
    if g.get_bono_gerencial() > 1000:
        print(f"{g.get_nombre()} {g.get_apellido()} - Bono: {g.get_bono_gerencial()}")
print()

# -----------------------------
# d) Desarrolladores con más de 10 horas extra
# -----------------------------

print(">>> Desarrolladores con más de 10 horas extras:")
for d in [d1, d2]:
    if d.get_horas_extras() > 10:
        print(f"{d.get_nombre()} {d.get_apellido()} - Horas extra: {d.get_horas_extras()}")
