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

#funcion para calcular mrua
def calcular_mrua(yo, vo, g, intervalo, angulo):
    vx = round(vo*math.cos(math.radians(angulo)), 2)
    voy = round(vo*math.sin(math.radians(angulo)), 2)
    y = yo
    data = []
    t=0
    tf = round((voy+math.sqrt(voy**2+(2*abs(g)*yo)))/abs(g), 2)
    x_max = round(vx*tf, 2)
    y_max = round(yo+(voy**2/(2*abs(g))), 2)
    i = 0
    while i < round(tf/intervalo,1):
        y =  round((voy*t)+(g*(t**2)/2)+yo, 2)
        x =  round(vx*t, 2)
        vy = round(voy +(g*t), 2)
        data.append([t,x,y,vx,vy])
        print(data)
        i += 1
        t = t + intervalo
    return data, tf, x_max, y_max

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