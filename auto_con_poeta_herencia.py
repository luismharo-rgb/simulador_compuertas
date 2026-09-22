class Autor:
    # Este es el mismo código de uso anterior 
    # por lo que hay también los mismo comentarios
    # pero se han agregado más con los cambios de @property
    # y @dato.setter
        
    
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

    # --- NOMBRE con @property---
    @property
    def nombre(self):
        """Getter para el atributo privado _nombre."""
        return self._nombre
    # --- NOMBRE con @.setter ---
    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Setter que intercepta y valida que el nombre no sea una cadena vacía."""
        # la instrucción isinstance() verifica si el valor que le ingresan es del tipo
        # de dato que se le pide, en este caso str (string)
        if not isinstance(nuevo_nombre, str) or nuevo_nombre.strip() == "":
            print("Error: El nombre del autor no puede estar vacío.")
        else:
            self._nombre = nuevo_nombre.strip()

    # --- NACIONALIDAD trasnformado en @property ---
    @property
    def nacionalidad(self):
        """Getter para el atributo privado _nacionalidad."""
        return self._nacionalidad
    # --- NACIONALIDAD trasnformado en setter ---
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
        """Método para que se pueda imprimir correctamente self.nombre.
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


# --- CLASE HIJA / SUBCLASE ---
class Poeta(Autor):
    def __init__(self, nombre="", nacionalidad="", tipo_poesia="", libros=None):
        # super() llama al __init__ de Autor para heredar 'nombre', 'nacionalidad' 
        # y la lógica de la lista de "libros", ejecutando sus getters y setters.
        super().__init__(nombre, nacionalidad, libros)
        # nuevo dato en la clase Poeta, que no está en Autor
        self.tipo_poesia = tipo_poesia

    # Método para mostrar la información del poeta
    def mostrar_poeta(self):
        # Reutilizamos el método mostrar_autor() heredado
        # al usar herencias podemos heredar los datos pero también
        # los médotos/funciones de la clase padre, en este caso Autor.
        self.mostrar_autor()
        if self.tipo_poesia:
            poesia = self.tipo_poesia
        else:
            poesia = 'No especificado'
        print(f"Tipo de poesía: {poesia}")

        


# --- Prueba de Herencia ---

# Crear dos objetos Poeta
poeta1 = Poeta("Pablo Neruda", "Chilena", "Lírica")
poeta2 = Poeta("Gabriela Mistral", "Chilena", "Educativa/Lírica")

# Mostrar sus datos completos
print("--- DATOS DE LOS POETAS ---")
poeta1.mostrar_poeta()
# Separador visual, hace 30 lineas para separar
print("-" * 30)
poeta2.mostrar_poeta()

# Verificación de herencia: Usar métodos y validaciones heredados de Autor
print("\n --- VERIFICACIÓN DE HERENCIA DE AUTOR ---")

# Aqui usamos el metodo de autor para agregar libros a los poetas 
poeta1.agregar_libro("Veinte poemas de amor y una canción desesperada")
poeta2.agregar_libro("Tala")

# Validaciones heredadas: setters de nombre/nacionalidad
#se intenta asignar un nombre vacio, lo que causa un error 
poeta1.nombre = "   "  

# Imprimimos para comprobar qeu la lista está correcta 
print(f"\nLibros de {poeta1.nombre}: {poeta1.libros}")





