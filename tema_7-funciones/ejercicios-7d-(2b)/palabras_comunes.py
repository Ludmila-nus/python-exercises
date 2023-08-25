'''Encuentra o crea algunos textos que te gustaría analizar (puedes visitar 
Project Gutenberg (http://gutenberg.org/) o crear textos usando ChatGPT). 
Copia el texto sin formato desde tu navegador en un archivo de texto en tu 
computadora (o descarga los archivos). Averigua cuántas veces aparece una 
palabra o frase en el texto (puedes usar el método count()). 
'''

def contar_palabra(filename):
    """funcion que cuenta cuantas veces se repite la palabra ingresada por el usuario en el texto """
    
    # abrimos el archivo 
    with open(filename) as f_obj:  
            # guardamos el contenido del archivo en una variable
            contenido = f_obj.read()
            # pedimos que ingrese una palabra
            palabra = input('Ingrese la palabra que desea contar: ')
            # contamos cuantas veces aparece
            palabra_cantidad = contenido.count(palabra)
            # si no aparece nunca enviamos un mensaje avisando que la palabra no se encuentra
            if palabra_cantidad == 0:
                  print(f'La palabra {palabra} no se encuentra en el texto')    
            # si la palabra esta, enviamos un mensaje de cuantas veces se repite      
            else:
                  print(f'La palabra {palabra} se repite {palabra_cantidad} veces en el texto')

# iniciamos el programa
print('Bienvenido a -contando palabras-')

# el bulce continua si el usuario quiere seguir buscando palabras
continuar = True
while continuar:
    # llamamos a la funcion que cuenta palabras en un texto 
    contar_palabra('ejercicios-7-d/text.txt')
    # preguntamos si quiere seguir buscando palabras
    continuar = input('¿Desea buscar otra palabra? si/no: ')
    # si no quiere buscar mas, finalizamos el bucle
    if continuar.lower() == 'no':
          print('¡Gracias por usar nuestro programa!')
          continuar = False
          