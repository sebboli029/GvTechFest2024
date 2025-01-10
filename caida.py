from tabulate import tabulate
import matplotlib.pyplot as plt
import math

def caida():
    print("\nSimulador de Caida libre")
    print("Escriba los datos a medir a continuación:")
    yo = float(input("Ingrese la posición incicial (m):"))
    vo = float(input("Ingrese la velocidad inicial: (m/s)"))
    g = -9.8
    intervalo = float(input("Ingrese el intervalo de tiempo: (s)"))
    informacion,tf,vf = calcular_caida(yo,vo,g,intervalo)
    mostrar(informacion, tf,  vf)

def calcular_caida(yo, vo, g, intervalo):
    y = yo
    data = []
    t=0
    vf = (vo**2 +(2*abs(g)*yo))**0.5
    tf = ((2*yo)/(vo+vf))
    i = 0
    while i < round(tf/intervalo,1):
        y = ((vo*t)+(g*(t**2)/2)+yo)
        v = vo +(g*t)
        data.append([t,y,v])
        t += intervalo
        i += 1
    return data, round(tf, 2), round(vf, 2)


def mostrar(informacion, tf, vf):
    print(tabulate(informacion, headers=['Tiempo(s)', 'Distancia X (m)','Velocidad(m/s)'], tablefmt='fancy_grid')) 
    print(f"Tiempo total de caida: {tf}s")
    print(f"Velocidad final: {vf}(m/s)")
    x, y, z = zip(*informacion)
    plt.plot(x, y, color='red', linestyle='--', label='Caida libre', marker='.', markersize=10, linewidth=2)
    plt.title('Caida', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Distancia X (m)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print ("funcion de caida libre")
    caida()