#--- pedir al estudiante nombre, edad y nota mediap
print('<<<bienvenido al sistema de becas de excelencia>>> \n usted debe ingresar sus datos luego \
    luego el sistema evaluara si puede recibir la beca ')
nombre_completo = input('Nombre y Apellido: ')
edad = int(input('Edad: '))
nota_media = float (input('Nota media: '))

#--- indicar si puede optar por la beca
if (edad >= 17) and (edad <= 21) and (nota_media >= 8): #edad entre 17 y 21 años #nota media 8
    print(nombre_completo, 'ha obtenido la beca, ¡felicitaciones!')
else:
    print(nombre_completo, 'no puede acceder a la beca, lo lamentamos')       


