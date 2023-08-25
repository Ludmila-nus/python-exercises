'''Pedir un número (entero) y calcular su factorial (entero) 
Recordatorio: el factorial de un número se calcula mulEplicando los números desde el 
1 hasta el propio número, incluidos los números intermedios 
Ejemplo: el factorial de 6 sería 1 * 2 * 3 * 4 * 5 * 6 = 720'''

#--- pedimos un numero entero por pantalla
numero = int(input('ingrese un numero entero: '))
resultado = 1
#--- hacemos un bucle para calcular el factorial del numero
for i in range(1, (numero+1)):
    resultado = resultado * i
print('El resultado es:', resultado)
