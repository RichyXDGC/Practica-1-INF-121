'''
7. Crea una clase Celular con espacio para 20 aplicaciones o 1024Mb de Espacio
a) Crea un método para instalar una nueva aplicación
b) Crea un método para utilizar una aplicación (las aplicaciones que pesan más
de 100Mb utilizan un 2% de batería por cada 10 minutos uso, las que pesan
más de 250Mb utilizan 5% por cada 10 minutos de uso, en otros casos utiliza
un 1% cada 10 minutos de uso)
c) Muestra el porcentaje de batería restante
d) Cuando la batería se acabe al tratar de utilizar el celular este debe mostrar el
mensaje de celular apagado
'''
class Aplicacion:
    def __init__(self, nombre, peso_mb):
        self.nombre = nombre
        self.peso_mb = peso_mb
class Celular:
    def __init__(self):
        self.espacio_total = 1024
        self.max_apps = 20
        self.apps_instaladas = []
        self.espacio_usado = 0
        self.bateria = 100

    def instalar_app(self, app):
        if len(self.apps_instaladas) >= self.max_apps:
            print(f"No se puede instalar {app.nombre}: límite de aplicaciones alcanzado.")
            return
        if self.espacio_usado + app.peso_mb > self.espacio_total:
            print(f"No se puede instalar {app.nombre}: no hay suficiente espacio.")
            return
        self.apps_instaladas.append(app)
        self.espacio_usado += app.peso_mb
        print(f"{app.nombre} instalada correctamente.")

    def usar_app(self, nombre_app, minutos):
        if self.bateria <= 0:
            print("Celular apagado. No se puede usar ninguna app.")
            return
        app = next((a for a in self.apps_instaladas if a.nombre == nombre_app), None)
        if not app:
            print(f"La aplicación {nombre_app} no está instalada.")
            return

        if app.peso_mb > 250:
            consumo = 0.05
        elif app.peso_mb > 100:
            consumo = 0.02
        else:
            consumo = 0.01

        consumo_total = (minutos / 10) * consumo * 100
        self.bateria -= consumo_total

        if self.bateria <= 0:
            self.bateria = 0
            print("Batería agotada durante el uso. Celular apagado.")
        else:
            print(f"Usaste {nombre_app} por {minutos} minutos. Batería actual: {self.bateria:.2f}%")

    def mostrar_bateria(self):
        if self.bateria <= 0:
            print("Celular apagado.")
        else:
            print(f"Batería restante: {self.bateria:.2f}%")

mi_cel = Celular()

app1 = Aplicacion("Notas", 50)
app2 = Aplicacion("JuegoPesado", 300)
app3 = Aplicacion("RedSocial", 120)

mi_cel.instalar_app(app1)
mi_cel.instalar_app(app2)
mi_cel.instalar_app(app3)

mi_cel.usar_app("Notas", 30)
mi_cel.usar_app("RedSocial", 20)
mi_cel.usar_app("JuegoPesado", 180)

mi_cel.mostrar_bateria()

mi_cel.usar_app("Notas", 100)
