#---pedir al usuario 2 numeros
num1 = int(input('Ingrese un numero que sera usado como dividendo: '))
num2 = int(input('Ingrese un numero que sera usado como divisor: '))

#--- si el divisor es cero se muestra un error
while num2 == 0:
    num2 = int(input('Usted debe ingresar un numero distinto que cero'))

#--- mostrar por pantalla la division de ambos
resultado = num1 / num2
print(resultado)