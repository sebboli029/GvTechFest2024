import math
import time
from mru import mru
from caida import caida
from mrua import mrua

def mostrar_menu():
    opciones = [
        {'ejercicio': 'Movimiento rectilieno uniforme (MRU)', 'funcion':mru},
        {'ejercicio': 'Movimiento rectilineo uniformemente acelerado (MRUA) en 2D', 'funcion':mrua},
        {'ejercicio': 'Caida libre', 'funcion':caida},
        {'ejercicio': 'Salir del menú', 'funcion':None}
    ]

    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion['ejercicio']}")

def menu():
    while True:
        print("\nSimulador de Cinematica")
        print("Seleccione el tipo de movimiento a simular")
        mostrar_menu()
        opcion = input()
        print("Elegiste el numero:", opcion)
        if opcion == "1":
            mru()
            time.sleep(3)
        elif opcion == "2":
            mrua()
            time.sleep(3)
        elif opcion == "3":
            caida()
            time.sleep(3)
        elif opcion == "4":
            break
        else:
            print("Intentalo de nuevo")
            time.sleep(3)





if __name__ == "__main__":
    menu()