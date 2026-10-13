def dividir_numeros(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: No ha ingresado un numero valido. Use solo enteros.")
    

print("-" * 50)
print("USEMOS UN TRY/EXCEPT")
print("-" * 50)

numero1=dividir_numeros("Ingrese el primer numero: ")
numero2=dividir_numeros("Ingrese el segundo numero: ")

try:
    resultado = numero1 / numero2
    print(f"El resultado de la division es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
