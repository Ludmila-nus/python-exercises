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

    formulario = True
    while formulario == False:
        # si el nombre de usuario tiene una longitud menor a 3 caracteres, 
        # manda mensaje de error y vuelve a pedir que llene los campos
        if  len(nombre) < 3:  
            print(colored('nombre invalido: longitud minima del nombre de 3 caracteres', 'red'))  
            nombre = input('Ingrese un nombre valido')
            formulario= False
        # si el nombre de usuario es correcto, envia mensaje de registro.    
        else:
            print(colored(f'Nombre {nombre} se ha registrado con exito','green'))
            

        # si el email no tiene un "@"", manda mensaje de error y vuelve a pedir que llene los campos
        if '@' not in email:
            print(colored('email invalido: el emial debe contener un "@"', 'red'))
            email = input('Ingrese un email valido')
            formulario= False
        else:
             print(colored(f'Email {email} se ha registrado con exito','green'))  
              

        # si el email no tiene un ".", manda mensaje de error y vuelve a pedir que llene los campos    
        if '.' not in email:
            print(colored('email invalido: el emial debe contener un "."', 'red'))
            email = input('Ingrese un email valido')
            formulario= False
        else:
            print(colored(f'Email {email} se ha registrado con exito','green'))  
              
        
        # si el telefono no esta compuesto por 9 numeros, manda mensaje de error y vuelve a pedir que llene los campos
        n = 0
        while telefono > 0:
            telefono = telefono // 10
            n += 1
        if n != 9:
            print(colored('Telefono invalido, debe estar compuesto solo por numeros','red')) 
            telefono = input('Ingrese un telefono valido')
            formulario= False
        else:
              print(colored(f'Email {telefono} se ha registrado con exito','green'))  
             
        
        # si el telefono no esta compuesto solo de numeros, manda mensaje de error y vuelve a pedir que llene los campos
        if telefono != int(telefono):
            print(colored('Telefono invalido, debe estar compuesto solo por numeros','red')) 
            telefono = input('Ingrese un telefono valido')
            formulario= False
        else:
             print(colored(f'Email {telefono} se ha registrado con exito','green'))  
             
             
    if formulario == True:
        print=('Su formulario ha sido cargado correctamente. ¡Bienvenido!')
        
 

print('Bienvenido al sistema, ingrese sus datos para registrarse')
su_nombre = input('Ingrese su nombre, (longitud minima de 3 caracteres ): ')        
su_email = input('Ingrese su email, ( que contenga un “@“ y un “.”): ')
su_telefono = int(input('Ingrese su telefono, (longitud 9 caracteres conformado por digitos): '))

validacion = validar_formulario(su_nombre,su_email,su_telefono)    
print(validacion)