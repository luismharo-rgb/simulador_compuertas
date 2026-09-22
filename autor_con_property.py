class Autor:
    # En un principio se usó libros= [] pero investigué que 
    # si lo pongo en el __init__ se lee solamente cuando 
    # se crea la instancia y no cada vez que se usa
    # por tanto se declara como "None" como una variable sin datos
    # de manera intencional, y así no crear una lista vacia
    # que comparte memoria con todas las variables que se creen.
    # Esto haría que cada autor que se cree nuevo comparta la misma
    # lista de libros
    
    # aqui estaba antes libros = []
    def __init__(self, nombre="", nacionalidad="", libros=None): 
        # Al asignar self.nombre y self.nacionalidad invocas a los @setter,
        # aplicando la validación desde el momento de instanciar el objeto.
        self.nombre = nombre
        self.nacionalidad = nacionalidad

        # Evita el compartir memoria: si el usuario pasó una lista
        # entonces usa esa "habitación"
        if libros is not None:
            self.libros = libros  
        else:
            # Si no se pasó nada (es None), crea una lista VACÍA NUEVA para esta instancia.
            # o sea, crea una "habitación vacia" solo para ella
            self.libros = []      

    # --- PROPIEDAD NOMBRE ---
    @property
    def nombre(self):
        """Getter para el atributo privado _nombre."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Setter que intercepta y valida que el nombre no sea una cadena vacía."""
        # la instrucción isinstance() verifica si el valor que le ingresan es del tipo
        # de dato que se le pide, en este caso str (string)
        if not isinstance(nuevo_nombre, str) or nuevo_nombre.strip() == "":
            print("Error: El nombre del autor no puede estar vacío.")
        else:
            self._nombre = nuevo_nombre.strip()

    # NACIONALIDAD trasnformado en @property
    @property
    def nacionalidad(self):
        """Getter para el atributo privado _nacionalidad."""
        return self._nacionalidad
    # NACIONALIDAD trasnformado en setter
    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        """Setter que intercepta y valida que la nacionalidad no sea una cadena vacía."""
        # la instrucción isinstance() verifica si el valor que le ingresan es del tipo
        # de dato que se le pide, en este caso str (string)
        if not isinstance(nueva_nacionalidad, str) or nueva_nacionalidad.strip() == "":
            print("Error: La nacionalidad no puede estar vacía.")
        else:
            self._nacionalidad = nueva_nacionalidad.strip()

    def __repr__(self):
        """Método para representar la instancia como texto legible.
        Esto es para que muestre el nombre del autor en vez de la dirección de memoria
        cuando se imprime la instancia en consola.
        """
        return f"Autor('{self.nombre}')"

    """
      Ahora, nacionalidad y nombre estan en un getter y un property, así la asignación
      de datos vacios no se permite y se puede controlar desde el setter.
                       
    """

    def agregar_libro(self, libro):
        # Agrega un libro a la lista si no existe previamente.
        if libro not in self.libros:
            self.libros.append(libro)
            return True
        return False

    def eliminar_libro(self, libro):
        # Elimina un libro de la lista si existe
        # dentro de la variable a la que se le pregunta
        if libro in self.libros: # si el libro fué encontrado en esa variable
            self.libros.remove(libro) # eliminala
            return True
        return False

    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Libros: {', '.join(self.libros) if self.libros else 'Sin libros registrados'}")


#--- TEST DEL CODIGO ---


# 1. Crear un objeto Autor
autor1 = Autor("Agatha Christie", "Reino Unido")

# 2. Mostrar sus datos utilizando las propiedades (@property)
# el @property permite acceder a los datos de manera controlada, es como
# un "acceso directo", permitiendo leer los datos pero no directamente
# sinó a travéz de una función  que se encarga de hacerlo.
print("=== 1. Lectura inicial mediante @property ===")
print(f"Nombre (vía getter): {autor1.nombre}")
print(f"Nacionalidad (vía getter): {autor1.nacionalidad}")

# 3. Modificar su nombre o nacionalidad mediante los setters (Cambio Válido)
# el @setter permite modificar los datos pero no los modificamos directamente
# sinó que es un "enmascaramiento", el setter se encarga de validar y modificar.
print("\n=== 2. Modificación válida mediante @setter ===")
autor1.nombre = "Agatha Mary Clarissa Christie"  # Invoca a @nombre.setter
autor1.nacionalidad = "Inglaterra"              # Invoca a @nacionalidad.setter

# Mostramos el cambio exitoso
print(f"Nuevo nombre: {autor1.nombre}")
print(f"Nueva nacionalidad: {autor1.nacionalidad}")

# 4. Resultado de asignar un valor vaciio
print("\n=== 3. Intento de asignación de valores vacíos ===")
autor1.nombre = ""       # El setter "ataja" el error y retiene el nombre anterior
autor1.nacionalidad = "   " # El setter "ataja" el error y retiene la nacionalidad anterior

# Como quedan los datos después de los intentos inválidos.
print("\n=== 4. Estado final del objeto (Datos retenidos intactos) ===")
autor1.mostrar_autor()