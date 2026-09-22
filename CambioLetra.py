#  # Texto en negrita
# print("\033[1mEste texto está en negrita\033[0m")

# # Texto en cursiva
# print("\033[3mEste texto está en cursiva\033[0m")

# # Texto rojo y subrayado a la vez
# print("\033[31m\033[4mTexto rojo y subrayado\033[0m")

# ANSI = {
#     # Estilos
#     "reset": "\033[0m",
#     "negrita": "\033[1m",
#     "debil": "\033[2m",
#     "italica": "\033[3m",
#     "subrayado": "\033[4m",
#     "invertido": "\033[7m",
#     "tachado": "\033[9m",
    
#     # Colores Texto
#     "rojo": "\033[31m",
#     "verde": "\033[32m",
#     "azul": "\033[34m",
#     "amarillo_b": "\033[93m", # Variante brillante
    
#     # Colores Fondo
#     "fondo_rojo": "\033[41m",
#     "fondo_verde": "\033[42m",
# }
print("ingrese texto")
texto=input()
print ("ingrese estilo")
estilo= input()

    texto=""
    estilo=""
    cambio = 
    {
#   # Estilos
     "reset": "\033[0m",
     "negrita": "\033[1m",
     "debil": "\033[2m",
     "italica": "\033[3m",
     "subrayado": "\033[4m",
     "invertido": "\033[7m",
     "tachado": "\033[9m",
    }
return f"{cambio[estilo]}{texto}\033[0m"

print(" vamos a cambiar tu texto, escribelo a continuación:")
texto= input()
print(f"elige el estilo de tu texto")
estilo= int(input("reset: resetear texto \nneg: negrita \ndeb: debil \nita: italica \nsub: subrayado \ninv: invertido \ntac: tachado \n")) 
print(f"elije color")
formato(texto, estilo)

      
