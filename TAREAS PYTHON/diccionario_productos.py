"""
Desarrolla un sistema de inventario para una tienda utilizando diccionarios, donde:
La clave es el código del producto.
El valor es otro diccionario con detalles como nombre, precio y cantidad en stock.
El programa debe permitir:
Agregar nuevos productos.
Actualizar el stock de productos existentes.
Buscar productos por código y mostrar sus detalles.
"""
diccionario_productos={
    "001": {"nombre": "Camiseta", "precio": 20.0, "stock": 50},
    "002": {"nombre": "Pantalón", "precio": 35.0, "stock": 30},
    "003": {"nombre": "Zapatos", "precio": 50.0, "stock": 20}
}
print("Bienvenido al sistema de inventario de la tienda")
def buscar_producto(codigo):
    if codigo in diccionario_productos:
        producto = diccionario_productos[codigo]
        print(f"Producto encontrado: {producto['nombre']}, Precio: ${producto['precio']}, Stock: {producto['stock']}")
    else:
        print("Producto no encontrado.")
def agregar_producto(codigo, nombre, precio, stock):
    if codigo in diccionario_productos:
        print("El producto ya existe. Use la opción de actualizar stock.")
    else:
        diccionario_productos[codigo] = {"nombre": nombre, "precio": precio, "stock": stock}
        print(f"Producto {nombre} agregado con éxito.")
def actualizar_stock(codigo, cantidad):
    if codigo in diccionario_productos:
        diccionario_productos[codigo]["stock"] += cantidad
        print(f"Stock actualizado. Nuevo stock de {diccionario_productos[codigo]['nombre']}: {diccionario_productos[codigo]['stock']}")
    else:
        print("Producto no encontrado. No se puede actualizar el stock.")
        