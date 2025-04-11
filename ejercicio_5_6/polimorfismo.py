class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad += 10
        print(f"Vehículo aceleró a {self.velocidad} km/h")

class Coche(Vehiculo):
    def __init__(self, velocidad, marca, modelo):
        super().__init__(velocidad)
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        self.velocidad += 20
        print(f"Coche {self.marca} {self.modelo} aceleró a {self.velocidad} km/h")

class Bicicleta(Vehiculo):
    def __init__(self, velocidad, tipo):
        super().__init__(velocidad)
        self.tipo = tipo

    def acelerar(self):
        self.velocidad += 5
        print(f"Bicicleta tipo {self.tipo} aceleró a {self.velocidad} km/h")
