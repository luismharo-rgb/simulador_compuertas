#print("ingrese su texto")
#texto=input().strip()
#largo=len(texto)
#lista=[]
#nueva=[]
#reves=0
#for i in range(largo):
#    lista.append(texto[(largo - 1) - i])
#print("".join(lista))
indice=0
def contar_palabra(texto, indice=0):
    #palabras = texto.split()  # Divide el texto en palabras
    nueva_lista=[]
    largo=len(texto)
    if largo  == indice + 1 :
        return 0  # Caso base: hemos terminado de revisar el texto
    # Caso recursivo: suma 1 si la palabra coincide, de lo contrario sigue buscando
    indice = indice + 1
    return (nueva_lista.append(texto[(largo - 1)]))

print("ingrese palabra")
texto=input()       
contar_palabra(texto,indice)