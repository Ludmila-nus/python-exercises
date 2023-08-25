'''Crea un programa que valide un formulario de registro. Crea una función 
llamada validar_formulario que reciba diferentes campos de un formulario 
(nombre, correo electrónico y número de teléfono) y verifique si los valores 
ingresados cumplen con los requisitos especificados, siendo estos: 
1. Que el nombre tenga una longitud minima de 3 caracteres 
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9 
caracteres 
3. Que el email contenga un “@“ y un “.”'''

# importamos modulos
from termcolor import colored

# funciones
def validar_formulario(nombre,email,telefono):
    'Esta funcion va a validar el ingreso correcto de los datos'

    if  len(nombre) < 3 or '@' not in email or '.' not in email or len(telefono) != 9 or not telefono.isdigit():  
        return False
    
    return True    
 

print('Bienvenido al sistema, ingrese sus datos para registrarse')
su_nombre = input('Ingrese su nombre, (longitud minima de 3 caracteres ): ')        
su_email = input('Ingrese su email, ( que contenga un “@“ y un “.”): ')
su_telefono = input('Ingrese su telefono, (longitud 9 caracteres conformado por digitos): ')

validacion = validar_formulario(su_nombre,su_email,su_telefono)    

if validacion is True:
    print(colored('Su formulario ha sido cargado correctamente. ¡Bienvenido!', 'green'))
else:
    print(colored('Su formulario es invalido', 'red'))