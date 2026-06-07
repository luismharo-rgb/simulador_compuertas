import sys
import time

# Tu idea: El arreglo con los caracteres
iconos = ['|', '/', '-', '\\']
pasos = 20  # Cuántas veces va a girar

print("Calculando... ", end="")

for i in range(pasos):
    # Usamos el operador módulo (%) para que el índice siempre esté entre 0 y 3
    caracter_actual = iconos[i % 4] 
    
    # Imprimimos sin salto de línea
    sys.stdout.write(caracter_actual)
    sys.stdout.flush() # <--- Evitamos el problema del búfer
    
    time.sleep(0.1)
    
    # En lugar de borrar la pantalla, regresamos el cursor al inicio de la palabra
    sys.stdout.write('\rCalculando... ')

print("\r¡Listo!                      ")