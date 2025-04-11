# main.py - Ejecuta ejercicios del Taller de Programación I desde consola

from ejercicio_1_2.coche import Coche as Coche12
from ejercicio_3_4.vehiculos import Coche as CocheH, Bicicleta
from ejercicio_5_6.polimorfismo import Coche as CocheP, Bicicleta as BicicletaP
from ejercicio_7_8.animales import Perro, Gato
from ejercicio_7_8.voladores import Pajaro, Avion, Helicoptero
from ejercicio_9_10.composicion import Motor, Coche as CocheCM
from ejercicio_9_10.excepciones import CocheRapido, ExcesoVelocidadException

def ejercicio_1_2():
    print("\n Ejercicio 1 y 2:")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    anio = int(input("Año: "))
    coche = Coche12(marca, modelo, anio)
    coche.describir()

    coche.setMarca(input("Nueva marca: "))
    coche.setModelo(input("Nuevo modelo: "))
    coche.setAnio(int(input("Nuevo año: ")))
    coche.describir()

def ejercicio_3_4():
    print("\n Ejercicio 3 y 4:")
    tipo = input("¿Deseas crear un coche o bicicleta?: ").strip().lower()
    if tipo == "coche":
        vel = int(input("Velocidad: "))
        coche = CocheH(vel, input("Marca: "), input("Modelo: "), int(input("Año: ")))
        coche.describir()
        coche.acelerar()
        coche.frenar()
    elif tipo == "bicicleta":
        bici = Bicicleta(int(input("Velocidad: ")), input("Tipo: "))
        bici.describir()
        bici.acelerar()
        bici.frenar()

def ejercicio_5_6():
    print("\n Ejercicio 5 y 6:")
    vehiculos = []
    for i in range(int(input("¿Cuántos vehículos quieres crear?: "))):
        tipo = input(f"Vehículo #{i+1} - coche/bicicleta: ").strip().lower()
        vel = int(input("Velocidad: "))
        if tipo == "coche":
            vehiculos.append(CocheP(vel, input("Marca: "), input("Modelo: ")))
        elif tipo == "bicicleta":
            vehiculos.append(BicicletaP(vel, input("Tipo: ")))
    for v in vehiculos:
        v.acelerar()

def ejercicio_7_8():
    print("\n Ejercicio 7 y 8:")
    animales = [Perro(), Gato()]
    for a in animales:
        print(f"{str(a)}: {a.hacerSonido()}")
    voladores = [Pajaro(), Avion(), Helicoptero()]
    for v in voladores:
        print(v.volar())

def ejercicio_9_10():
    print("\n Ejercicio 9 y 10:")
    motor = Motor(int(input("Potencia: ")), input("Tipo de motor: "))
    coche = CocheCM(input("Marca: "), input("Modelo: "), int(input("Año: ")), motor)
    coche.describir()

    coche_rapido = CocheRapido()
    while True:
        try:
            inc = int(input("Incrementar velocidad (0 para salir): "))
            if inc == 0:
                break
            coche_rapido.incrementarVelocidad(inc)
        except ExcesoVelocidadException as e:
            print(" Excepción:", e)
            break

if __name__ == "__main__":
    print("=== TALLER PROGRAMACIÓN I ===")
    ejercicio_1_2()
    ejercicio_3_4()
    ejercicio_5_6()
    ejercicio_7_8()
    ejercicio_9_10()
