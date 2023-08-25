'''MANIPULACION DE ARCHIVOS  Y FILENOTFOUNDERROR 
Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de 
gatos en el primer archivo y tres nombres de perros en el segundo archivo. 
Escribe un programa que intente leer estos archivos e imprima el contenido 
de cada archivo en la pantalla. Envuelve tu código en un bloque try-except 
para capturar el error de FileNotFoundError, e imprime un mensaje amigable 
si falta algún archivo. Mueve uno de los archivos a una ubicación diferente 
en tu sistema y asegúrate de que el código en el bloque except se ejecute 
correctamente. Modifica tu bloque except para que falle en silencio si falta 
alguno de los archivos. '''

filename = 'ejercicios-7-d/cats1.txt'

try: 
    with open(filename) as f_obj:
        contenido = f_obj.read()
        print(contenido)  
except FileNotFoundError:
    print('El archivo no se encuentra')

      

def leer_archivos(filename):
    """Funcion que lee archivos si existen sino da un aviso de que no los encuentra"""
    
    try: 
        # abrimos el texto
        with open(filename) as f_obj:
            # guaredamos el texto en una variable en este caso -contenido-
            contenido = f_obj.read()
    except FileNotFoundError:
        pass
        #print(f'El archivo {filename} no se encuentra')
    else:
        palabras = contenido.split()
        num_palabras = len(palabras)
        print(f'La cantidad de palabras son {num_palabras}')

filenames = ('ejercicios-7-d/cats1.txt','ejercicios-7-d/cats2.txt','ejercicios-7-d/dogs1.txt','ejercicios-7-d/dogs2.txt')        

for filename in filenames:
    leer_archivos(filename)