'''Juego “Adivina mi número”.  Pedir  al  jugador  que  piense  un  número  (entero)  del  1  al 
10,  y  dejarle  5  segundos  para  pensar  (“Esperar  5  Segundos”).  A  partir  de  ahí,  el 
ordenador tratará de adivinar el número, preguntando al jugador si su número es “X”. 
En caso de que no lo sea, volverá a preguntar por otro número. Tiene 5 intentos para 
tratar de adivinarlo. 
Nota: UElizar las función “azar” para que el ordenador pregunte de forma aleatoria. 
Recordatorio:  el  juego  acaba  cuando  el  “número  es  acertado"  O  “se  han  hecho  5 
intentos”
'''
import time  # importamos time para hacer que el programa se detenga en algunos momentos
import random  # importamos random para que el ordenador elija al azar

#--- el usuario debe ingresar un numero entero del 1 al 10
print('<<<<<<BIENVENIDO AL JUEGO>>>>>>')
print('<<<<<<<<<¡comenzamos!>>>>>>>>>>')
print('Ingrese un numero entero del 1 al 10:')
time.sleep(5)  # esperamos 5 segundos para que el usuario piense
numero_usuario = int(input('numero elegido: '))

#--- creamos un bucle para que se repita hasta 5 veces 
for i in range(5): 
    #--- el ordenador elige al azar un numero del 1 al 10
    opciones = [1,2,3,4,5,6,7,8,9,10]
    numero_ordenador = random.choices(opciones)
    #--- le preguntamos al usuario si el numero al azar del ordenador es igual al ingresado por el
    print('¿El numero que ustede eligio es el:', numero_ordenador, '?')
    resultado = input('responda si | no: ')
    resultado = resultado.lower()
    if resultado == 'si':
        print('¡El ordenador a adivinado su numero!') # si acierta el ordenador imprimimos el resultado positivo
        break
    elif resultado == 'no':
        print('El ordenador no a adivinado su numero.') # si no acierta el ordenador, imprimimos el resultado negativo


