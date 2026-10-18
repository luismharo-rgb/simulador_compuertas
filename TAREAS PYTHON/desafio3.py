# ingresamos el numero entero para calcular 
print ("EJERCICIO 3")
print (" ")
print("Este programa calcula la suma de los primeros n números enteros positivos."  )

elnumero = input("Ingrese un número entero, debe ser positivo: ")
numero = int(elnumero)
#inicializamos la variable suma en cero para acumular el resultado de la suma
suma = 0
#comprobamos primero que el numero ingresado es positivo
if numero <= 0:
    print("Error: El número debe ser un enteo positivo mayor a cero.")
else:
    suma = 0
    for i in range(1, numero + 1):
        suma = suma + i
# esto suma el numero siguiente mas el resultado anterior hasta
#Terminar en el numero ingresado, de ahí el rango “numero”
# se imprime el resultado de la suma
    print(f"La suma de los {numero} primeros números es: {suma}")
    # se explica que también se puede calcular usando la fórmula n(n+1)/2, el resultado es: n * (n + 1) // 2
    print(f"También se puede calcular usando la fórmula n(n+1)/2, el resultado es: {numero} * ({numero} + 1) // 2")
    print("presione enter para continuar")
    input() 