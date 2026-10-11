# ==========================================
# EJERCICIO 1: Gestión de Inventario Simple
# ==========================================
# OBJETIVO: Crear una clase 'Producto' con validaciones en su setter
# y administrar una lista global de productos.

class Producto:
    def __init__(self, nombre="", precio=0.0):
        self.nombre = nombre
        self._precio = 0.0
        self.precio = precio  # Llama al setter para validar

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print ("Error: El precio debe ser mayor a 0. Se asignará 0.0 por defecto")
            self._precio =0.0

        # TODO: Implementar validación.
        # Si 'nuevo_precio' es mayor a 0, asignarlo a self._precio.
        # Si es menor o igual a 0, imprimir un mensaje de error y asignar 0.0.
        

    def mostrar_detalle(self):
        # TODO: Imprimir el nombre y el precio formateado (ej: "Producto: Laptop | Precio: $850.00")
        pass


# --- PRUEBA Y CONTROL DE FLUJO ---
def ejecutar_ejercicio_1():
    inventario = []

    # TODO: Usa un bucle 'while' o 'for' para solicitar al usuario que ingrese 3 productos por consola.
    # Instancia cada 'Producto', agrégalo a la lista 'inventario' y finalmente
    # recorre la lista con un bucle 'for' mostrando el detalle de cada uno.
    pass

if __name__ == "__main__":
    ejecutar_ejercicio_1()