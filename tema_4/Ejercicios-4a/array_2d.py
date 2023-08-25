'''
9.  Crea un arrays lleno de 1s con una longitud dada por el usuario 
10. Cambia la forma del array para que tenga una estructura de tipo (filas, columnas) 
11. Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas) 
12. Concatena ambas estructuras horizontalmente y verticalmente  
      (Pista: Investiga el funcionamiento de concatenate() y de vstack() y hstack() de numpy) '''
import numpy as np
from termcolor import colored

# 9.  Crea un arrays lleno de 1s con una longitud dada por el usuario 
#  pedimos la longitud al usuario
long_usuario = int(input('introduzca la longitud del array:  '))
#  creamos el array con la longitu pedida por pantalla
array_usuario = np.ones(long_usuario, dtype=np.float64)
print(array_usuario)

# 10. Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)
#  cambiamos la estructura de array unidimensional a bidimensionnal ( 2 x 5)
array_usuario = array_usuario.reshape(2,5)
print(array_usuario)

# 11. Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas) 
# creamos una matriz con la funcion copy
matriz_identidad = array_usuario.copy()

print(colored(array_usuario,'magenta'))
print(colored(matriz_identidad,'blue'))

# 12. Concatena ambas estructuras horizontalmente y verticalmente 
# concatenamos los dos arrays
concat_horiz = np.concatenate((array_usuario,matriz_identidad))
concat_horiz_2 = np.vstack((array_usuario,matriz_identidad))
concat_vert = np.hstack((array_usuario,matriz_identidad))
print(concat_horiz)
print(colored(concat_horiz_2,'yellow'))
print(colored(concat_vert, 'green'))