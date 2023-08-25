'''Pedir un número (entero) y escribir por consola todos los números hasta ese número, 
en orden creciente. 
Ejemplo: si el número es 12, habría que escribir por consola todos los números desde 
el hasta el 12'''

#--- pedir un numero entero por pantalla
numero=int(input('Introduzca un numero entero: '))

#--- escribir todos los numero hasta ese numero en orden creciente

for i in range(1,numero + 1):
    print(i)
    i = i + 1