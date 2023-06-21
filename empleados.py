empleos = open('empleados.txt','a')


resp = 1

while resp != 4:

    print("\nMENU DE OPCIONES: ")
    print("1. Agregar empleados")
    print("2. Mostrar lista de empleados")
    print("3. Buscar empleados")
    print("4. Salir")
    resp = int(input("Seleccione una accion: "))
    if resp == 1:
        empleos = open('empleados.txt','a')
        nombre = input('Ingrese el nombre del empleado : ')
        apellido = input('Ahora su apellido: ')
        documento = int(input('Y por ultimo su documento: '))

        empleos.write(f'\n {nombre} { apellido} { documento} ')
        empleos.close()

    if resp == 2:
        empleos= open('empleados.txt', 'r')

        texto = empleos.read()

        print(texto)
        empleos.close()
        
    if resp == 3:
        empleos= open('empleados.txt', 'r')
        busqueda = input("Ingrese el nombre del empleado que desea buscar: ")
        encontrado = False
        for x in empleos.readlines(): 
            
            if busqueda in x:
                encontrado = True
                break 
        if encontrado:
             print(f'El empleado {busqueda} se encuentra en la lista')
        else:
            print("El empleado no se encuentra en la lista")
              

print("Gracias por visitar el programa")