print("EJERCICIO 4")
print(" ")
print("Este ejercicio consiste en pedir al usuario que ingrese una lista de números enteros separados por espacios, luego contar cuántos de esos números son pares y mostrar el resultado.  ")
print(" ")

# Como el valor "imput", al tener una lista
# nos dará un valor tipo texto, le pedimos primero
# que ingrese los numeros pero separados por espacios

lista = input("Ingresa una lista de números enteros separados por espacios: ")

# el comando ".split()" separará cada palabra
# y las guardará en una lista, por ejemplo, si el usuario ingresa "1 2 3 4"
#comprobar que la cantidad sea un numero

if not lista.replace(" ", "").replace ("-", "").isdigit():
    print("Error: ingresa solo números enteros separados por espacios.")
    print("presione enter para continuar")
    input() 
    exit()  
else:
    palabras = lista.split()

# Se inicializa una lista para guardar los numeros después de convertirlos a enteros

    numeros = []

# Vamos parabra por palabra en la lista 

    for p in palabras:
        numeros.append(int(p)) 
        # Convertimos cada palabra a un número entero y lo agregamos a la lista "numeros"

# ahora tenemos una lista de números enteros, podemos contar los pares

    contador = 0
    for num in numeros: # Recorremos cada número en la lista "numeros"
            if num < 0:
                print("Atencion: se encontró un número negativo,", num, " se procesará normalmente")
                                                
            if num % 2 == 0:   # Si el número es par (es divisible por 2 sin dejar residuo)
                contador += 1

    print(f"En la lista {numeros}, hay {contador} números pares.")
    print("presione enter para continuar")
    input() 
