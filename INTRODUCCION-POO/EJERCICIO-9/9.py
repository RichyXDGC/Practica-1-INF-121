'''
9. Realiza la abstracción de una Computadora
a) Muestra los componentes principales de la computadora
b) Muestra el estado de la computadora (encendido o apagado)
c) Crea una instancia y simula encender y apagar la computadora.
'''
class Computadora:
    def __init__(self, procesador, ram, almacenamiento, gpu):
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.gpu = gpu
        self.encendida = False

    def mostrar_componentes(self):
        print("Componentes de la computadora:")
        print(f"- Procesador: {self.procesador}")
        print(f"- RAM: {self.ram}")
        print(f"- Almacenamiento: {self.almacenamiento}")
        print(f"- Tarjeta Gráfica: {self.gpu}")

    def mostrar_estado(self):
        estado = "Encendida" if self.encendida else "Apagada"
        print(f"La computadora está: {estado}")

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print("Computadora encendida.")
        else:
            print("La computadora ya está encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print("Computadora apagada.")
        else:
            print("La computadora ya está apagada.")

compu = Computadora("AMD Ryzen 5", "16GB", "1TB SSD", "NVIDIA GTX 1660")

compu.mostrar_componentes()
compu.mostrar_estado()

compu.encender()
compu.mostrar_estado()

compu.apagar()
compu.mostrar_estado()
