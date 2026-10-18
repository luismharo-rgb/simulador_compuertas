potencias=[2**i for i in range(10)]
print(potencias)

def contarletras_a(palabra):
    contador = 0
    for letra in palabra:
        if letra.lower() == 'a':
            contador += 1
    return contador 

print(contarletras_a("Hola, ¿cómo estás?"))


