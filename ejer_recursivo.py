def suma_lista (numeros):
    
    if not numeros:
        return 0
    return numeros[0] + suma_lista(numeros[1:])
# Convierte cada texto ingresado a un número entero
def contar_caracter(texto, caracter):
    if not texto:
        return 0
    
    if texto[0] == caracter:
        return 1 + contar_caracter(texto[1:], caracter)
    else:
        return 0 + contar_caracter(texto[1:], caracter)

def palindromo (palabra):
    contador= len (palabra)
    if palabra == "" or len(palabra)=0
        return True
    if palabra[0]== contador
        return True
    else    
        return False
    return palindromo(palabra[1:])



losnumeros = [int(x) for x in input("Ingrese números separados por espacios: ").split()]
print(suma_lista(losnumeros))

