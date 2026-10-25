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
print()
print("-" * 50)
print("Recorrido Preorden del árbol binario:")
print("-" * 50)

raiz = Nodo(1)
print("Nodo raíz:", raiz.val)
raiz.izq = Nodo(2)
print("Nodo hijo izquierdo del raíz:", raiz.izq.val)
raiz.der = Nodo(3)  
print("Nodo hijo derecho del raíz:", raiz.der.val)
raiz.izq.izq = Nodo(4)
print("Nodo hijo izquierdo del hijo izquierdo del raíz:", raiz.izq.izq.val)
raiz.izq.der = Nodo(5)
print("Nodo hijo derecho del hijo izquierdo del raíz:", raiz.izq.der.val)
raiz.der.izq = Nodo(6)
print("Nodo hijo izquierdo del hijo derecho del raíz:", raiz.der.izq.val)
raiz.der.der = Nodo(7)
print("Nodo hijo derecho del hijo derecho del raíz:", raiz.der.der.val)
print("-" * 50)
print("Recorrido Preorden del árbol binario:")
print("-" * 50)
print()
preorder(raiz)
print()
print("-" * 50)
