'''ARRAYS 1D PARTE 2:
1. Crea un array con 15 números enteros aleatorios entre 1 y 100
2. Multiplica todos los elementos del array usando un bucle y después usando un
método de numpy. Compara los resultados
3. Crea otro array con 10 números decimales aleatorios entre 0 y 1
4. Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un
operador y después con una función de numpy
 (Pista: busca en google que función de numpy hace esto)
5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
(Pista: busca en google que función de numpy hace esto)
6. Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y
después con una función de numpy
 (Pista: busca en google que función de numpy hace esto)
7. Encuentra el valor más alto del primer array que has creado.
8. Calcula la media (mean), la mediana (median) y al deviación estandar (standard
deviation) de los arrays (Nota: No nos importa el significado matemático de estos
valores, lo importante es que encuentres que función de numpy necesitas. Puedes
hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele
haber más resultados).'''

import numpy as np
from termcolor import colored
    
#1
array_1 = np.random.randint(1,101, size=15)
print(array_1)

#2
multip_bucle = 1
for num in array_1:
   multip_bucle = multip_bucle * num
   
multipl_numpy = np.prod(array_1)
print(multip_bucle,multipl_numpy)

#3
array_2 = np.random.random(1,11, size=10)
print(array_2)

#4
size_min = min(len(array_1),len(array_2))
#print(size_min)
array_suma_1 = array_1[:size_min]+ array_2 [:size_min]
array_suma_2 = np.add(array_1[:size_min] , array_2 [:size_min])

print(colored(array_suma_1,'magenta'))
print(colored(array_suma_2,'blue'))

#5
array_resta_1 = array_1[:size_min] - array_2 [:size_min]
array_resta_2 = np.subtract(array_1[:size_min] , array_2 [:size_min])

print(colored(array_resta_1,'magenta'))
print(colored(array_resta_2,'blue'))

#6
array_multiply_1 = array_1[:size_min] * array_2 [:size_min]
array_multiply_2 = np.multiply(array_1[:size_min] , array_2 [:size_min])

print(colored(array_multiply_1,'magenta'))
print(colored(array_multiply_2,'blue'))

#7
valor_mas_alto = array_1.max()
print(valor_mas_alto)
valor_mas_alto2 = np.max(array_1)
print('valos mas alto ' +
       valor_mas_alto2)

#8
media_array_1 = array_1.mean()
media_array_2 = array_2.mean()
print(media_array_1, media_array_2)

ds_array_1 = np.std(array_1, dtype=np.float64)
ds_array_2 = np.std(array_2, dtype=np.float64)
ds = np.std(array_1, dtype=np.float64)
print(f'{ds_array_1:.2f},{ds_array_2:.2f}')

mediana_array_1 = np.median(array_1)
mediana_array_2 = np.median(array_2)
print(colored(f'{mediana_array_1:.2f}, {mediana_array_2:.2f}','yellow'))






















