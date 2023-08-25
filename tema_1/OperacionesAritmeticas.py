''' 
a. Crea un script que muestre por pantalla el resultado de la siguiente operación aritmética:
b. Escribe un programa que lea un entero positivo, n, introducido por el usuario y después
muestre por pantalla el resultado de la siguiente operación:
c. Escribe un programa que pida al usuario dos números enteros y muestre por pantalla los
números de entrada, el cociente y el resto.'''

#a. script que muestra por pantalla el resultado de la siguiente operacion
print('Se mostrara por pantalla el resultado de una operacion matematica')
resultado = (((3+2)/(2*5))**2)
print(resultado)

print( )
#b. el usuario ingresa un numero "n" y este debe usarse para la siguiente operacion

print('Usted debe ingresar un numero')
num_usuario = input('numero ingresado: ')
operacion = (float(num_usuario) * (float(num_usuario) + 1 )/ 2)
print('El resultado de la operacion es:' + str(operacion))

print( )
#c. el usuario ingresa dos numero que se usan en una division y se muestran los resultados

print('Ingrese dos numeros enteros')
num_1 = input('primero numero: ')
num_2 = input('segundo numero: ')
cociente = int(num_1) / int(num_2)
cociente2 = int(num_1) // int(num_2)
resto = int(num_1) % int(num_2)
print( )
print('los valores que arroja la division son:')
print(' divisor: ' + str(num_1) + '\n dividendo: ' + str(num_2) + '\n cociente: ' + str(cociente) + '\n resto:' + str(resto))
print( str(cociente2))