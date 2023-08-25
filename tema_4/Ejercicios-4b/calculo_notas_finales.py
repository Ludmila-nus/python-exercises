'''CALCULO DE NOTAS FINALES 
Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un 
curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una 
participación en clase. Quieres calcular la nota final de cada estudiante, donde los 
exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase 
vale un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas, 
donde n es el número de estudiantes. Cada columna representa una de las calificaciones 
y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para 
calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola 
columna.'''
import numpy as np
from termcolor import colored


#  damos la bienvenida al sistema de notas
print(colored('--- Bienvenido al sistema de notas ---', 'yellow'))

#  preguntamos cuantos alumnos hay en el curso
alumnos = int(input('Ingrese la cantidad de alumnos que hay en el curso:  '))

#  creamos una lista vacia para cargar los alumnos
lista_alumnos = []

#  pedimos que se carguen los  nombres de los alumnos con un cilo while para que siga dando la opcion hasta que
#  se complete la cantidad de alumnos ingresada por el usuario
while len(lista_alumnos) < alumnos:
    nombre = input('Ingrese el nombre y apellido del alumno: ')
    lista_alumnos.append(nombre)

#  creamos un array de 4 columnas y tantas filas como alumnos haya en la clase
notas_alumnos = np.zeros((alumnos,4), dtype= np.float64)

#  pedimos al usuario que cargue las notas de los alumnos
print('---Ingrese las notas de cada alumno en las siguientes evaluaciones---')

#  vamos a remplazar cada notas ingresadas por el usuario, por los 0 en el array 
for i in range(len(lista_alumnos)):
    print(f'alumno: {lista_alumnos[i]}')
    examen_1 = float(input('Nota del primer examen: '))
    notas_alumnos[i , 0] = examen_1
    examen_2 = float(input('Nota del segundo examen: '))
    notas_alumnos[i , 1] = examen_2
    trabajo_final = float(input('Nota del trabajo final: '))
    notas_alumnos[i , 2] = trabajo_final
    partic_en_clase = float(input('Nota participacion en clase: '))
    notas_alumnos[i , 3] = partic_en_clase

print(notas_alumnos)
# calculamos la nota final y la almacenamos en un nuevo array de una sola columna

notas_finales = []
for i in range(len(lista_alumnos)):
        nota_porcentaje = []
        #examen 1 30%
        nota_final_alumno = np.multiply(notas_alumnos[i , 0], 0.30)
        nota_porcentaje.append(nota_final_alumno)
        #examen 2 30%
        nota_final_alumno = np.multiply(notas_alumnos[i , 1], 0.30)
        nota_porcentaje.append(nota_final_alumno)
        
        #trabajo final 30%
        nota_final_alumno = np.multiply(notas_alumnos[i , 2], 0.30)
        nota_porcentaje.append(nota_final_alumno)
        
        #participacion en clase 10%
        nota_final_alumno = np.multiply(notas_alumnos[i , 3], 0.10)
        nota_porcentaje.append(nota_final_alumno)

        nota_final = sum(nota_porcentaje)

        notas_finales.append(nota_final)

notas_finales_array = np.array((notas_finales), dtype= np.float64)

print(notas_finales)
print(notas_finales_array)
        #nota_porcentaje [i] = nota_final_alumno
1


