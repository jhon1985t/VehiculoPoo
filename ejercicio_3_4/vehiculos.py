class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10
        print(f"Vehículo aceleró. Velocidad: {self.velocidad} km/h")

    def frenar(self):
        self.velocidad = max(0, self.velocidad - 5)
        print(f"Vehículo frenó. Velocidad: {self.velocidad} km/h")

class Coche(Vehiculo):
    def __init__(self, velocidad, marca, modelo, anio):
        super().__init__(velocidad)
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def describir(self):
        print(f"Coche: {self.marca} {self.modelo}, Año: {self.anio}, Velocidad: {self.velocidad} km/h")

    def acelerar(self):
        self.velocidad += 20
        print(f"Coche aceleró. Velocidad: {self.velocidad} km/h")

class Bicicleta(Vehiculo):
    def __init__(self, velocidad, tipo):
        super().__init__(velocidad)
        self.tipo = tipo

    def describir(self):
        print(f"Bicicleta tipo {self.tipo}, Velocidad: {self.velocidad} km/h")

    def acelerar(self):
        self.velocidad += 5
        print(f"Bicicleta aceleró. Velocidad: {self.velocidad} km/h")

