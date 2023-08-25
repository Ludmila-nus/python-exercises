'''Una red social tiene una base de datos de usuarios y sus correspondientes amistades. 
Crea un programa que tome una base de datos de una red social como una lista de 
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los 
amigos repetidos en la lista de amigos corresponden a usuarios con varias cuentas 
diferentes. 
Deberas eliminar las cuentas duplicadas y después  devolver una tupla de 
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.'''
'''Pista 1: Tus datos de entrada podrían ser así  —>  red_social = [("Juan", ["Maria", "Pedro", 
"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])] 
Pista 2: Para eliminar duplicidades puedes usar set'''

from termcolor import colored

# creamos la base de datos de la red social            
red_social= [('Juan',['Maria','Pedro','Luis']),('Maria', ['Juan', 'Pedro','Juan']) \
             ,('Pedro', ['Juan', 'Maria']), ('Luis', ['Juan'])]    

# Eliminamos las cuentas duplicadas utilizando sets
# creamos una lista para almacenar los datos
amigos_lista = []
usuarios_lista = []
# pasamos por un bucle for para eliminat los duplicados transformando la tupla en sets
for amigos in red_social:
    amigos_set =set(amigos[1])
    # extraemos los amigos sin repetir en una lista aparte
    amigos_lista.append(amigos_set)
    # extramos los usuarios en una lista aparte 
    usuarios_lista.append(amigos[0])

# transformamos la lista de amigos en una tupla
amigos_tupla = tuple(amigos_lista)

# transformamos la lista de usuarios en una tupla
usuarios_tupla = tuple(usuarios_lista)

# unimos los usuarios de la primer tupla con la tupla de amigos sin repetir
red_social_modif = tuple(zip(usuarios_tupla,amigos_tupla))

# determinamos cual es el usuario con mas amigos, buscando en la tupla de amigos
max_amigos = max(amigos_tupla)

# determinamos el indice del usuario con mas amigos
indice = amigos_tupla.index(max_amigos)

# inmprimimos los resultados por pantalla
print('La red social esta conformada por los siguientes usuarios y sus respectivos amigos:')
for i in red_social_modif:
    print(colored (f'usuario: {i[0]}, amigos: {i[1]}', 'magenta'))
print(colored(f'El usuario con mas amigos es {usuarios_tupla[indice]}','yellow'))
                                                                              