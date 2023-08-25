'''Genera una listade todos los números pares entre 0 y 50'''

numeros_pares = [numero for numero in range(0,51) if numero % 2 == 0]
print(numeros_pares)


'''Comprensión de lista para crear una lista llamada cuadrados_pares 
cuadrados_pares incluye los cuadrados de los números del 1 al 10 que sean divisibles por 2, inclusive'''

cuadrados_pares = [(num**2) for num in range (0,11) if (num**2) % 2 == 0]
print(cuadrados_pares)


'''Comprensión de lista para crear una lista, cubos_por_cuatro, 
que consiste en los cubos de los números del 1 al 10 que son divisibles por cuatro. '''

cubos_por_cuatro = [(num**3) for num in range (1,11) if (num**3) % 4 == 0]
print(cubos_por_cuatro)


'''RED SOCIAL: 
Una red social tiene una base de datos de usuarios y sus correspondientes amistades. 
Crea un programa que tome una base de datos de una red social como una lista de 
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los 
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas 
diferentes. Deberas eliminar las cuentas duplicadas y después  devolver una tupla de 
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos. 
Pista 1: Tus datos de entrada podrían ser así  —>  red_social = [("Juan", ["Maria", "Pedro", 
"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])] 
Pista 2: Para eliminar duplicidades puedes usar sets'''


red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro","Juan"]),  ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]

amigos = [set(amigos[1]) for amigos in red_social]
print(amigos)

amigos_tupla = tuple(amigos)
print(amigos_tupla)

'''Dada una lista de palabras, crea una nueva lista que contenga solo las palabras con más de 5 caracteres.'''

palabras = ["casa", "perro", "gato", "elefante", "ratón", "jirafa"]

nueva_lista = [palabra for palabra in palabras if len(palabra) > 5]
print(nueva_lista)

'''Dada una lista de números, crea una nueva lista que contenga solo los números positivos.'''

numeros = [3, -6, 9, -12, 0, 7, -4, 1]

nueva_lista_positivos = [numero for numero in numeros if numero > 0]
print(nueva_lista_positivos)

'''Dada una matriz representada como una lista de listas, crea una nueva matriz que sea la transpuesta de la matriz original.'''

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]

print(transpuesta)

'''Dadas dos listas, crea una nueva lista que contenga todas las combinaciones posibles de elementos de ambas listas.'''

lista1 = [1, 2]
lista2 = ['a', 'b']

nueva_lista_combinada = [ (a, b) for a in lista1  for b in lista2]
print(nueva_lista_combinada)

