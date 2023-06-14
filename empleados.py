empleos = open('empleados.txt','a')

while resp != 4:

    print("MENU DE OPCIONES: ")
    print("1. Agregar empleados")
    print("2. Leer lista de empleados empleados")
    print("3. Buscar empleados")
    print("4. Salir")

    num_empleados = int(input("Digite la cantidad de empleados que desea almacenar: "))

    for i in range(num_empleados):

        nombre = input(f'Ingrese el nombre del empleado {i+1}: ')
        apellido = input(f'Ahora su apellido: ')
        telefono = int(input(f'Y por ultimo su telefono: '))

        empleos.write(f'\n {nombre} { apellido} { telefono} ')



empleos.close()


