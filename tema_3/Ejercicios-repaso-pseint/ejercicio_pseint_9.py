'''Dibuja la X del cuadrado. Pedir el tamaño del lado de un cuadrado (entero) y dibujar la 
“X” de ese cuadrado mediante “*” 
Pista1: Se necesita un “Para” anidado. 
Pista2: Se dibuja un “*” cuando: 
  - (altura = ancho) O  (lado + 1 = ancho + alto) 
  En otro caso, se dibuja un “ " 
Nota: al Escribir, recordad que podéis añadir “Sin Saltar” para que siga escribiendo en 
la misma línea'''
import time
#--- pedimos al usuario que ingrese un numero entero (lado del cuadrado)
print('------¡Bienvenido a dibuja la X del cuadrado!------')
print('---------------vamos a comenzar--------------------')
time.sleep(3) #esperamos 3 segundos para comenzar
tamaño = int(input('Ingrese un numero entero: \n'))

#--- dibujamos la "x" de ese cuadrado
for i in range(tamaño):
    for j in range(tamaño):
        if i == j or (tamaño + 1 ==  (i+1) + (j+1)):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')    
    print('')
