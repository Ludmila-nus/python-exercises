'''a. Crea un script en el que el usuario introduzca un número de más de una cifra. El script debe
imprimir los componentes del número uno a uno por pantalla. Por ejemplo si el número introducido
es el 4532 por pantalla deberá imprimirse:
4
5
3
2
b. Crea un script que dado un numero entero de cuatro cifras calcula e imprima el número que
resulta de leer el número introducido'''

#a
print('Introduza un numero de mas de una cifra')
numUsuario = input('numero: ')
for n in numUsuario:
    print(n) 

#b
print('Introduza un numero de 4 cifras')
numUsuario = input('numero: ')
inicio = 0
for n in numUsuario:
   resultado = int(n) + inicio
   inicio = resultado
print ('El resultado de la lectura de su numero es: ' + str(resultado))