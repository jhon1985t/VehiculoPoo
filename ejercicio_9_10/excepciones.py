class ExcesoVelocidadException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class CocheRapido:
    def __init__(self):
        self.velocidad = 0

    def incrementarVelocidad(self, incremento):
        if self.velocidad + incremento > 200:
            raise ExcesoVelocidadException("¡Velocidad no permitida! Excede los 200 km/h.")
        self.velocidad += incremento
        print(f"Velocidad actual: {self.velocidad} km/h")
