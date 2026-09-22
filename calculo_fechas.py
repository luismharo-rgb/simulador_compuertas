import datetime
import calendar
def formato_fecha(fecha):
    fecha_salida= datetime.date.strptime(fecha, "%Y-%m-%d") 
    return fecha_salida
def bisiesto(year_bisiesto):
    year = int(year_bisiesto[:4])
    if calendar.isleap(year):
        print("el año ", year, " es bisiesto")
        return True
#Titulo y explicación del programa
print("\033[7m----BIENVENIDO A CALCULO DE FECHAS----\033[0m")
print("ingresa tu fecha de inicio y fin para calcular la diferencia en días")
# pedimos al usario las fecha inicial
print("fecha inicio ( ingresalo con el formato AAAA-MM-DD )")
# a lo ingresado se borra los espacios en blanco en sus extremos
fecha_inicio = input().strip()
# pedimos al usuario la fecha final
print("fecha fin ( ingresalo con el formato AAAA-MM-DD )")
# a lo ingresado se borra los espacios en blanco en sus extremos
fecha_fin = input().strip()
# se convierten las fechas al formato aceptado por la libreria datetime
# se calcula la diferencia en días
resultado = (formato_fecha(fecha_fin) - formato_fecha(fecha_inicio)).days
bisiesto(fecha_inicio)
bisiesto(fecha_fin)
print(" la diferencia entre las fechas es de:", resultado, "días")









# # Caso 1: Año bisiesto (2024)
#inicio_2024 = datetime.date(2024, 1, 1)
#fin_2024 = datetime.date(2026, 1, 1)
#print((fin_2024 - inicio_2024).days)  
## Resultado: 366 (Python detectó el 29 de febrero)

## Caso 2: Año normal (2026)
#inicio_2026 = datetime.date(2026, 1, 1)
#fin_2026 = datetime.date(2027, 1, 1)
#print((fin_2026 - inicio_2026).days)  
##Resultado: 365