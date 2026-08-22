
import numpy as np
mar_computadora= np.zeros((6,6)) #creamos una matriz de ceros de 6x6, la primera fila y columna se usarán para mostrar los números de las coordenadas
tablero= np.zeros((7,7)) #creamos una matriz de ceros de 7x7, la primera fila y columna se usarán para mostrar los números de las coordenadas

mar_computadora = np.zeros((6, 6)) # Creamos una matriz de ceros para representar el tablero de la computadora, igual que el del jugador.
# Colocamos 5 barcos aleatoriamente para la computadora
for _ in range(5): #
    while True:
        x = np.random.randint(1, 6) #   Generamos coordenadas aleatorias para colocar un barco
        y = np.random.randint(1, 6) # Generamos coordenadas aleatorias para colocar un barco
        if mar_computadora[x][y] == 0:  # Aseguramos que no se coloque un barco en una posición ya ocupada
            mar_computadora[x][y] = 1 # Colocamos un barco en esa posición (valor 1) y salimos del bucle para colocar el siguiente barco
            break



print("\033[4m   1 2 3 4 5 \033[0m")
for i in range(1, 6): # Imprimimos las filas junto con los datos de la matriz
    print(f"|{i} ", end="") # Imprime el número de fila al principio
    for j in range(1, 6): #  Recorremos las columnas para imprimir el valor de cada celda
        print("\033[4m" + str(int(mar_computadora[i][j])) + "\033[0m", end=" ") # Imprime el valor de la matriz (0 o 1) con un espacio
    print()






print(" _ _ _ _ _ _ _ _")
for i in range(1, 6):
    print("|", end=" \n")
print()

print("\033[4mTexto subrayado\033[0m") # Ejemplo de texto subrayado usando códigos de escape ANSI
