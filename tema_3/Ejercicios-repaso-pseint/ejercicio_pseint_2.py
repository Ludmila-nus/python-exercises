'''Pedir dos números por consola (enteros) y sumar (entero) todos los números que hay 
entre ellos. 
  Nota: vamos a suponer que el primer número que introduce el usuario SIEMPRE es    
  menor que el segundo 
  Ejemplo: si los números introducidos son el 4 y el 11, el resultado sería: 
    5 + 6 + 7 + 8 + 9 + 10 = 45'''

#--- pedir al usuario que intruduzca un 
num_1 = int(input('Introduzca un numero entero: '))

#--- pedir que introduzca otro numero mayor al anterior
num_2 = int(input('Introduzca un numero entero (mayor al anterior): '))

lista_numeros = [] #creamos una lista para almacenar los numeros

#--- comprobamos que el segundo numero es mayor al primero
while (num_2 > num_1):
    #--- almacenamos los numeros en la lista creada 
    for i in range(num_1, (num_2-1)):
        num_1 = num_1 + 1
        print(num_1)
        lista_numeros.append(num_1) 
        
#--- sumamos todos los numeros que hay entre los dos numeros ingresados x el usuario
print('hola que paso')       



   