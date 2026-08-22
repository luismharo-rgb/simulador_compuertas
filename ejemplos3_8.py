numeros = [-5, 3, -2, 8, -7]
"""
el comando lambda hace una pequeña funcion dentro sin declararla, ahorrando
lineas de código, en este caso el resultado de key hace que abs sea el criterio de ordenamiento,
es decir, se ordena por el valor absoluto de los numeros, pero si hay dos numeros con el mismo 
valor absoluto, se ordenan por su valor real, es decir, primero los negativos y luego los positivos.


ordenado_absoluto = sorted(numeros, key=lambda x: abs(x))
ordenado_absoluto = sorted(numeros)
ordenado_absoluto
"""
# Desafio 27
#Crea una función que tome una lista de números y devuelva la suma y el promedio de esos números.
print("--------DESAFIO 27----------------")
print("lista numeros")
arreglo=input("Ingrese los numeros separados por espacios: ")
arreglo = list(map(int, arreglo.split())) 
# convierte la cadena de entrada en una lista 
# de enteros
print("Arreglo ingresado:", arreglo)
print("------------------------")
# Desafio 28
#Diseña una función que tome una cadena y devuelva la misma cadena, pero con el primer carácter de cada palabra en mayúsculas.

print("--------DESAFIO 28----------------")
arreglo_letra=input("Ingrese las palabras separadas por espacios: ")
arreglo_letra_capital=list(map(str.capitalize, arreglo_letra.split()))  
print("Arreglo de palabras capitalizadas:", arreglo_letra_capital)
print("------------------------")
# Desafio 29
#Construye una función que tome dos listas y devuelva `True` si tienen al menos un elemento en común, de lo contrario, que devuelva `False`.
print("--------DESAFIO 29----------------")
lista1=input("Ingrese la primera lista de elementos separados por espacios: ")
lista2=input("Ingrese la segunda lista de elementos separados por espacios: ")
lista1 = set(lista1.split())  # Convertimos la primera lista a un conjunto
lista2 = set(lista2.split())  # Convertimos la segunda lista a un conjunto  
for i in lista1:
    if i in lista2:
        print("Elemento en común encontrado:", i)
        print("True")
        break
else:    print("False")
print("------------------------")

### Desafío 30: Algoritmo MCD
"""""
El Máximo Común Divisor (MCD) es un concepto matemático que ha sido estudiado desde tiempos antiguos.
Atribuido a Euclides, el algoritmo para determinarlo es elegante y eficiente. Tu tarea es 
implementar una función que calcule el MCD de dos números utilizando el algoritmo de Euclides.
""""""
