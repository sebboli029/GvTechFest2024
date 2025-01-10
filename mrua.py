from tabulate import tabulate
import matplotlib.pyplot as plt
import math

def mrua():
    print("\nSimulador de MRUA")
    print("Escriba los datos a medir a continuación:")
    vo = float(input("Ingrese la velocidad inicial (m/s): "))
    angulo = float(input("Ingrese el ángulo de lanzamiento:"))
    yo = float(input("Ingrese la altura incicial (m):"))
    g = -9.8
    intervalo = float(input("Ingrese el intervalo de tiempo (s): "))
    informacion, tf, x_max, y_max = calcular_mrua(yo, vo, g, intervalo, angulo)
    mostrar(informacion, tf, x_max, y_max)

def calcular_mrua(yo, vo, g, intervalo, angulo):
    vx = vo*math.cos(math.radians(angulo))
    voy = vo*math.sin(math.radians(angulo))
    y = yo
    data = []
    t=0
    tf = (voy+math.sqrt(voy**2+(2*abs(g)*yo)))/abs(g)
    x_max = vx*tf
    y_max = yo+(voy**2/(2*abs(g)))
    i = 0
    while i < round(tf/intervalo,1):
        y = (voy*t)+(g*(t**2)/2)+yo
        x = vx*t
        vy = voy +(g*t)
        data.append([t,x,y,vx,vy])
        i += 1
        t += intervalo
    return data, round(tf, 2), round(x_max, 2), round(y_max, 2)

def mostrar(informacion, tf , x_max, y_max):
    print(tabulate(informacion, headers=['Tiempo(s)', 'Posicion X (m)','Posicion Y (m)','Velocidad X(m/s)','Velocidad Y(m/s)'], tablefmt='fancy_grid')) 
    print(f"Timepo total de vuelo {tf} s")
    print(f"Altura maxima alcanzada: {y_max}m")
    print(f"Alcance máximo: {x_max} m")
    x, y, z, w, v = zip(*informacion)
    plt.plot(y, z, color='red', linestyle='--', label='MRUA', marker='.', markersize=10, linewidth=2)
    plt.title('MRUA', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
    plt.xlabel('Posicion X (m)')
    plt.ylabel('Posicion Y (m)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print ("funcion de mrua")
    mrua()