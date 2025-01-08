from tabulate import tabulate
import matplotlib.pyplot as plt

def mru():
    print("\nSimulador de MRU")
    print("Escriba los datos a medir a continuación:")
    xo = float(input("Ingrese la posición incicial (m):"))
    v = float(input("Ingrese la velocidad constante: (m/s)"))
    tiempo_total = float(input("Ingrese el tiempo total: (s)"))
    intervalo = float(input("Ingrese el intervalo de tiempo: (s)"))
    informacion = calcular_mru(xo,v,tiempo_total,intervalo)
    mostrar(informacion)

def calcular_mru(xo,v,tiempo_total,intervalo):
    x = float()
    data = []
    t=0
    while t < tiempo_total:
        x = ((v*t)+xo)
        data.append([t,x])
        t = t + intervalo
    return data

def mostrar(informacion):
    print(tabulate(informacion, headers=['Tiempo(s)', 'Distancia X (m)'], tablefmt='fancy_grid')) 
    x, y = zip(*informacion)
    plt.plot(x, y, color='red', linestyle='--', label='MRU', marker='.', markersize=10, linewidth=2)
    plt.title('MRU', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Distancia X (m)')
    plt.legend()
    plt.show()
        




if __name__ == "__main__":
    print ("funcion de mru")
    mru()