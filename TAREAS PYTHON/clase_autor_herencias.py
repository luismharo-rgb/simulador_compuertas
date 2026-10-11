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

class Libro_Digital(Libro):
    """Clase que representa un libro digital dentro del sistema."""
    def __init__(self, titulo="", genero="", isbn="", autores=None, formato="", tamaño_archivo=0.0):
            # llamamos al constructor de la clase "padre" Libro
            super().__init__(titulo, genero, isbn, autores)
            # nuevo dato en la clase Libro_Digital, que no está en Libro
            self.formato = formato
            self.tamaño_archivo = tamaño_archivo

    def mostrar_digital(self):
         """Muestra la información detallada del libro digital y sus autores."""
         super().mostrar_libro()  
         # Usamos el mismo método de la clase Libro heredado, asi solo agregamos
         # los nuevos datos de la clase Libro_Digital
         print(f"Formato: {self.formato}")
         print(f"Tamaño del archivo: {self.tamaño_archivo} MB")

class EBook(Libro_Digital):
         
    def __init__(self, titulo="", genero="", isbn="", autores=None, formato="", tamaño_archivo=0.0, enlace_descarga=""):
        # Reutiliza la inicialización de LibroDigital (que a su vez llama a Libro)
        super().__init__(titulo, genero, isbn, autores, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def mostrar_ebook(self):
        """Muestra la información detallada del eBook y sus autores."""
        super().mostrar_digital()  # Usamos el mismo "truco" pero para la clase Libro_Digital
        print(f"Enlace de descarga: {self.enlace_descarga}")
        
# ---- TODOS LOS RESULTADOS  ----
# 1. Creamos un autor 
autor1 = Autor("Juanito Perez", "Argentina")

# 2. Objeto LibroDigital
libro_digital = Libro_Digital(
    titulo="Python es Re Fácil",
    genero="Ciencia Ficción",
    isbn="978-950-07-1110-3",
    autores=[autor1],
    formato="PDF",
    tamaño_archivo=1.8
)

# 3. Objeto EBook
ebook = EBook(
    titulo="Plan de evasión de impuestos",
    genero="Biografía",
    isbn="978-950-07-2200-1",
    autores=[autor1],
    formato="EPUB",
    tamaño_archivo=2.4,
    enlace_descarga="https://biblioteca.ejemplo.com/descarga/plan-de-evasion_impuestos.epub"
)

# 4. Impresión de información usando el mismo método mostrar_informacion()
print("=== DATOS DE LIBRO DIGITAL ===")
libro_digital.mostrar_digital()

print("\n" + "="*30 + "\n")

print("=== DATOS DE EBOOK ===")
ebook.mostrar_ebook()
