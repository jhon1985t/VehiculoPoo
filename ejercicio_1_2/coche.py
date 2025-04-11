class Coche:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    def describir(self):
        print(f"Coche: {self.__marca} {self.__modelo}, Año: {self.__anio}")

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getAnio(self):
        return self.__anio

    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setAnio(self, anio):
        self.__anio = anio
