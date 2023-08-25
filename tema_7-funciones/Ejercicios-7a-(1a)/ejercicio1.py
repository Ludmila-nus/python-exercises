'''TEMA: FUNCIONES
OBJETIVO: FAMILIARIZACIÓN CON EL USO EL USO DE
PARAMETROS Y ARGUMENTOS.'''
# importamos modulos
import numpy as np

'''
# 1. Define una función llamada "saludar" que tome un parámetro "nombre"
# y muestre un saludo personalizado.
def saludar(nombre):
    print(f'¡Hola {nombre}!')

saludar('Ludmila')
print('--------')

# 2. Crea una función llamada "suma" que tome dos parámetros "a" y "b" e
# imprima la suma de ambos.
def suma(a,b):
    print(f'Resultado de la suma: {a+b}')

suma(10,10)
print('--------')

# 3. Escribe una función llamada "calcular_area_rectangulo" que tome dos
# parámetros "base" y "altura" y calcule el área de un rectángulo.
def calcular_area_rectangulo(base,altura):
    print(f'El área del rectangulo es: {base*altura}')

calcular_area_rectangulo(5,10)
print('--------')

# 4. Define una función llamada "imprimir_lista" que tome una lista como
# parámetro y la imprima en la consola.
def imprimir_lista(lista):
    print(f'Lista de supermercado: {lista}')

lista_super=['lechuga','huevos','tomate','queso','pan']
imprimir_lista(lista_super)
print('--------')

# 5. Crea una función llamada "es_par" que tome un número como
# parámetro e imprima True si es par, o False si es impar.
def es_par(numero):
    if numero % 2 == 0:
        print(True)
    else:
        print(False)    

es_par(3)
print('--------')

# 6. Escribe una función llamada "concatenar_strings" que tome dos
# parámetros "cadena1" y “cadena2" e imprima la concatenación de
# ambas cadenas.
def concatenar_strings(cadena1,cadena2):
    print(f'{cadena1} {cadena2}')
    
concatenar_strings('mi mama se llama','Alejandra')    
print('--------')

# 7. Define una función llamada "obtener_maximo" que tome una lista de
# números como parámetro y devuelva el número máximo de la lista.
def obtener_maximo(lista_numeros):
    numero_max = max(lista_numeros)
    print(numero_max)

numeros = list(range(1,21))    
obtener_maximo(numeros)
print('--------')

# 8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un
# parámetro "fahrenheit" y devuelva su equivalente en grados Celsius.
def convertir_fahrenheit_a_celsius(grados_fahrenhet):
    grados_celsius = (grados_fahrenhet - 32) * 0.5556
    print(f'{grados_celsius} grados celsius')

grados = int(input('Grados fahrenheit: '))
convertir_fahrenheit_a_celsius(grados)
print('--------')

# 9. Escribe una función llamada "calcular_edad" que tome dos parámetros:
# "año_actual" y "año_nacimiento" y calcule la edad de una persona.
def calcular_edad(año_actual,año_nacimiento):
    print( f'Su edad es: {año_actual - año_nacimiento} años')

año_hoy = int(input('Ingrese el año actual: '))    
año_nac = int(input('Ingrese el año de nacimiento: '))
calcular_edad(año_hoy,año_nac)
print('--------')

# 10. Define una función llamada "es_divisible" que tome dos parámetros
# "num" y "divisor" e imprima True si "num" es divisible por "divisor", o
# False si no lo es.
def es_divisible(num,divis):
    if num % divis == 0:
        print(True)
    else:
        print(False) 

numero = int(input('Ingrese un numero: '))
divisor = int(input('Ingrese el numero divisor: '))
es_divisible(numero,divisor)
print('--------')

# 11. Crea una función llamada "mostrar_info_persona" que tome tres
# argumentos de palabra clave: "nombre", "edad" y "ciudad". La función
# debe imprimir en la consola la información de una persona en un
# formato legible.
def mostrar_info_persona(nombre,edad,ciudad):
    print(f'La persona de nombre {nombre} tiene {edad} años y vive en la ciudad de {ciudad}')

mostrar_info_persona('Ludmila','38','Bell Ville')
print('--------')

# 12. Escribe una función llamada "calcular_promedio" que tome una lista de números como parámetro y 
# calcule el promedio de esos números. Si no se proporciona una lista, debe usar una lista vacía por defecto.
def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma/len(lista)
    print(promedio)

numeros = list(range(1,11))
calcular_promedio(numeros)
print('--------')

# 13. Crea una función llamada "calcular_potencia" que tome dosparámetros "base" y "exponente", 
# y calcule la potencia de la base elevada al exponente. Utiliza 2 como valor por defecto para el exponente.
def calcular_potencia(base, exponente=2):
    print(f'Resultado: {base**exponente}')

calcular_potencia(5)

print('--------')
'''
# 14. Define una función llamada "imprimir_info_alumno" que tome un argumento posicional “nombre”(y sin valor por defecto) y varios
# argumentos de palabra clave: "edad", "curso" y “promedio" (puedes ponerles como valor por defecto None). La función debe imprimir 
# la información del alumno en un formato legible.
def imprimir_info_alumno(nombre,edad=None,curso=None,promedio=None):
    print(f'Nomnre alumno: {nombre}')
    if edad is not None:
        print(f'Edad: {edad}')
    if curso is not None:
        print(f'Curso: {edad}')
    if promedio is not None:
        print(f'Promedio: {edad}')        
        
imprimir_info_alumno(nombre='Ludmila', edad=38, curso='MasterBlockchain')        