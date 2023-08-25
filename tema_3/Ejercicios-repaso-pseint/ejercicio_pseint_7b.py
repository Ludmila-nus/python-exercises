'''Juego “Piedra, Papel, Tijera”. Vamos a enfrentarnos contra el ordenador en el juego de 
piedra, papel o Ejera. Reglas: 
    - Piedra gana a Tijera y pierde con Papel 
    - Papel gana a Piedra y pierde con Tijera 
    - Tijera gana a Papel y pierde con Piedra 
  Pedir al jugador que escoja entre “Piedra | Papel | Tijera” (texto); el ordenador hará su   
  elección al azar. Y se comparan las dos elecciones para ver quién gana. Al terminar una   
  partida, se pedirá si se quiere jugar de nuevo (texto) y, en caso afirmaEvo, se reinicia el   
  juego (sin que acabe el programa). 
  Recordatorio: hay que controlar que el jugador introduzca una de las 3 opciones    
  (Piedra | Papel | Tijera), y no otra. 
  Pista: la función “azar(3)” devuelve un número al azar entre 0, 1 y 2. Cada una de estas   
  opciones podríamos asociarla a “piedra”, “papel” o “Ejera”: “Si numAzar = 0 Entonces    
  ordenador = “Piedra” SiNo ...” '''
import random #importamos random para que el ordenador elija al azar
opciones = ['piedra' , 'papel' , 'tijera']
#--- pedir al usuario que elija una opcion (piedra,papel o tijera)
print('<<<<<BIENVENIDO AL JUEGO>>>>>>')
print('<<<<<<¡Vamos a comenza!>>>>>>>')

eleccion_jugador = input('Escriba una opcion. piedra | papel | tijera: \n')

# pasamos la palabra a minuscula para que la lea el programa
eleccion_jugador = eleccion_jugador.lower()

# controlamos que haya elejido una opcion valida
while (eleccion_jugador != 'piedra' and eleccion_jugador != 'papel' and eleccion_jugador != 'tijera'):
    print('No entendemos su respuesta')
    eleccion_jugador = input('vuelva a escribir su eleccion (piedra | papel | tijera): \n ')
    # pasamos la palabra a minuscula para que la lea el programa
    eleccion_jugador = eleccion_jugador.lower()

# le confirmamos al usuario su eleccion
print('ustes ha elejido', eleccion_jugador)

#--- el programa elije una opcion al azar

eleccion_ordenador = random.choice(opciones)
print('La eleccion del ordenador ha sido:', eleccion_ordenador)

#--- comparamos a ver quien gano
if eleccion_jugador == 'piedra':
    if eleccion_ordenador == 'tijera':
        print('has ganado la partida. ¡felicitaciones!')
    elif eleccion_ordenador == 'papel':  
        print('El ordenador te ha ganado. pierdes la partida :(')
    else:
        print('¡hay un empate!')
elif eleccion_jugador == 'papel':
    if eleccion_ordenador == 'piedra':
        print('has ganado la partida. ¡felicitaciones!')
    elif eleccion_ordenador == 'tijera':  
        print('El ordenador te ha ganado. pierdes la partida :(')
    else:
        print('¡hay un empate!')
elif eleccion_jugador == 'tijera':
    if eleccion_ordenador == 'papel':
        print('has ganado la partida. ¡felicitaciones!')
    elif eleccion_ordenador == 'piedra':  
        print('El ordenador te ha ganado. pierdes la partida :(')
    else:
        print('¡hay un empate!')
    
#--- terminada la partida preguntamos si quiere volver a jugar y reiniciamos si es afirmativo