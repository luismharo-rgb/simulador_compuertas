import os # importamos para limpieza de pantalla
def limpiar_pantalla(): # definimos una funcion que limpie patanlla
    os.system('cls' if os.name == 'nt' else 'clear')

# biblioteca = [] # Ahora esta variable guarda que biblioteca se usa
que_uso="Accion"
biblioteca = que_uso
libreria = {   # contiene las bibliotecas
    "Accion": [],
    "Aventura": [], 
    "Drama": [],
}           


def librerias_disponibles():
    print("\n--- LIBRERÍAS DISPONIBLES ---")
    for i, nombre in enumerate(libreria, start = 1): 
        print(i, ":", nombre)
        
    que_uso = input("¿Qué librería quiere usar? (1, 2 o 3): ").strip()
    
    if que_uso == '1':
        print("Librería seleccionada: Acción")
        return "Accion"
    elif que_uso == '2':
        print("Librería seleccionada: Aventura")
        return "Aventura"
    elif que_uso == '3':
        print("Librería seleccionada: Drama")
        return "Drama"
    else:
        print("Opción no válida.")
        return None


# aqui dejo la función anterior cuando se usaba solo
# una biblioteca                       
#def agrega_libro (libro): # Función que agrega libro
       
#    if buscar_libro(libro) == []: # Verifica si el libro ya está
#        biblioteca.append(libro) # en caso busqueda vacia, lo ingresa
#        return True
#    else:
#        return False # retorna falso si el libro ya existe

# esta es la nueva función, la que utiliza bibliotecas
# seleccionadas por el usuario
def agrega_libro(biblio_activa, libro):
    # Le pasamos 'biblio_activa' también a buscar_libro
    if buscar_libro(biblio_activa, libro) == []:
        biblio_activa.append(libro) # Agrega el libro a esa lista específica
        return True
    else:
        return False


    

#def eliminar_libro(libro): # función que elimina libros
#    para_eliminar = buscar_libro(libro) # busca si el libro existe
#    if para_eliminar == []: # si el libro no existe, informa error
#        print("EL LIBRO INGRESADO NO SE ENCUENTRA")
#        return False
    # el siguiente código imprime todas las coincidencias
    # del libro a buscar  

#    print("\nLibros coincidentes encontrados:") 

    # 'enumerate' nos da el índice (i) y el texto del libro
    # Empezamos a contar desde 1 para el usuario (asi no muestra "0")
    # la sección "start=1" configura desde que número inicia la cuenta

#    for i, libro_encontrado in enumerate(para_eliminar, start=1): 
#        print(f"{i}. {libro_encontrado}")
    # el "for" anterior, imprime la lista de los libros, dandole un número
    # a cada uno, luego, pedimos al usuario que seleccione el número
    # para esto, usamos ".strip()" que configure el ingreso correctamente
#    opcion = input("\nIngrese el número del libro que desea eliminar: ").strip()
    # Validamos que el usuario haya ingresado un número válido

#    if opcion.isdigit(): # si la opción es un número...
#        seleccion = int(opcion) - 1 
        # Restamos 1 para volver al índice real de Python (0, 1, 2...)
        # Verificamos que el número esté dentro del rango de la lista de encontrados
#        if 0 <= seleccion < len(para_eliminar):
#            libro_seleccionado = para_eliminar[seleccion]
            # Buscamos ese libro específico en la 'biblioteca' real y lo eliminamos
#            biblioteca.remove(libro_seleccionado)
#            print(f"¡El libro '{libro_seleccionado}' ha sido eliminado con éxito!")
#            return True
    # en caso de un mal ingreso de opciones        
#    print("Opción inválida. No se eliminó ningún libro.")
#    return False




# esta nueva función busca eliminar un libro en la biblioteca seleccionada
def eliminar_libro(biblio_activa, libro):
    # Le pasamos la lista 'biblio_activa' a buscar_libro
    para_eliminar = buscar_libro(biblio_activa, libro) 
    if para_eliminar == []: 
        print("EL LIBRO INGRESADO NO SE ENCUENTRA")
        return False

    print("\nLibros coincidentes encontrados:") 
    for i, libro_encontrado in enumerate(para_eliminar, start=1): 
        print(f"{i}. {libro_encontrado}")

    opcion = input("\nIngrese el número del libro que desea eliminar: ").strip()

    if opcion.isdigit():
        seleccion = int(opcion) - 1 
        if 0 <= seleccion < len(para_eliminar):
            libro_seleccionado = para_eliminar[seleccion]
            # Eliminamos directamente de la lista activa
            biblio_activa.remove(libro_seleccionado)
            print(f"¡El libro '{libro_seleccionado}' ha sido eliminado con éxito!")
            return True
        
    print("Opción inválida. No se eliminó ningún libro.")
    return False











# esta es la función anterior de buscar libro, usando solo
# una biblioteca
#def buscar_libro(titulo_buscado): # busca libro
    # quitamos mayusculas y espacios para buscar correctamente
