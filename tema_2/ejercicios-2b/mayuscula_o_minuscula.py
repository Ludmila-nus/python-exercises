'''Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es 
una mayúscula o una minúscula.'''

#--- el usuario debe ingresar una letra del abecedario
letra = input('Por favor, ingrese una letra: ')

#--- comprobamos si es mayuscula o minuscula
if letra.islower():
    print('La letra ingresada es minuscula')
elif letra.isupper():
    print('La letra ingresada es mayuscula')