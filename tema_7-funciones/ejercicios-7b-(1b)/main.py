# importamos modulos
from termcolor import colored
import validador
import creador

def solicitar_contraseña():
    """La funcion llama a los modulos validador para validar si la contraseña es segura de lo contrario
    llama al modulo creador para sugerir una contraseña segura"""
    
    # pedimos al usuario que ingrese una contraseña
    contraseña = input('Ingrese una contraseña segura: ') 
    
    # llamamos la modulo validador de contraseña segura
    if validador.validar_contraseña(contraseña) == True:
        print(colored('Su contraseña es segura','green'))

    # llamamos al modulo creador de contraseña nueva     
    else:
        sugerencia = creador.generar_contraseña()
        print(colored(f'Su contraseña no es segura, le sugerimos utilice esta: {sugerencia}','yellow'))


solicitar_contraseña()

