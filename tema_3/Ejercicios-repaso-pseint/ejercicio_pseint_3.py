'''Pedir un número por consola (entero) y escribir todos los números impares, en orden 
decreciente, desde ese número hasta el 1. 
  Ejemplo: si el número introducido es el 23, se escribirían el: 23, 21, 19, 17, ..., 5, 3, 1'''

#--- pedimos un numero por pantalla
numero = int(input('ingrese un numero entero: '))

# #--- creamos un bucle para que muestre todos los numero en forma decreciente
for i in range(numero,0,-1):
    print(i)
