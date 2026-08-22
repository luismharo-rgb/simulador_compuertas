import os
import numpy as np
import time
VERDE = "\033[0;32m"
BLANCO_SOBRE_AZUL = "\033[1;37;44m"
RESET = "\033[0m"
ERRORES = "\033[0;31m"

# Se crea una una matriz de ceros de 6x6. 
# Usaremos los índices del 1 al 5 para que coincida con lo que el usuario ve.
mar = np.zeros((6, 6)) 

print(f"{VERDE}----------¡Bienvenido al juego de batalla naval!----------{RESET}")
print("")
print(f"{BLANCO_SOBRE_AZUL} Ingrese las coordenadas para colocar su barco (fila, columna) ej: 3,4 {RESET}")
print(f"{BLANCO_SOBRE_AZUL} Ingrese 'ok' para finalizar. {RESET}")


while True:
    print("\033[4m  1 2 3 4 5 \033[0m")
    # la siguiente sección se encarga de imprimir el tablero cada vez 
    # que el usuario ingresa una coordenada, para que pueda ver cómo 
    # va quedando su mapa de barcos. Se reemplazo por algo mas limpio y ordenado 
    # conforme a la ultima evaluación de corrección de IA.
    #------------------------------------------------------------------
    #print("  ", end="")  # Espacio inicial para alinear con las filas
    #for c in range(1, 6):
    #   print(f"{c}_", end="") # Imprime los números de las columnas
    #print()  # Salto de línea
    #------------------------------------------------------------------
    # Imprimimos las filas junto con los datos de la matriz
    for i in range(1, 6):
        print(f"{i}|", end="")  # Número de fila al principio
        for j in range(1, 6):
            print("\033[4m" + str(int(mar[i][j])) + "\033[0m", end=" ") # Imprime el valor de la matriz (0 o 1) con un espacio
        print()  # Salto de línea al terminar la fila
    print("-----------------------")
    # --------------------------------------------------

    coordenada = input("Ingrese coordenada (fila,columna): ")
    
    if coordenada.lower() == 'ok': # al escribir ok, sale del bucle, aun en mayuscula o minuscula
        break
    if coordenada == '':
        print(f"{ERRORES}No se ha ingresado ninguna coordenada, intente de nuevo.{RESET}")
        continue
        
    try:
        x, y = map(int, coordenada.split(',')) #
        if x < 1 or x > 5 or y < 1 or y > 5: # validamos que las coordenadas estén dentro del rango permitido
            print(f"{ERRORES}Error: Las coordenadas deben estar en el rango de 1 a 5.{RESET}")
            continue
            
        # si habia un barco, se avisa al usuario 
        if mar[x][y] == 1:
            print(f"{ERRORES}¡Ya colocaste un barco en esa posición!{RESET}")
            continue
            
        mar[x][y] = 1  # Guardamos el barco
        
        # Opcional: Limpia la terminal para que el tablero no se repita hacia abajo
        os.system('cls' if os.name == 'nt' else 'clear') # Limpia la pantalla para una mejor experiencia de juego
        print(f"{VERDE}¡Barco colocado con éxito!{RESET}\n")

    except ValueError:
        print(f"{ERRORES}Error: Formato inválido. Debe usar números separados por coma (ej: 2,3).{RESET}\n")
        continue

print(f"{VERDE}\nPosiciones de tus barcos. Así quedó tu mapa final:{RESET}")
# Imprimimos el tablero para mostrar las posiciones finales de los barcos
print("\033[4m  1 2 3 4 5 \033[0m")
for i in range(1, 6): # Imprimimos las filas junto con los datos de la matriz
    print(f"{i}| ", end="") # Imprime el número de fila al principio
    for j in range(1, 6): #  Recorremos las columnas para imprimir el valor de cada celda
        print("\033[4m" + str(int(mar[i][j])) + "\033[0m", end=" ") # Imprime el valor de la matriz (0 o 1) con un espacio
    print()

