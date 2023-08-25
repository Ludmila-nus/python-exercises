#--- Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: [1,2,3,4,5,6,7,8,9,10].
numeros = list(range(1,11))
print(numeros)

#--- Crea una nueva lista con los números pares de la lista anterior en orden inverso
numeros_inversos = numeros[:]
numeros_inversos.reverse()
numeros_pares_inversos = []
#print(numeros_inversos)
for num in numeros_inversos:
    if num % 2 == 0:
        numeros_pares_inversos.append(num)
print(numeros_pares_inversos)

#--- Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por consola. 
for i in numeros:
    numeros_cuadrados = i ** 2
    print(f'El cuadrado del numero {i} es {numeros_cuadrados}')

#---Intenta rehacer los pasos 2 y 3  con el menor número de lineas posible (método de compresión).
#Crea una nueva lista con los números pares de la lista anterior en orden inverso
numeros_inversos = numeros[:]
numeros_inversos.reverse()
numeros_pares_inversos = [num for num in numeros_inversos if num % 2 == 0]
print('Los numeros pares inversos son: ', numeros_pares_inversos)
#print(numeros_inversos)

#--- Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por consola. 
numeros_cuadrados = [i ** 2 for i in numeros]
print(numeros_cuadrados)

#---Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla 
print(min(numeros))

#---Haz lo mismo con el número más alto 
print(max(numeros))

#---Suma todos los elementos de la lista con y sin un bucle. 
print(sum(numeros)) 

suma_total = 0
for i in numeros:
    suma_total = i + suma_total
print(suma_total)

#---Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras el punto 2.     
print(numeros[8], numeros_inversos[8])