'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
triángulo rectángulo como el de más abajo, de altura el número introducido.'''

#--- pedir al usuario un numero
numero = int(input('Introduce un numero:  '))
triangulo = '*'
#--- mostrar un triangulo de altura del numero introducido x el usuario
for i in range(numero):
    print(triangulo)
    triangulo = triangulo + '*'