print(f"{VERDE}\nTENDRÉ 5 TIROS, VEAMOS SI PUEDO ACERTAR A TUS BARCOS{RESET}")
print("")
acierto_enemigo=0
for i in range(5):
    random_x = np.random.randint(1, 6) # Genera un número aleatorio entre 1 y 5 para la fila
    random_y = np.random.randint(1, 6) # Genera un número aleatorio entre 1 y 5 para la columna
    print("-----------------------")
    print(f"{BLANCO_SOBRE_AZUL}pensando...{RESET}")
    time.sleep(2)  # Simula un tiempo de espera para hacer el juego más dinámico
    # Imprime el tiro que la computadora va a realizar, mostrando las coordenadas elegidas 
    print(f"{BLANCO_SOBRE_AZUL}Tiro {i+1}: Disparo a la coordenada ({random_x}, {random_y}){RESET}")
    if mar[random_x][random_y] == 1: # Si en esa coordenada hay un barco (valor 1), es un acierto
        print(f"{VERDE}¡BOOM! He acertado a un barco enemigo.\n{RESET}")
        acierto_enemigo= acierto_enemigo+1
    else: # Si no hay un barco (valor 0), es agua
        print(f"{ERRORES}¡Agua! No he acertado ningún barco.\n{RESET}")


print(f"{BLANCO_SOBRE_AZUL}\nTe toca a ti, organizaré mis barcos... a ver si puedes ganarle a la computadora{RESET}")
print("")
mar_computadora = np.zeros((6, 6)) # Creamos una matriz de ceros para representar el tablero de la computadora, igual que el del jugador.
# Colocamos 5 barcos aleatoriamente para la computadora
for _ in range(5): #
    while True:
        x = np.random.randint(1, 6) #   Generamos coordenadas aleatorias para colocar un barco
        y = np.random.randint(1, 6) # Generamos coordenadas aleatorias para colocar un barco
        if mar_computadora[x][y] == 0:  # Aseguramos que no se coloque un barco en una posición ya ocupada
            mar_computadora[x][y] = 1 # Colocamos un barco en esa posición (valor 1) y salimos del bucle para colocar el siguiente barco
            break
print(f"{BLANCO_SOBRE_AZUL}¡He colocado mis barcos! Ahora es tu turno de disparar. Ingrese las coordenadas (fila,columna) para atacar.\n{RESET}")
acierto_jugador=0

acierto_jugador = 0
tiros_totales = 0  # contadore de tiros del jugador, maximo 5 tiros

while True:
    # Calculamos los tiros restantes basados en los intentos totales
    tiros_restantes = 5 - tiros_totales
    print(f"Tiros restantes: {tiros_restantes}")
    
    coordenada = input("Ingrese coordenada para atacar (fila,columna) o 'ok' para finalizar: ")
    
    if coordenada.lower() == 'ok':
        break
    if coordenada == '':
        print("\nNo se ha ingresado ninguna coordenada, intente de nuevo.")
        continue
        
    try:
        x, y = map(int, coordenada.split(','))
        if x < 1 or x > 5 or y < 1 or y > 5:
            print("\nError: Las coordenadas deben estar en el rango de 1 a 5.")
            continue
            
        # Si la coordenada es válida se ejecuta el aataque
        tiros_totales += 1  # <--- Sumamos un intento realizado
            
        if mar_computadora[x][y] == 1:
            print(f"\n{VERDE}¡NOO! Has acertado a un barco enemigo.{RESET}")
            acierto_jugador += 1
            mar_computadora[x][y] = 0  # Marcamos el barco como hundido
            time.sleep(1)  # Pequeña pausa para mejorar la experiencia de juego
        else:
            print(f"\n{ERRORES} Je, je ¡Agua! No has acertado ningún barco.{RESET}")
            time.sleep(1)  # Pequeña pausa para mejorar la experiencia de juego
            
        # Comprobamos si ya se alcanzaron los 5 tiros
        if tiros_totales >= 5:
            print("¡Has agotado tus 5 tiros! Finalizando el turno.\n")
            break

    except ValueError:
        print("\nError: Formato inválido. Debe usar números separados por coma (ej: 2,3).")
        continue

print(f"\n{BLANCO_SOBRE_AZUL}He acertado a {acierto_enemigo} de tus barcos de un total de 5 tiros.{RESET}")
print(f"\n{BLANCO_SOBRE_AZUL}Has acertado a {acierto_jugador} de mis barcos.{RESET}")
if acierto_enemigo > acierto_jugador:
    print(f"\n{BLANCO_SOBRE_AZUL}¡La computadora gana! Mejor suerte la próxima vez.{RESET}")
elif acierto_jugador > acierto_enemigo:
    print(f"\n{BLANCO_SOBRE_AZUL}¡Felicidades! Has ganado a la computadora.{RESET}")
else:
    print(f"\n{BLANCO_SOBRE_AZUL}¡Es un empate! Ambos hemos acertado la misma cantidad de barcos.{RESET}")   
print(f"\n{BLANCO_SOBRE_AZUL}\n¡Gracias por jugar! ¡Hasta luego!{RESET}")