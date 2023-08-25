'''Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por 
pantalla'''

#--- primero vamos a crear una lista
numeros = []

#--- luego pedimos 4 numeros por pantalla y los agregamos a la lista
for i in range(4):
   numero = float(input("Introduce el número #{}: ".format(i + 1)))
   numeros.append(numero)

#--- asumimos que el 1 numero es el mayor

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

#--- imprimimos por pantalla el numero mayor
print('el mayor numero ingresado es: ' , mayor)        