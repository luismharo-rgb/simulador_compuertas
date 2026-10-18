
diccionario_productos={
    "001": {"nombre": "Camiseta", "precio": 20.0, "stock": 50},
    "002": {"nombre": "Pantalón", "precio": 35.0, "stock": 30},
    "003": {"nombre": "Zapatos", "precio": 50.0, "stock": 20}
    }
resultado=""
def busca_producto(codigo):
    if codigo in diccionario_productos:
        print("Codigo encontrado: ", diccionario_productos[codigo])
    else:
        print("producto no encontrado")
        return False
    return True
        
def ingresa_producto(codigo,nombre,precio,stock):
    if codigo in diccionario_productos:
        print("Error, producto ya ingresado:  ", diccionario_productos[codigo])
    else:
        diccionario_productos[codigo]={"nombre":nombre,"precio":precio,"stock":stock}
        
def modificar_producto(codigo,opcion,nuevo_valor):
    if codigo in diccionario_productos:
        diccionario_productos[codigo][opcion]=nuevo_valor
    else:
        print("producto no encontrado")
        return False
    return True

while True:
    print("--------MENU DE PRODUCTOS----------------")
    print("1. Buscar producto")
    print("2. Ingresar producto")
    print("3. Modificar producto")
    print("4. Salir")
    print("5. Mostrar todos los productos")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        codigo = input("Ingrese el código del producto a buscar: ")
        busca_producto(codigo)
        
    elif opcion == "2":
        codigo = input("Ingrese el código del nuevo producto: ")
        if codigo in diccionario_productos:
            print()
            print("Error, producto ya ingresado:  ", diccionario_productos[codigo])
            print()
            continue
        else:
            nombre = input("Ingrese el nombre del nuevo producto: ")
            precio = float(input("Ingrese el precio del nuevo producto: "))
            stock = int(input("Ingrese el stock del nuevo producto: "))
            ingresa_producto(codigo, nombre, precio, stock)
            print("Producto ingresado exitosamente. " + str(diccionario_productos[codigo]))
        
    elif opcion == "3":
        codigo = input("Ingrese el código del producto a modificar: ")
        if codigo in diccionario_productos:
            print("Opciones de modificación:")
            print("1. Nombre")
            print("2. Precio")
            print("3. Stock")
            sub_opcion = input("Seleccione una opción: ")
            
            if sub_opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                modificar_producto(codigo, "nombre", nuevo_nombre)
                print("Producto modificado exitosamente. " + str(diccionario_productos[codigo]))
            elif sub_opcion == "2":
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                modificar_producto(codigo, "precio", nuevo_precio)
                print("Producto modificado exitosamente. " + str(diccionario_productos[codigo]))

            elif sub_opcion == "3":
                nuevo_stock = int(input("Ingrese el nuevo stock: "))
                modificar_producto(codigo, "stock", nuevo_stock)
                print("Producto modificado exitosamente. " + str(diccionario_productos[codigo]))

            else:
                print("Opción inválida.")
        else:
            print("Producto no encontrado.")
            
    elif opcion == "4":
        break
    elif opcion == "5":
        print()
        print("Todos los productos:")
        from pprint import pprint
        pprint(diccionario_productos, indent=4, width=30, sort_dicts=False)
        
    else:
        print("Opción inválida.")
    
