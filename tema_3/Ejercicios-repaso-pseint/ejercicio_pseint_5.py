'''Pedir  un  número  por  consola  (entero)  y  decir  si  es  menor,  igual  o  mayor  a  10.  Hacer 
que  el  programa  conEnúe  pidiendo  un  número  hasta  que  introduzcamos  el  0,  y 
entonces, terminará.'''

print('¡Aqui comienza el programa!')
numero = 1
#--- decir si es < = o > a 10
while numero != 0: # crear un bucle para que siga preguntando hasta que intriduzcan el numero 0
    numero = int(input('introduzca un numero: '))
    if numero == 10:
        print('El numero', numero, 'es igual a 10')
    elif numero > 10:
        print('El numero', numero, 'es mayor a 10')
    elif numero < 10:
        print('El numero', numero, 'es menor a 10')
if numero == 0:
    print('El numero', numero, 'es igual a 0, se acaba el programa. ¡Hasta luego!')

