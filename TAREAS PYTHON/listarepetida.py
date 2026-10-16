"""lista=["estufa","cocina","estufa","horno","cocina"]
nuevalista=[]
for i in range(len(lista)):
    for j in range(len(lista[i+1:])):
        if lista[i] == lista[i+1:][j]:
            nuevalista.append(lista[i])
for articulo in nuevalista:
    lista.remove(articulo)
print(nuevalista)
print(lista)"""

lista = ["estufa", "cocina", "estufa", "horno", "cocina"]
nuevalista = []
lista_limpia = []

for articulo in lista: 
    if articulo not in lista_limpia:  # juzga si el articulo no esta en la lista limpia
    else:
        nuevalista.append(articulo) # Agrega a la lista de duplicados si ya esta en la lista limpia

lista = lista_limpia

print("Duplicados (nuevalista):", nuevalista)
print("Únicos (lista):", lista)
