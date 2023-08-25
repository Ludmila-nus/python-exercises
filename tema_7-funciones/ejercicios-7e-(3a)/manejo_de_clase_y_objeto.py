'''CLASE PERSONA 
Define una clase Persona con atributos como nombre, edad y profesión. 
Luego, crea varios objetos de esta clase y muestra su información. '''

class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

ludmila = persona('Ludmila', '38', 'Ingeniera')
rodrigo = persona('Rodrigo', '39', 'Ingeniero')

print(f'\n {ludmila.nombre}, {ludmila.edad}, {ludmila.profesion} \n {rodrigo.nombre}, {rodrigo.edad}, {rodrigo.profesion}')

print('---------------------------------------------')
'''CALCULADORA BÁSICA 
Crea una clase llamada "Calculadora" con métodos para sumar, restar, 
multiplicar y dividir. Crea objetos de esta clase y realiza algunas operaciones 
básicas. '''

class calculadora:
    def __init__(self, a, b):

        self.suma = a + b
        self.resta = a - b
        self.multip = a * b
        self.divis = a / b

resultado = calculadora(100,50)  

print (f'\n suma = {resultado.suma} \n resta = {resultado.resta} \
        \n multiplicacion = {resultado.multip} \n division = {resultado.divis} ')      

print('---------------------------------------------')
'''
LIBRO 
Crea una clase "Libro" con atributos como título, autor y año de publicación. 
Luego, crea varios objetos Libro y muestra su información. '''

class libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    def details(self):
        print(f'El libro {self.titulo} fue escrito por {self.autor} en el año {self.año}')    

libro1 = libro('Pepe Luis', 'Luis Gonzalez', '1990')
libro2 = libro('La odisea', 'Carlos Gomez', '1890')

libro1.details()

print('---------------------------------------------')

'''
RECTÁNGULO 
Crea una clase "Rectangulo" con atributos de longitud y ancho. Implementa 
un método para calcular el área y el perímetro del rectángulo. '''

class rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    def details(self):
       resultado = self.longitud + self.ancho  + self.longitud + self.ancho
       print(f'El perimetro del rectangulo es: {resultado}') 

longitud = float(input('Ingrese la longitud del rectangulo: ')) 
ancho = float(input('Ingrese el ancho del rectangulo: ')) 

calculo = rectangulo(longitud, ancho)
calculo.details()

print('---------------------------------------------')
'''
DADO 
Crea una clase "Dado" que simule el lanzamiento de un dado de 6 caras. 
Implementa un método para lanzar el dado y mostrar el resultado (quizás te 
convenga usar el modulo random). '''
# importamos el modulo random para el tiro del dado
import random
'''
class dado:
    def __init__(self):
        self.tirada = random.randint(1,6)
    def details(self):
        print(f'Usted obtuvo el numero {self.tirada}')    

print('¡Bienvenido al juego!')
continuar = True
while continuar:
    tirada = input('¿Desea tirar el dado? si/no:  ')
    if tirada.lower() == 'si':
        jugada = dado()
        jugada.details()
    else:
        print('Hasta luego, ¡vuelve a jugar pronto!')    
        continuar = False

print('---------------------------------------------')
'''
class dado:
    def __init__(self):
        self.tirada = random.randint(1,6)
    def details(self):
        print('¡Bienvenido al juego!')
        continuar = True
        while continuar:
            tirada = input('¿Desea tirar el dado? si/no:  ')
            if tirada.lower() == 'si':
                print(f'Usted obtuvo el numero {self.tirada}')   
            else:
                print('Hasta luego, ¡vuelve a jugar pronto!')    
                continuar = False

mi_jugada = dado()                 
mi_jugada.details()

print('---------------------------------------------')


'''
COCHE 
Crea una clase "Coche" con atributos como marca, modelo y año. 
Implementa un método para encender el coche y otro para apagarlo (puedes 
simulae el encendido y apagado con una variable booleana). '''

class coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def details(self):
        print('¡Bienvenido!')
        continuar = True
        while continuar:
            tirada = input('¿Desea tirar el dado? si/no:  ')
            if tirada.lower() == 'si':
                print(f'Usted obtuvo el numero {self.tirada}')   
            else:
                print('Hasta luego, ¡vuelve a jugar pronto!')    
                continuar = False

 




