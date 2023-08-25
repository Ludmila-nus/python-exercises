"""
Juego “Piedra, Papel, Tijera”.
Vamos a enfrentarnos contra el ordenador en el juego de piedra, papel o Tijera.
Reglas:
- Piedra gana a Tijera y pierde con Papel
- Papel gana a Piedra y pierde con Tijera
- Tijera gana a Papel y pierde con Piedra
Pedir al jugador que escoja entre “Piedra | Papel | Tijera” (texto); el ordenador hará su elección al azar.
Y se comparan las dos elecciones para ver quién gana. Al terminar una partida, se pedirá si se quiere jugar
de nuevo (texto) y, en caso afirmativo, se reinicia el juego (sin que acabe el programa).
"""
import random

lista_de_juego = ['Piedra', 'Papel', 'Tijera']
respuesta = 'Si'
while respuesta != 'No':

    Jugador = input('Escoje: Piedra, Papel o Tijera: ').title()
    ordenador = random.choice(lista_de_juego)
    match Jugador:
        case 'Piedra':
            if ordenador == 'Piedra':
                print(f'{Jugador} vs {ordenador}. Es un empate.')
            elif ordenador == 'Papel':
                print(f'{Jugador} vs {ordenador}. Gana ordenador.')
            elif ordenador == 'Tijera':
                print(f'{Jugador} vs {ordenador}. He ganado.')
        case 'Papel':
            if ordenador == 'Papel':
                print(f'{Jugador} vs {ordenador}. Es un empate.')
            elif ordenador == 'Tijera':
                print(f'{Jugador} vs {ordenador}. Gana ordenador.')
            elif ordenador == 'Piedra':
                print(f'{jugador} vs {ordenador}. He ganado.')
        case 'Tijera':
            if ordenador == 'Tijera':
                print(f'{Jugador} vs {ordenador}. Es un empate.')
            elif ordenador == 'Piedra':
                print(f'{Jugador} vs {ordenador}. Gana ordenador.')
            elif ordenador == 'Papel':
                print(f'{Jugador} vs {ordenador}. He ganado.')        
        case _:
            print('Error intentelo de nuevo')
    respuesta = input('Quiere jugar otra vez (SI o NO):').title()        
print('¡Adios!')