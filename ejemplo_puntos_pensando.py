import sys
import time

# Los diferentes estados de los puntos suspensivos
estados_puntos = ['.  ', '.. ', '...']
segundos_totales = 5
tiempo_final = time.time() + segundos_totales

print("Procesando", end="")

i = 0
while time.time() < tiempo_final:
    # Seleccionamos el estado actual
    puntos = estados_puntos[i % len(estados_puntos)]
    
    # Escribimos los puntos
    sys.stdout.write(puntos)
    sys.stdout.flush()   # Forzamos la salida en tiempo real
    
    time.sleep(0.4)      # Un poco más lento para que se note el avance
    
    # El truco: retrocedemos exactamente 3 espacios para sobreescribir los puntos
    sys.stdout.write('\b\b\b')
    
    i += 1

# Al terminar, limpiamos la zona de los puntos y mostramos el final
print("\r¡Proceso terminado con éxito!   ")