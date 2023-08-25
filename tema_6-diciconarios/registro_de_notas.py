'''Ejercicio: Registro de Notas
Crea un programa que permita a un profesor registrar las notas de sus estudiantes y luego muestre estadísticas simples sobre las notas ingresadas. 
El programa debe permitir al usuario:

Ingresar el nombre de un estudiante y sus notas (puedes considerar varias notas, como examen, tarea, participación, etc.).
Calcular el promedio de las notas de un estudiante.
Mostrar el promedio más alto y más bajo de todas las notas ingresadas.
Mostrar la cantidad total de estudiantes registrados.'''

print('-----Bienvenido al sistema de carga de notas de estudiantes------')
def registro_de_notas():
    """ funcion que registra las notas que se cargaran luego a los estudiantess 
    (puedes considerar varias notas, como examen, tarea, participación, etc.)."""

    print('Usted debe cargar las notas que quiera evaluar de los estudiante tales como examentes, tareas, partyicipacion, etc.')

    # creamos un diccionario para almacenar las notas de los estudiantes
    registro_notas = {}

    # pedimos que ingrese las notas con un ciclo while para que pueda ingresar tantas notas como desee
    while True:  
        notas = input('Ingrese el nombre del examen/trabajo (o "salir" para finalizar): ')
        if notas.lower() == 'salir':
            break
        registro_notas[notas] = 0
    
    return registro_notas

def registro_de_estudiantes():
    """Funcion que permite Ingresar el nombre de un estudiante y sus notas"""

    print('Usted debe cargar los nombres de los estudiantes')
          
    # creamos una lista para almacenar luego a los estudiantes
    registro_estudiantes = []

    # pedimos que ingrese el nombre del estudiante
    while True:
        nombre = input('Ingrese el nombre del estudiante (o "salir" para finalizar): ')
        if nombre.lower() == 'salir':
            break
        
        # almacenamos el nombre en una lista
        registro_estudiantes.append(nombre)
   
    return registro_estudiantes

def registro_notas_estudiantes():
    """funcion que registra las notas de los estudiantess, llama a las funciones registro de notas y registro de estudiantess"""

    # llamamos a la funcion registro de notas 
    notas = registro_de_notas()

    # llama a la funcion registro estudiantes
    estudiantes = registro_de_estudiantes()

     # creamos un diccionario para almacenar toda la informacion
    informacion_estudiantes = {}
    
    for estudiante in estudiantes:
        print(f'Cargue las notas del estudiante {estudiante}')
        
        # creamos un diccionario para almacenar las notas 
        notas_estudiante = {}

        # recorremos cada nombre de la nota a cargar
        for nota in notas:
            carga_nota = float(input(f'Nota de {nota}: '))
            notas_estudiante[nota] = carga_nota

        # Agrega las notas del estudiante al diccionario informacion_estudiantes
        informacion_estudiantes[estudiante] = notas_estudiante
    

    return informacion_estudiantes

# Llamada a la función principal para registrar las notas de los estudiantes
registro = registro_notas_estudiantes()
print(registro)

'''
def calcular_promedio():
        """funcion que calcula el promedio de notas del estudiantes solicitado"""

        registro_notas = registro_estudiante ()

        
        suma_notas = [sum(valor['']) for clave, valor in registro_notas.items()]
       
        

registro_notas = registro_estudiante()        
print(registro_notas)        
'''




    