#    titulo_buscado = titulo_buscado.lower().strip() 
#    coincidencias = [] # inicializamos una lista que tendra las coincidencias
#    for libro in biblioteca: # cambiamos libro por titulo_buscado
#        # Quitamos ['titulo'] porque 'libro' ya es el texto del título
#        if titulo_buscado in libro.lower().strip(): # si hay coincidencia...
#            coincidencias.append (libro) # se agrega a la nueva lista
#    return coincidencias  # retorna todas las coincidencias


# esta es la nueva función, la que utiliza bibliotecas
# seleccionadas por el usuario
def buscar_libro(biblio_activa, titulo_buscado):
    titulo_buscado = titulo_buscado.lower().strip() 
    coincidencias = [] 
    for libro in biblio_activa: # Busca dentro de la lista recibida
        if titulo_buscado in libro.lower().strip():
            coincidencias.append(libro) 
    return coincidencias







#def lista_completa(): # muestra toda la lista de libros
#    print()
#    print ("\n Y la lista de libros son...:")
#    print("---------------------------------")
    # enumera los libros de la biblioteca
#    for i, libro in enumerate(biblioteca, start=1): 
#        print(i, ".", libro)
#    print("---------------------------------")
#    print("PRESIONE ENTER PARA SALIR")
#    input()
    # luego de enumerarlos, limpia la pantalla
#    limpiar_pantalla()  
#    return True
            

def lista_completa():
    print("\n Y la lista de libros por biblioteca son...:")
    print("---------------------------------")
    
    # Bucle 1: Recorre los nombres de las bibliotecas ("Accion", "Aventura", etc.)
    for i, nombre_biblio in enumerate(libreria, start=1): 
        print(f"\n{i}. --- Biblioteca: {nombre_biblio} ---")
        
        # Obtenemos la lista real de libros de esa biblioteca
        lista_de_libros = libreria[nombre_biblio]
        
        if len(lista_de_libros) == 0:
            print("   (Esta biblioteca no tiene libros)")
        else:
            # Bucle 2: Recorre los libros de la biblioteca actual
            for j, libro in enumerate(lista_de_libros, start=1): 
                print(f"   {j}. {libro}")
                
    print("---------------------------------")
    print("PRESIONE ENTER PARA SALIR")
    input()
    limpiar_pantalla() 
    return True


def menu(nombre_actual): 
    print(f"\n--- MENÚ BIBLIOTECA (Librería activa: {nombre_actual}) ---")
    print("Presione 'B' para elegir bibliotecas")
    print("0. Registrar libro")
    print("1. Eliminar libro")
    print("2. Buscar coincidencia parcial (ej. 'Harry')")
    print("3. Lista de todos los libros")
    print("4. Salir")
    print("Luego de elegir, presione ENTER")
    opcion = input().strip().lower() 
    return opcion

que_uso = "Accion" # Nombre de la biblioteca inicial

while True: 
    # Asignamos la biblioteca real que se está usando
    biblio_activa = libreria[que_uso]
    
    ingreso = menu(que_uso)
    
    if ingreso == '0':
        libro = input("Ingrese el nombre del libro: ").lower().strip()
        # pasamos la lista 'biblio_activa' como 1er parámetro
        if not agrega_libro(biblio_activa, libro): 
            print("ESTE LIBRO YA ESTA INGRESADO")
        else: 
            print("LIBRO INGRESADO CORRECTAMENTE, presione ENTER")
            input()

    elif ingreso == '1':
        libro_a_borrar = input("Ingrese el libro a eliminar: ").lower().strip()
        # Le pasamos la lista 'biblio_activa'
        eliminar_libro(biblio_activa, libro_a_borrar)
        print("Presione ENTER para continuar")
        input()

    elif ingreso == '2':
        print("INGRESE EL NOMBRE DEL LIBRO")
        buscado = input().strip().lower()
        # Le pasamos la lista 'biblio_activa'
        resultado = buscar_libro(biblio_activa, buscado)

        if not resultado: 
            print("El libro no está en la biblioteca. ¿Deseas agregarlo?")
            respuesta = input("ESCRIBA 'S' POR SI Y 'N' POR NO: ").lower().strip()

            if respuesta == 's':
                libro = input("Ingrese el nombre del libro: ").lower().strip()
                # Le pasamos la lista 'biblio_activa'
                agrega_libro(biblio_activa, libro) 
                print("LIBRO INGRESADO CORRECTAMENTE, presione ENTER para continuar")
                input()
            elif respuesta == 'n':
                pass 
        else:
            print(f"¡Libro encontrado! Aquí está: {resultado}")
            print("Presione ENTER para continuar")
            input()

    elif ingreso == '3':
        # Le pasamos la lista 'biblio_activa'
        lista_completa() 

    elif ingreso == '4':
        print("Gracias por usar la biblioteca. ¡Hasta luego!")
        break 

    elif ingreso == 'b':
        # Guardamos la nueva selección en 'que_uso'
        nueva_libreria = librerias_disponibles()
        if nueva_libreria: # Si no eligió una opción inválida
            que_uso = nueva_libreria
        
    else:
        print("\n--------------------------------------------------")
        print("Opción inválida. Debe ingresar un número entre 0 y 4 o 'B'.")
        print("--------------------------------------------------")
        print("Presione ENTER para continuar")
        input()