#-- importamos modulos
import json

#-- comprobamos si el archivo existe o no y lo leemos 
def lee_numero_favorito():
    """La funcion trae el numero favorito del usuario que esta almacenado si no existe devuelve """

    try:
        with open('numero_favorito.json') as file:
            numero_fav = json.load(file)

            return numero_fav
        
    except FileNotFoundError:
        return None

#-- guardar el numero favorito
def almacena_numero_favorito(numero_favorito):
    """La funcion almacena el numero favorito del usuario
      en un archivo json"""

    filename = 'numero_favorito.json'
    # abro el archivo de forma escritura, si noe xiste lo crea
    with open(filename, 'w') as file:
        # guarda el numero favorito en file
        json.dump(numero_favorito, file)

#-- pedir el numero favorito
def numero_favorito():
    """La funcion pide al usuario el numero favorito y llama a la funcion 
    almacenar_numero_favorito para que la guarde """
    
    # pedimos el numero favorito
    numero_fav = int(input('Ingrese su numero favorito: '))
    # llamamos a la funcion para almacenarlo
    almacena_numero_favorito(numero_fav)

    return numero_fav



def principal():
    """Funcion principal del sistema que llama a las demas funciones"""
    
    # llamamos a la funcion leer_numero_favorito para que traiga el numero favorito del usuario que tiene almacenado
    numero_almacenado = lee_numero_favorito()

    if numero_almacenado:
        print(f'Sé cuál es tu número favorito... Es {numero_almacenado}.')

    # si el numero no esta almacenado lo pide y le avisa al usuario que ha sido guardado con exito
    else:
        numero = numero_favorito()
        print(f'Su numero favorito {numero} ha sido guardado con exito!') 

       
    

principal()   