# llamada a función y nuevo alias
import cambio_texto as ct

# inicia variable para evitar error en while.
texto = ""

# Titulo
print("\033[7m----BIENVENIDO A TEXTO A TU ESTILO----\033[0m")
print("vamos a cambiar tu texto")
print()

while True:
    print("------------------------------------------------")
    # pedimos los datos al usuario para la función.
    print("ingrese su texto (ingrese '0' para salir)")

    texto = input().strip()  # ingresamos los datos en la variable "texto".

    if texto == "0":
        print("saliendo del programa... ¡Gracias!")
        break

    print()
    # le damos al usuario las opciones de la función.
    print("estas son tus opciones")
    print()
    print("texto subrayado: ingrese 1")
    print("texto invertido: ingrese 2")
    print("texto cursiva  : ingrese 3")
    print("texto tachado  : ingrese 4")
    print("texto negrita  : ingrese 5")
    print()
    print("ingrese su opción")
    entrada_opcion = input().strip()
    # Verificamos si es un numero o no, para evitar errores en la función.
    if entrada_opcion.isdigit():
        opcion = int(entrada_opcion)
        print(ct.cambio_texto(texto, opcion))
    else:
        print("¡Error! Debe ingresar un número válido (del 1 al 5).")
