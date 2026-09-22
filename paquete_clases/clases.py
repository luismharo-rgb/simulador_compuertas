# Clase base Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
    def mayoria_de_edad(self):
        if self.edad >= 18 : return "Soy mayor de edad !!"
        else: 
            return "Soy menor de edad !!"

# Clase Profesional que hereda de Persona
class Profesional(Persona):
    def __init__(self, nombre, edad, profesion):
        super().__init__(nombre, edad)
        self.profesion = profesion
    
    def trabajar(self):
        print(f"Soy {self.nombre} y trabajo como {self.profesion}.")

# Clase Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def estudiar(self):
        print(f"Soy {self.nombre} y estoy estudiando {self.carrera}.")

# Clase Deportista que hereda de Persona
class Deportista(Persona):
    def __init__(self, nombre, edad, deporte):
        super().__init__(nombre, edad)
        self.deporte = deporte
    
    def entrenar(self):
        print(f"Soy {self.nombre} y practico {self.deporte}.")

# Clase Futbolista que hereda de Deportista
class Futbolista(Deportista):
    def __init__(self, nombre, edad, equipo):
        super().__init__(nombre, edad, "fútbol")
        self.equipo = equipo
    
    def jugar_partido(self):
        print(f"Soy {self.nombre}, juego en el equipo {self.equipo} y estoy listo para el próximo partido.")

