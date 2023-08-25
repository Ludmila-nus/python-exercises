# iniciamos los valores que debe tener la contraseña como falsos
tiene_minuscula = False
tiene_mayuscula = False
Tiene_numero = False
Tiene_caract_especial = False
longitud = 8


def validar_contraseña(contraseña):
    """La funcion dara un valor booleano (True/False) de acuerdo si cumple con todos los requisitos o no"""
    
    # devuekve false y sale de la funcion si la longitud es menor a la requerida
    if len(contraseña) < longitud:
        return False
    
    # verificamos cada uno de los requisitos
    for caracter in contraseña:
        if caracter.islower():
            tiene_minuscula = True
        elif caracter.isupper():
            tiene_mayuscula = True
        elif caracter.isdigit():
            Tiene_numero = True
        else:
            Tiene_caract_especial = True

    # retorna True si cumple con todos los requisitos sino devuelve False
    return tiene_minuscula and tiene_mayuscula and Tiene_caract_especial and Tiene_numero

