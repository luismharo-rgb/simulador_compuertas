import os
os.system('cls' if os.name == 'nt' else 'clear')
print("-"*30)
print("LLENEMOS ESA LISTA!")
print("-"*30)
print("A continuación...")

def eliminar_duplicados(lista): 
    #toma la lista ingresada por el usario y la procesa para eliminar los duplicados
    nuevalista = [] # datos ingresados por usuario
    lista_limpia = [] # lista procesada sin duplicados

    for numero in lista: 
        if numero not in lista_limpia:  # juzga si el numero no esta en la lista limpia
            lista_limpia.append(numero) # agrega a la lista limpia si no esta
        else:
            nuevalista.append(numero) # Agrega a la lista de duplicados si ya esta en la lista limpia

    return lista_limpia, nuevalista # devuelve lista limpia y lista de duplicados

lista=[] #inicializa la lista vacia para que el usuario ingrese los datos
while True: # bucle para ingresar datos hasta que el usuario ingrese 'fin'
    try: # se ejecutará el bloque de código y si hay un error se ejecutará el bloque ´except´
        print("Ingrese un elemento, ingrese 'fin' para terminar: ")
        numero= input()
        if numero.lower() == 'fin': # si el usuario ingresa 'fin' se termina el bucle
            break
        else:
            lista=lista + [int(numero)]  # Agrega el número a la lista
    
    except ValueError:
        print("Por favor, ingrese solo números.")

#lista = [1,2,3,2,1,4,5,2,3,6]

#ubica los resultados de la función
#en orden de la tupla que devuelve la función


lista_limpia, nuevalista = eliminar_duplicados(lista) # se envian los datos a la función 
print("-"*30)
print("RESULTADOS DE LA FUNCION")
print("-"*30)
print("Lista original:", lista)
print("Duplicados (nuevalista):", nuevalista)
print("Únicos (lista):", lista_limpia)
