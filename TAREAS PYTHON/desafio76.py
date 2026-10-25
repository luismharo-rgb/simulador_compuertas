class Nodo: # clase que define un nodo en un árbol binario
    def __init__(self, key):
        self.izq = None # nodo izquierdo
        self.der = None # nodo derecho
        self.val = key # valor del nodo

def preorder(raiz): # funcion que recorre el árbol en preorden
    if raiz:
        print(raiz.val, end=" ") # imprime el valor del nodo
        preorder(raiz.izq) # recorre el subárbol izquierdo en recursivo
        preorder(raiz.der) # recorre el subárbol derecho en recursivo

# Titulo del programa
print()
print("-" * 50)
print("Recorrido Preorden del árbol binario:")
print("-" * 50)
# Crear el nodo raíz y los nodos hijos
raiz = Nodo(1)
raiz.izq = Nodo(2)
raiz.der = Nodo(3)  
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)
# imprime un resultado 
print("-" * 50)
print("Recorrido Preorden del árbol binario:")
print("-" * 50)
print()
# esta es la llamada de la función que recorre el árbol en preorden 
preorder(raiz)
print()
print("-" * 50)
