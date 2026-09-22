# se define una función que recibe el texto
def invert_text(text):
    # el texto se divide en palabras
    palabras = text.split()

    # se crea una nueva función que será la recursiva
    # esta recibirá la lista de las palabras para reorganizar 
    def recursiva(lista): 
        # en caso que la lista esté vacia devuelve ""
        if not lista:
            return ""
        
        # en caso que la lista tenga un solo objeto (ingresado o final)
        # devuelve el resto la lista (esta es la condición de final recursivo)
        if len(lista) == 1:
            return lista[0]
        
        # El orden sería con el ejemplo : "la casa roja"
        # 1er iteración - toma el resto de la lista "casa roja" para llevarlo nuevamente
        # a la recursividad, dejando en pausa el espacio + el primer elemento ,o sea,
        # "roja"  
        # 2da iteración - toma desde el 1 elemento en adelante ("roja") y deja en pausa la
        # suma de espacio + "casa"
        # 3er iteración -  al ser un unico elemento "roja" en la lista, entra en el 
        # if que dice que si el largo de la lista es 1 debe retornar el único elemento, o sea
        # en este caso "roja".
        # Luego de haber arrojado un resultado, el if se "desdenrolla" y comienza a realizar
        # las sumas que tenía en pausa, sumando: roja + espacio + casa + espacio + la
        # dejando en la lista "roja casa la"
        return recursiva(lista[1:]) + " " + lista[0]
        
    # devoluci[on de la oración cambiada]
    return recursiva(palabras)


# titulo del programa
print(" --- INVERSOR DE ORACIÓN ---")
print() # espacio separador 

# aviso de ingreso de oración
print("Ingrese su oración")

# la oración se ingersa en una variable
oracion = input()

# la variable se ingresa en la recursividad
print("Tu texto invertido es el:")
print("----------")
print(invert_text(oracion))
print("----------")
