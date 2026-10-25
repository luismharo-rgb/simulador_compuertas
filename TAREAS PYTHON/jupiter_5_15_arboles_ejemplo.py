class Nodo:
    def __init__(self, key):
        self.izq = None
        self.der = None
        self.val = key

def preorder(raiz):
    if raiz:
        print(raiz.val, end=" ")
        preorder(raiz.izq)
        preorder(raiz.der)



# Crear el nodo raíz
raiz = Nodo(1)

# Añadir nodos hijos
raiz.izq = Nodo(2)
raiz.der = Nodo(3)

# Añadir nodos hijos al nodo izquierdo del raíz
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)

# Añadir nodos hijos al nodo derecho del raíz
raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)

# Añadir nodos hijos al nodo hijo derecho del hijo izquierdo del raíz
raiz.izq.der.izq = Nodo(8)
raiz.izq.der.der = Nodo(9)

# Añadir nodos hijos al nodo hijo derecho del hijo derecho del raíz
raiz.der.der.izq = Nodo(10)
raiz.der.der.der = Nodo(11)

preorder(raiz)  # Salida esperada: 1 2 4 5 8 9 3 6 7 10 11 