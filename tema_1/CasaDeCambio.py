''' Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida
por el usuario de el resultante en dólares.'''

#script que reciba una cantidad de euros del usuario 
print('Hola, ¿cuantos euros quiere usted cambiar a dolares?')
euros = input()

#tipo de cambio de 1 EU = 1.2 $
dolares = float(euros) / 1.2

#La casa de cambios se queda un 10% en concepto de ‘tasas de gestión’.
#Calcula el monto recibido, cambio en $, tasa gestion, $ que recibe el usuario
tasaDeGestion = dolares * 0.1
dolaresFinal = dolares - tasaDeGestion

#Imprime el desglose por pantalla formateado de tal forma que quede claro para el usuario.
print('El monto recibido en Euros es de', euros)
print('La cantidad de dolares al tipo de cambio de 1 EU = 1.2 $ es de: ', dolares)
print('El monto que le corresponde a la casa de cambio por la gestion es ', tasaDeGestion, ' Dolares')
print('La cantidad de dolares que recibira usted  es ', dolaresFinal, ' Dolares')


