import numpy as np
mar= np.zeros((6,6)) #creamos una matriz de ceros de 6x6, la primera fila y columna se usarán para mostrar los números de las coordenadas

print(" Bienveido al juego de batalla naval ")
print(" Ingrese las coordenadas para colocar su barco (x,y) ")
print(" Ingrese 'ok' para finalizar. ")
for i in range(1, 6):   
    print(f'{i} ', end='') #imprimimos los números de las filas
print()
for i in range(1, 6):
    print(f'{i} ', end='') #imprimimos los números de las columnas
    for j in range(1, 6):
        print(int(mar[i][j]), end=' ')
    print() 
while True:
    coordenada= input("Ingrese coordenada: ")
    if coordenada.lower() == 'ok':
        break
    if coordenada == '':
        print("No se ha ingresado ninguna coordenada, intente de nuevo.")
        continue
    try:
        x, y = map(int, coordenada.split(','))
        if x < 1 or x > 5 or y < 1 or y > 5:
            print("Error: Las coordenadas deben estar en el rango de 1 a 5.")
            continue
        mar[x][y] = 1
    except ValueError:
        print("No se ha ingresado una coordenada válida, intente de nuevo.")
        continue
print("Coordenadas ingresadas:")
for i in range(1, 6):
    for j in range(1, 6):
        print(int(mar[i][j]), end=' ')
    print()
print("Gracias por jugar. ¡Hasta luego!")