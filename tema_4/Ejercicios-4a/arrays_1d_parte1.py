'''
1. Crea un array_1 lleno ceros con una longitud de 8 elementos.  
2. Haz que todos los elementos de este array sean igual a 2  
3. Crea un array_2 que contenga todos los números pares del 1 al 10. 
4. Suma todos los elementos del array_2 usando un bucle y después usando un método 
de numpy. Compara los resultados 
5. Revierte array_2 y guárdalo en una variable independiente.  
6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y 
array_2_revertido  
     (Pista: Investiga el uso de intersect1d() de numpy) 
7. Crea un arrays lleno de 1s con una longitud dada por el usuario'''

import numpy as np
from termcolor import colored
array_1 = np.zeros((8))
print(array_1)

array_1 [:] = 2
print(array_1)

array_2 = np.arange(2,11,2)
print(colored(array_2,'magenta'))

suma_bucle = 0
for i in array_2:
    suma_bucle = suma_bucle + i
print(suma_bucle)    

suma_array = np.sum(array_2)
print(suma_array)

if suma_bucle == suma_array:
    print('Los resultados son iguales')
else:
    print('Los resultados son distintos')


array_revertido =  np.zeros(len(array_2), dtype=int)
array_revertido [:] = array_2[::-1]
array_revertido[:] = 2
print(colored(array_revertido,'yellow'))
print(colored(array_2,'blue'))

elementos_comunes = np.intersect1d(array_1,array_2)
print(elementos_comunes)

elementos_comunes = np.intersect1d(array_revertido,array_2)
print(elementos_comunes)

long_array = int(input('Ingrese la longitud del array: '))
array_usuario = np.ones(long_array)
print(array_usuario)