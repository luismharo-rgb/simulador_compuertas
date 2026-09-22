import os
from paquete_clases.clases import Persona, Profesional, \
     Estudiante, Deportista, Futbolista


# Ejemplo de implementación de las clases
def implementacion(): 
    os.system("cls")

    # Crear una instancia de Persona
    persona1 = Persona("Ana", 30)
    persona1.presentarse()
    print(persona1.mayoria_de_edad())
    print("\n")

    # Crear una instancia de Profesional
    profesional1 = Profesional("Carlos", 40, "Ingeniero")
    profesional1.presentarse()
    profesional1.trabajar()
    print(profesional1.mayoria_de_edad())
    print("\n")

    # Crear una instancia de Estudiante
    estudiante1 = Estudiante("Lucía", 17, "Medicina")
    estudiante1.presentarse()
    estudiante1.estudiar()
    print(estudiante1.mayoria_de_edad())
    print("\n")

    # Crear una instancia de Deportista
    deportista1 = Deportista("Miguel", 25, "Natación")
    deportista1.presentarse()
    deportista1.entrenar()
    print(deportista1.mayoria_de_edad())
    print("\n")

    # Crear una instancia de Futbolista
    futbolista1 = Futbolista("Lionel", 34, "Barcelona")
    futbolista1.presentarse()
    futbolista1.entrenar()
    futbolista1.jugar_partido()
    print(futbolista1.mayoria_de_edad())
    print("\n")
