'''DATOS CINEMATOGRÁFICOS 
Supongamos que tienes un conjunto de datos de películas que contiene información 
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar 
estos datos para determinar cuál es el género de película más popular, cuántas películas 
se lanzaron en cada década y cuál es la duración promedio de cada género de película. 
(Pista 2: puede ser util investigar np.unique, np.argsort y np.count_nonzero) 
'''

import numpy as np

# creamos el array con los datos cinematograficos
#titulo - genero - duracion - año lanzamiento - calificacion
peliculas = np.array([
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
])

#  definimos el tamaño del array para usarlo luego en los bucles 
tamaño_array = len(peliculas)

#-- determinamos cual es el genero de pelicula mas populas
# determinamos cuantos generos hay y que cantidad de veces se repiten
for genero in range(tamaño_array):
    generos, conteos = np.unique(peliculas[:,1],return_counts=True)
print(generos)    

# determinamos cual es el genero mas popular   
ordenamiento = np.argsort(conteos)[::-1]
print('El genero mas popular es: ' , generos[ordenamiento[0]])

#  determinamos cuantas peliculas se lanzaron en cada decada
# extraer el año de realizacion de cada pelicula en un nuevo array 
año = np.array([int(registro[3]) for registro in peliculas])
print(año)
decada_2000 = np.zeros(tamaño_array)

# contamos la cantidad de peliculas por decada
for años in range(tamaño_array):
    decada_2000 = np.count_nonzero(año>=2000)
    decada_90 = np.count_nonzero(año<2000)

# imprimimos por pantalla la cantidad de peliculas por decada
print(f'En la decada del 90 se realizaron {decada_90} peliculas y en la decada del 2000 {decada_2000} peliculas')    
# imprimimos por pantalla la decada con mas peliculas    
if decada_2000 > decada_90:
    print('La decada con mayor cantidad de peliculas es la DECADA DEL 2000')  
else:
    print('La decada con mayor cantidad de peliculas es la DECADA DEL 90')   

#  determinamos cual es la duracion promedio de cada genero de pelicula
# extraemos los generos en un array 
generos_lista = np.array([(registro[1]) for registro in peliculas])

# creamos un array para cada 
duracion_accion = np.zeros(1)
duracion_comedia = np.zeros(1)
duracion_drama  = np.zeros(1)

# determinamos la duracion media por genero 
for genero_peli in generos: # traemos los 3 generos extraidos 
     # recorremos el array generos_lista 
     duracion_genero = peliculas[generos_lista == genero_peli]
     if genero_peli == 'Acción':
         duracion_accion = np.mean(duracion_genero[:,2].astype(int))
     if genero_peli == 'Comedia':
         duracion_comedia = np.mean(duracion_genero[:,2].astype(int))
         print(duracion_comedia)
     if genero_peli == 'Drama':
         duracion_drama = np.mean(duracion_genero[:,2].astype(int))

# imprimimos por pantalla los resultados
print(f'La duracion promedio de cada genero es \n Accion: {duracion_accion:.2f} \
     \n Comedia {duracion_comedia:.2f} \n Drama {duracion_drama:.2f}')
