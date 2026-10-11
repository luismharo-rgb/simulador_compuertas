# de caracteres a ascii
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

def ascii_to_char(num_ascii):
    return chr(int(num_ascii))    #chr() devuelve el caracter de un valor ASCII
lista_codigos = []
print("         Programa para convertir ASCII a caracteres       " )
print("")
print("Ingrese numeros para convertir  ASCII a caracteres. Escriba 'ok' para finalizar.")


while True:
    caracter= input("Ingrese un numero: ")
    if caracter.lower() == 'ok':
        break
    if caracter == '':
        print("No se ha ingresado ningún numero, intente de nuevo.")
        continue
    if int(caracter) < 0 or int(caracter) > 255:
        print("Error: El número debe estar en el rango de 0 a 255.")
        continue
    if not caracter.isdigit():
        print("No se ha ingresado un numero válido, intente de nuevo.")
        continue
    lista_codigos.append(caracter)

for codigo in lista_codigos:
    print(f'El caracter de valor ASCII "{codigo}" es: {ascii_to_char(codigo)}')

print("Gracias por usar el programa. ¡Hasta luego!")
