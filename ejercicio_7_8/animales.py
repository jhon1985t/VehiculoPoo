from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacerSonido(self):
        pass

class Perro(Animal):
    def hacerSonido(self):
        return "Wuff wuff"

    def __str__(self):
        return "Perro"

class Gato(Animal):
    def hacerSonido(self):
        return "Miau miau"

    def __str__(self):
        return "Gato"
