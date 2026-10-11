# ==========================================
# EJERCICIO 3: Centro Educativo y Cursos
# ==========================================
# OBJETIVO: Crear la jerarquía Curso -> CursoOnline -> CursoEnVivo,
# vincular cursos con estudiantes y construir un menú funcional.

class Curso:
    def __init__(self, titulo="", codigo=""):
        self.titulo = titulo
        self.codigo = codigo
        self.estudiantes = []  # Lista que guardará nombres de estudiantes (strings)

    def inscribir_estudiante(self, nombre_estudiante):
        # TODO: Agregar el estudiante a la lista solo si no está previamente inscrito.
        pass

    def mostrar_curso(self):
        print(f"Curso: {self.titulo} [{self.codigo}]")
        print(f"Inscritos: {', '.join(self.estudiantes) if self.estudiantes else 'Sin estudiantes'}")


class CursoOnline(Curso):
    def __init__(self, titulo="", codigo="", plataforma=""):
        # TODO: Inicializar con super() e integrar 'plataforma'
        pass

    def mostrar_curso(self):
        # TODO: Usar super().mostrar_curso() e incluir la plataforma
        pass


class CursoEnVivo(CursoOnline):
    def __init__(self, titulo="", codigo="", plataforma="", horario=""):
        # TODO: Inicializar con super() e integrar 'horario'
        pass

    def mostrar_curso(self):
        # TODO: Usar super().mostrar_curso() e incluir el horario
        pass


# --- MENÚ INTERACTIVO ---
def menu():
    cursos_registrados = []

    while True:
        print("\n--- SISTEMA DE GESTIÓN ACADÉMICA ---")
        print("1. Crear Curso en Vivo")
        print("2. Inscribir Estudiante a un Curso")
        print("3. Ver Cursos y sus Estudiantes")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # TODO: Pedir los datos por consola (titulo, codigo, plataforma, horario),
            # instanciar CursoEnVivo y guardarlo en 'cursos_registrados'.
            pass
        elif opcion == "2":
            # TODO: Pedir el código del curso. Buscarlo en 'cursos_registrados'.
            # Si existe, pedir el nombre del estudiante e inscribirlo usando 'inscribir_estudiante()'.
            pass
        elif opcion == "3":
            # TODO: Recorrer 'cursos_registrados' y llamar a 'mostrar_curso()'.
            pass
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()