'''Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista 
de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del 
libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del 
libro y el apellido del autor. 
Pista: Tus datos de entrada podrían ser así —> lista_libros = [('El aleph', 'Jorge Luis
Borges'), ('Cien años de soledad', 'Garbriel Garcia Márquez'), ('La ciudad y los perros',
'Mario Vargas Llosa')]'''

# creamos la lista de libros de la biblioteca
lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Garbriel Garcia Márquez'), 
                ('La ciudad y los perros','Mario Vargas Llosa')]

lista_modificada = []
for titulo, autor in lista_libros:
    # eliminamos el nombre de la lista
    apellido = autor.split()[-1]
    lista_modificada.append((titulo,apellido))

print(lista_modificada)

'''
# extraemos el nombre y apellido del autor de cada libro a una lista
# extraemos los titulos de cada libro a una lista
lista_autores= []
lista_titulos = []
for titulo, autor in lista_libros:
    # eliminamos el nombre de la lista
    apellido = autor.split()[-1]
    # agregamos los titulos a una lista
    lista_titulos.append(titulo)
    # agregamos los apellidos a una lista
    lista_autores.append(apellido)

# convertimos la lista de apellidos en una tupla
tupla_apellidos = tuple(lista_autores)
# convertimos la lista de titulos de libros en una tupla
tupla_titulos = tuple(lista_titulos)
# unimos las dos tuplas (titulos de libros + autores)
lista_libros_modif = tuple(zip(tupla_titulos,tupla_apellidos))
print(lista_libros_modif)
'''