class Libro:
    """Clase crea un libro dentro del sistema."""

    def __init__(self, titulo="", genero="", isbn="", autores=None):
        # Atributos solicitados por la rúbrica
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        
        # Lista que guardará los objetos de la clase Autor
        # lo mismo que hace el objeto "libros" 
        if autores is not None:
            self.autores = autores
        else:
            self.autores = []
    def __repr__(self):  # def para mostrar correctamente en consola los datos y no
                         # direcciones de memoria
        return f"Libro('{self.titulo}')"
    
    def agregar_autor(self, autor):
        """Agrega una instancia de la clase Autor a este Libro y vincula el libro al autor."""
        if autor not in self.autores: # si el autor no está en autores
            self.autores.append(autor) # lo agrega
            #  actualiza la lista del autor
            if self not in autor.libros: # si el autor no está en la lista del libro
                autor.libros.append(self) # se agrega, el "self" es el dato del autor dado
            return True
        return False

    def eliminar_autor(self, autor):
        """Elimina una instancia de la clase Autor de este Libro."""
        if autor in self.autores:
            self.autores.remove(autor)
            if self in autor.libros: # elimina el autor también de los libros
                autor.libros.remove(self)
            return True
        return False

    def mostrar_libro(self):
        """Muestra la información detallada del libro y sus autores."""
        # Obtenemos los nombres de los objetos Autor vinculados
        if self.autores:
            nombres = [] # se crea una lista con los autores
            for a in self.autores:
                nombres.append(a.nombre)
        else:
                nombres = ["Sin autor registrado"] 
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.isbn}")
        print(f"Autor(es): {', '.join (nombres)}")


class Autor:
    """Clase que representa un autor dentro del sistema."""

    def __init__(self, nombre="", nacionalidad="", libros=None):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        
        # Lista que guardará instancias/objetos de la clase Libro
        if libros is not None:
            self.libros = libros
        else:
            self.libros = []

    def __repr__(self):  # def para mostrar correctamente en consola los datos y no
                         # direcciones de memoria
        return f"Autor('{self.nombre}')"


    def agregar_libro(self, libro):
        """Agrega una instancia de Libro a este Autor y vincula el autor al libro."""
        if libro not in self.libros:
            self.libros.append(libro)
            # actualiza la lista del libro de acuerdo al autor
            if self not in libro.autores:
                libro.autores.append(self)
            return True
        return False

    def eliminar_libro(self, libro):
        """Elimina una instancia de Libro de la lista del Autor."""
        if libro in self.libros:
            self.libros.remove(libro)
            if self in libro.autores: # lo elimina de los libros y autores
                libro.autores.remove(self)
            return True
        return False

    def eliminar_autor(self):
        """
        Aquí eliminamos el autor y se eliminan las referencias cruzadas entre
        libros y autores
        
        """
        for libro in list(self.libros):
            libro.eliminar_autor(self) #elimina al autor de la clase Libro
        print(f"Se ha eliminado el autor '{self.nombre}' y sus vínculos con los libros.")

    def mostrar_autor(self):
        """Muestra los detalles del autor y los títulos de sus libros."""
        # Obtenemos los títulos de los objetos Libro vinculados
       
        if self.libros:
            titulos_libros = [] # se crea una lista para agregarlos
            for l in self.libros:
                titulos_libros.append(l.titulo) # se llena la lista
        else:
            titulos_libros = ["Sin libros registrados"]

        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Libros escritos: {', '.join(titulos_libros)}")

# 1. Creamos objetos Autor
autor1 = Autor("Adolfo Bioy Casares", "Argentina")
autor2 = Autor("Jorge Luis Borges", "Argentina")

# 2. Creamos objetos Libro (cumpliendo atributos: título, género, ISBN)
libro1 = Libro("La invención de Morel", "Ciencia Ficción", "978-950-07-1110-3")
libro2 = Libro("Un modelo para la muerte", "Policial", "978-987-56-6200-1")  # Escrito en coautoría

# 3. Establecemos relaciones (1 autor escribe varios libros / 1 libro tiene varios autores)
# Agregar libros individualmente a un autor:
autor1.agregar_libro(libro1)

# Vincular un libro con coautores (múltiples autores):
libro2.agregar_autor(autor1)
libro2.agregar_autor(autor2)

print("=== Datos de Libros ===")
libro1.mostrar_libro()
print("---")
libro2.mostrar_libro()  # Mostrará a Bioy Casares y Borges

print("\n=== Datos de Autores ===")
autor1.mostrar_autor()  # Mostrará 'La invención de Morel' y 'Un modelo para la muerte'
autor2.mostrar_autor()  # Mostrará 'Un modelo para la muerte'

print("\n=== Eliminación Autor ===")
autor2.eliminar_autor()

print("\n=== Nueva Lista de Autores (después de eliminar) ===")
libro2.mostrar_libro()  # Ahora solo aparecerá autor1