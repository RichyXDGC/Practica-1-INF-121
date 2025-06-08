'''5.- Sea el siguiente diagrama de clases:
a) Crear, leer y mostrar un Archivo de Farmacias
b) Mostrar los medicamentos para la tos, de la Sucursal numero X
c) Mostrar el número de sucursal y su dirección que tienen el medicamento
“Golpex”
'''
import pickle
import os

class Medicamento:
    def __init__(self, nombre="", codMedicamento=0, tipo="", precio=0.0):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo
        self.precio = precio
    
    def leer(self):
        self.nombre = input("Ingrese nombre del medicamento: ")
        self.codMedicamento = int(input("Ingrese código del medicamento: "))
        self.tipo = input("Ingrese tipo de medicamento (tos/resfrio/etc): ")
        self.precio = float(input("Ingrese precio del medicamento: "))
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Código: {self.codMedicamento}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio: {self.precio:.2f}")
    
    def getTipo(self):
        return self.tipo
    
    def getPrecio(self):
        return self.precio

class Farmacia:
    def __init__(self, nombreFarmacia="", sucursal=0, direccion="", nroMedicamentos=0):
        self.nombreFarmacia = nombreFarmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.nroMedicamentos = nroMedicamentos
        self.m = [None] * 100  # Arreglo de medicamentos
    
    def leer(self):
        self.nombreFarmacia = input("Ingrese nombre de la farmacia: ")
        self.sucursal = int(input("Ingrese número de sucursal: "))
        self.direccion = input("Ingrese dirección de la farmacia: ")
        self.nroMedicamentos = int(input("Ingrese cantidad de medicamentos (max 100): "))
        
        for i in range(self.nroMedicamentos):
            print(f"\nMedicamento {i+1}:")
            self.m[i] = Medicamento()
            self.m[i].leer()
    
    def mostrar(self):
        print(f"\nNombre Farmacia: {self.nombreFarmacia}")
        print(f"Sucursal: {self.sucursal}")
        print(f"Dirección: {self.direccion}")
        print(f"Número de Medicamentos: {self.nroMedicamentos}")
        
        print("\nMedicamentos disponibles:")
        for i in range(self.nroMedicamentos):
            if self.m[i] is not None:
                self.m[i].mostrar()
                print("-----")
    
    def getDireccion(self):
        return self.direccion
    
    def getSucursal(self):
        return self.sucursal
    
    def mostrarMedicamentos(self, x):
        # Asumo que x es el tipo de medicamento a mostrar
        print(f"\nMedicamentos para {x}:")
        encontrados = False
        for i in range(self.nroMedicamentos):
            if self.m[i] is not None and self.m[i].getTipo().lower() == x.lower():
                self.m[i].mostrar()
                print("-----")
                encontrados = True
        if not encontrados:
            print(f"No se encontraron medicamentos para {x}")
    
    def buscaMedicamento(self, x):
        # Busca un medicamento por nombre
        for i in range(self.nroMedicamentos):
            if self.m[i] is not None and self.m[i].nombre.lower() == x.lower():
                return True
        return False

