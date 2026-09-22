# Este ejemplo muestra como funciona las propiedades "publicas", "protegidas" y "privadas"
# Este es el inicio para entender @property, @setter y @deleter
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin_secreto):
        self.titular = titular          # Público
        self._saldo = saldo_inicial     # Protegido (Aviso: solo para la clase y sus hijos)
        self.__pin = pin_secreto        # Privado (Python activará el Name Mangling)

class CuentaJoven(CuentaBancaria):
    def mostrar_datos(self):
        # 1. Acceder al protegido (_) SÍ se puede en la subclase
        print(f"Saldo disponible: ${self._saldo}") 
        
        # 2. Acceder al privado (__) va a fallar
        try:
            print(f"Tu PIN es: {self.__pin}")
        except AttributeError:
            print("❌ Error: No puedo acceder a __pin desde la subclase.")

# --- Probando el código ---
cuenta = CuentaJoven("Sofía", 1500, "1234")

# Intentando usar los datos desde FUERA de la clase:
print(cuenta.titular)      #  Funciona: Imprime "Sofía"
print(cuenta._saldo)       #  Funciona (Pero está mal visto porque es protegido): Imprime 1500

# Ejecutamos el método de la subclase
cuenta.mostrar_datos()
# Esto funciona porque Python renombró la variable internamente:
print()
print("la siguiente es una llamada al 'nombre secreto'")
print(cuenta._CuentaBancaria__pin)  # Imprime "1234"
# la estamos llamando por su nombre interno, pero no es recomendable hacerlo.