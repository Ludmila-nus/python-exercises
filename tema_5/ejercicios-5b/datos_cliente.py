'''Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene 
el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La 
segunda base de datos contiene el nombre del cliente, la dirección y el historial de 
pedidos. 
Escribe un programa que tome las dos bases de datos como listas de tuplas y 
devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en 
ambas bases de datos. 
Los clientes se consideran iguales si tienen el mismo nombre. 

Pista: Tus datos de entrada podrían ser así  —>   
base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", 
"maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", “555-9012")] 
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), 
("Luis", "Calle 789", ["Libro4"])] '''

# creamos la base de tados
base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"), 
               ("Pedro", "pedro@example.com", "555-9012")] 
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])]

# extraemos en un set los nombres de los clientes
nombres1 = set(nombre[0] for nombre in base_datos1)
nombres2 = set(nombre[0] for nombre in base_datos2)

# utilizamos intersection para quedarlos con los nombres comunes a los dos sets
nombres_comunes = nombres1.intersection(nombres2)
print(nombres_comunes)

#  obtenemos solo los clientes comunes con sus datos en una lista aparte
base_datos_unida = []
for datos1 in base_datos1:
    if datos1[0] in nombres_comunes:
        for datos2 in base_datos2:
            if datos2[0] == datos1[0]:
                base_datos_unida.append((datos1[0],datos1[1],datos1[2],datos2[1],datos2[2]))
                break
print(base_datos_unida)        
'''
# extraemos los nombres de las tuplas en una lista
lista_nombres1 = []
lista_nombres2 = []
for nombre,mail,telefono in base_datos1:
    lista_nombres1.append(nombre)
for nombre,direccion,pedido in base_datos2:
    lista_nombres2.append(nombre)

# pasamos las listas de nombres a sets para poder combinaras 
set_bs1 = set(lista_nombres1)
set_bs2 = set(lista_nombres2)

# utilizamos intersection para quedarlos con los nombres comunes a los dos sets
set_bd_combinada = set_bs1.intersection(set_bs2)

# seleccionamos los clientes comunes 
# los clientes comunes de la primer base de datos
lista_base_datos1 = []
for i in range(len(base_datos1)):
    if lista_nombres1[i] in set_bd_combinada:
        lista_base_datos1.append(base_datos1[i])
# los clientes comunes de la seguna base de datos        
lista_base_datos2 = []
for i in range(len(base_datos2)):
    if lista_nombres1[i] in set_bd_combinada:
        lista_base_datos2.append(base_datos2[i])   

# pasamos las listas a sets para unirlas
for i in range(len(lista_base_datos1)):
    lista_base_datos1[i].append(lista_base_datos2[i])

# mostramos los datos por pantalla
print(lista_base_datos1)
'''
