import random
import time
from termcolor import colored

'''Escribe un programa en Python para encontrar los elementos duplicados de una lista, 
añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los 
elementos únicos '''

#---- armar una lista (lista 1)
lista_1 =['soja','maiz','trigo','soja','alfalfa','avena']
print('Los cultivos de la lista son:', lista_1)

#--- creamos un programa que encuentre los elementos duplicados 
lista_2=[]
for repetido in lista_1:
   if repetido not in lista_2: 
       lista_2.append(repetido)
for repetido in lista_2:
   if repetido in lista_2:
      lista_1.remove(repetido)  # borrar los elementos duplicados de la lista 1

print('Los cultivos repetidos en la lista son:', lista_1) # imprimir la lista 1 correjida
print('La nueva lista conformada con los cultivos repetidos es:', lista_2) # armar una nueva lista (lista 2)


'''Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.'''

#--- crear dos listas
lista_a = ['soja','maiz','trigo']
lista_b = ['lenteja','alfalfa','avena']

#--- unir las dos listas de manera ascendente
lista_c = []
for elemento in lista_a:
   lista_c.append(elemento)
for elemento in lista_b:
   lista_c.append(elemento)
lista_c.sort()
print(lista_c)

'''Escribe un script que encuentre el segundo número más grande de una lista'''
#--- creamos una lista de numeros
lista_numeros = [52,89,78,102,120,15,41,36,82,79]

#--- buscamos el segundo numero mas alto
lista_numeros.sort()
print('El segundo numero mas alto es:', lista_numeros[-2])

'''Crea un script que cuente el número de elementos más grandes que un determinado número 
dado por el usuario (supón una lista numérica)'''

#--- creamos una lista numerica
lista_numeros_b = [52,89,78,102,120,15,41,36,82,79]

#--- pedimos al usuario que introduzca un  numero
numero_usuario = int(input('Introduzca un numero: '))
numeros_mayores = []
#--- indicamos cuantos numeros hay en la lista mas grandes que el numero del usuario
for num in lista_numeros_b:
   if num > numero_usuario:
      numeros_mayores.append(num)
print(f'Los numero mayores al {numero_usuario} son {numeros_mayores}')

'''Crea un script dado un número introducido por el usuario o determinado al inicio del 
programa, realice la suma de aquellos números que sean divisibles por este.'''

#--- el programa da un numero al azar
lista_de_numeros = list(range(1,100+1))
numero_ordenador = random.choice(lista_de_numeros)
print(f'El numero elegido es: {numero_ordenador}')

#--- determinamos que numeros son divisibles por este numero
numeros_divisibles = [num for num in lista_de_numeros if numero_ordenador % num ==0]
print(f'Los numeros divisibles por el numero {numero_ordenador} son {numeros_divisibles}')

#--- sumamos los numeros que sean divisibles
total = sum(numeros_divisibles)
print(f'El total de los numero divisibles es: {total}')

'''Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto 
que es inferior al número introducido o determinado al inicio del programa'''

#--- pedir numero al usuario
lista_3 = [4,7,2,4,1,67,45,23,45,21,89,100]
numero_usuario_b =int(input('Introduzca un numero del 1 al 100: '))
lista_max = []
for i in lista_3:
   if i < numero_usuario_b:
      lista_max.append(i)
print(colored(f'El número más alto por debajo de {numero_usuario_b} es {max(lista_max)}','red'))    

'''Crea un script que extraiga los elementos comunes entre dos listas. '''
#--- creamos 2 listas
lista_primera =['soja','maiz','trigo','soja','alfalfa','avena']
lista_segunda =['maiz','trigo','centeno', 'cebada']
#--- extraemos los elementos comunes
lista_comunes = []
for i in lista_primera:
    for j in lista_segunda:
        if i == j:
          lista_comunes.append(i)
print(colored(f'Primera lista formada por: {lista_primera}','yellow'))  
print(colored(f'Segunda lista formada por: {lista_primera}','green'))     
print(colored(f'los elementos comunes entre las dos listas son{lista_comunes}','magenta'))

'''Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista 
(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2) '''
#--- creamos una lista con numeros repetidos
lista_repetidos =[20,85,98,20,54,69,20,71,52]
#--- elegimos uno y buscamos cuantas veces se repite(vamos a tomar el 20)
contador = 0

'''Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo 
números positivos de la lista original. '''
#--- creamos una lista de numeros positivos y negativos
lista_completa = [-10,30,-5,82,90]
print(lista_completa)
nueva_lista_f = []
#--- extraemos de la lista solo los numeros positivos en una nueva lista
for num in lista_completa:
   if num > 0:
      nueva_lista_f.append(num)
print(nueva_lista_f)

nueva_lista_f = [num for num in lista_completa if num > 0]
print(colored(f'La lista con numeros solo positivos es: {nueva_lista_f}','magenta'))

'''Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño 
de los strings de la lista original.''' 
#--- creamos una lista con str
#tomamos la lista_2
#--- creamos una lista nueva del tamaño de los str de la anterior lista
lista_3 =[]
for i in lista_2:
   longitud = len(i)
   lista_3.append(longitud)
total = sum(lista_3)
lista_3 = list(range(0,total+1))   
print(colored(lista_3,'yellow'))

'''Crea un programa que dada una lista de strings, devuelva otra lista con los strings en mayúscula. '''
#--- tomamos una lista usada anteriormente
#lista 2

#devolvemos la lista en mayuscula
lista_2_mayuscula = []
for i in lista_2:
   i = i.upper()
   lista_2_mayuscula.append(i)
print(colored(lista_2_mayuscula, 'green'))


