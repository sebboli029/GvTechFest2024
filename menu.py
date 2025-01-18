import time
from mru import mru
from caida import caida
from mrua import mrua

opciones = [
    {'ejercicio': 'Movimiento rectilieno uniforme (MRU)', 'funcion':mru},
    {'ejercicio': 'Movimiento rectilineo uniformemente acelerado (MRUA) en 2D', 'funcion':mrua},
    {'ejercicio': 'Caida libre', 'funcion':caida},
    {'ejercicio': 'Salir del menú', 'funcion':None}
]

def mostrar_menu():
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion['ejercicio']}")

def menu():
    while True:
        print("\nSimulador de Cinematica")
        print("Seleccione el tipo de movimiento a simular")
        mostrar_menu()
        try:
            opcion = int(input())
            print("Elegiste el numero:", opcion)
            seleccion = opciones[opcion-1]
            if seleccion['funcion'] == None:
                break
            else:
                seleccion['funcion']()
            time.sleep(3)
        except NameError:
            print("la funcion no es correcta")
            time.sleep(3)
        except IndexError:
            print("El caracter que elgiste no es correcto, intentalo de nuevo")
            time.sleep(3)
            
if __name__ == "__main__":
    menu()