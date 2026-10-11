# ==========================================
# EJERCICIO 2: Sistema de Empleados
# ==========================================
# OBJETIVO: Implementar herencia entre Empleado y EmpleadoComision,
# sobrescribir métodos y gestionar altas/bajas en una lista.

class Empleado:
    def __init__(self, nombre="", salario_base=0.0):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_sueldo(self):
        return self.salario_base

    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre} | Sueldo final: ${self.calcular_sueldo():.2f}")


class EmpleadoComision(Empleado):
    def __init__(self, nombre="", salario_base=0.0, ventas=0, comision_por_venta=0.0):
        # TODO: Usar super() para inicializar los atributos heredados
        # y asignar los atributos nuevos (ventas y comision_por_venta)
        pass

    def calcular_sueldo(self):
        # TODO: Sobrescribir este método.
        # El sueldo final es: salario_base + (ventas * comision_por_venta)
        pass


# --- LÓGICA DE GESTIÓN ---
def eliminar_empleado(lista_empleados, nombre_empleado):
    # TODO: Buscar en 'lista_empleados' un objeto cuyo atributo 'nombre' coincida con 'nombre_empleado'.
    # Si lo encuentra, eliminarlo de la lista y retornar True.
    # Si no lo encuentra, imprimir un aviso y retornar False.
    pass

def ejecutar_ejercicio_2():
    nomina = []

    # TODO:
    # 1. Crear un Empleado común y un EmpleadoComision y agregarlos a 'nomina'.
    # 2. Recorrer 'nomina' invocando 'mostrar_informacion()' en cada uno (Polimorfismo).
    # 3. Probar la función 'eliminar_empleado' y volver a mostrar la lista resultante.
    pass

if __name__ == "__main__":
    ejecutar_ejercicio_2()