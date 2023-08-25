'''REGISTRO DE PUNTAJES: 
Implementa un programa en Python que permita registrar y mantener un 
seguimiento de los puntajes de un juego. El programa debe permitir a los 
jugadores ingresar sus nombres y puntajes, almacenarlos en un 
diccionario y proporcionar funcionalidades para mostrar el puntaje más 
alto, el promedio de puntajes y la cantidad total de jugadores.'''

# diccionario vacio
registro = {}

# cargamos los jugadores y sus puntajes
continuar = True

while continuar:
    # pedimos que ingrese el nombre del jugador
    nombre = input('Ingrese el nombre del jugador: ')
    # si el jugador ya se encuenta registrado
    if nombre in registro:
        # preguntamos si quiere actualizar los puntos del jugador ya registrado
        actualizar= input('El jugador ya se encuentra registrado, ¿quiere actualizar su puntaje? (si/no): ')
        if actualizar == 'si':
            # si quiere actualizar los puntos pedimos que los ingrese por pantalla
            puntaje = int(input(f'Ingrese el puntade del jugador {nombre}: '))
            registro[nombre] = puntaje
        else:
            # si no quiere actualizar los pountos preguntamos si quiere cargar los puntos de otro jugador
            seguir = input('¿quiere cargar otro jugador? (si/no): ')
            # si no quiere cargar otro jugador sale del ciclo while
            if seguir == 'no':
                continuar = False
    else:
        # si el jugador es nuevo le pedimos que ingrese el puntaje de este nuevo jugador
        puntaje = int(input(f'Ingrese el puntaje del jugador {nombre}: '))
        registro[nombre] = puntaje
        # preguntamos si quiere cargar otro jugador
        seguir = input('¿quiere cargar otro jugador? (si/no): ')
        # si no quiere cargar otro jugador sale del ciclo while
        if seguir == 'no':
            continuar = False 

jugador_mas_alto = max(registro, key=nombre.get)
puntaje_mas_alto = registro[jugador_mas_alto]
total_puntos = sum(registro.values())
total_jugadores = len(registro)
promedio_puntos = total_puntos/ total_jugadores

print(f'El puntaje mas alto es del jugador {puntaje_mas_alto}')    
print(f'El promedio de puntos de la jugada es de {promedio_puntos}')   
print(f'La cantidad de jugadores en la partida fue de {total_jugadores}') 
