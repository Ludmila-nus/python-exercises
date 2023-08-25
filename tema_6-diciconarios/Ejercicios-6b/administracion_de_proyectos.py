'''Eres un gerente de proyectos y necesitas un programa para administrar 
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre, 
una descripción y un responsable asignado. Implementa un programa en 
Python que utilice un diccionario para almacenar la información de las 
tareas. El programa debe permitir agregar nuevas tareas, asignar 
responsables a las tareas existentes, actualizar las descripciones de las 
tareas y mostrar la lista completa de tareas y responsables.  
(Pista: puedes comenzar con un diccionario vacío y construir un 
diccionario de diccionarios)'''

from termcolor import colored
#--- comenzamos con un diccionario vacio
proyecto = {}

#--- vamos a llenar el dicionario vacio con los datos TAREA:.... / DESCRIPCION:..../RESPONSABLE:....
# implementamos un ciclo while para dar opcion de seguir cargando tareas o salir del sistema
finalizar = ''
while finalizar != 'no':
    # preguntamos de que tarea quiere cargar datos
    print('ingrese el nombre de la tarea')
    tarea = input('Tarea: ')
    # si la tarea ya esta cargada seguimos por aca
    if tarea in proyecto:
        # preguntamos si quiere actualizar la descripcion de la tarea
        respuesta1 = input('La tarea ya se encuentra registrada, ¿quiere actualizar la descripcion? si/no: ')
        if respuesta1 == 'si':
            dato1 = input(f'Agregue una nueva descripcion de la tarea {tarea}: ')
            # actualizamos la descripcion en el diccionario 'proyecto'
            proyecto[tarea] = {'descripcion':dato1}
        # preguntamos si quiere actualizar el responsable de la tarea    
            respuesta2 = input('¿quiere actualizar el responsable asignado? si/no: ')    
            if respuesta2 == 'si':
                dato2 = input(f'Agregue una nuevo responsable a la tarea {tarea}: ')
                # actualizamos el responsable en el diccionario 'proyecto'
                proyecto[tarea] = {'responsable':dato2}
            else:
                finalizar = input('¿Quiere añadir/consultar una nueva tarea? si / no: ') 
        else:
                finalizar = input('¿Quiere añadir/consultar una nueva tarea? si / no: ')        
    # si la tarea no esta cargada damos la opcion de crear una nueva tarea
    else:
        respuesta3 = input('La tarea no se encuentra registrada, ¿quiere ingresar una nueva tarea? si/no: ')
        if respuesta3 == 'si':
            # pedimos que le de nombre a la nueva tarea
            dato3 = input('Agregue un nombre a la nueva tarea: ')
            # pedimos que de una descripcion de la nueva tarea
            dato4 = input(f'Agregue una descripcion de la tarea {dato3}: ')
            # pedimos que asigne un responsable a la nueva tarea
            dato5 = input(f'Agregue un responsable de la tarea {dato3}: ')
            # cargamos los datos en el diccionario dato3(nueva tarea cargada) que se encuentra del diciconario proyecto
            proyecto[dato3] = {'descripcion':dato4,'responsable':dato5}
            print(proyecto)
            finalizar = input('¿Quiere añadir/consultar una nueva tarea? si / no: ')
        else:
            finalizar = input('¿Quiere añadir/consultar una nueva tarea? si / no: ')     

#--- mostramos por pantalla la lista completa de tareas y responsable 
# usamos un bucle for para listar una debajo de la otra
for tarea, info_tareas in proyecto.items():
    descripcion = info_tareas['descripcion']
    responsable = info_tareas['responsable']
    print(f'\nLas tareas registradas son: {tarea}')
    print(f'\nDescripcion: {descripcion}')
    print(f'\tResponsable asignado: {responsable}')


