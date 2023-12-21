def añadir_datos (fecha, peso, NAB, NAM):
    '''Esta función añade los datos al fichero empresa_ander
    si el fichero no existe lo crea.

    Parámetros:
        Fecha: un str con la fecha
        Peso: un int con el peso de albondigas
        NAB: un int con el nº de albondigas buenas
        NAM: un int con el nº de albondgas malas
    Salidas:
        Esta función no devuelve nada'''


    import os
    if os.path.isfile('empresa_ander.txt'):
        with open ('Empresa_ander.txt', "a") as file:
            file.write(fecha + '\t ' + str(peso) + '\t\t' + str(NAB) + '\t\t' + str(NAM) + '\n')
    else:
        with open ('Empresa_ander.txt', "w") as file:
            file.write('Fecha \t\t Peso\t NAB\t NAM\n' + fecha + '\t' + 
            str(peso) + '\t' + str(NAB) + '\t' + str(NAM) + '\n')

    return

añadir_datos ("14/04/2023",145,80,10)