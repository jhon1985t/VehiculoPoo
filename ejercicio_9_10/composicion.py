class Motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def describir(self):
        return f"Motor {self.tipo} de {self.potencia} HP"

class Coche:
    def __init__(self, marca, modelo, anio, motor):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.motor = motor

    def describir(self):
        print(f"{self.marca} {self.modelo}, Año: {self.anio}")
        print(self.motor.describir())
