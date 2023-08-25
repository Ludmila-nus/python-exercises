'''Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los 
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y 
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos. 
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al 
completo'''

from termcolor import colored

#--- lista de alumnos
alumnos = [['Pedro Gonzalez'],['Lorenzo Martinez'],['Laura Gomez'],['Sofia Alvarez']]
cantidad_de_alumnos = len(alumnos)

#--- le agregamos las notas a cada alumno (lista anidada)
# nota de ingles / clases / proyecto
for alumno in range(0,len(alumnos)):
    nota = float(input(f'Alumno {alumnos[alumno]} Ingrese nota de Ingles: '))
    alumnos[alumno].append(nota)
    nota = float(input(f'Alumno {alumnos[alumno]} Ingrese nota de Clases: '))
    alumnos[alumno].append(nota)
    nota = float(input(f'Alumno {alumnos[alumno]} Ingrese nota de Proyecto: '))
    alumnos[alumno].append(nota)

    # calculamos la nota media de cada estudiante  
    promedio_individual = ((sum(alumnos[alumno][1:])/3)) # dividimos por 3 porque son 3 materias

    # promedio individual impreso en azul (6>=) o rojo (<6)
    if promedio_individual >= 6:
        print(colored(f'La nota media del alumno {alumnos[alumno][0]} es: {promedio_individual}','blue')) 
    else:
        print(colored(f'La nota media del alumno {alumnos[alumno][0]} es: {promedio_individual}','red'))
    
# calculamos el promedio de la clase
suma_notas_alumnos = []    
for alumno in range(0,len(alumnos)):  
    notas_alumnos = ((sum(alumnos[alumno][1:])/3))
    suma_notas_alumnos.append(notas_alumnos)
promedio_clase = sum(suma_notas_alumnos) / cantidad_de_alumnos

# imprimimos todos los datos por pantalla (el resumen)
# Lista de alumnos y sus notas   
print(colored(f'Lista de alumnos y notas:\n{alumnos}','green'))   
#promedio general de la clase
print(colored(f'La nota promedio general de la clase es {promedio_clase}','green'))
