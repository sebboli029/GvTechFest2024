# GvTechFest2024
Competencia de programación
# Simulador de Cinemática

Este repositorio contiene un simulador de cinemática interactivo desarrollado en Python. Permite a los usuarios simular diferentes tipos de movimientos, como Movimiento Rectilíneo Uniforme (MRU), Movimiento Rectilíneo Uniformemente Acelerado (MRUA) en 2D y Caída Libre, mostrando los resultados en tablas y gráficos.

## Descripción

El proyecto consta de los siguientes módulos:

*   **`menu.py`:** Módulo principal que muestra un menú interactivo para que el usuario seleccione el tipo de simulación que desea ejecutar.
*   **`mru.py`:** Módulo que simula el Movimiento Rectilíneo Uniforme (MRU). Calcula la posición en función del tiempo y muestra los resultados en una tabla y un gráfico.
*   **`caida.py`:** Módulo que simula la Caída Libre. Calcula la posición y la velocidad en función del tiempo y muestra los resultados en una tabla y un gráfico, junto con el tiempo total de caída y la velocidad final.
*   **`mrua.py`:** Módulo que simula el Movimiento Rectilíneo Uniformemente Acelerado (MRUA) en 2D (tiro parabólico). Calcula la posición y la velocidad en función del tiempo y muestra los resultados en una tabla y un gráfico, junto con el tiempo total de vuelo, la altura máxima y el alcance máximo.

## Características

*   **Menú interactivo:** Permite al usuario elegir entre diferentes tipos de simulación.
*   **Simulaciones:**
    *   **MRU:** Calcula y muestra la posición en función del tiempo.
    *   **Caída Libre:** Calcula y muestra la posición y la velocidad en función del tiempo, junto con el tiempo total de caída y la velocidad final.
    *   **MRUA:** Simula el movimiento en 2D (tiro parabólico), calcula y muestra la posición y la velocidad en función del tiempo, junto con el tiempo total de vuelo, la altura máxima y el alcance máximo.
*   **Visualización de datos:** Los resultados se muestran en tablas formateadas y en gráficos utilizando la librería `matplotlib`.
*   **Fácil de usar:** La interfaz es sencilla y guiada mediante preguntas al usuario para ingresar los datos necesarios.

## Tecnologías Utilizadas

*   **Python 3.x:** Lenguaje de programación.
*   **`tabulate`:** Librería para mostrar datos en formato de tabla.
*   **`matplotlib`:** Librería para generar gráficos.
*   **`math`:** Módulo para operaciones matemáticas.
*   **`time`:** Módulo para manejar tiempos de espera

## Instalación y Ejecución

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/<tu-usuario>/<nombre-del-repositorio>.git
    cd <nombre-del-repositorio>
    ```
2.  **Instala las dependencias:**
    ```bash
    pip install tabulate matplotlib
    ```
3.  **Ejecuta el simulador:**
    ```bash
    python menu.py
    ```
    El menú se mostrará en la consola y podrás interactuar con él.

## Uso

1.  Ejecuta el script `menu.py`.
2.  Elige la opción de la simulación que deseas ejecutar ingresando el número correspondiente.
3.  Ingresa los datos solicitados por el programa.
4.  Verás los resultados en una tabla y un gráfico.
5.  Para volver al menú, cierra la ventana del gráfico y espera unos segundos.
6.  Para salir del simulador, selecciona la opción "Salir del menú".

   ## Ejemplo de Uso y Salida

Aquí hay un ejemplo de cómo se vería la ejecución del simulador al elegir la opción de MRU:

1.  **Ejecución:**
    ```bash
    python menu.py
    ```

2.  **Menú en la consola:**
    ```
    Simulador de Cinematica
    Seleccione el tipo de movimiento a simular
    1. Movimiento rectilieno uniforme (MRU)
    2. Movimiento rectilineo uniformemente acelerado (MRUA) en 2D
    3. Caida libre
    4. Salir del menú
    
    Elegiste el numero: 1
    ```
3.  **Entrada del Usuario (MRU):**
    ```
    
    Simulador de MRU
    Escriba los datos a medir a continuación:
    Ingrese la posición inicial (m): 10
    Ingrese la velocidad constante: (m/s) 5
    Ingrese el tiempo total: (s) 10
    Ingrese el intervalo de tiempo: (s) 2
    ```
4. **Salida en Consola:**
    ```
    ╒═════════════╤══════════════════╕
    │   Tiempo(s) │   Distancia X (m) │
    ╞═════════════╪══════════════════╡
    │           0 │               10 │
    ├─────────────┼──────────────────┤
    │           2 │               20 │
    ├─────────────┼──────────────────┤
    │           4 │               30 │
    ├─────────────┼──────────────────┤
    │           6 │               40 │
    ├─────────────┼──────────────────┤
    │           8 │               50 │
    ├─────────────┼──────────────────┤
    │          10 │               60 │
    ╘═════════════╧══════════════════╛
    ```
5. **Salida Gráfica (MRU):**

  ![image](https://github.com/user-attachments/assets/3618371c-1c93-49ed-bb51-26d2232c9130)

  *Nota: La imagen mostrada aquí es una representación de cómo se vería la gráfica. La gráfica real se abrirá en una ventana separada al ejecutar el código.*
   *   Después de cerrar la ventana del gráfico, volverás al menú principal.
