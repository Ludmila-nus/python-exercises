#--- pedir un numero por pantalla (numero)
numero1 = float(input ('Ingrese un numero que sera usado como base: '))
#--- pedir otro numero por pantalla (potencia)
numero2 = float(input('Ingrese otro numero que sera usado como exponente: '))
#--- comprobar si el resultado de ese calculo es par o impar

resultado = numero1 ** numero2

if resultado % 2 == 0:
    print('El resultado de la operacion es un numero par')
else:
    print('El resultado de la operacion es un numero impar')


