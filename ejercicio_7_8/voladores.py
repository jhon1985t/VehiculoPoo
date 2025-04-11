from abc import ABC, abstractmethod

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Pajaro(Volador):
    def volar(self):
        return "El pájaro vuela con sus alas batiendo."

class Avion(Volador):
    def volar(self):
        return "El avión enciende sus motores, toma impulso y despega."

class Helicoptero(Volador):
    def volar(self):
        return "El helicóptero despega al rotar sus hélices."
