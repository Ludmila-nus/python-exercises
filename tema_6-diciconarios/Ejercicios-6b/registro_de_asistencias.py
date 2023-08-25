'''REGISTRO DE ASISTENCIAS: 
Eres un profesor y deseas realizar un seguimiento de la asistencia de tus 
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y 
una lista de fechas en las que asistió a clases. Implementa un programa 
en Python que utilice un diccionario para almacenar la información de las 
asistencias. El programa debe permitir registrar la asistencia de los 
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de 
estudiantes y las fechas en las que asistieron. 
(Pista: puedes comenzar con un diccionario vacío y construir un 
diccionario de listas)'''

#-- comenzamos con un diccionario vacio
asistencias = {}

#-- creamos una lista de los alumnos
lista_de_alumnos = ['juan','lucas','sofia','maria','pedro']
longitd_lista = len(lista_de_alumnos)
print(longitd_lista)
presentes = []

#-- registramos los datos de asistencia de los alumnos
nueva_fecha = ''
while nueva_fecha != 'no':
    # pedimos que ingrese la fecha del dia de asistencia que se quiere registrar
    print('Ingrese la fecha de asistencia que quiere registrar. 00/00/00')
    fecha_asistencia = input('Fecha: ')
    # mostramos alumno por alumno pidiendo que registre si asistio o no a clases ese dia
    print(f'Registre la asistencia en la fecha {fecha_asistencia} de los siguientes alumnos: ')
    # bucle para recorrer todos los alumnos y cargar la asistencia
    for i in range(0,longitd_lista):
        print(lista_de_alumnos[i])
        asistio = input('¿Asistio? si/no: ')
        # si asistio cargamos la asistencia y sumamos la misma para contar al final a cuantas clases asistio el alumno.
        if asistio == 'si':
            presentes.append(1)       
            asistencias[lista_de_alumnos[i]] = {'fechas de asistencia':fecha_asistencia,'cantidad de presentes': presentes}
            
    # preguntamos si hay una nueva fecha de asistencia para continuar en el bucle 
    nueva_fecha = input('¿Quiere registrar una nueva fecha de sistencia? si/no:  ')

#-- mostramos la lista de estudiantes y las fechas en que asistieron
print('Listado de asistencias:')
for alumno, asistencia in asistencias.items():
    print(f'Detalle de asistencias del alumno {alumno}')
    print(f'\nFechas de asistencias', asistencia['fechas de asistencia'] )
    print(f'\nCantidad total de clases asistidas:', asistencia['cantidad de presentes'])
print(asistencias)






