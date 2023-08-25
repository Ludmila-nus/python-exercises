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
fechas_asistencias = []
cantidad_asistencias = []
numero_de_alumno = 1

#-- cargar a los alumnos de la clase
print('Cargue los alumnos de su clase')
# ciclo while para que me corte el bucle cuando ya esten cargados todos los alumnos
cargar_alumnos = ''
while cargar_alumnos != 'no':
    nombre_alumno = input('ingrese el nombre del alumno: ')
    # si el nombre ya se encuentra registrado, da un aviso y pregusta si quiere cargar mas alumnos, sino cierra el bucle.
    if nombre_alumno in asistencias:
        print(f'El alumno {nombre_alumno} ya se encuentra registrado')
        cargar_alumnos = input('¿Quiere cargar otro alumno? si/no: ')
    else:    
        # si el alumno no esta registrado, se registra en un diccionario numero 'x' con la clave 'nombre' y el valor 'nombre del alumno'
        asistencias[numero_de_alumno] = {'nombre':nombre_alumno}
        numero_de_alumno += 1
        # tambien se pregunta si quiere seguir cargando alumnos o no.
        cargar_alumnos = input('¿Quiere cargar otro alumno? si/no: ')
print(asistencias)    

#-- registramos los datos de asistencia de los alumnos
nueva_fecha = ''
while nueva_fecha != 'no':
    # pedimos que ingrese la fecha del dia de asistencia que se quiere registrar
    print('Ingrese la fecha de asistencia que quiere registrar. 00/00/00')
    fecha_asistencia = input('Fecha: ')
    # mostramos alumno por alumno pidiendo que registre si asistio o no a clases ese dia
    print(f'Registre la asistencia en la fecha {fecha_asistencia} de los siguientes alumnos: ')
    # bucle para recorrer todos los alumnos y cargar la asistencia
    for numero, alumno in asistencias.items():
        print(alumno['nombre'])
        asistio = input('¿Asistio? si/no: ')
        # si asistio cargamos el presente
        if asistio == 'si':
            asistencias[numero][fecha_asistencia] = 'presente'
        # si no asistio le cargamos un ausente    
        else:
            asistencias[numero][fecha_asistencia] = 'ausente'
    # preguntamos si hay una nueva fecha de asistencia para continuar en el bucle 
    nueva_fecha = input('¿Quiere registrar una nueva fecha de sistencia? si/no:  ')

    for numero, alumno in asistencias.items():
        if 'presente' in asistencias[numero]:
            

print(asistencias)
