'''Escribe un programa que pida al usuario un número entero y muestre por pantalla una 
estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el 
centro de la estructura.'''

import time

#--- pedir un numero al usuario
print('-----¡Bienvenido a dibuja la flecha!-------')
print('-----------vamos a comenzar----------------')
time.sleep(2) #esperamos 2 segundos para comenzar
numero = int(input('ingrese un numero entero: \n'))

#--- crear un bucle que dibuje una flecha con *
# el centro de la felcha tiene la cantidad de * que el numero de usuarios

for i in range (1,numero+1):
    for j in range(i):
        print('*', end = ' ')
    print('')   
    
for i in range (1,numero+1):
    for j in range(numero-i):
        print('*', end = ' ')
    print('')    


'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

#--- escribir la contraseña en una variable
print('para ingresar al sistema se necesita una contraseña')
contraseña = 'miperrobartolo2023'

#--- bucle que pregunte al usuario la contraseña y siga hasta que sea correcta
contraseña_usuario = input('ingrese la contraseña: ')
while contraseña != contraseña_usuario:
    print('la contraseña es incorrecta, intentelo nuevamente')
    contraseña_usuario = input('ingrese la contraseña: ')
print('la contraseña es correcta, usted puede ingresar al sistema.')

'''Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última'''

#--- pedir al usuario una palabra
palabra = input('ingrese una palabra: \n')

#--- damos vuelta la palabra
palabra = palabra[::-1]

#--- mostrar las letras una a una  de la palabra intriducida empezando por la ultima letra
for i in range(len(palabra)):
    print(palabra[i])

for i in palabra:
    print(i)

'''Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por 
pantalla el número de veces que aparece la letra en la frase.'''   

#--- pedir al usuario una frase y una letra
frase = input('Intruduzca una frase: \n')
letra = input('Introduzca una letra: \n')

#--- mostramos cuantas veces aparece esa letra en la frase
for i in frase:
    repeticiones = frase.count(letra)
print(f'La letra {letra} se repite {repeticiones} veces')    

