'''Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y 
en que posición. Puedes usar find()). 
Puedes usar el archivo pi_10000.txt'''

def encontrar_fecha(filename,fecha):
    """Funcion que busca tu fecha de nacimiento en pi"""

    # abrimos el archivo que contiene los valores de pi
    with open(filename, 'r') as f_obj:
        # guardamos el contenido en una variable
        contenido = f_obj.read()
    # buscamos fecha en los valores de pi
    encontrar = contenido.find(fecha)
    # rerornamos un mensaje con la ubicacion de la fecha en pi
    if encontrar == -1:
        return print('Su fecha de nacimiento no se encuentra en los primeros 10.000 digitos de pi')
    else:     
        return print(f'Su fecha de nacimiento se encuentra en la posicion {encontrar}')  
    

# iniciamos el programa
print('¡Encuentra tu fecha de nacimiento en pi!')
# pedimos la fecha de nacimeinto
fecha = input('Ingresa el fecha de tu cumpleaños: ')
# llamamos a la funcion y le pasamos los datos
encontrar_fecha('ejercicios-7-d/pi.txt',fecha)


  

