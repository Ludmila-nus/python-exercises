'''Crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos
los caracteres en forma de asterisco salvo los últimos cuatro. Si por ejemplo el número de tarjeta
es 1234 2345 3456 5678, el output deberá ser **** **** **** 5678.'''

#ingresa por pantalla el numero de la tarjeta de credito
tarjeta = input('Ingrese el numero de su tarjeta de credito sin espacios: ')

#imprime todos los caracteres con **** salvo los ultimos 4
print('**** **** **** '+ tarjeta[12:16])
