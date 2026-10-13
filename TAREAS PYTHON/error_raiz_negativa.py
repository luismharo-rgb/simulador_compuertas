import math      # libreria de python para operaciones matematicas
class NegativeNumberError (Exception):
    # se hereda de Exception para crear una clase de error
    #personalizada
    # el siguiente comentario en ("""") es para documentar la clase y explicar su uso
    """Clase que hereda de Exception y maneja mensajes de error de 
    raiz cuadrada de numeros negativos."""
    def __init__(self, mensaje="ERROR: No se puede calcular la raíz cuadrada de un número negativo."):
        self.mensaje=mensaje
        super().__init__(self.mensaje)
def calcular_raiz_cuadrada(numero): # función que calcula la raíz cuadrada de un número
    if numero < 0:
    # "raise" muestra el mensaje de error definido en la clase NegativeNumberError, deteniendo
    # la ejecución del programa, evitando que siga funcionando con datos posiblemente corruptos.
        raise NegativeNumberError() 
    else:
        return math.sqrt(numero) # formula para raiz cuadrada, usando la libreria math de python
print("-" * 50)
print("VAMOS A CALCULAR RAICES CUADRADAS")
print("-" * 50)
numero1=int(input("Ingrese un numero para calcular su raiz cuadrada: "))
try:
    resultado = calcular_raiz_cuadrada(numero1) # llamada a función
    print(f"La raiz cuadrada de {numero1} es: {resultado}")
# se puede usar el siguente código con la variable "e" para mostrar el mensaje de error,
#  pero en este caso no es necesario
# except NegativeNumberError as e:
#    print(e)
except NegativeNumberError :
    print(NegativeNumberError().mensaje)
