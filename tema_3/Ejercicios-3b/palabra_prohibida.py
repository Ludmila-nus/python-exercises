'''Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras. 
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga 
aquellas palabras que no tienen ninguna palababra prohibida'''

from termcolor import colored

#--- definimos una lista de 5 palabras
lista_palabras = ['queso','humus','tomate', 'pan', 'lechuga', 'huevo']
print(colored(lista_palabras, 'blue'))
lista_palabras_nueva = []
#--- definimos una lista de letras prohibidas
letras_prohibidas = ['q', 'h','p']
#--- bucle recorre la lista de palabras y eliminamos las que contengan alguna palababra prohibida
for palabra in lista_palabras: 
    if  letras_prohibidas[0] not in palabra and letras_prohibidas[1] not in palabra \
        and letras_prohibidas[2] not in palabra:
            lista_palabras_nueva.append(palabra) # lista con palabras filtradas
print(colored(lista_palabras_nueva, 'yellow')) 

#la forma en que lo resolvio Elena es la siguiente

#--- definimos una lista de 5 palabras, una lista de letras prohibidas y una lista para almacenar las palabras admitidas
lista_palabras = ['queso','humus','tomate', 'pan', 'lechuga', 'huevo']
letras_prohibidas = ['q', 'h','p']
lista_palabras_nueva = []

#--- bucle recorre la lista de palabras para eliminar las que contengan alguna letra prohibida
for palabra in lista_palabras: 
    incluir = True
    for letra_prohibida in letras_prohibidas:
        if letra_prohibida in palabra:        
            incluir = False
    if incluir:
        lista_palabras_nueva.append(palabra) # lista con palabras filtradas

print(colored(lista_palabras, 'blue'))  
print(colored(letras_prohibidas, 'blue'))          
print(colored(lista_palabras_nueva, 'yellow')) 