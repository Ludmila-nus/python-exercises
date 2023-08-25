'''TRABJANDO CON TUPLAS: '''
# 1. Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una nueva linea. 
tupla_1 = ('fruta', 45, True)
for elemento in tupla_1:
    print(elemento)
# 2. Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla.  ¿Cuáles son las diferencias? 
lista_1 = ['pera','manzana','banana']
print(lista_1)
lista_1[0] = 'frutila'
print(lista_1)

'''tupla_2 = ('pera','manzana','banana')
print(tupla_2)
tupla_2[0] = 'frutila'
print(tupla_2)''' # no se puede modificar una tupla

# 3. Crea una tupla de enteros y devuelve la suma de los elementos. 
tupla_3 = (8,18,25,100)
suma_tupla_3 = sum(tupla_3)
print(suma_tupla_3)

# 4. Crea un script que dada una tupla que contiene strings cree una nueva tupla con el primer caracter de cada string. 
tupla_4_a = ('camino','abeja','sapo','avion')
lista_4 = []
lista_4.append([palabra[0] for palabra in tupla_4_a])
tupla_4_b = tuple(lista_4)  
print(tupla_4_b) 

'''for palabra in tupla_4_a:
    lista_4.append(palabra[0])
tupla_4_b = tuple(lista_4)  
print(tupla_4_b) '''
# 5. Crea un script que dada una tupla de números devuelva el producto de todos los números pares. 
tupla_5 = (20,27,40,51) 
producto = 1
for numero in tupla_5:
    if numero % 2 == 0:
        producto *=numero
print(producto)

# 6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros ordeandos en orden descendente. 
tupla_6 = (5,92,84,15,7,63,10)
tupla_6_descendente = tuple(reversed(tupla_6))
print(tupla_6_descendente)

# 7. Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados. (Puedes usar sets). 
tupla_7 = (5,5,9,9,17,64,10,10,30)
set_de_tupla_7 = set(tupla_7)
tupla_7_unicos= tuple(set_de_tupla_7)
print(tupla_7_unicos)

# 8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el numero se encuentra en la tupla 
# y falso en el caso contrario. 
numero_a = int(input('ingrese un numero y verificaremos si esta en la tupla: '))

if numero_a in tupla_7_unicos:
    coincidencia = True
else:
    coincidencia = False    
print(coincidencia)

# 9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas. 
tupla_9_a = ('queso', 'pan', 'tomate')
tupla_9_b = ('huevo', 'lechuga', 'palta')
tupla_combinada = tuple(zip(tupla_9_a,tupla_9_b))
print(tupla_combinada)

# 10.  Crea un script que dada una tupla de números devuelva e máximo y el mínimo. 
tupla_10 = (9,10,87,15,24,6,46)
maximo = max(tupla_10)
minimo = min(tupla_10)
print(maximo, minimo)

# 11.  Crea un script que dada una tupla con strings devuelva el string más largo y el más corto. 
# (Prueba añadiendo key=len a las funciones max y min). 
tupla_11 = ('rojo','verde','amarillo','naranja')
string_largo = max(tupla_11, key=len)
string_corto = min(tupla_11, key=len)
print(string_largo, string_corto)

# 12.  Crea un script que dada una tupla devuelva el contenido en orden revertido. 
tupla_inversa = tuple(reversed(tupla_11))
print(tupla_inversa)
# 13.  Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos elementos, 
# devuelva una nueva tupla en la que cada elemento sea la suma de los dos elementos de la tupla interna correspondiente. 
tupla_13 = ((5,10),(15,20),(25,5))

nueva_lista =[]
for i in range(len(tupla_13)):
    suma = sum(tupla_13[i])
    nueva_lista.append(suma)
nueva_tupla_13 = tuple(nueva_lista)   
print(nueva_tupla_13)