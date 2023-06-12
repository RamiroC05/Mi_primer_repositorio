empleos = open('empleados.txt','a')

num_empleados = int(input("Digite la cantidad de empleados que desea almacenar: "))

for i in range(num_empleados):

    nombre = input(f'Ingrese el nombre del empleado {i+1}: ')
    apellido = input(f'Ahora su apellido: ')
    telefono = int(input(f'Y por ultimo su telefono: '))

    empleos.write(f'\n {nombre} { apellido} { telefono} ')



empleos.close()


