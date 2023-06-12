variable2 = open('archivo.txt','a')

nombre = input('Ingrese el nombre de una persona: ')
variable2.write(f'\n {nombre}')




variable2.close()