class ArchFarmacia:
    def __init__(self, na):
        self.na = na
    
    def crearArchivo(self):
        # Crear archivo vacío
        with open(self.na, "wb") as archivo:
            pickle.dump(0, archivo)  # Guardamos 0 como marcador de final
    
    def adicionar(self):
        with open(self.na, "ab") as archivo:
            farmacia = Farmacia()
            farmacia.leer()
            pickle.dump(farmacia, archivo)
    
    def listar(self):
        if not os.path.exists(self.na):
            print("El archivo no existe!")
            return
        
        with open(self.na, "rb") as archivo:
            try:
                while True:
                    farmacia = pickle.load(archivo)
                    if isinstance(farmacia, int):  # Saltamos el marcador de final
                        continue
                    farmacia.mostrar()
                    print("====================")
            except EOFError:
                pass
    
    def mostrarMedicamentosResfrios(self):
        if not os.path.exists(self.na):
            print("El archivo no existe!")
            return
        
        with open(self.na, "rb") as archivo:
            try:
                while True:
                    farmacia = pickle.load(archivo)
                    if isinstance(farmacia, int):
                        continue
                    farmacia.mostrarMedicamentos("resfrio")
                    print("====================")
            except EOFError:
                pass
    
    def precioMedicamentoTos(self):
        total = 0.0
        if not os.path.exists(self.na):
            print("El archivo no existe!")
            return total
        
        with open(self.na, "rb") as archivo:
            try:
                while True:
                    farmacia = pickle.load(archivo)
                    if isinstance(farmacia, int):
                        continue
                    for i in range(farmacia.nroMedicamentos):
                        if farmacia.m[i] is not None and farmacia.m[i].getTipo().lower() == "tos":
                            total += farmacia.m[i].getPrecio()
            except EOFError:
                pass
        
        return total
    
    def mostrarMedicamentosMenorTos(self):
        if not os.path.exists(self.na):
            print("El archivo no existe!")
            return
        
        precio_tos = self.precioMedicamentoTos()
        print(f"\nPrecio total de medicamentos para la tos: {precio_tos:.2f}")
        
        with open(self.na, "rb") as archivo:
            try:
                while True:
                    farmacia = pickle.load(archivo)
                    if isinstance(farmacia, int):
                        continue
                    
                    suma_farmacia = 0.0
                    for i in range(farmacia.nroMedicamentos):
                        if farmacia.m[i] is not None and farmacia.m[i].getTipo().lower() == "tos":
                            suma_farmacia += farmacia.m[i].getPrecio()
                    
                    if suma_farmacia < precio_tos:
                        print(f"\nFarmacia {farmacia.nombreFarmacia} (Sucursal {farmacia.sucursal})")
                        print(f"Total medicamentos tos: {suma_farmacia:.2f}")
            except EOFError:
                pass
    
    # Métodos para los incisos del problema
    def mostrarMedicamentosTosSucursalX(self, x):
        if not os.path.exists(self.na):
            print("El archivo no existe!")
            return
        
        encontrada = False
        with open(self.na, "rb") as archivo:
            try:
                while True:
                    farmacia = pickle.load(archivo)
                    if isinstance(farmacia, int):
                        continue
                    
                    if farmacia.getSucursal() == x:
                        encontrada = True
                        print(f"\nMedicamentos para la tos en Sucursal {x}:")
                        farmacia.mostrarMedicamentos("tos")
            except EOFError:
                pass
        
        if not encontrada:
            print(f"No se encontró la sucursal {x}")
    
    def mostrarSucursalesConGolpex(self):
        if not os.path.exists(self.na):
            print("El archivo no existe!")
            return
        
        print("\nSucursales que tienen el medicamento 'Golpex':")
        with open(self.na, "rb") as archivo:
            try:
                while True:
                    farmacia = pickle.load(archivo)
                    if isinstance(farmacia, int):
                        continue
                    
                    if farmacia.buscaMedicamento("Golpex"):
                        print(f"Sucursal: {farmacia.getSucursal()}")
                        print(f"Dirección: {farmacia.getDireccion()}")
                        print("-----")
            except EOFError:
                pass

# Función principal para probar las clases
def main():
    archivo = ArchFarmacia("farmacias.dat")
    
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Crear archivo de farmacias")
        print("2. Adicionar farmacia")
        print("3. Listar todas las farmacias")
        print("4. Mostrar medicamentos para resfríos")
        print("5. Mostrar precio total de medicamentos para la tos")
        print("6. Mostrar farmacias con medicamentos para la tos menor al precio total")
        print("7. Mostrar medicamentos para la tos en sucursal X")
        print("8. Mostrar sucursales con medicamento 'Golpex'")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            archivo.crearArchivo()
            print("Archivo creado exitosamente!")
        elif opcion == "2":
            archivo.adicionar()
        elif opcion == "3":
            archivo.listar()
        elif opcion == "4":
            archivo.mostrarMedicamentosResfrios()
        elif opcion == "5":
            total = archivo.precioMedicamentoTos()
            print(f"\nPrecio total de medicamentos para la tos: {total:.2f}")
        elif opcion == "6":
            archivo.mostrarMedicamentosMenorTos()
        elif opcion == "7":
            x = int(input("Ingrese el número de sucursal: "))
            archivo.mostrarMedicamentosTosSucursalX(x)
        elif opcion == "8":
            archivo.mostrarSucursalesConGolpex()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()