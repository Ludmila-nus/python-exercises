'''Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en 
ese caso imprima dos listas correspondientes a: 
1. La fila cuyos elementos suman el máximo 
2. La columna cuyos elementos suman el máximo 
Si no se trata de una matriz devolverá dos listas vacías.
Por ejemplo: 
M1=[[2,5,3],[6,1,8],[7,5,4]]  devolverá: L1 = [7,5,4] y L2 = [2,6,9,7] 
M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = [] 
(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo 
numero de objetos)'''
import random
import time
from termcolor import colored
import numpy as np

#--- creamos una lista numerica matriz
matriz_1=[[2,5,3],[6,1,8],[7,5,4]] 
print(colored(f'Matriz 1 formada por:{matriz_1}','red'))
#--- creamos una lista numerica comun
matriz_2 = [[4,2,3],[4,5],[6,8,2]]
print(colored(f'Matriz 2 formada por:{matriz_2}','blue'))


#--- identificamos si la lista matriz_1 es una matriz 
for i in range(0,len(matriz_1)):
    for j in range(i):
        # if len(matriz_1[i]) == len(matriz_1[i]): no me da!!!!!!!!!!!!!!!!!!!
            print('es una matriz')


suma_filas = []
suma_columnas = []
lista_1 = []
# devolvemos una lista de La fila cuyos elementos suman el máximo
for i in range(0, len(matriz_1)):
    for j in range(0, len(matriz_1)):
        suma_filas += matriz_1[i][j]
        suma_columnas += matriz_1[i][j]

   


print(colored(f'La lista cuyos elementos suman el maximo es: \n {lista_1}','yellow'))

# devolvemos una lista de La columna cuyos elementos suman el máximo 
# si no es una matriz devolvera dos listas vacias

#--- identificamos si la lista matriz_2 es una matriz 
# devolvemos una lista de La fila cuyos elementos suman el máximo
# devolvemos una lista de La columna cuyos elementos suman el máximo 
# si no es una matriz devolvera dos listas vacias
