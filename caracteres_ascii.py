# de caracteres a ascii
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

def char_to_ascii(char):
    return ord(char)    #ord() devuelve el valor ASCII de un caracter
lista_caracteres = []
print("         Programa para convertir numeros a ASCII.       " )
print("")
print("Ingrese numeros para convertir a ASCII. Escriba 'ok' para finalizar.")


while True:
    caracter= input("Ingrese un numero: ")
    if caracter.lower() == 'ok':
        break
    if caracter == '':
        print("No se ha ingresado ningún numero, intente de nuevo.")
        continue
    if len(caracter) > 1:
        print("Se ha ingresado más de un numero, intente de nuevo.")
        continue
    if not caracter.isdigit():
        print("No se ha ingresado un numero válido, intente de nuevo.")
        continue
    lista_caracteres.append(caracter)

for caracter in lista_caracteres:
    print(f'El valor ASCII de "{caracter}" es: {char_to_ascii(caracter)}')

print("Gracias por usar el programa. ¡Hasta luego!")
