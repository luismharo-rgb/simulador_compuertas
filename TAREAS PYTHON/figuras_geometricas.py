import math

class Figura:
    # esta clase no se instancia, es solo un "molde" para las demás
    # así podemos crear una función area() que sea llamada con el mismo nombre
    # pero funcione diferente en cada clase hija.
    def area(self):
       pass

class Cuadrado(Figura):

    def __init__(self, lado):
        # usar el nombre del método area() y sobre escribirlo en cada clase hija
        # Al no tener datos, la clase padre no hace nada, pero si tuvieramos datos, los heredaría
        self.lado =lado

    def area(self):
        return self.lado ** 2
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)      

calculo_cuadrado= Cuadrado(5)
calculo_circulo= Circulo(3)

figuras=[calculo_cuadrado, calculo_circulo]

print(" === ÁREAS DE LAS FIGURAS GEOMÉTRICAS ===")
print("-" * 42)
for figura in figuras:
# el type lo que hace es mostrar el nombre de la clase a la que pertenece el objeto
# por eso llama a "__name__" 
    print()
    print(f"El área de la figura {type(figura).__name__} es: {figura.area()}")

        
        