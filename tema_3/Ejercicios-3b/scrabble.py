'''Supongamos una lista de caracteres llamada “palabras“ que representa una mano de 
Scrabble. Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el 
segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la 
ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos 
en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano'''

from termcolor import colored

#--- lista de caracteres que representa una mano de scrabble
palabra = [['P','3'],['I','1'],['T','1'],['H','4'],['O','1'],['N','1']] #1 caracter letra de una ficha, segundo caracter puntos de la ficha

print('Las fichas de su palabra son:' , palabra[0:len(palabra)-1])

#--- calculamos el valor total de los puntos de la mano de scrabble
# obtenemos los puntos de las fichas
puntos = []
letra = 0
for num in palabra: 
    punto = palabra[letra][1]
    puntos.append(punto)
    letra = letra + 1
print(f'Los puntos de las fichas son: {puntos}')

# pasamos los puntos a enteros para poder sumarlos
suma_puntos = []
for num in range(len(puntos)): 
    puntos_num = int(puntos[num])
    suma_puntos.append(puntos_num)

# sumamos todos los puntos de las fichas
print(colored(f'Los puntos de la mano suman: {sum(suma_puntos)}','magenta')) 
