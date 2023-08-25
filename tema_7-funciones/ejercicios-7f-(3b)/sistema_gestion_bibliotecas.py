'''SISTEMA DE GESTION DE BIBLIOTECA 
Crea un sistema de gestión de una biblioteca utilizando clases en Python. 
Debes implementar las siguientes clases: 
1. “Libro”: Representa un libro con atributos como título, autor y número de 
ejemplares disponibles. 
2. “Usuario”: Representa a un usuario de la biblioteca con atributos como 
nombre, número de identificación y lista de libros prestados. 
3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar 
libros, prestar libros a usuarios, devolver libros y mostrar el inventario.'''


class Libro:
    def __init__(self, titulo, autor, num_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.num_ejemplares = num_ejemplares

class Usuario:
    def __init__(self, nombre, num_identificacion):
        self.nombre = nombre
        self.num_identificacion = num_identificacion
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libros(self, libro):
        self.libros.append({'Titulo':libro.titulo, 'Autor':libro.autor, 'Numero de ejemplares': libro.num_ejemplares})

    def agregar_usuarios(self, usuario):
        self.usuarios.append({'usuario':usuario.nombre, 'Numero de identificacion':usuario.num_identificacion, 'Libros prestados':usuario.libros_prestados})

    def prestamo_libro(self, usuario, libro): # Estos argumentos son instancias de las clases Usuario y Libro, respectivamente
        for u in self.usuarios:
            if u['usuario'] == usuario.nombre:
                if len(u['Libros prestados']) > 3:
                    print('Usted tiene 3 libros prestados, debe devolverlos para poder retirar nuevos libros')
                    return
                for lib in self.libros:
                    if lib['Titulo'] == libro.titulo:
                       if lib['Numero de ejemplares'] >= 1:
                           lib['Numero de ejemplares'] -= 1
                           u['Libros prestados'] = libro.titulo
                           print(f'El usuario {usuario.nombre} ha retirado el libro titulado {libro.titulo} del autor {libro.autor}')


def iniciar_biblioteca():
    """FUncion que inicia la biblioteca, permite cargar libros y usuarios"""
    
    continuar = True
    while continuar:
        accion = input('¿Que accion necesita realizar? \n 1: agregar una libro \n 2: agregar un usuario \n 3: Salir \n Ingrese el numero de la accion seleccionada: ')    
        print('---------------------------------------')

    # Creamos los libros a cargar
    libro1 = Libro('Mujercitas','Louise May Alcot', 2)
    libro2 = Libro('El cuento de la criada', 'Margaret Atwood',3)

    # Creamos los usuarios a cargar
    usuario1 = Usuario('Ludmila', '1055')
    usuario2 = Usuario('Rodrigo', '1060')
    
    # instancia de biblioteca
    biblio = Biblioteca()
    #agregamos libros
    biblio.agregar_libros(libro1)
    biblio.agregar_libros(libro2)
    # agregamos usuarios
    biblio.agregar_usuarios(usuario1)
    biblio.agregar_usuarios(usuario2)
    #prestamos libro a usuario
    biblio.prestamo_libro(usuario1,libro1)






        