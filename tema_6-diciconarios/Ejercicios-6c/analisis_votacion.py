'''ANÁLISIS DE VOTACIONES: 
Supongamos que tienes los resultados de una elección con los nombres 
de los candidatos y la cantidad de votos obtenidos por cada uno. 
Implementa un programa en Python que permita registrar los votos, 
mostrar la lista completa de candidatos y sus votos, encontrar al 
candidato ganador (con más votos) y calcular el porcentaje de votos que 
obtuvo cada candidato. '''

# diccionario vacio
votacion = {}

# programa
continuar = True

# comeinza el programa dando las opciones
while continuar:
    print('---------------------------------------------------')
    print('1- Registrar voto')
    print('2- Mostrar lista de candidatos y sus votos')
    print('3- Candidato con mas votos, "ganador"')
    print('4- Porcentaje de votos que obtuvo cada candidato')
    print('5- Salir')
    opcion = input('Ingrese una opcion: ')
    print('---------------------------------------------------')

    # si decide registrar un voto
    if opcion == '1':
        # pedimos que ingrese el nombre del candidato
        candidato = input('Ingrese el nombre del candidato: ')
        # si el candidato esta regustrado sumamos un voto
        if candidato in votacion:
            votacion[candidato] = votacion[candidato] + 1
        # si el candidato no esta registrado sumamos el primer voto    
        else:
            votacion[candidato] = 1    
        print('Voto registrado correctamente')
    
    # si decie mostrar la lista de candidatos y sus votos
    elif opcion == '2':
        for candidatos, votos in votacion.items():
            print(f'candidato: {candidatos}, cantidad de votos: {votos}')         
    
    # si decide determinar cual es el candidato ganador
    elif opcion == '3':
        # si no hay votos registrados avisamos por pantalla
        if len(votacion) == 0:
            print('No hay candidatos registrados')

        # imprimimos por pantalla el candidato con mas votos    
        else:     
            candidato_ganador = max(votacion, key = votacion.get)  
            # imprimimos por pantalla el candidato ganador
            print(f'Candidato ganador: {candidato_ganador}')     

    # si decide saber el porcentaje de votos que obtuvo cada candidato
    elif opcion == '4':
        total_votos = sum(votacion.values())
        for candidatos, votos in votacion.items():
            porcentaje = votos*100/total_votos
            # imprimimos por pantalla los porcentajes
            print(f'Candidato: {candidatos}, porcentaje de votos obtenido: {porcentaje}')

    # si decide salir del sistema 
    elif opcion == '5':
        # imprimimos por pamntalla un mensaje de despedida
        print('---cerrando sistema de votacion---') 
        continuar = False

    # si la opcion que eligio no es correcta, imprimimos por pantalla un mensaje
    else:
        print('Opción inválida')    

