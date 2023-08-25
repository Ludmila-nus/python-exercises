'''LISTA DE TAREAS 
Crea una clase "ListaTareas" que contenga una lista de tareas pendientes. 
Implementa métodos para agregar una tarea, marcar una tarea como 
completada y mostrar todas las tareas'''

'''Aclaracion de Elena para corregir el ejercicio:
El ejercicio está muy bien! Te recomiendo tan solo un par de cosillas: Intenta que cada método se encargue solo de una tarea. 
Por ejemplo, puedes separar la funcionalidad de agregar una tarea, la de marcarla como completada y la de mostrarlas, en distintos métodos. 
Eso ayuda a que el código sea de primeras más legible y modular. También suele ser conveniente simplificar el método init. En vez de pasarle una 
lista de tareas puedes empezar con la lista vacía e ir añadiendo elementos. 
Ah y si quieres llevar el programa al siguiente nivel puedes intentar aplicar el manejo de excepciones también'''
# importamos modulos
from termcolor import colored


print('¡Bienvenido a la agenda de tareas pendientes!')

# creamos la clase lista de tareas 
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea_agregada):
        # agregamos al listado la tarea ingresada
        self.tareas.append(tarea_agregada)
        # mostramos por pantalla la tarea que se ha ingresado a la lista de pendientes
        print(colored(f'La siguiente tarea se ha agregado con exito: \n {tarea_agregada} ', 'green'))
        print('---------------------------------------')    
    
    def tarea_completada(self, tarea_completada):
        ubicacion = tarea_completada - 1 
        # mostramos por pantalla la tarea eliminada
        print(colored(f'La siguiente tarea se ha eliminado con exito: \n {self.tareas[ubicacion]}','red'))
        # eliminamos la tarea completada de la lista segun su ubiacion en la misma
        del self.tareas[ubicacion]
        print('---------------------------------------')

    def listado_pendientes(self):        
        # imporimimos por pantalla la lista de pendientes
        print('Listado de tareas pendientes')
        contador = 1
        for tarea in self.tareas:
            print(f'{contador}: {tarea}')
            contador += 1
        print('---------------------------------------')

    def salir(self):    
        print('¡Usted esta saliendo de la agenda de tareas!')
        


def inicio():
     """Funcion que da inicion a la agenda de pendientes y da las opciones para seleccionar"""

     continuar = True
     while continuar:
         accion = input('¿Que accion necesita realizar? \n 1: agregar una tarea \n 2: marcar tarea como completada \n 3: mostrar todas las tareas \
               \n 4: salir \n Ingrese el numero de la accion seleccionada: ')    
         print('---------------------------------------')

         # iniciamos la clase
         listado_pendientes = []        
         listado_de_tareas = ListaTareas(listado_pendientes)

         # ingresa aqui si necesita agregar una tarea a la lista de tareas pendiente original
         if accion == '1':
            # pedimos que ingrese por pantalla la tarea que desea agregar a la lista
            tarea_agregada = input('Ingrese una tarea: ')
            listado_de_tareas.agregar_tarea(tarea_agregada)

         # ingresa aqui si necesita marcar una tarea como completad
         if accion == '2':
            listado = listado_de_tareas.listado_pendientes()
            # inmprimimos el listado de tareas enumeradas
            print('Listado de tareas') 
            # iniciamos el contador para que ubique las tareas enumeradamente
            contador = 1
            for tarea in listado:
                print(f'{contador}: {tarea}')
                contador += 1
            # pedimos que seleccione el numero de la tarea completada
            tarea_completada = int(input('Indique el numero de la tarea que desea marcar como completada: '))
            # pasamos el dato de la tarea compleatda a la funcion para que la elimine de la lista
            listado_de_tareas.tarea_completada(tarea_completada)

         # aqui ingresa si quiere ver el listado de tareas pendientes
         if accion == '3':
            # llamamos a la funcion de listado de pendientes
            listado_de_tareas.listado_pendientes()

         # aqui ingresa si quiere salir de la agenda
         if accion == '4':    
              listado_de_tareas.salir()
              continuar = False

