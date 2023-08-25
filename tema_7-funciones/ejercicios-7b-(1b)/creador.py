# importamos funciones
import random
import string

def generar_contraseña():
    """La funcion genera una contraseña aleatoria"""
    
    # damos una longitud de 8 caracteres
    longitud = 8
    # iniciamos el string caracteres
    caracteres = ''
    # sumamos al string caracteres digitos, minusculas, mayusculas y caracteres especiales
    caracteres += string.digits
    caracteres += string.ascii_lowercase
    caracteres += string.ascii_uppercase
    caracteres += string.punctuation
    
    # generamos la contraseña aleatoriamente con random.choise, usamos ''.join para unir los caracteres sin espacio
    contraseña_segura = ''.join(random.choice(caracteres) for i in range (longitud))   

    return contraseña_segura 
         



