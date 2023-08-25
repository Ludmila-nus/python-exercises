'''Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas 
de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa. 
'''
import random
import time
from termcolor import colored
#--- creamos una lista
lista = ['manzana', 'plátano', 'cereza', 'pera', 'higo', 'frambuesa' , 'fresa']

#--- Usa la función len() para imprimir la longitud de la lista frutas

print(len(lista))

#--- Accede al objeto numero 3 de la lista e imprímelo por consola
print(f'{lista[2]}')

#--- Modifica el segundo objeto de la lista y cambiado a mora
lista[1] = 'mora'
print(lista)

#--- Añade el string mango al final de la lista
lista.insert(len(lista),'mango')
print(lista)

#---Usa el método insert() y añade el string “uva“ al comienzo de la lista
lista.insert(0,'uva')
print(lista)

#--- Usa un bucle para recorrer la lista e imprimir cada fruta por la consola
for frutas in lista:
    print(frutas)

#--- Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable llamada “ultima_fruta“  
ultima_fruta = lista.pop()
print(ultima_fruta)

#--- Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola
#--- Modifica el script para que imprima también la longitud de cada nombre de fruta por consola      
print('--ejerc 10---') 
for frutas in lista:
    long_de_fruta = len(frutas)
    print(f'la longuitud de {frutas} es {long_de_fruta}')
print('--ejerc 10---')    
for frutas in lista:
    print(f'la longuitud de {frutas} es {len(frutas)}')
print('')
#--- Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que tengan más de 5 caracteres
for frutas in lista:
    long_de_fruta = len(frutas)
    if long_de_fruta >= 5:
        print(colored(f'la longuitud de {frutas} es {long_de_fruta}','yellow'))

#--- Usa el método remove() para borrar el string “cereza“ de la lista
lista.remove('cereza')
print(lista)

#--- Usa el método clear() para vaciar la lista
lista.clear()
print(lista)