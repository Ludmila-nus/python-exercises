'''LISTA DE TAREAS 
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes. 
Implementa métodos para agregar una tarea, marcar una tarea como 
completada y mostrar todas las tareas'''
# importamos modulos
from termcolor import colored

# creamos la clase lista de tareas 
class ListaTareas:
    def __init__(self, tareas):
        self.tareas = tareas

    def details(self):
        print('¡Bienvenido a la agenda de tareas pendientes!')
        continuar = True
        while continuar:
            accion = input('¿Que accion necesita realizar? \n 1: agregar una tarea \n 2: marcar tarea como completada \n 3: mostrar todas las tareas \
                  \n 4: salir \n Ingrese el numero de la accion seleccionada: ')    
            print('---------------------------------------')
            
            # ingresa aqui si necesita agregar una tarea a la lista de tareas pendiente original
            if accion == '1':
                # pedimos que ingrese por pantalla la tarea que desea agregar a la lista
                tarea_agregada = input('Ingrese una tarea: ')
                # agregamos al listado la tarea ingresada
                self.tareas.append(tarea_agregada)
                # mostramos por pantalla la tarea que se ha ingresado a la lista de pendientes
                print(colored(f'La siguiente tarea se ha agregado con exito: \n {tarea_agregada} ', 'green'))
                print('---------------------------------------')    
    
            # ingresa aqui si necesita marcar una tarea como completada
            if accion == '2':
                # inmprimimos el listado de tareas enumeradas
                print('Listado de tareas') 
                # iniciamos el contador para que ubique las tareas enumeradamente
                contador = 1
                for tarea in self.tareas:
                    print(f'{contador}: {tarea}')
                    contador += 1
                # pedimos que seleccione el numero de la tarea completada
                tarea_completada = int(input('Indique el numero de la tarea que desea marcar como completada: '))  
                ubicacion = tarea_completada - 1 
                # mostramos por pantalla la tarea eliminada
                print(colored(f'La siguiente tarea se ha eliminado con exito: \n {self.tareas[ubicacion]}','red'))
                # eliminamos la tarea completada de la lista segun su ubiacion en la misma
                del self.tareas[ubicacion]
                print('---------------------------------------')

            # aqui ingresa si quiere ver el listado de tareas pendientes
            if accion == '3':
                # imporimimos por pantalla la lista de pendientes
                print('Listado de tareas pendientes')
                contador = 1
                for tarea in self.tareas:
                    print(f'{contador}: {tarea}')
                    contador += 1
                print('---------------------------------------')

            # aqui ingresa si quiere salir de la agenda
            if accion == '4':
                print('¡Usted esta saliendo de la agenda de tareas!')
                continuar = False
    
listado_pendientes = ['comprar verduras', 'llamar al abuelo por el cumple', 'sacar turno pediatra', 'comprar frutas', 'comprar regalo cumple']        
listado_de_tareas = ListaTareas(listado_pendientes)
listado_de_tareas.details()