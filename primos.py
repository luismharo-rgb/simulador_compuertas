import time
import os

# ==========================================
# FUNCIONES
# ==========================================

def primos(n): 
    """
    Verifica de manera eficiente si un número es primo a travez
    de dar un límite por la raíz cuadrada para optimizar las divisiones.
    También maneja casos como números menores a 2.
    """
    if n < 2: 
        return False 
    for i in range(2, int(n**0.5) + 1): #cálculo raiz cuadrada 
        if n % i == 0: 
            return False 
    return True

def llenar_lista():
    """
    Permite al usuario ingresar números en una lista.
    Se detiene cuando el usuario escribe 'ok' y valida errores de entrada.
    """
    lista = []
    print("Ingresa los números que quieras (o escribe 'ok' para terminar):")
    
    while True:
        entrada = input("-> ").strip().lower() # da una posición de entrada mas "gráfica"
        #también transforma todo a minuscula para que siempre sea un ok y no un Ok o oK
        if entrada == "ok":
            break
            
        try:
            numero = int(entrada)
            lista.append(numero)
        except ValueError:
            print("¡Error! Eso no es un número válido ni la palabra 'ok'. Intenta de nuevo.")
            
    return lista

def contar_primos(lista_numeros):
    """
    Recorre una lista dada, filtra los números primos usando la función 
    'primos()' y devuelve la cantidad y la lista de primos encontrados.
    """
    contador_primo = 0
    lista_primos = []
    
    for numero in lista_numeros:
        if primos(numero):
            contador_primo += 1
            lista_primos.append(numero)
            
    return contador_primo, lista_primos


# ==========================================
# PROGRAMA PRINCIPAL (MAIN)
# ==========================================
if __name__ == "__main__": # buscado como "norma de buenas costumbres" al momento de crear y 
                           # documentar códigos, así el main y este código se ejecuta solo si se presiona RUN. Puedo, gracias a esto
                          #llamar a una función como si fuera herramienta propia y no ejecutar todo el código suelto.
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--------- BUSCADOR DE PRIMOS --------\n")
    print("Este programa busca números primos dentro de una lista.")
    print("Primero, ingrese una lista de números para comprobar su 'primosidad':")
    
    # Carga de datos
    mi_lista = llenar_lista()
    print("\nTu lista está LISTA para ser 'primoseada': ", mi_lista)
    time.sleep(2)
    
    # Simulación de procesamiento (Animación)
    tempo = ""
    for i in range(5):
        tempo = tempo + "." 
        time.sleep(0.5) 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Procesando" + tempo)
    
    # Procesamiento usando la nueva función requerida
    cantidad, los_primos = contar_primos(mi_lista)
    
    # Despliegue de resultados
    print(f"Se encontraron {cantidad} números primos en tu lista.")
    print("Los números primos son:")
    print(los_primos)