def cambio_texto(texto, opcion): # ingreso variables de módulo
    # de acuerdo a la opcion, se aplican los cambios
    if opcion==1:
        print(f"texto a subrayado:")
        resultado=f"\033[4m{texto}\033[0m" # las opciones están en codigo ANSI
    elif opcion==2: # en caso de que no sea 1 usamos elif para evaluar las otras opciones
        print(f"texto en invertido:")
        resultado=f"\033[7m{texto}\033[0m"
    elif opcion==3:
        print(f"texto cursiva:")
        resultado=f"\033[3m{texto}\033[0m"
    elif opcion==4:
        print(f"texto tachado:")
        resultado=f"\033[9m{texto}\033[0m"
    elif opcion==5:
        print(f"texto en negrita:")
        resultado=f"\033[1m{texto}\033[0m"
    else:    
        print(f"opción no válida, no se hizo cambio") # en caso de no ser alguna de las opciones.
        resultado= texto # se retorna texto sin cambios.   
    return resultado # retorna el resultado de acuerdo a lo elegido


